"""Local read-only HTTP API for the M2-verified NASA C-MAPSS FD001 files."""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
import sys
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

DATASET_ID = "NASA_CMAPSS_FD001"
CONTRACT_VERSION = "M2_FD001_DATA_CONTRACT"
ROOT = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = ROOT / "data" / "FD001"
SOURCE_SPECS = {
    "train": {"file": "train_FD001.txt", "sha256": "963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8", "bytes": 3515356, "rows": 20631, "columns": 26},
    "test": {"file": "test_FD001.txt", "sha256": "3CDA7109CE17BAFB5443F2AC926CFCF88154B941B8C4CF95EB55D1DDD6F52851", "bytes": 2228855, "rows": 13096, "columns": 26},
    "rul": {"file": "RUL_FD001.txt", "sha256": "A19C8EC94931949D0485BDC35118206E9C81C4547B422EFB9CF86F4CEDDBCECA", "bytes": 429, "rows": 100, "columns": 1},
}
SENSOR_FIRST_RAW_INDEX = 5
SENSOR_COUNT = 21
SETTING_FIRST_RAW_INDEX = 2
SETTING_COUNT = 3


class DataSourceError(Exception):
    """A required data source is unavailable or violates the verified contract."""


class APIError(Exception):
    def __init__(self, status: int, code: str, message: str):
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message


def json_bytes(value: object) -> bytes:
    """Serialize JSON consistently; Python None is represented as JSON null."""
    return json.dumps(value, ensure_ascii=False, allow_nan=False, separators=(",", ":")).encode("utf-8")


def _parse_physical_lines(raw: bytes, filename: str, columns: int) -> list[tuple[int, tuple[float, ...]]]:
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as exc:
        raise DataSourceError("A required source is not ASCII text.") from exc
    parsed: list[tuple[int, tuple[float, ...]]] = []
    for physical_line, line in enumerate(text.splitlines(), start=1):
        tokens = line.split()
        if not tokens:
            raise DataSourceError("A required source contains a blank physical line.")
        if len(tokens) != columns:
            raise DataSourceError("A required source does not match the verified column schema.")
        try:
            values = tuple(float(token) for token in tokens)
        except ValueError as exc:
            raise DataSourceError("A required source contains a non-numeric value.") from exc
        if not all(math.isfinite(value) for value in values):
            raise DataSourceError("A required source contains a non-finite value.")
        parsed.append((physical_line, values))
    return parsed


class DataStore:
    """Validates exact source bytes and retains their original physical line numbers."""

    def __init__(self, data_dir: Path = DEFAULT_DATA_DIR, expected_hashes: dict[str, str] | None = None):
        self.data_dir = Path(data_dir)
        self.expected_hashes = dict(expected_hashes or {key: spec["sha256"] for key, spec in SOURCE_SPECS.items()})
        self._snapshot: dict | None = None
        self._fingerprint: tuple | None = None

    def _stat_fingerprint(self) -> tuple:
        try:
            stats = tuple((key, (self.data_dir / spec["file"]).stat().st_size,
                           (self.data_dir / spec["file"]).stat().st_mtime_ns)
                          for key, spec in SOURCE_SPECS.items())
        except OSError as exc:
            raise DataSourceError("A required FD001 source file is unavailable.") from exc
        return stats

    def get_snapshot(self) -> dict:
        fingerprint = self._stat_fingerprint()
        if self._snapshot is not None and fingerprint == self._fingerprint:
            # Recheck exact bytes before every served response, even if file metadata is unchanged.
            for key, spec in SOURCE_SPECS.items():
                try:
                    raw = (self.data_dir / spec["file"]).read_bytes()
                except OSError as exc:
                    self._snapshot = None
                    self._fingerprint = None
                    raise DataSourceError("A required FD001 source file is unavailable.") from exc
                if len(raw) != spec["bytes"] or hashlib.sha256(raw).hexdigest().upper() != self.expected_hashes.get(key):
                    self._snapshot = None
                    self._fingerprint = None
                    raise DataSourceError("A required FD001 source failed its size or SHA-256 check.")
            return self._snapshot
        metadata: dict[str, dict] = {}
        split_units: dict[str, dict[int, dict[int, dict]]] = {"train": defaultdict(dict), "test": defaultdict(dict)}
        unit_order: dict[str, list[int]] = {"train": [], "test": []}
        rul_values: list[tuple[int, int]] = []
        for key, spec in SOURCE_SPECS.items():
            path = self.data_dir / spec["file"]
            try:
                raw = path.read_bytes()
            except OSError as exc:
                raise DataSourceError("A required FD001 source file is unavailable.") from exc
            digest = hashlib.sha256(raw).hexdigest().upper()
            if len(raw) != spec["bytes"] or digest != self.expected_hashes.get(key):
                raise DataSourceError("A required FD001 source failed its size or SHA-256 check.")
            lines = _parse_physical_lines(raw, spec["file"], spec["columns"])
            if len(lines) != spec["rows"]:
                raise DataSourceError("A required FD001 source failed its verified row-count check.")
            metadata[key] = {
                "source_file": f"data/FD001/{spec['file']}", "bytes": len(raw), "sha256": digest,
                "physical_lines": len(lines), "parsed_rows": len(lines), "columns": spec["columns"],
            }
            if key in ("train", "test"):
                for source_line, row in lines:
                    unit_raw, cycle_raw = row[0], row[1]
                    if not unit_raw.is_integer() or not cycle_raw.is_integer():
                        raise DataSourceError("A required FD001 source has a non-integer Unit or Cycle value.")
                    unit_id, cycle = int(unit_raw), int(cycle_raw)
                    if unit_id < 1 or cycle < 1:
                        raise DataSourceError("A required FD001 source has an invalid or duplicate Unit-Cycle key.")
                    if unit_id not in split_units[key]:
                        unit_order[key].append(unit_id)
                    if cycle in split_units[key][unit_id]:
                        raise DataSourceError("A required FD001 source has an invalid or duplicate Unit-Cycle key.")
                    split_units[key][unit_id][cycle] = {"row": row, "source_line": source_line}
            else:
                for source_line, row in lines:
                    if not row[0].is_integer():
                        raise DataSourceError("RUL source contains a non-integer value.")
                    rul_values.append((source_line, int(row[0])))

        if len(split_units["train"]) != 100 or len(split_units["test"]) != 100:
            raise DataSourceError("Train or Test Unit count differs from the verified contract.")
        if unit_order["test"] != list(range(1, 101)) or len(rul_values) != len(unit_order["test"]):
            raise DataSourceError("Test Unit and RUL positional coverage differs from the verified contract.")
        unit_summaries: dict[str, list[dict]] = {}
        for split in ("train", "test"):
            summaries = []
            for unit_id in sorted(split_units[split]):
                cycles = sorted(split_units[split][unit_id])
                if cycles != list(range(1, cycles[-1] + 1)):
                    raise DataSourceError("A Unit Cycle sequence differs from the verified contiguous-cycle contract.")
                summaries.append({"unit_id": unit_id, "first_cycle": cycles[0], "last_cycle": cycles[-1], "cycle_count": len(cycles)})
            unit_summaries[split] = summaries
        snapshot = {
            "sources": metadata, "units": unit_summaries, "rows": dict(split_units),
            "rul": rul_values, "test_unit_order": unit_order["test"],
        }
        self._snapshot = snapshot
        self._fingerprint = fingerprint
        return snapshot


def _error_payload(code: str, message: str) -> dict:
    return {"ok": False, "error": {"code": code, "message": message}}


def _success_payload(data: object, provenance: object) -> dict:
    return {"ok": True, "data": data, "provenance": provenance}


def _query(query: str, required: set[str]) -> dict[str, str]:
    parsed = parse_qs(query, keep_blank_values=True, strict_parsing=False)
    if set(parsed) != required or any(len(values) != 1 or values[0] == "" for values in parsed.values()):
        raise APIError(400, "INVALID_PARAMETER", "Provide each required query parameter exactly once and no others.")
    return {key: values[0] for key, values in parsed.items()}


def _positive_integer(value: str, label: str) -> int:
    if not re.fullmatch(r"[+-]?[0-9]+", value):
        raise APIError(400, "INVALID_PARAMETER", f"{label} must be an integer.")
    try:
        return int(value)
    except ValueError as exc:
        raise APIError(400, "INVALID_PARAMETER", f"{label} is outside the supported integer range.") from exc


def _split(value: str) -> str:
    if value not in ("train", "test"):
        raise APIError(400, "INVALID_SPLIT", "split must be train or test.")
    return value


def _catalog(snapshot: dict) -> dict:
    sensors = [
        {"sensor_id": sensor_id, "sensor_field": f"sensor_{sensor_id:02d}",
         "raw_column_index": SENSOR_FIRST_RAW_INDEX + sensor_id - 1,
         "physical_meaning": "UNKNOWN", "unit": "UNKNOWN"}
        for sensor_id in range(1, SENSOR_COUNT + 1)
    ]
    return {
        "dataset_id": DATASET_ID,
        "dataset_name": "NASA C-MAPSS FD001",
        "contract_version": CONTRACT_VERSION,
        "available_splits": ["train", "test"],
        "splits": {
            split: {"unit_count": len(snapshot["units"][split]),
                    "cycle_range": [min(u["first_cycle"] for u in snapshot["units"][split]),
                                    max(u["last_cycle"] for u in snapshot["units"][split])]}
            for split in ("train", "test")
        },
        "raw_index_basis": "0-based; sensor_id is 1-based",
        "unit_field": {"name": "unit_id", "raw_column_index": 0, "identity_scope": "split-local"},
        "cycle_field": {"name": "cycle", "raw_column_index": 1, "meaning": "per-Unit observation index"},
        "operating_settings": [
            {"field": f"operating_setting_{i}", "raw_column_index": SETTING_FIRST_RAW_INDEX + i - 1,
             "physical_meaning": "UNKNOWN", "unit": "UNKNOWN"}
            for i in range(1, SETTING_COUNT + 1)
        ],
        "sensors": sensors,
        "source_files": list(snapshot["sources"].values()),
        "provenance_rules": {
            "source_line": "1-based original physical line number in the source file",
            "sensor_mapping": "sensor_id 1 maps to sensor_01 at raw column 5; sensor_id 7 maps to sensor_07 at raw column 11; sensor_id 21 maps to sensor_21 at raw column 25",
            "train_labels": "No explicit fault label or RUL column.",
            "test_rul": "RUL_FD001 has one row per Test Unit by first-occurrence position, but contains no Unit ID key; it is not a per-Cycle Test label and is not exposed as an endpoint.",
            "failure_semantics": "A final observed Train Cycle is not proof of physical failure.",
        },
    }


def make_handler(store: DataStore):
    class FD001Handler(BaseHTTPRequestHandler):
        server_version = "FD001ReadOnlyAPI/1.0"
        sys_version = ""

        def _send(self, status: int, payload: dict) -> None:
            body = json_bytes(payload)
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _get_snapshot(self):
            try:
                return store.get_snapshot()
            except DataSourceError as exc:
                raise APIError(503, "DATA_SOURCE_UNAVAILABLE", str(exc)) from exc

        def do_GET(self):
            route = urlsplit(self.path)
            try:
                if route.path not in ("/api/health", "/api/catalog", "/api/units", "/api/history"):
                    raise APIError(404, "INVALID_PARAMETER", "Unknown API route.")
                snapshot = self._get_snapshot()
                if route.path == "/api/health":
                    if route.query:
                        raise APIError(400, "INVALID_PARAMETER", "health does not accept query parameters.")
                    self._send(200, _success_payload({"service": "NTUST NASA C-MAPSS FD001 Read-only API",
                                 "dataset_id": DATASET_ID, "data_loaded": True,
                                 "source_validation": "PASS"}, {"sources": list(snapshot["sources"].values())}))
                    return
                if route.path == "/api/catalog":
                    if route.query:
                        raise APIError(400, "INVALID_PARAMETER", "catalog does not accept query parameters.")
                    self._send(200, _success_payload(_catalog(snapshot), {"contract": CONTRACT_VERSION}))
                    return
                if route.path == "/api/units":
                    values = _query(route.query, {"split"})
                    split = _split(values["split"])
                    self._send(200, _success_payload({"dataset_id": DATASET_ID, "split": split,
                                 "units": snapshot["units"][split]}, {"source_file": snapshot["sources"][split]["source_file"],
                                 "source_sha256": snapshot["sources"][split]["sha256"],
                                 "source_line_basis": "1-based original physical line"}))
                    return
                values = _query(route.query, {"split", "unit", "sensor", "start", "end"})
                split = _split(values["split"])
                unit_id = _positive_integer(values["unit"], "unit")
                sensor_id = _positive_integer(values["sensor"], "sensor")
                start = _positive_integer(values["start"], "start")
                end = _positive_integer(values["end"], "end")
                if sensor_id < 1 or sensor_id > SENSOR_COUNT:
                    raise APIError(400, "SENSOR_NOT_FOUND", "sensor must be an available ID from 1 through 21.")
                if unit_id not in snapshot["rows"][split]:
                    raise APIError(404, "UNIT_NOT_FOUND", "Unit does not exist in the selected split.")
                cycles = snapshot["rows"][split][unit_id]
                if start > end or start not in cycles or end not in cycles:
                    raise APIError(400, "CYCLE_RANGE_INVALID", "start and end must form an ordered range within the Unit's observed cycles.")
                raw_index = SENSOR_FIRST_RAW_INDEX + sensor_id - 1
                field = f"sensor_{sensor_id:02d}"
                records = []
                for cycle in range(start, end + 1):
                    entry = cycles.get(cycle)
                    if entry is None:
                        raise APIError(400, "CYCLE_RANGE_INVALID", "The requested range includes an unobserved Cycle.")
                    records.append({
                        "unit_id": unit_id, "cycle": cycle, "sensor_id": sensor_id,
                        "sensor_field": field, "raw_column_index": raw_index,
                        "value": entry["row"][raw_index],
                        "source_file": snapshot["sources"][split]["source_file"],
                        "source_line": entry["source_line"], "split": split,
                    })
                data = {"dataset_id": DATASET_ID, "split": split, "unit_id": unit_id,
                        "sensor": {"sensor_id": sensor_id, "sensor_field": field, "raw_column_index": raw_index},
                        "range": {"start": start, "end": end, "inclusive": True},
                        "actual_count": len(records), "records": records}
                provenance = {"source_file": snapshot["sources"][split]["source_file"],
                              "source_sha256": snapshot["sources"][split]["sha256"],
                              "source_line_basis": "1-based original physical line number"}
                self._send(200, _success_payload(data, provenance))
            except APIError as exc:
                self._send(exc.status, _error_payload(exc.code, exc.message))
            except Exception:
                self._send(500, _error_payload("INTERNAL_ERROR", "The request could not be completed."))

        def _method_not_allowed(self):
            self._send(405, _error_payload("INVALID_PARAMETER", "This API supports GET requests only."))

        do_POST = _method_not_allowed
        do_PUT = _method_not_allowed
        do_PATCH = _method_not_allowed
        do_DELETE = _method_not_allowed

        def log_message(self, fmt, *args):
            sys.stderr.write("%s - %s\n" % (self.log_date_time_string(), fmt % args))

    return FD001Handler


def create_server(host: str = "127.0.0.1", port: int = 8000, data_dir: Path = DEFAULT_DATA_DIR,
                  expected_hashes: dict[str, str] | None = None) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), make_handler(DataStore(data_dir, expected_hashes)))


def main() -> int:
    host = os.environ.get("FD001_API_HOST", "127.0.0.1")
    port = int(os.environ.get("FD001_API_PORT", "8000"))
    server = create_server(host, port)
    print(f"Serving {DATASET_ID} read-only API at http://{host}:{port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
