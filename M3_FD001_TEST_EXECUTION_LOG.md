# M3 FD001 API Test Execution Log

- Command: python -m unittest -v test_M3_FD001_api.py
- Python: Python 3.13.14
- Started: 2026-11-27T01:21:28.1741571+08:00
- Finished: 2026-11-27T01:21:31.4435699+08:00
- Exit code: 0
- Stdout/stderr: combined captured process output.
- Result: PASS

Actual test runner output (indented):
    test_catalog_reports_verified_mapping_and_limits (test_M3_FD001_api.APITestCase.test_catalog_reports_verified_mapping_and_limits) ... 27/Nov/2026 01:21:29 - "GET /api/catalog HTTP/1.1" 200 -
    ok
    test_cycle_range_errors (test_M3_FD001_api.APITestCase.test_cycle_range_errors) ... 27/Nov/2026 01:21:29 - "GET /api/history?split=train&unit=1&sensor=7&start=2&end=1 HTTP/1.1" 400 -
    27/Nov/2026 01:21:29 - "GET /api/history?split=train&unit=1&sensor=7&start=1&end=999 HTTP/1.1" 400 -
    ok
    test_hash_mismatch_returns_503 (test_M3_FD001_api.APITestCase.test_hash_mismatch_returns_503) ... 27/Nov/2026 01:21:29 - "GET /api/catalog HTTP/1.1" 503 -
    ok
    test_health_validates_real_sources (test_M3_FD001_api.APITestCase.test_health_validates_real_sources) ... 27/Nov/2026 01:21:29 - "GET /api/health HTTP/1.1" 200 -
    ok
    test_invalid_split (test_M3_FD001_api.APITestCase.test_invalid_split) ... 27/Nov/2026 01:21:29 - "GET /api/units?split=FD002 HTTP/1.1" 400 -
    ok
    test_missing_and_malformed_parameters (test_M3_FD001_api.APITestCase.test_missing_and_malformed_parameters) ... 27/Nov/2026 01:21:29 - "GET /api/units HTTP/1.1" 400 -
    27/Nov/2026 01:21:29 - "GET /api/history?split=train&unit=1&sensor=7&start=1 HTTP/1.1" 400 -
    27/Nov/2026 01:21:29 - "GET /api/history?split=train&unit=1.5&sensor=7&start=1&end=2 HTTP/1.1" 400 -
    ok
    test_missing_source_returns_503_and_not_healthy (test_M3_FD001_api.APITestCase.test_missing_source_returns_503_and_not_healthy) ... 27/Nov/2026 01:21:29 - "GET /api/health HTTP/1.1" 503 -
    ok
    test_null_serializes_as_json_null (test_M3_FD001_api.APITestCase.test_null_serializes_as_json_null) ... ok
    test_schema_mismatch_is_rejected_without_fixture_dataset (test_M3_FD001_api.APITestCase.test_schema_mismatch_is_rejected_without_fixture_dataset) ... ok
    test_sensor_not_found (test_M3_FD001_api.APITestCase.test_sensor_not_found) ... 27/Nov/2026 01:21:30 - "GET /api/history?split=train&unit=1&sensor=22&start=1&end=2 HTTP/1.1" 400 -
    27/Nov/2026 01:21:30 - "GET /api/history?split=train&unit=1&sensor=-1&start=1&end=2 HTTP/1.1" 400 -
    ok
    test_source_hash_is_rechecked_on_cached_requests (test_M3_FD001_api.APITestCase.test_source_hash_is_rechecked_on_cached_requests) ... ok
    test_source_hashes_remain_unchanged (test_M3_FD001_api.APITestCase.test_source_hashes_remain_unchanged) ... ok
    test_test_history_uses_test_only (test_M3_FD001_api.APITestCase.test_test_history_uses_test_only) ... 27/Nov/2026 01:21:30 - "GET /api/history?split=test&unit=1&sensor=7&start=1&end=20 HTTP/1.1" 200 -
    ok
    test_train_history_sensor_7_source_provenance (test_M3_FD001_api.APITestCase.test_train_history_sensor_7_source_provenance) ... 27/Nov/2026 01:21:30 - "GET /api/history?split=train&unit=1&sensor=7&start=1&end=20 HTTP/1.1" 200 -
    ok
    test_unit_not_found (test_M3_FD001_api.APITestCase.test_unit_not_found) ... 27/Nov/2026 01:21:30 - "GET /api/history?split=train&unit=999&sensor=7&start=1&end=2 HTTP/1.1" 404 -
    ok
    test_units_returns_only_selected_split (test_M3_FD001_api.APITestCase.test_units_returns_only_selected_split) ... 27/Nov/2026 01:21:30 - "GET /api/units?split=train HTTP/1.1" 200 -
    27/Nov/2026 01:21:30 - "GET /api/units?split=test HTTP/1.1" 200 -
    ok
    test_write_methods_are_not_exposed (test_M3_FD001_api.APITestCase.test_write_methods_are_not_exposed) ... 27/Nov/2026 01:21:30 - "POST /api/history HTTP/1.1" 405 -
    27/Nov/2026 01:21:30 - "PUT /api/history HTTP/1.1" 405 -
    27/Nov/2026 01:21:30 - "PATCH /api/history HTTP/1.1" 405 -
    27/Nov/2026 01:21:30 - "DELETE /api/history HTTP/1.1" 405 -
    ok

    ----------------------------------------------------------------------
    Ran 17 tests in 2.670s

    OK
