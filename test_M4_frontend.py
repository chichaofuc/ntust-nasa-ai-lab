"""M4 frontend hosting and transparent M3 pass-through tests."""
import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import M3_FD001_api
import M4_FD001_web_server


class M4FrontendTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_server = M3_FD001_api.create_server(port=0)
        cls.api_thread = threading.Thread(target=cls.api_server.serve_forever, daemon=True)
        cls.api_thread.start()
        api_base = f"http://127.0.0.1:{cls.api_server.server_port}"
        cls.web_server = M4_FD001_web_server.ThreadingHTTPServer(("127.0.0.1", 0), M4_FD001_web_server.make_handler(api_base))
        cls.web_thread = threading.Thread(target=cls.web_server.serve_forever, daemon=True)
        cls.web_thread.start()
        cls.web_base = f"http://127.0.0.1:{cls.web_server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.web_server.shutdown(); cls.web_server.server_close(); cls.web_thread.join(timeout=5)
        cls.api_server.shutdown(); cls.api_server.server_close(); cls.api_thread.join(timeout=5)

    def fetch(self, path, method="GET"):
        request = Request(self.web_base + path, method=method)
        try:
            with urlopen(request, timeout=20) as response:
                return response.status, response.headers.get("Content-Type"), response.read()
        except HTTPError as error:
            return error.code, error.headers.get("Content-Type"), error.read()

    def test_ui_assets_are_served_locally(self):
        for path, marker in (("/", b"FD001 Engine Health Analysis"), ("/", b"Raw index"), ("/app.js", b"/api/catalog"), ("/styles.css", b"--ink:")):
            with self.subTest(path=path):
                status, _, body = self.fetch(path)
                self.assertEqual(status, 200)
                self.assertIn(marker, body)
        _, _, app = self.fetch("/app.js")
        self.assertNotIn(b"data/FD001/", app)

    def test_proxy_forwards_success_payload_unchanged(self):
        api_url = f"http://127.0.0.1:{self.api_server.server_port}/api/history?split=train&unit=1&sensor=7&start=1&end=3"
        with urlopen(api_url, timeout=20) as direct:
            direct_status, direct_body = direct.status, direct.read()
        web_status, content_type, web_body = self.fetch("/api/history?split=train&unit=1&sensor=7&start=1&end=3")
        self.assertEqual(web_status, direct_status)
        self.assertEqual(content_type, "application/json; charset=utf-8")
        self.assertEqual(web_body, direct_body)
        payload = json.loads(web_body)
        self.assertEqual(payload["data"]["actual_count"], 3)

    def test_proxy_preserves_upstream_error_status_and_body(self):
        status, content_type, body = self.fetch("/api/units?split=FD002")
        self.assertEqual(status, 400)
        self.assertEqual(content_type, "application/json; charset=utf-8")
        self.assertEqual(json.loads(body)["error"]["code"], "INVALID_SPLIT")

    def test_proxy_unavailable_error_is_safe(self):
        server = M4_FD001_web_server.ThreadingHTTPServer(("127.0.0.1", 0), M4_FD001_web_server.make_handler("http://127.0.0.1:1"))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            request = Request(f"http://127.0.0.1:{server.server_port}/api/health")
            with self.assertRaises(HTTPError) as caught:
                urlopen(request, timeout=10)
            self.assertEqual(caught.exception.code, 503)
            payload = json.loads(caught.exception.read())
            self.assertEqual(payload["error"]["code"], "DATA_SOURCE_UNAVAILABLE")
            self.assertNotIn("traceback", payload["error"]["message"].lower())
        finally:
            server.shutdown(); server.server_close(); thread.join(timeout=5)

    def test_mutation_methods_are_rejected(self):
        for method in ("POST", "PUT", "PATCH", "DELETE"):
            with self.subTest(method=method):
                status, _, body = self.fetch("/api/history", method=method)
                self.assertEqual(status, 405)
                self.assertFalse(json.loads(body)["ok"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
