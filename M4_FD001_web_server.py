"""Serve the M4 static UI and transparently forward /api GET requests to M3."""
from __future__ import annotations

import argparse
import json
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
WEB_ROOT = ROOT / "web"


def make_handler(api_base: str):
    upstream_base = api_base.rstrip("/")

    class M4Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(WEB_ROOT), **kwargs)

        def do_GET(self):
            if self.path == "/api" or self.path.startswith("/api/"):
                self._proxy_get()
            else:
                super().do_GET()

        def _proxy_get(self):
            url = upstream_base + self.path
            request = Request(url, headers={"Accept": self.headers.get("Accept", "application/json")}, method="GET")
            try:
                response = urlopen(request, timeout=20)
                status, body, content_type = response.status, response.read(), response.headers.get("Content-Type", "application/json; charset=utf-8")
                response.close()
            except HTTPError as exc:
                status, body, content_type = exc.code, exc.read(), exc.headers.get("Content-Type", "application/json; charset=utf-8")
                exc.close()
            except (URLError, TimeoutError, OSError):
                status = 503
                body = json.dumps({"ok": False, "error": {"code": "DATA_SOURCE_UNAVAILABLE", "message": "The M3 API is unavailable."}}, separators=(",", ":")).encode("utf-8")
                content_type = "application/json; charset=utf-8"
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _method_not_allowed(self):
            body = json.dumps({"ok": False, "error": {"code": "INVALID_PARAMETER", "message": "This application supports GET requests only."}}, separators=(",", ":")).encode("utf-8")
            self.send_response(405)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        do_POST = _method_not_allowed
        do_PUT = _method_not_allowed
        do_PATCH = _method_not_allowed
        do_DELETE = _method_not_allowed

        def log_message(self, fmt, *args):
            sys.stderr.write("%s - %s\n" % (self.log_date_time_string(), fmt % args))

    return M4Handler


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default=os.environ.get("M4_WEB_HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("M4_WEB_PORT", "4173")))
    parser.add_argument("--api-base", default=os.environ.get("M3_API_BASE_URL", "http://127.0.0.1:8000"))
    args = parser.parse_args()
    if not WEB_ROOT.is_dir():
        parser.error("web/ directory is missing")
    if not args.api_base.startswith(("http://127.0.0.1:", "http://localhost:")):
        parser.error("M3 API must use a local loopback URL")
    server = ThreadingHTTPServer((args.host, args.port), make_handler(args.api_base))
    print(f"Serving M4 UI at http://{args.host}:{server.server_port} (M3 API: {args.api_base})", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
