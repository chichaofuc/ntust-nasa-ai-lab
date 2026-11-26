"""Generate a raw-source to live-HTTP API comparison report for Train/Test."""
import json
import threading
from pathlib import Path
from urllib.request import urlopen

import M3_FD001_api as api


def get_json(url: str) -> dict:
    with urlopen(url, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    server = api.create_server(port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    rows = []
    try:
        for split in ("train", "test"):
            filename = api.SOURCE_SPECS[split]["file"]
            source_path = api.DEFAULT_DATA_DIR / filename
            raw_rows = {}
            for source_line, line in enumerate(source_path.read_text(encoding="ascii").splitlines(), start=1):
                values = line.split()
                if int(float(values[0])) == 1 and int(float(values[1])) <= 20:
                    raw_rows[int(float(values[1]))] = (source_line, float(values[11]))
            if set(raw_rows) != set(range(1, 21)):
                raise RuntimeError(f"Expected actual Unit 1 Cycles 1..20 in {filename}; observed {sorted(raw_rows)}")
            payload = get_json(f"{base}/api/history?split={split}&unit=1&sensor=7&start=1&end=20")
            if not payload.get("ok"):
                raise RuntimeError(f"API returned an error for {split}: {payload}")
            records = payload["data"]["records"]
            if len(records) != 20 or payload["data"]["actual_count"] != 20:
                raise RuntimeError(f"API count mismatch for {split}")
            for cycle, record in enumerate(records, start=1):
                source_line, source_value = raw_rows[cycle]
                match = (
                    record["split"] == split and record["unit_id"] == 1 and record["cycle"] == cycle
                    and record["sensor_id"] == 7 and record["sensor_field"] == "sensor_07"
                    and record["raw_column_index"] == 11 and record["source_file"] == f"data/FD001/{filename}"
                    and record["source_line"] == source_line and record["value"] == source_value
                )
                if not match:
                    raise RuntimeError(f"Raw/API mismatch for {split} Cycle {cycle}")
                rows.append((split, filename, cycle, source_line, source_value, record["value"], 11,
                             record["source_line"], "PASS"))
        health = get_json(f"{base}/api/health")
        if not health.get("ok"):
            raise RuntimeError("API health check failed during reconciliation")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    lines = [
        "# M3 FD001 Raw Source Row Reconciliation",
        "",
        "Actual local HTTP API responses were compared with the exact original physical lines in the M2-verified source files.",
        "",
        "Query per split: `/api/history?split={train|test}&unit=1&sensor=7&start=1&end=20`.",
        "Sensor API ID 7 maps to `sensor_07`, raw column index 11 (0-based). Physical source lines are 1-based.",
        "Each comparison was generated from the raw source and actual HTTP response; all numeric comparisons use parsed source numeric values without rounding.",
        "",
        "| Split | Exact source file | Cycle | Raw source physical line | Raw Sensor 7 value | API Sensor 7 value | Raw column index | API source line | Match |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        split, filename, cycle, source_line, source_value, api_value, raw_index, api_line, status = row
        lines.append(f"| {split} | `data/FD001/{filename}` | {cycle} | {source_line} | {source_value:.10g} | {api_value:.10g} | {raw_index} | {api_line} | {status} |")
    lines.extend([
        "",
        f"Compared records: {len(rows)} (Train 20, Test 20). Result: PASS ({sum(row[-1] == 'PASS' for row in rows)}/{len(rows)} matched).",
        "The API does not serve RUL values or a per-Test-Cycle label. `/api/catalog` reports the RUL file's source identity and explicitly states the positional mapping limitation; no RUL row mapping endpoint is exposed.",
        "",
    ])
    output = Path(__file__).resolve().parent / "M3_FD001_SOURCE_ROW_RECONCILIATION.md"
    output.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(json.dumps({"report": output.name, "rows_compared": len(rows), "train": 20, "test": 20,
                      "result": "PASS", "health": "PASS"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
