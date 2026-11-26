# M3 FD001 Read-only API Contract

## Dataset and trusted sources

Dataset ID: `NASA_CMAPSS_FD001`; schema reference: `M2_FD001_DATA_CONTRACT.md`. The server reads exactly these local files and checks byte size, SHA-256, ASCII decoding, row width, finite numeric parsing, verified row counts, Unit/Cycle keys, and contiguous cycles before responding:

| Split / role | Relative file | Bytes | Rows | Columns | SHA-256 |
|---|---|---:|---:|---:|---|
| Train | `data/FD001/train_FD001.txt` | 3515356 | 20631 | 26 | `963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8` |
| Test | `data/FD001/test_FD001.txt` | 2228855 | 13096 | 26 | `3CDA7109CE17BAFB5443F2AC926CFCF88154B941B8C4CF95EB55D1DDD6F52851` |
| RUL metadata / integrity only | `data/FD001/RUL_FD001.txt` | 429 | 100 | 1 | `A19C8EC94931949D0485BDC35118206E9C81C4547B422EFB9CF86F4CEDDBCECA` |

The API does not return RUL values or an RUL mapping endpoint. The catalog states that RUL rows correspond positionally to Test Unit first-occurrence order 1–100 but have no in-file Unit ID key; they are not per-Cycle Test labels. No RUL values are attached to history records.

## Schema and mappings

Raw columns are 0-based: `unit_id` 0, `cycle` 1, operating settings 2–4, and `sensor_01` through `sensor_21` at columns 5–25. The API's `sensor_id` is 1-based, so `sensor_id=7` maps to `sensor_07`, raw column index 11. Unit IDs are split-local; Train and Test timelines are never joined. Sensor meanings, units, and operating-setting physical meanings/units are `UNKNOWN`.

## Endpoints

### `GET /api/health`

Returns service identity, dataset identity, `data_loaded`, `source_validation`, and all verified source hashes. If a file is missing, hash/size differs, or validation fails, returns HTTP 503 and never reports healthy.

### `GET /api/catalog`

Returns dataset/contract IDs, Train/Test counts and observed Cycle ranges, schema fields and raw indices, 1-based sensor mapping, source file sizes/hashes, provenance rules, and semantic limitations. Counts/ranges are calculated from the validated local sources.

### `GET /api/units?split=train|test`

Requires exactly one `split` query parameter. Returns only that split's actual Unit IDs, first/last Cycle, and cycle count.

### `GET /api/history?split=train|test&unit=N&sensor=N&start=N&end=N`

Requires all five parameters exactly once. Cycle range is inclusive and must have both endpoints within the selected Unit's observed cycles. Every record includes `split`, `unit_id`, `cycle`, 1-based `sensor_id`, canonical `sensor_field`, `raw_column_index`, `value`, relative `source_file`, and 1-based original physical `source_line`.

## JSON and errors

Success: `{"ok":true,"data":{},"provenance":{}}`. Error: `{"ok":false,"error":{"code":"...","message":"..."}}`. JSON serialization disallows NaN/Infinity; Python `None`, if used, serializes as JSON `null`. Current source has no missing cells and the API does not impute.

| HTTP | Error code | Meaning |
|---:|---|---|
| 400 | `INVALID_PARAMETER` | Missing, repeated, extra, or malformed query parameter. |
| 400 | `INVALID_SPLIT` | Split is not `train` or `test`. |
| 404 | `UNIT_NOT_FOUND` | Unit is absent from the selected split. |
| 400 | `SENSOR_NOT_FOUND` | Sensor ID is outside 1–21. |
| 400 | `CYCLE_RANGE_INVALID` | Reversed or unobserved requested Cycle range. |
| 503 | `DATA_SOURCE_UNAVAILABLE` | Missing/invalid source, size/hash mismatch, or schema validation failure. |
| 500 | `INTERNAL_ERROR` | Unexpected server error; response does not expose traceback or absolute paths. |
| 405 | `INVALID_PARAMETER` | Non-GET methods are not supported. |

## Read-only and limitations

The service exposes only GET data routes; POST, PUT, PATCH, and DELETE return 405. It does not alter source data, make a normalized copy, or write data. No fault labels, verified sensor physical meanings, healthy baseline, physical thresholds, or failure diagnosis are provided. A Train trajectory's last observed Cycle is not asserted as a physical failure event.
