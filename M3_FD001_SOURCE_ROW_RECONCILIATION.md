# M3 FD001 Raw Source Row Reconciliation

Actual local HTTP API responses were compared with the exact original physical lines in the M2-verified source files.

Query per split: `/api/history?split={train|test}&unit=1&sensor=7&start=1&end=20`.
Sensor API ID 7 maps to `sensor_07`, raw column index 11 (0-based). Physical source lines are 1-based.
Each comparison was generated from the raw source and actual HTTP response; all numeric comparisons use parsed source numeric values without rounding.

| Split | Exact source file | Cycle | Raw source physical line | Raw Sensor 7 value | API Sensor 7 value | Raw column index | API source line | Match |
|---|---|---:|---:|---:|---:|---:|---:|---|
| train | `data/FD001/train_FD001.txt` | 1 | 1 | 554.36 | 554.36 | 11 | 1 | PASS |
| train | `data/FD001/train_FD001.txt` | 2 | 2 | 553.75 | 553.75 | 11 | 2 | PASS |
| train | `data/FD001/train_FD001.txt` | 3 | 3 | 554.26 | 554.26 | 11 | 3 | PASS |
| train | `data/FD001/train_FD001.txt` | 4 | 4 | 554.45 | 554.45 | 11 | 4 | PASS |
| train | `data/FD001/train_FD001.txt` | 5 | 5 | 554 | 554 | 11 | 5 | PASS |
| train | `data/FD001/train_FD001.txt` | 6 | 6 | 554.67 | 554.67 | 11 | 6 | PASS |
| train | `data/FD001/train_FD001.txt` | 7 | 7 | 554.34 | 554.34 | 11 | 7 | PASS |
| train | `data/FD001/train_FD001.txt` | 8 | 8 | 553.85 | 553.85 | 11 | 8 | PASS |
| train | `data/FD001/train_FD001.txt` | 9 | 9 | 553.69 | 553.69 | 11 | 9 | PASS |
| train | `data/FD001/train_FD001.txt` | 10 | 10 | 553.59 | 553.59 | 11 | 10 | PASS |
| train | `data/FD001/train_FD001.txt` | 11 | 11 | 554.54 | 554.54 | 11 | 11 | PASS |
| train | `data/FD001/train_FD001.txt` | 12 | 12 | 554.52 | 554.52 | 11 | 12 | PASS |
| train | `data/FD001/train_FD001.txt` | 13 | 13 | 553.44 | 553.44 | 11 | 13 | PASS |
| train | `data/FD001/train_FD001.txt` | 14 | 14 | 554.48 | 554.48 | 11 | 14 | PASS |
| train | `data/FD001/train_FD001.txt` | 15 | 15 | 553.64 | 553.64 | 11 | 15 | PASS |
| train | `data/FD001/train_FD001.txt` | 16 | 16 | 553.94 | 553.94 | 11 | 16 | PASS |
| train | `data/FD001/train_FD001.txt` | 17 | 17 | 553.8 | 553.8 | 11 | 17 | PASS |
| train | `data/FD001/train_FD001.txt` | 18 | 18 | 554.2 | 554.2 | 11 | 18 | PASS |
| train | `data/FD001/train_FD001.txt` | 19 | 19 | 554.18 | 554.18 | 11 | 19 | PASS |
| train | `data/FD001/train_FD001.txt` | 20 | 20 | 554.81 | 554.81 | 11 | 20 | PASS |
| test | `data/FD001/test_FD001.txt` | 1 | 1 | 553.9 | 553.9 | 11 | 1 | PASS |
| test | `data/FD001/test_FD001.txt` | 2 | 2 | 554.85 | 554.85 | 11 | 2 | PASS |
| test | `data/FD001/test_FD001.txt` | 3 | 3 | 554.11 | 554.11 | 11 | 3 | PASS |
| test | `data/FD001/test_FD001.txt` | 4 | 4 | 554.07 | 554.07 | 11 | 4 | PASS |
| test | `data/FD001/test_FD001.txt` | 5 | 5 | 554.16 | 554.16 | 11 | 5 | PASS |
| test | `data/FD001/test_FD001.txt` | 6 | 6 | 554.22 | 554.22 | 11 | 6 | PASS |
| test | `data/FD001/test_FD001.txt` | 7 | 7 | 553.89 | 553.89 | 11 | 7 | PASS |
| test | `data/FD001/test_FD001.txt` | 8 | 8 | 553.59 | 553.59 | 11 | 8 | PASS |
| test | `data/FD001/test_FD001.txt` | 9 | 9 | 554.49 | 554.49 | 11 | 9 | PASS |
| test | `data/FD001/test_FD001.txt` | 10 | 10 | 554.28 | 554.28 | 11 | 10 | PASS |
| test | `data/FD001/test_FD001.txt` | 11 | 11 | 554.69 | 554.69 | 11 | 11 | PASS |
| test | `data/FD001/test_FD001.txt` | 12 | 12 | 554.35 | 554.35 | 11 | 12 | PASS |
| test | `data/FD001/test_FD001.txt` | 13 | 13 | 554.04 | 554.04 | 11 | 13 | PASS |
| test | `data/FD001/test_FD001.txt` | 14 | 14 | 554.66 | 554.66 | 11 | 14 | PASS |
| test | `data/FD001/test_FD001.txt` | 15 | 15 | 554.15 | 554.15 | 11 | 15 | PASS |
| test | `data/FD001/test_FD001.txt` | 16 | 16 | 553.82 | 553.82 | 11 | 16 | PASS |
| test | `data/FD001/test_FD001.txt` | 17 | 17 | 554.42 | 554.42 | 11 | 17 | PASS |
| test | `data/FD001/test_FD001.txt` | 18 | 18 | 553.5 | 553.5 | 11 | 18 | PASS |
| test | `data/FD001/test_FD001.txt` | 19 | 19 | 553.87 | 553.87 | 11 | 19 | PASS |
| test | `data/FD001/test_FD001.txt` | 20 | 20 | 554.31 | 554.31 | 11 | 20 | PASS |

Compared records: 40 (Train 20, Test 20). Result: PASS (40/40 matched).
The API does not serve RUL values or a per-Test-Cycle label. `/api/catalog` reports the RUL file's source identity and explicitly states the positional mapping limitation; no RUL row mapping endpoint is exposed.
