# NTUST NASA AI Lab — FD001 Read-only API (M3)

This repository currently contains a local, read-only HTTP API for the M2-verified NASA C-MAPSS FD001 sources. It uses Python's standard library only and does not include a frontend, ML model, fault diagnosis, or M4 Evidence Prompt implementation.

## Requirements and run

- Python 3.11 or later (verified with Python 3.13.14).
- Keep the three original source files under `data/FD001/` with the verified bytes and SHA-256 values documented in [M3_FD001_API_CONTRACT.md](M3_FD001_API_CONTRACT.md).
- Start locally: `python M3_FD001_api.py`
- Default address: `http://127.0.0.1:8000`. Optional `FD001_API_HOST` and `FD001_API_PORT` environment variables configure the local bind address and port.

## Read-only endpoints

- `GET /api/health`
- `GET /api/catalog`
- `GET /api/units?split=train`
- `GET /api/units?split=test`
- `GET /api/history?split=train&unit=1&sensor=7&start=1&end=20`

Only GET requests are supported. See [API contract](M3_FD001_API_CONTRACT.md) for response fields, errors, validation, provenance, and semantic limits.

## Verification

- Run API tests: `python -m unittest -v test_M3_FD001_api.py`
- Regenerate actual Train/Test source-line comparison: `python M3_FD001_reconcile.py`
- See [test execution log](M3_FD001_TEST_EXECUTION_LOG.md), [source-row reconciliation](M3_FD001_SOURCE_ROW_RECONCILIATION.md), and [M3 execution log](M3_FD001_EXECUTION_LOG.md).

The API never downloads, modifies, or writes source data. It verifies all three expected source-file hashes before serving data and preserves each original physical line number.
