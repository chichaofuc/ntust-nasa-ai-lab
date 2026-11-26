# M1 Basic Profile — Partial Evidence; Work Item Incomplete

**Work Item:** `M1_DATASET_PROFILE_001`
**Execution status:** `PARTIAL / INCOMPLETE`
**Repository baseline:** `9e070fcfb033b90d0bd3952487b53cfae60a5708`
**Input scope:** Synthetic CSV only. NASA C-MAPSS is out of scope.

## Inventory result

The repository inventory contains **2 CSV paths including this generated inventory deliverable**. One is generated output and is not an input dataset. There is **1 verified logical synthetic dataset**: `data/synthetic_sensor.csv`. The Owner explicitly confirmed that `data/synthetic_sensor.csv` and the historical reference `data/intro/synthetic_sensor.csv` refer to the same logical dataset. The historical path does not exist locally. Thus only **1 of the 6 intended datasets** is present and verified; five intended datasets are not available. No substitute was used.

The source file is 234 bytes and has SHA-256 `CD536B46EB628909FDC986BBAD956C24A2E50AFB287968998374BEFC62204377` both before and after reading. It remains unmodified and untracked.

## Observations — actual file

Parsing used Python's standard-library `csv` module with strict row parsing. The file is valid UTF-8 CSV, comma-delimited, with header plus 6 data rows and 4 columns. One exact duplicate data row is present (the two `2026-01-01T10:04:00,70,84,3.8` records). There are no duplicate column names and no malformed rows. There are no entirely blank rows. One field value is missing: `oil_pressure_bar` in the `10:03` row. No non-numeric values occur in numeric columns; the `timestamp` field is textual and looks timestamp-shaped, but was not assigned a datetime type by schema or contract. Column types below are inferred from observed values only.

| Field | Inferred type | Missing | Non-numeric/non-finite | Min | Q1 | Median | Q3 | Max | Mean | Sample SD | Constant |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `timestamp` | string | 0 | 6 (expected nonnumeric for string) | — | — | — | — | — | — | — | No |
| `load_pct` | integer-like | 0 | 0 | 50 | 55 | 70 | 70 | 70 | 63.3333 | 10.3280 | No |
| `coolant_out_c` | integer-like | 0 | 0 | 78 | 79.75 | 82.5 | 83.75 | 84 | 81.6667 | 2.5820 | No |
| `oil_pressure_bar` | numeric | 1 | 0 | 3.8 | 3.8 | 3.9 | 4.0 | 4.0 | 3.9 | 0.1000 | No |

Quartiles use inclusive linear interpolation. Standard deviation is sample SD; for timestamp, numeric statistics are not applicable. Duplicate-column check was exact header equality. Missing check treats empty/whitespace-only cells as missing. No domain schema or valid ranges were supplied, so domain-invalid values cannot be determined.

## Semantics and limits

**OBSERVATION:** The header names suggest timestamp, load percentage, coolant outlet temperature in degrees C, and oil pressure in bar. Timestamp strings advance by one minute from 10:00 through 10:04, with the final timestamp repeated once. The values in load and coolant fields change across these six rows; oil pressure has one missing reading and otherwise ranges from 3.8 to 4.0.

**INFERENCE:** The rows may represent time-ordered measurements, based on the `timestamp` header and observed minute-spaced values. This is only a name/value-pattern inference; equipment identity, sensor calibration, sampling policy, and operational context are not established.

**UNKNOWN:** Actual field definitions, units/measurement accuracy, equipment or sensor identity, expected time cadence, validity limits, and whether any value indicates abnormality. No health baseline or fault threshold is established. These observations do not diagnose equipment or sensor faults.

## Stop event and status

**STOP_EVENT:** Fewer than six intended datasets were verified.
**Observed evidence:** One logical source dataset at `data/synthetic_sensor.csv`; five expected datasets are absent from the discovered input inventory.
**Impact:** This is partial profiling only. `M1_DATASET_PROFILE_001` is not complete and is not accepted; no later milestone is authorized.
**Waiting for:** STUDENT-RESEARCH Brain review/instruction.

Previous stop evidence is retained in `M1_EXECUTION_LOG.md`; this profile records the supplemental run and does not replace historical governance records.
