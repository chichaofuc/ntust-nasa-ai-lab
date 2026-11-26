# M1 Basic Profile — Synthetic Sensor Dataset

**Work Item:** `M1_DATASET_PROFILE_001`
**Current milestone:** `M1_SYNTHETIC_DATASET_PROFILE`
**Profile result:** One logical CSV dataset containing six data records.
**Acceptance:** Not declared; Research Brain review is pending.

## Dataset identity and source integrity

- Logical dataset count: **1**.
- Source: `data/synthetic_sensor.csv`.
- Historical alias: `data/intro/synthetic_sensor.csv`; Owner confirmed it refers to the same logical dataset and must not be counted twice.
- Resolved local path: `C:\Users\as555\Desktop\20261123_AI\20261123_AI\data\synthetic_sensor.csv`.
- Size: **234 bytes**.
- SHA-256 before analysis: `CD536B46EB628909FDC986BBAD956C24A2E50AFB287968998374BEFC62204377`.
- SHA-256 after analysis: `CD536B46EB628909FDC986BBAD956C24A2E50AFB287968998374BEFC62204377`.
- Source remained unchanged and read-only. The raw CSV was not staged or committed.

## Shape and schema

The comma-delimited CSV has a header and **6 data rows × 4 columns**. Each row has four fields; no malformed-width rows were found. Types below are inferred from nonmissing cell values using Python built-ins, not from an external schema.

| Column | Inferred dtype | Data values | Missing | Min | Max | Mean | Median | Sample SD | Constant |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `timestamp` | string | 6 | 0 | N/A | N/A | N/A | N/A | N/A | No |
| `load_pct` | integer | 6 | 0 | 50 | 70 | 63.333333 | 70 | 10.327956 | No |
| `coolant_out_c` | integer | 6 | 0 | 78 | 84 | 81.666667 | 82.5 | 2.581989 | No |
| `oil_pressure_bar` | float | 5 | 1 | 3.8 | 4.0 | 3.9 | 3.9 | 0.1 | No |

Standard deviation is sample standard deviation (`statistics.stdev`). Numeric statistics exclude missing values. No column names are duplicated.

## Duplicate and missing-value results

- Duplicate definition: two data records are duplicates only when their complete field tuples, including string values and blanks, are exactly equal. Header is excluded.
- Exact duplicate excess rows: **1** (one repeated row beyond its first occurrence).
- Duplicate group: `2026-01-01T10:04:00,70,84,3.8` occurs twice.
- Missing cells are empty or whitespace-only CSV fields.
- Missing by column: `timestamp` 0; `load_pct` 0; `coolant_out_c` 0; `oil_pressure_bar` 1.
- Total missing cells: **1**; rows containing at least one missing cell: **1**.
- Constant columns: **none**.

## Data-quality observations and limits

**OBSERVATION:** Six data rows and four columns were parsed. One exact repeated row and one blank `oil_pressure_bar` cell were found. Timestamps run from 10:00 to 10:04 at minute intervals, with 10:04 appearing in two rows. Numeric ranges and summaries are shown above.

**INFERENCE:** The timestamp-shaped values and column names suggest time-indexed sensor readings. This is a limited interpretation of field names and values only.

**UNKNOWN:** No data dictionary or independent source establishes equipment identity, calibration, sampling guarantees, operating context, exact field semantics, or valid/normal ranges. The column names suggest units, but those units are not independently verified. These descriptive statistics do not establish a health baseline, fault threshold, diagnosis, or equipment health state.

## Status

This report profiles the one authorized logical dataset and its six records. M1 remains subject to independent Research Brain review; this Worker does not declare M1 accepted.
