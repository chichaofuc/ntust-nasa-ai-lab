# M2 FD001 Data Quality

Phase A: `PASS_WITH_NOTES`; no source values were changed, dropped, or filled.

| Check | Train | Test | RUL | Method |
|---|---|---|---|---|
| Records | 20631 | 13096 | 100 | One record per nonblank physical line. |
| Malformed width | 0 | 0 | 0 | Expected 26/26/1 tokens. |
| Unparseable/nonfinite | 0 | 0 | 0 | All tokens finite numeric values. |
| Blank lines | 0 | 0 | 0 | Whitespace-only physical lines. |
| Exact duplicate rows | 0 | 0 | 29 | Exact tuple equality; excess occurrences. |
| Duplicate Unit-Cycle | 0 | 0 | N/A | Exact (Unit ID, Cycle) pair. |
| Missing cells | 0 | 0 | 0 | Fixed-width whitespace records have no null tokens. |

## Unit-cycle integrity

| Split | Units | Strict order | Contiguous from 1 | Duplicate keys | Missing internal cycles |
|---|---|---|---|---|---|
| Train | 100 | YES | YES | 0 | 0 |
| Test | 100 | YES | YES | 0 | 0 |

## Sensor statistics and statistical flags

| Sensor | Index | Train min | Train max | Train mean | Train SD | Train unique | Train constant | Train Tukey flags | Test unique | Test constant | Test Tukey flags |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sensor_01 | 5 | 518.67 | 518.67 | 518.67 | 0 | 1 | True | 0 | 1 | True | 0 |
| sensor_02 | 6 | 641.21 | 644.53 | 642.681 | 0.500053 | 310 | False | 128 | 262 | False | 104 |
| sensor_03 | 7 | 1571.04 | 1616.91 | 1590.52 | 6.13115 | 3012 | False | 165 | 2361 | False | 106 |
| sensor_04 | 8 | 1382.25 | 1441.49 | 1408.93 | 9.0006 | 4051 | False | 120 | 2954 | False | 123 |
| sensor_05 | 9 | 14.62 | 14.62 | 14.62 | 0 | 1 | True | 0 | 1 | True | 0 |
| sensor_06 | 10 | 21.6 | 21.61 | 21.6098 | 0.00138898 | 2 | False | 406 | 2 | False | 392 |
| sensor_07 | 11 | 549.85 | 556.06 | 553.368 | 0.885092 | 513 | False | 110 | 415 | False | 103 |
| sensor_08 | 12 | 2387.9 | 2388.56 | 2388.1 | 0.0709855 | 53 | False | 320 | 41 | False | 69 |
| sensor_09 | 13 | 9021.73 | 9244.59 | 9065.24 | 22.0829 | 6403 | False | 1686 | 4047 | False | 335 |
| sensor_10 | 14 | 1.3 | 1.3 | 1.3 | 0 | 1 | True | 0 | 1 | True | 0 |
| sensor_11 | 15 | 46.85 | 48.53 | 47.5412 | 0.267087 | 159 | False | 167 | 136 | False | 140 |
| sensor_12 | 16 | 518.69 | 523.38 | 521.413 | 0.737553 | 427 | False | 146 | 357 | False | 120 |
| sensor_13 | 17 | 2387.88 | 2388.56 | 2388.1 | 0.0719189 | 56 | False | 161 | 43 | False | 55 |
| sensor_14 | 18 | 8099.94 | 8293.72 | 8143.75 | 19.0762 | 6078 | False | 1543 | 3786 | False | 283 |
| sensor_15 | 19 | 8.3249 | 8.5848 | 8.44215 | 0.037505 | 1918 | False | 120 | 1506 | False | 117 |
| sensor_16 | 20 | 0.03 | 0.03 | 0.03 | 0 | 1 | True | 0 | 1 | True | 0 |
| sensor_17 | 21 | 388 | 400 | 393.211 | 1.54876 | 13 | False | 81 | 9 | False | 1239 |
| sensor_18 | 22 | 2388 | 2388 | 2388 | 0 | 1 | True | 0 | 1 | True | 0 |
| sensor_19 | 23 | 100 | 100 | 100 | 0 | 1 | True | 0 | 1 | True | 0 |
| sensor_20 | 24 | 38.14 | 39.43 | 38.8163 | 0.180746 | 120 | False | 117 | 103 | False | 129 |
| sensor_21 | 25 | 22.8942 | 23.6184 | 23.2897 | 0.108251 | 4745 | False | 136 | 3555 | False | 121 |

Tukey flags use pooled-split Q1/Q3 with linear interpolation at (n−1)p and the descriptive 1.5×IQR rule, computed separately for Train and Test. These are statistical flags only, not physical anomalies, alarm thresholds, or fault diagnoses. Counts are exact; the five first file-order examples per sensor/split are printed below where any flags occur. No rows were deleted. Constant means exact min=max. No near-constant threshold was invented.

| Split | Sensor | Index | Unit | Cycle | Flagged value |
|---|---|---|---|---|---|
| Train | sensor_02 | 6 | 1 | 182 | 644.21 |
| Train | sensor_02 | 6 | 1 | 184 | 644.07 |
| Train | sensor_02 | 6 | 1 | 189 | 644.18 |
| Train | sensor_02 | 6 | 2 | 6 | 641.3 |
| Train | sensor_02 | 6 | 2 | 36 | 641.27 |
| Test | sensor_02 | 6 | 20 | 163 | 643.58 |
| Test | sensor_02 | 6 | 20 | 173 | 643.61 |
| Test | sensor_02 | 6 | 20 | 181 | 643.74 |
| Test | sensor_02 | 6 | 20 | 184 | 643.75 |
| Test | sensor_02 | 6 | 23 | 52 | 641.34 |
| Train | sensor_03 | 7 | 2 | 264 | 1610.1 |
| Train | sensor_03 | 7 | 2 | 271 | 1607.43 |
| Train | sensor_03 | 7 | 2 | 287 | 1608.5 |
| Train | sensor_03 | 7 | 4 | 180 | 1610.29 |
| Train | sensor_03 | 7 | 4 | 184 | 1608.22 |
| Test | sensor_03 | 7 | 7 | 12 | 1572.37 |
| Test | sensor_03 | 7 | 10 | 3 | 1574.22 |
| Test | sensor_03 | 7 | 11 | 46 | 1601.84 |
| Test | sensor_03 | 7 | 12 | 37 | 1574.27 |
| Test | sensor_03 | 7 | 13 | 66 | 1574.42 |
| Train | sensor_04 | 8 | 3 | 176 | 1438.51 |
| Train | sensor_04 | 8 | 4 | 188 | 1434.12 |
| Train | sensor_04 | 8 | 5 | 266 | 1434.4 |
| Train | sensor_04 | 8 | 5 | 268 | 1434.59 |
| Train | sensor_04 | 8 | 6 | 185 | 1434.09 |
| Test | sensor_04 | 8 | 7 | 21 | 1385.67 |
| Test | sensor_04 | 8 | 10 | 75 | 1385.51 |
| Test | sensor_04 | 8 | 20 | 169 | 1423.55 |
| Test | sensor_04 | 8 | 20 | 171 | 1425.58 |
| Test | sensor_04 | 8 | 20 | 172 | 1423.52 |
| Train | sensor_06 | 10 | 2 | 1 | 21.6 |
| Train | sensor_06 | 10 | 2 | 3 | 21.6 |
| Train | sensor_06 | 10 | 2 | 5 | 21.6 |
| Train | sensor_06 | 10 | 2 | 9 | 21.6 |
| Train | sensor_06 | 10 | 2 | 10 | 21.6 |
| Test | sensor_06 | 10 | 6 | 62 | 21.6 |
| Test | sensor_06 | 10 | 7 | 5 | 21.6 |
| Test | sensor_06 | 10 | 7 | 20 | 21.6 |
| Test | sensor_06 | 10 | 7 | 36 | 21.6 |
| Test | sensor_06 | 10 | 7 | 96 | 21.6 |
| Train | sensor_07 | 11 | 1 | 184 | 551 |
| Train | sensor_07 | 11 | 1 | 189 | 550.7 |
| Train | sensor_07 | 11 | 1 | 191 | 550.92 |
| Train | sensor_07 | 11 | 2 | 285 | 550.85 |
| Train | sensor_07 | 11 | 5 | 269 | 550.77 |
| Test | sensor_07 | 11 | 18 | 28 | 555.81 |
| Test | sensor_07 | 11 | 20 | 168 | 551.71 |
| Test | sensor_07 | 11 | 20 | 178 | 551.48 |
| Test | sensor_07 | 11 | 20 | 179 | 551.72 |
| Test | sensor_07 | 11 | 20 | 180 | 551.71 |
| Train | sensor_08 | 12 | 1 | 185 | 2388.29 |
| Train | sensor_08 | 12 | 1 | 187 | 2388.29 |
| Train | sensor_08 | 12 | 1 | 188 | 2388.31 |
| Train | sensor_08 | 12 | 1 | 190 | 2388.29 |
| Train | sensor_08 | 12 | 1 | 191 | 2388.28 |
| Test | sensor_08 | 12 | 11 | 80 | 2388.24 |
| Test | sensor_08 | 12 | 12 | 69 | 2387.91 |
| Test | sensor_08 | 12 | 18 | 27 | 2387.91 |
| Test | sensor_08 | 12 | 20 | 183 | 2388.24 |
| Test | sensor_08 | 12 | 31 | 187 | 2388.24 |
| Train | sensor_09 | 13 | 2 | 273 | 9094.09 |
| Train | sensor_09 | 13 | 2 | 275 | 9094.94 |
| Train | sensor_09 | 13 | 2 | 278 | 9096.47 |
| Train | sensor_09 | 13 | 2 | 279 | 9096.6 |
| Train | sensor_09 | 13 | 2 | 280 | 9101.42 |
| Test | sensor_09 | 13 | 11 | 15 | 9031.3 |
| Test | sensor_09 | 13 | 11 | 20 | 9030.8 |
| Test | sensor_09 | 13 | 11 | 32 | 9030.68 |
| Test | sensor_09 | 13 | 14 | 10 | 9029.72 |
| Test | sensor_09 | 13 | 14 | 29 | 9024.53 |
| Train | sensor_11 | 15 | 1 | 187 | 48.23 |
| Train | sensor_11 | 15 | 1 | 190 | 48.33 |
| Train | sensor_11 | 15 | 1 | 192 | 48.25 |
| Train | sensor_11 | 15 | 2 | 282 | 48.27 |
| Train | sensor_11 | 15 | 2 | 285 | 48.27 |
| Test | sensor_11 | 15 | 20 | 174 | 48 |
| Test | sensor_11 | 15 | 20 | 176 | 47.97 |
| Test | sensor_11 | 15 | 20 | 179 | 48.04 |
| Test | sensor_11 | 15 | 20 | 181 | 47.96 |
| Test | sensor_11 | 15 | 20 | 182 | 48.02 |
| Train | sensor_12 | 16 | 6 | 176 | 519.41 |
| Train | sensor_12 | 16 | 6 | 179 | 519.37 |
| Train | sensor_12 | 16 | 6 | 184 | 519.42 |
| Train | sensor_12 | 16 | 6 | 187 | 519.03 |
| Train | sensor_12 | 16 | 6 | 188 | 518.98 |
| Test | sensor_12 | 16 | 3 | 125 | 520.13 |
| Test | sensor_12 | 16 | 20 | 162 | 520.15 |
| Test | sensor_12 | 16 | 20 | 177 | 519.9 |
| Test | sensor_12 | 16 | 24 | 5 | 523.33 |
| Test | sensor_12 | 16 | 31 | 179 | 519.71 |
| Train | sensor_13 | 17 | 1 | 189 | 2388.33 |
| Train | sensor_13 | 17 | 1 | 190 | 2388.35 |
| Train | sensor_13 | 17 | 1 | 191 | 2388.3 |
| Train | sensor_13 | 17 | 1 | 192 | 2388.32 |
| Train | sensor_13 | 17 | 6 | 170 | 2388.31 |
| Test | sensor_13 | 17 | 20 | 180 | 2388.24 |
| Test | sensor_13 | 17 | 24 | 58 | 2387.89 |
| Test | sensor_13 | 17 | 34 | 19 | 2387.89 |
| Test | sensor_13 | 17 | 34 | 25 | 2387.91 |
| Test | sensor_13 | 17 | 34 | 61 | 2387.9 |
| Train | sensor_14 | 18 | 2 | 277 | 8171.9 |
| Train | sensor_14 | 18 | 2 | 283 | 8174.85 |
| Train | sensor_14 | 18 | 2 | 287 | 8175.57 |
| Train | sensor_14 | 18 | 3 | 137 | 8173.71 |
| Train | sensor_14 | 18 | 3 | 139 | 8173.47 |
| Test | sensor_14 | 18 | 11 | 46 | 8113.25 |
| Test | sensor_14 | 18 | 14 | 8 | 8111.3 |
| Test | sensor_14 | 18 | 14 | 11 | 8112.19 |
| Test | sensor_14 | 18 | 14 | 40 | 8111.16 |
| Test | sensor_14 | 18 | 14 | 42 | 8113.73 |
| Train | sensor_15 | 19 | 4 | 188 | 8.5462 |
| Train | sensor_15 | 19 | 7 | 254 | 8.5627 |
| Train | sensor_15 | 19 | 8 | 137 | 8.5639 |
| Train | sensor_15 | 19 | 8 | 150 | 8.5509 |
| Train | sensor_15 | 19 | 10 | 57 | 8.3279 |
| Test | sensor_15 | 19 | 3 | 68 | 8.5025 |
| Test | sensor_15 | 19 | 3 | 90 | 8.5043 |
| Test | sensor_15 | 19 | 12 | 17 | 8.333 |
| Test | sensor_15 | 19 | 18 | 127 | 8.5174 |
| Test | sensor_15 | 19 | 20 | 169 | 8.5198 |
| Train | sensor_17 | 21 | 1 | 190 | 398 |
| Train | sensor_17 | 21 | 2 | 281 | 398 |
| Train | sensor_17 | 21 | 2 | 283 | 398 |
| Train | sensor_17 | 21 | 2 | 287 | 398 |
| Train | sensor_17 | 21 | 3 | 178 | 399 |
| Test | sensor_17 | 21 | 1 | 5 | 390 |
| Test | sensor_17 | 21 | 1 | 16 | 390 |
| Test | sensor_17 | 21 | 2 | 33 | 395 |
| Test | sensor_17 | 21 | 3 | 4 | 395 |
| Test | sensor_17 | 21 | 3 | 15 | 396 |
| Train | sensor_20 | 24 | 2 | 274 | 38.27 |
| Train | sensor_20 | 24 | 2 | 284 | 38.23 |
| Train | sensor_20 | 24 | 4 | 182 | 38.29 |
| Train | sensor_20 | 24 | 6 | 186 | 38.25 |
| Train | sensor_20 | 24 | 8 | 143 | 38.29 |
| Test | sensor_20 | 24 | 7 | 7 | 39.28 |
| Test | sensor_20 | 24 | 7 | 26 | 39.29 |
| Test | sensor_20 | 24 | 7 | 32 | 39.3 |
| Test | sensor_20 | 24 | 10 | 3 | 39.31 |
| Test | sensor_20 | 24 | 15 | 24 | 39.33 |
| Train | sensor_21 | 25 | 1 | 188 | 22.9588 |
| Train | sensor_21 | 25 | 1 | 192 | 22.9649 |
| Train | sensor_21 | 25 | 2 | 10 | 23.6005 |
| Train | sensor_21 | 25 | 2 | 269 | 22.9897 |
| Train | sensor_21 | 25 | 2 | 271 | 22.9721 |
| Test | sensor_21 | 25 | 7 | 18 | 23.5749 |
| Test | sensor_21 | 25 | 7 | 23 | 23.6021 |
| Test | sensor_21 | 25 | 11 | 12 | 23.1016 |
| Test | sensor_21 | 25 | 12 | 38 | 23.5852 |
| Test | sensor_21 | 25 | 12 | 56 | 23.5707 |

The table gives up to five traceable examples for every Sensor/Split with statistical flags; counts above include all flagged observations. Statistical flags do not establish physical abnormality.
