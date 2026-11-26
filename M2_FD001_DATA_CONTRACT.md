# M2 FD001 Data Contract

## Source and file mapping

Use only local `data/FD001/train_FD001.txt`, `test_FD001.txt`, and `RUL_FD001.txt`; identities and hashes are in `M2_FD001_FILE_INVENTORY.md`. Inputs are ASCII, headerless, whitespace-delimited finite numeric rows. Raw files are read-only and never enter Git.

## Canonical positional schema (0-based)

| Raw index | Canonical name | Category | Type | Semantic status | Evidence / limitation |
|---|---|---|---|---|---|
| 0 | unit_id | identifier | integer | VERIFIED | Integral IDs group trajectories; identity is split-local. |
| 1 | cycle | index | integer | VERIFIED | Integral, contiguous sequence from 1 within each observed Unit. |
| 2 | operating_setting_1 | operating setting | numeric | INFERRED | Position/layout only; physical definition and unit unknown. |
| 3 | operating_setting_2 | operating setting | numeric | INFERRED | Position/layout only; physical definition and unit unknown. |
| 4 | operating_setting_3 | operating setting | numeric | INFERRED | Position/layout only; physical definition and unit unknown. |
| 5 | sensor_01 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 6 | sensor_02 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 7 | sensor_03 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 8 | sensor_04 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 9 | sensor_05 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 10 | sensor_06 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 11 | sensor_07 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 12 | sensor_08 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 13 | sensor_09 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 14 | sensor_10 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 15 | sensor_11 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 16 | sensor_12 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 17 | sensor_13 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 18 | sensor_14 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 19 | sensor_15 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 20 | sensor_16 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 21 | sensor_17 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 22 | sensor_18 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 23 | sensor_19 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 24 | sensor_20 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |
| 25 | sensor_21 | sensor slot | numeric | UNKNOWN | Raw slot verified; physical meaning and unit not supplied. |

Unit IDs and Cycle are integer-valued; settings and sensor slots are numeric. Sensor field names are position-based aliases only. Physical identities/units are UNKNOWN.

## Unit and Cycle semantics

Unit IDs index trajectories within each split; equal Train/Test IDs do not prove same physical asset. Cycle is the integer per-Unit observation index. Do not merge Unit timelines. Train's last supplied Cycle is an observed endpoint, not file-level proof of failure.

## Train / Test / RUL relationship

Train has no explicit fault class or RUL column. A value `last_cycle(unit)-cycle` is derivable to the observed endpoint, but true failure RUL depends on an unverified endpoint assumption. Test has no per-Cycle labels. RUL has one integer per Test Unit by row position: Test first-occurrence order is 1..100 and row count is 100. RUL has no Unit ID, so its semantic pairing is a positional contract with a limitation, not an in-file foreign key. RUL is not a fault label.

## Missing policy and validation rules

Require 26 tokens per Train/Test line and one per RUL line; finite numeric conversion; integer-valued Unit/Cycle/RUL; split-local Unit IDs; contiguous increasing per-Unit cycles for this validated input. Reject/report invalid lines; never silently drop or impute. These constraints describe the observed source and parser contract.

## API-ready schema (definition only)

```json
{
  "split": "train|test",
  "unit_id": 1,
  "cycle": 1,
  "operating_settings": [0.0, 0.0, 0.0],
  "sensors": {"sensor_01": 0.0, "sensor_21": 0.0},
  "rul_at_last_observation": null
}
```

A Test RUL may be attached to the trajectory endpoint by positional index with the stated caveat. Do not replicate it as ground truth for each Test Cycle. No website/API is implemented here.

## Known limitations

`BASELINE_STATUS: NOT_ESTABLISHED`. No fault-class labels, verified physical sensor meanings, validated units, maintenance/failure records, healthy ranges, or fault thresholds are provided. Statistical distributions and Tukey flags are descriptive. No trend or correlation is a fault diagnosis. M3–M5 are not authorized.
