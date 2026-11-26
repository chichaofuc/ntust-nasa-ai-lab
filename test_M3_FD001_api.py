"""HTTP and parser contract tests; tests do not create dataset rows or alter sources."""
import hashlib
import json
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import M3_FD001_api as api


class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = api.create_server(port=0)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def request(self, path, method="GET", server=None):
        base = self.base if server is None else f"http://127.0.0.1:{server.server_port}"
        req = Request(base + path, method=method)
        try:
            response = urlopen(req, timeout=20)
        except HTTPError as exc:
            return exc.code, json.loads(exc.read().decode("utf-8"))
        with response:
            return response.status, json.loads(response.read().decode("utf-8"))

    def test_health_validates_real_sources(self):
        status, body = self.request("/api/health")
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        self.assertTrue(body["data"]["data_loaded"])
        self.assertEqual(body["data"]["source_validation"], "PASS")
        self.assertEqual(len(body["provenance"]["sources"]), 3)

    def test_catalog_reports_verified_mapping_and_limits(self):
        status, body = self.request("/api/catalog")
        self.assertEqual(status, 200)
        data = body["data"]
        self.assertEqual(data["splits"]["train"]["unit_count"], 100)
        self.assertEqual(data["splits"]["test"]["unit_count"], 100)
        self.assertEqual(data["sensors"][0]["raw_column_index"], 5)
        self.assertEqual(data["sensors"][6]["sensor_field"], "sensor_07")
        self.assertEqual(data["sensors"][6]["raw_column_index"], 11)
        self.assertEqual(data["sensors"][20]["raw_column_index"], 25)
        self.assertEqual(data["sensors"][6]["physical_meaning"], "UNKNOWN")
        self.assertIn("no Unit ID key", data["provenance_rules"]["test_rul"])

    def test_units_returns_only_selected_split(self):
        for split in ("train", "test"):
            with self.subTest(split=split):
                status, body = self.request(f"/api/units?split={split}")
                self.assertEqual(status, 200)
                self.assertEqual(body["data"]["split"], split)
                self.assertEqual(len(body["data"]["units"]), 100)
                self.assertEqual(body["data"]["units"][0]["unit_id"], 1)
                self.assertGreater(body["data"]["units"][0]["cycle_count"], 0)

    def test_train_history_sensor_7_source_provenance(self):
        status, body = self.request("/api/history?split=train&unit=1&sensor=7&start=1&end=20")
        self.assertEqual(status, 200)
        data = body["data"]
        self.assertEqual(data["actual_count"], 20)
        self.assertEqual(data["sensor"], {"sensor_id": 7, "sensor_field": "sensor_07", "raw_column_index": 11})
        self.assertEqual([row["cycle"] for row in data["records"]], list(range(1, 21)))
        for row in data["records"]:
            self.assertEqual(row["split"], "train")
            self.assertEqual(row["unit_id"], 1)
            self.assertEqual(row["sensor_id"], 7)
            self.assertEqual(row["source_file"], "data/FD001/train_FD001.txt")
            self.assertGreaterEqual(row["source_line"], 1)

    def test_test_history_uses_test_only(self):
        status, body = self.request("/api/history?split=test&unit=1&sensor=7&start=1&end=20")
        self.assertEqual(status, 200)
        self.assertEqual(body["data"]["actual_count"], 20)
        self.assertEqual(body["provenance"]["source_file"], "data/FD001/test_FD001.txt")
        self.assertTrue(all(row["split"] == "test" for row in body["data"]["records"]))

    def test_invalid_split(self):
        status, body = self.request("/api/units?split=FD002")
        self.assertEqual((status, body["error"]["code"]), (400, "INVALID_SPLIT"))

    def test_sensor_not_found(self):
        for sensor in ("22", "-1"):
            with self.subTest(sensor=sensor):
                status, body = self.request(f"/api/history?split=train&unit=1&sensor={sensor}&start=1&end=2")
                self.assertEqual((status, body["error"]["code"]), (400, "SENSOR_NOT_FOUND"))

    def test_unit_not_found(self):
        status, body = self.request("/api/history?split=train&unit=999&sensor=7&start=1&end=2")
        self.assertEqual((status, body["error"]["code"]), (404, "UNIT_NOT_FOUND"))

    def test_cycle_range_errors(self):
        for query in ("start=2&end=1", "start=1&end=999"):
            with self.subTest(query=query):
                status, body = self.request(f"/api/history?split=train&unit=1&sensor=7&{query}")
                self.assertEqual((status, body["error"]["code"]), (400, "CYCLE_RANGE_INVALID"))

    def test_missing_and_malformed_parameters(self):
        for path in ("/api/units", "/api/history?split=train&unit=1&sensor=7&start=1",
                     "/api/history?split=train&unit=1.5&sensor=7&start=1&end=2"):
            with self.subTest(path=path):
                status, body = self.request(path)
                self.assertEqual((status, body["error"]["code"]), (400, "INVALID_PARAMETER"))

    def test_missing_source_returns_503_and_not_healthy(self):
        with tempfile.TemporaryDirectory() as directory:
            server = api.create_server(port=0, data_dir=Path(directory))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                status, body = self.request("/api/health", server=server)
                self.assertEqual((status, body["error"]["code"]), (503, "DATA_SOURCE_UNAVAILABLE"))
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=5)

    def test_hash_mismatch_returns_503(self):
        hashes = {key: value["sha256"] for key, value in api.SOURCE_SPECS.items()}
        hashes["train"] = "0" * 64
        server = api.create_server(port=0, expected_hashes=hashes)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            status, body = self.request("/api/catalog", server=server)
            self.assertEqual((status, body["error"]["code"]), (503, "DATA_SOURCE_UNAVAILABLE"))
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)

    def test_source_hash_is_rechecked_on_cached_requests(self):
        store = api.DataStore()
        store.get_snapshot()
        store.expected_hashes["train"] = "0" * 64
        with self.assertRaises(api.DataSourceError):
            store.get_snapshot()

    def test_source_hashes_remain_unchanged(self):
        for spec in api.SOURCE_SPECS.values():
            path = api.DEFAULT_DATA_DIR / spec["file"]
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest().upper(), spec["sha256"])

    def test_schema_mismatch_is_rejected_without_fixture_dataset(self):
        with self.assertRaises(api.DataSourceError):
            api._parse_physical_lines(b"not a numeric row\n", "in-memory malformed parser input", 26)

    def test_null_serializes_as_json_null(self):
        self.assertEqual(api.json_bytes({"value": None}), b'{"value":null}')

    def test_write_methods_are_not_exposed(self):
        for method in ("POST", "PUT", "PATCH", "DELETE"):
            with self.subTest(method=method):
                status, body = self.request("/api/history", method=method)
                self.assertEqual(status, 405)
                self.assertFalse(body["ok"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
