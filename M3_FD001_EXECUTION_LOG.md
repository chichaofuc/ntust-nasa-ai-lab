# M3 FD001 Read-only API Execution Log

**Work Item:** `M3_FD001_READONLY_API_001`
**Authority / return:** STUDENT-MAIN authorization; STUDENT-WEB dispatch; return to STUDENT-WEB Brain.
**Workspace:** `C:\Users\as555\Desktop\20261123_AI\20261123_AI`
**Branch:** `main`
**Python:** 3.13.14; Python standard library only.
**Execution date:** 2026-11-27, Asia/Taipei.

## Governance preflight

Before implementation, GitHub `main` was independently read at `f2f26d531d80e6afe4a6f134ca70a7906b2c2065`. Remote governance blobs: `AGENTS.md` `a35b499b9679af8d9a6a9518db1a1f8e931a9476`; `ROADMAP.md` `2159fd52a33eee6f7adaa62fc511757610628199`; `WORK_ITEM.md` `37e60107cf35140e04407724f705e87be18b51ae`; `DECISIONS.md` `95eaaed3717b60245e03157531d20fad6813a11b`; `M2_FD001_DATA_CONTRACT.md` `05a617f80efc562430718ec90ea8f9a16b01daac`; `M2_FD001_FILE_INVENTORY.md` `6b0202edef49e99725b259c1284cea6dfd4d7674`.

The dispatch snapshot HEAD was current remote `main`. Local `main` was `599330b39b9a484ec89115e21ea5977dd1d5be71`, tracked tree clean, and behind by four commits limited to governance files. Local `main` was fast-forwarded to `f2f26d531d80e6afe4a6f134ca70a7906b2c2065`; no local user changes were overwritten. Only files under M2-verified `data/FD001/` were accessed. Pre-existing unrelated untracked user items and the untracked `data/` directory were left untouched.

## Source verification and integrity

Source files were checked before implementation and again after API tests and reconciliation. All values matched the M2 inventory:

| Source | Bytes | Physical / parsed rows | Columns | SHA-256 before | SHA-256 after |
|---|---:|---:|---:|---|---|
| `data/FD001/train_FD001.txt` | 3515356 | 20631 / 20631 | 26 | `963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8` | `963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8` |
| `data/FD001/test_FD001.txt` | 2228855 | 13096 / 13096 | 26 | `3CDA7109CE17BAFB5443F2AC926CFCF88154B941B8C4CF95EB55D1DDD6F52851` | `3CDA7109CE17BAFB5443F2AC926CFCF88154B941B8C4CF95EB55D1DDD6F52851` |
| `data/FD001/RUL_FD001.txt` | 429 | 100 / 100 | 1 | `A19C8EC94931949D0485BDC35118206E9C81C4547B422EFB9CF86F4CEDDBCECA` | `A19C8EC94931949D0485BDC35118206E9C81C4547B422EFB9CF86F4CEDDBCECA` |

Inputs were ASCII whitespace-delimited numeric text with the verified widths. Files were never written, copied into the repository, or staged. No synthetic data, other NASA partition, downloaded source, fixture records, or generated sample rows were used. The schema-error parser test uses only one malformed in-memory byte string, not a dataset row.

## Implementation and workspace inventory

This Work Item added only these eight API/test/documentation/evidence files:

| File | Purpose |
|---|---|
| `M3_FD001_api.py` | Read-only local HTTP API and application entry point. |
| `test_M3_FD001_api.py` | Standard-library HTTP, validation, provenance, and integrity tests. |
| `M3_FD001_reconcile.py` | Reproducibly compares real Train/Test source lines with live API responses. |
| `M3_FD001_API_CONTRACT.md` | Endpoint, schema, errors, provenance, read-only and limitation contract. |
| `M3_FD001_SOURCE_ROW_RECONCILIATION.md` | Forty generated raw-to-API comparison rows. |
| `M3_FD001_TEST_EXECUTION_LOG.md` | Captured final test output. |
| `M3_FD001_EXECUTION_LOG.md` | This execution, integrity, and Git evidence record. |
| `README.md` | Run and verification instructions. |

The API reads only the three sources, validates size/hash/format and verified row/Unit/Cycle invariants, and returns original 1-based physical line provenance. Sensor IDs are 1-based (`sensor=7` → `sensor_07` → raw index 11). RUL values and row mapping are not exposed; the catalog identifies the RUL source and states the positional mapping limitation. Only GET data routes are implemented; POST/PUT/PATCH/DELETE return 405. Errors contain no absolute filesystem paths or tracebacks.

## Commands and execution evidence

- `python --version` → `Python 3.13.14`.
- `python -m unittest -v test_M3_FD001_api.py` → final run started `2026-11-27T01:21:28.1741571+08:00`, finished `2026-11-27T01:21:31.4435699+08:00`; exit code 0; 17 tests passed in 2.670 seconds. Captured output is in `M3_FD001_TEST_EXECUTION_LOG.md`.
- The first test run exposed a Unit first-occurrence index construction bug. It was corrected before final verification; that run was not accepted as passing evidence.
- `python M3_FD001_reconcile.py` → exit code 0; actual local API server returned 20 Train and 20 Test records, all 40 source value, Unit, Cycle, sensor mapping, physical source-line, and provenance comparisons matched. See `M3_FD001_SOURCE_ROW_RECONCILIATION.md`.
- Entry-point smoke run: `python M3_FD001_api.py` with `FD001_API_PORT=18765`; actual process started successfully, `/api/health` returned HTTP 200 with `source_validation=PASS`, and `/api/history?split=train&unit=1&sensor=7&start=1&end=20` returned HTTP 200 with 20 records and `sensor_07` raw index 11. Captured stdout: `Serving NASA_CMAPSS_FD001 read-only API at http://127.0.0.1:18765`; stderr recorded the two successful GET requests and no errors. The smoke-test process was stopped after verification.
- `git diff --check` → passed before staging.
- The server re-hashes all three source files before every response, including cache hits. Source hashes after tests, reconciliation, and CLI smoke verification remain identical to the verified values above.

## Git and remote evidence

At the time this log was first prepared, the authorized M3 files were ready for review and commit to the existing `main`; no raw or unrelated file was staged. The implementation commit SHA, parent SHA, changed-file list, push result, final remote HEAD, and remote readback of all eight files are recorded in the Worker Return after the authorized commits and post-push verification. The execution-log commit's own SHA is also reported there to avoid circular self-reference inside this log.

M3 scope only: the FD001 read-only API, API tests, source-row reconciliation, documentation, and execution evidence. No frontend, ML, diagnosis, M4, M5, or dataset modification was performed. Final M3 acceptance remains with STUDENT-WEB review and the MAIN authority; this Worker does not declare acceptance.
