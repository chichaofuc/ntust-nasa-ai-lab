# M4 Frontend Test Execution Log

- Command: python -m unittest -v test_M4_frontend
- Started: 2026-11-27T11:43:19.1868954+08:00
- Finished: 2026-11-27T11:43:23.5579662+08:00
- Exit code: 0
- Python: Python 3.13.14
- Result: PASS

## Actual stdout/stderr

```text
test_mutation_methods_are_rejected (test_M4_frontend.M4FrontendTest.test_mutation_methods_are_rejected) ... 27/Nov/2026 11:43:19 - "POST /api/history HTTP/1.1" 405 -
27/Nov/2026 11:43:19 - "PUT /api/history HTTP/1.1" 405 -
27/Nov/2026 11:43:19 - "PATCH /api/history HTTP/1.1" 405 -
27/Nov/2026 11:43:19 - "DELETE /api/history HTTP/1.1" 405 -
ok
test_proxy_forwards_success_payload_unchanged (test_M4_frontend.M4FrontendTest.test_proxy_forwards_success_payload_unchanged) ... 27/Nov/2026 11:43:19 - "GET /api/history?split=train&unit=1&sensor=7&start=1&end=3 HTTP/1.1" 200 -
27/Nov/2026 11:43:19 - "GET /api/history?split=train&unit=1&sensor=7&start=1&end=3 HTTP/1.1" 200 -
27/Nov/2026 11:43:19 - "GET /api/history?split=train&unit=1&sensor=7&start=1&end=3 HTTP/1.1" 200 -
ok
test_proxy_preserves_upstream_error_status_and_body (test_M4_frontend.M4FrontendTest.test_proxy_preserves_upstream_error_status_and_body) ... 27/Nov/2026 11:43:19 - "GET /api/units?split=FD002 HTTP/1.1" 400 -
27/Nov/2026 11:43:19 - "GET /api/units?split=FD002 HTTP/1.1" 400 -
ok
test_proxy_unavailable_error_is_safe (test_M4_frontend.M4FrontendTest.test_proxy_unavailable_error_is_safe) ... 27/Nov/2026 11:43:22 - "GET /api/health HTTP/1.1" 503 -
ok
test_ui_assets_are_served_locally (test_M4_frontend.M4FrontendTest.test_ui_assets_are_served_locally) ... 27/Nov/2026 11:43:22 - "GET / HTTP/1.1" 200 -
27/Nov/2026 11:43:22 - "GET / HTTP/1.1" 200 -
27/Nov/2026 11:43:22 - "GET /app.js HTTP/1.1" 200 -
27/Nov/2026 11:43:22 - "GET /styles.css HTTP/1.1" 200 -
27/Nov/2026 11:43:22 - "GET /app.js HTTP/1.1" 200 -
ok

----------------------------------------------------------------------
Ran 5 tests in 3.962s

OK
```
