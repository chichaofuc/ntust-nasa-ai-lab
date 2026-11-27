# M4 FD001 UI / API / Raw CSV Reconciliation

Values below came from real browser UI table rows, captured JSON responses to the UI's actual M3 API fetches, and the original read-only FD001 physical source lines.
Sensor IDs are 1-based; raw data columns are 0-based. Physical source lines are 1-based.

| Scenario | Split | Unit | Cycle | Sensor ID / field | Raw index | UI value | Browser API value | Source file | Source line | Raw CSV token | Match |
|---|---|---:|---:|---|---:|---:|---:|---|---:|---:|---|
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 1 | 7 / `sensor_07` | 11 | 554.53 | 554.53 | `data/FD001/train_FD001.txt` | 193 | 554.53 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 2 | 7 / `sensor_07` | 11 | 554.77 | 554.77 | `data/FD001/train_FD001.txt` | 194 | 554.77 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 3 | 7 / `sensor_07` | 11 | 555.14 | 555.14 | `data/FD001/train_FD001.txt` | 195 | 555.14 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 4 | 7 / `sensor_07` | 11 | 554.25 | 554.25 | `data/FD001/train_FD001.txt` | 196 | 554.25 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 5 | 7 / `sensor_07` | 11 | 555.12 | 555.12 | `data/FD001/train_FD001.txt` | 197 | 555.12 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 6 | 7 / `sensor_07` | 11 | 554.98 | 554.98 | `data/FD001/train_FD001.txt` | 198 | 554.98 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 7 | 7 / `sensor_07` | 11 | 554.84 | 554.84 | `data/FD001/train_FD001.txt` | 199 | 554.84 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 8 | 7 / `sensor_07` | 11 | 554.65 | 554.65 | `data/FD001/train_FD001.txt` | 200 | 554.65 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 9 | 7 / `sensor_07` | 11 | 554.69 | 554.69 | `data/FD001/train_FD001.txt` | 201 | 554.69 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 10 | 7 / `sensor_07` | 11 | 554.63 | 554.63 | `data/FD001/train_FD001.txt` | 202 | 554.63 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 11 | 7 / `sensor_07` | 11 | 554.7 | 554.7 | `data/FD001/train_FD001.txt` | 203 | 554.70 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 12 | 7 / `sensor_07` | 11 | 554.57 | 554.57 | `data/FD001/train_FD001.txt` | 204 | 554.57 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 13 | 7 / `sensor_07` | 11 | 554.69 | 554.69 | `data/FD001/train_FD001.txt` | 205 | 554.69 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 14 | 7 / `sensor_07` | 11 | 554.47 | 554.47 | `data/FD001/train_FD001.txt` | 206 | 554.47 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 15 | 7 / `sensor_07` | 11 | 554.17 | 554.17 | `data/FD001/train_FD001.txt` | 207 | 554.17 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 16 | 7 / `sensor_07` | 11 | 554.53 | 554.53 | `data/FD001/train_FD001.txt` | 208 | 554.53 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 17 | 7 / `sensor_07` | 11 | 553.62 | 553.62 | `data/FD001/train_FD001.txt` | 209 | 553.62 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 18 | 7 / `sensor_07` | 11 | 554.83 | 554.83 | `data/FD001/train_FD001.txt` | 210 | 554.83 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 19 | 7 / `sensor_07` | 11 | 555.25 | 555.25 | `data/FD001/train_FD001.txt` | 211 | 555.25 | PASS |
| Train Unit 2 Sensor 7 Cycle 1–20 | train | 2 | 20 | 7 / `sensor_07` | 11 | 554.64 | 554.64 | `data/FD001/train_FD001.txt` | 212 | 554.64 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 3 | 11 / `sensor_11` | 15 | 47.22 | 47.22 | `data/FD001/train_FD001.txt` | 195 | 47.22 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 4 | 11 / `sensor_11` | 15 | 47.1 | 47.1 | `data/FD001/train_FD001.txt` | 196 | 47.10 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 5 | 11 / `sensor_11` | 15 | 47.25 | 47.25 | `data/FD001/train_FD001.txt` | 197 | 47.25 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 6 | 11 / `sensor_11` | 15 | 47.05 | 47.05 | `data/FD001/train_FD001.txt` | 198 | 47.05 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 7 | 11 / `sensor_11` | 15 | 47.1 | 47.1 | `data/FD001/train_FD001.txt` | 199 | 47.10 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 8 | 11 / `sensor_11` | 15 | 47.2 | 47.2 | `data/FD001/train_FD001.txt` | 200 | 47.20 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 9 | 11 / `sensor_11` | 15 | 47.14 | 47.14 | `data/FD001/train_FD001.txt` | 201 | 47.14 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 10 | 11 / `sensor_11` | 15 | 47.21 | 47.21 | `data/FD001/train_FD001.txt` | 202 | 47.21 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 11 | 11 / `sensor_11` | 15 | 47.21 | 47.21 | `data/FD001/train_FD001.txt` | 203 | 47.21 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 12 | 11 / `sensor_11` | 15 | 47.13 | 47.13 | `data/FD001/train_FD001.txt` | 204 | 47.13 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 13 | 11 / `sensor_11` | 15 | 47.03 | 47.03 | `data/FD001/train_FD001.txt` | 205 | 47.03 | PASS |
| Train Unit 2 Sensor 11 Cycle 3–14 | train | 2 | 14 | 11 / `sensor_11` | 15 | 47.12 | 47.12 | `data/FD001/train_FD001.txt` | 206 | 47.12 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 1 | 7 / `sensor_07` | 11 | 554.36 | 554.36 | `data/FD001/train_FD001.txt` | 1 | 554.36 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 2 | 7 / `sensor_07` | 11 | 553.75 | 553.75 | `data/FD001/train_FD001.txt` | 2 | 553.75 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 3 | 7 / `sensor_07` | 11 | 554.26 | 554.26 | `data/FD001/train_FD001.txt` | 3 | 554.26 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 4 | 7 / `sensor_07` | 11 | 554.45 | 554.45 | `data/FD001/train_FD001.txt` | 4 | 554.45 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 5 | 7 / `sensor_07` | 11 | 554 | 554 | `data/FD001/train_FD001.txt` | 5 | 554.00 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 6 | 7 / `sensor_07` | 11 | 554.67 | 554.67 | `data/FD001/train_FD001.txt` | 6 | 554.67 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 7 | 7 / `sensor_07` | 11 | 554.34 | 554.34 | `data/FD001/train_FD001.txt` | 7 | 554.34 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 8 | 7 / `sensor_07` | 11 | 553.85 | 553.85 | `data/FD001/train_FD001.txt` | 8 | 553.85 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 9 | 7 / `sensor_07` | 11 | 553.69 | 553.69 | `data/FD001/train_FD001.txt` | 9 | 553.69 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 10 | 7 / `sensor_07` | 11 | 553.59 | 553.59 | `data/FD001/train_FD001.txt` | 10 | 553.59 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 11 | 7 / `sensor_07` | 11 | 554.54 | 554.54 | `data/FD001/train_FD001.txt` | 11 | 554.54 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 12 | 7 / `sensor_07` | 11 | 554.52 | 554.52 | `data/FD001/train_FD001.txt` | 12 | 554.52 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 13 | 7 / `sensor_07` | 11 | 553.44 | 553.44 | `data/FD001/train_FD001.txt` | 13 | 553.44 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 14 | 7 / `sensor_07` | 11 | 554.48 | 554.48 | `data/FD001/train_FD001.txt` | 14 | 554.48 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 15 | 7 / `sensor_07` | 11 | 553.64 | 553.64 | `data/FD001/train_FD001.txt` | 15 | 553.64 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 16 | 7 / `sensor_07` | 11 | 553.94 | 553.94 | `data/FD001/train_FD001.txt` | 16 | 553.94 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 17 | 7 / `sensor_07` | 11 | 553.8 | 553.8 | `data/FD001/train_FD001.txt` | 17 | 553.80 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 18 | 7 / `sensor_07` | 11 | 554.2 | 554.2 | `data/FD001/train_FD001.txt` | 18 | 554.20 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 19 | 7 / `sensor_07` | 11 | 554.18 | 554.18 | `data/FD001/train_FD001.txt` | 19 | 554.18 | PASS |
| Train Unit 1 Sensor 7 Cycle 1–20 | train | 1 | 20 | 7 / `sensor_07` | 11 | 554.81 | 554.81 | `data/FD001/train_FD001.txt` | 20 | 554.81 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 1 | 7 / `sensor_07` | 11 | 553.14 | 553.14 | `data/FD001/test_FD001.txt` | 32 | 553.14 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 2 | 7 / `sensor_07` | 11 | 553.53 | 553.53 | `data/FD001/test_FD001.txt` | 33 | 553.53 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 3 | 7 / `sensor_07` | 11 | 553.34 | 553.34 | `data/FD001/test_FD001.txt` | 34 | 553.34 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 4 | 7 / `sensor_07` | 11 | 554.15 | 554.15 | `data/FD001/test_FD001.txt` | 35 | 554.15 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 5 | 7 / `sensor_07` | 11 | 553.98 | 553.98 | `data/FD001/test_FD001.txt` | 36 | 553.98 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 6 | 7 / `sensor_07` | 11 | 553.79 | 553.79 | `data/FD001/test_FD001.txt` | 37 | 553.79 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 7 | 7 / `sensor_07` | 11 | 553.56 | 553.56 | `data/FD001/test_FD001.txt` | 38 | 553.56 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 8 | 7 / `sensor_07` | 11 | 553.16 | 553.16 | `data/FD001/test_FD001.txt` | 39 | 553.16 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 9 | 7 / `sensor_07` | 11 | 553.25 | 553.25 | `data/FD001/test_FD001.txt` | 40 | 553.25 | PASS |
| Test Unit 2 Sensor 7 Cycle 1–10 | test | 2 | 10 | 7 / `sensor_07` | 11 | 553.45 | 553.45 | `data/FD001/test_FD001.txt` | 41 | 553.45 | PASS |

Compared 62 actual displayed rows across Train and Test; 62/62 passed exact parsed numeric and provenance comparisons.
