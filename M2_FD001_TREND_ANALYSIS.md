# M2 FD001 Sensor Trend Evidence

Phase A: `PASS_WITH_NOTES`. Phase B: `COMPLETED_AFTER_PHASE_A_PASS_WITH_NOTES`.

## Unit / Cycle observations

Train has 100 split-local Units, 20,631 rows; cycle count per Unit 128–362 (median 199, mean 206.31). Test has 100 Units, 13,096 rows; cycle counts 31–303 (median 133.5, mean 130.96). Cycles are assessed within each Unit, not concatenated. Test last observed Cycle is an observation boundary, not failure Cycle.

## Per-Sensor distribution and cycle trend

OLS slopes are computed independently per Train Unit as raw sensor value regressed on Cycle. Direction counts use strict slope signs (> 0 positive; < 0 negative; == 0 zero), with no tolerance threshold. Early/Middle/Late are equal-weight means of per-Unit means after splitting each Unit's ordered cycles into three near-equal contiguous sections. No smoothing or normalization.

| Sensor | Index | Train min | Train max | Train mean | Train SD | Test min | Test max | Test mean | Test SD | Units + slope | Units - slope | Units ZERO_SLOPE | Median Unit slope | Train Unit mean min to max | Train Early | Train Mid | Train Late | Test Early | Test Mid | Test Late |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sensor_01 | 5 | 518.67 | 518.67 | 518.67 | 0 | 518.67 | 518.67 | 518.67 | 0 | 0 | 0 | 100 | 0 | 518.67 to 518.67 | 518.67 | 518.67 | 518.67 | 518.67 | 518.67 | 518.67 |
| sensor_02 | 6 | 641.21 | 644.53 | 642.681 | 0.500053 | 641.13 | 644.3 | 642.475 | 0.400899 | 100 | 0 | 0 | 0.00530096 | 642.39 to 643.04 | 642.403 | 642.558 | 643.108 | 642.362 | 642.422 | 642.605 |
| sensor_03 | 7 | 1571.04 | 1616.91 | 1590.52 | 6.13115 | 1569.04 | 1607.55 | 1588.1 | 5.00327 | 100 | 0 | 0 | 0.0650958 | 1587.52 to 1594.3 | 1587.19 | 1589 | 1595.59 | 1586.76 | 1587.53 | 1589.55 |
| sensor_04 | 8 | 1382.25 | 1441.49 | 1408.93 | 9.0006 | 1384.39 | 1433.36 | 1404.74 | 6.68831 | 100 | 0 | 0 | 0.109292 | 1402.9 to 1416.23 | 1403.21 | 1406.51 | 1417.51 | 1402.34 | 1403.72 | 1407.46 |
| sensor_05 | 9 | 14.62 | 14.62 | 14.62 | 0 | 14.62 | 14.62 | 14.62 | 0 | 0 | 0 | 100 | 0 | 14.62 to 14.62 | 14.62 | 14.62 | 14.62 | 14.62 | 14.62 | 14.62 |
| sensor_06 | 10 | 21.6 | 21.61 | 21.6098 | 0.00138898 | 21.6 | 21.61 | 21.6097 | 0.00170408 | 61 | 1 | 38 | 9.22506e-07 | 21.6091 to 21.61 | 21.6096 | 21.6098 | 21.61 | 21.6096 | 21.6097 | 21.6098 |
| sensor_07 | 11 | 549.85 | 556.06 | 553.368 | 0.885092 | 550.88 | 555.84 | 553.758 | 0.681286 | 0 | 100 | 0 | -0.00990993 | 552.639 to 554.074 | 553.9 | 553.61 | 552.543 | 553.985 | 553.849 | 553.492 |
| sensor_08 | 12 | 2387.9 | 2388.56 | 2388.1 | 0.0709855 | 2387.89 | 2388.3 | 2388.07 | 0.0574418 | 100 | 0 | 0 | 0.000697551 | 2388.02 to 2388.18 | 2388.06 | 2388.08 | 2388.15 | 2388.06 | 2388.07 | 2388.09 |
| sensor_09 | 13 | 9021.73 | 9244.59 | 9065.24 | 22.0829 | 9024.53 | 9155.03 | 9058.41 | 11.4363 | 71 | 29 | 0 | 0.0878312 | 9039.28 to 9094.55 | 9056.43 | 9060.21 | 9077.52 | 9055.18 | 9056.37 | 9060.13 |
| sensor_10 | 14 | 1.3 | 1.3 | 1.3 | 0 | 1.3 | 1.3 | 1.3 | 0 | 0 | 0 | 100 | 0 | 1.3 to 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 |
| sensor_11 | 15 | 46.85 | 48.53 | 47.5412 | 0.267087 | 46.8 | 48.26 | 47.4162 | 0.195917 | 100 | 0 | 0 | 0.00333456 | 47.3433 to 47.7636 | 47.3682 | 47.4682 | 47.802 | 47.3442 | 47.3863 | 47.4966 |
| sensor_12 | 16 | 518.69 | 523.38 | 521.413 | 0.737553 | 519.38 | 523.76 | 521.748 | 0.559627 | 0 | 100 | 0 | -0.00845357 | 520.79 to 522.032 | 521.872 | 521.614 | 520.713 | 521.944 | 521.822 | 521.521 |
| sensor_13 | 17 | 2387.88 | 2388.56 | 2388.1 | 0.0719189 | 2387.89 | 2388.32 | 2388.07 | 0.0569343 | 100 | 0 | 0 | 0.000700021 | 2388.01 to 2388.18 | 2388.06 | 2388.08 | 2388.15 | 2388.06 | 2388.07 | 2388.09 |
| sensor_14 | 18 | 8099.94 | 8293.72 | 8143.75 | 19.0762 | 8108.5 | 8220.48 | 8138.95 | 10.1886 | 60 | 40 | 0 | 0.0574651 | 8119.32 to 8172.11 | 8137.59 | 8139.99 | 8152.11 | 8136.73 | 8137.49 | 8139.57 |
| sensor_15 | 19 | 8.3249 | 8.5848 | 8.44215 | 0.037505 | 8.3328 | 8.5414 | 8.42584 | 0.0290093 | 100 | 0 | 0 | 0.000426736 | 8.41944 to 8.46983 | 8.42004 | 8.4318 | 8.47637 | 8.41651 | 8.42189 | 8.43626 |
| sensor_16 | 20 | 0.03 | 0.03 | 0.03 | 0 | 0.03 | 0.03 | 0.03 | 0 | 0 | 0 | 100 | 0 | 0.03 to 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 |
| sensor_17 | 21 | 388 | 400 | 393.211 | 1.54876 | 389 | 397 | 392.572 | 1.23358 | 100 | 0 | 0 | 0.0169752 | 392.368 to 394.188 | 392.329 | 392.818 | 394.535 | 392.2 | 392.416 | 392.964 |
| sensor_18 | 22 | 2388 | 2388 | 2388 | 0 | 2388 | 2388 | 2388 | 0 | 0 | 0 | 100 | 0 | 2388 to 2388 | 2388 | 2388 | 2388 | 2388 | 2388 | 2388 |
| sensor_19 | 23 | 100 | 100 | 100 | 0 | 100 | 100 | 100 | 0 | 0 | 0 | 100 | 0 | 100 to 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| sensor_20 | 24 | 38.14 | 39.43 | 38.8163 | 0.180746 | 38.31 | 39.41 | 38.8925 | 0.141681 | 0 | 100 | 0 | -0.00201542 | 38.6931 to 38.9222 | 38.9243 | 38.8617 | 38.6554 | 38.938 | 38.91 | 38.8444 |
| sensor_21 | 25 | 22.8942 | 23.6184 | 23.2897 | 0.108251 | 22.9354 | 23.6419 | 23.3357 | 0.0841203 | 0 | 100 | 0 | -0.00122132 | 23.2167 to 23.3534 | 23.3541 | 23.3171 | 23.1933 | 23.3617 | 23.3472 | 23.307 |

## Unit-specific trend evidence

For each sensor, these are up to the two most negative (strictly < 0) and two most positive (strictly > 0) Train per-Unit slopes. Exact zero slopes are excluded from directional extremes and counted as `ZERO_SLOPE` above. No arbitrary slope threshold is applied. They are descriptive extremes, not diagnoses.

| Sensor | Index | Selection | Unit | Cycle range | N | OLS slope/cycle |
|---|---|---|---|---|---|---|
| sensor_02 | 6 | increase | 28 | 1–165 | 165 | 0.00905874 |
| sensor_02 | 6 | increase | 70 | 1–137 | 137 | 0.00900498 |
| sensor_03 | 7 | increase | 98 | 1–156 | 156 | 0.100307 |
| sensor_03 | 7 | increase | 45 | 1–158 | 158 | 0.096992 |
| sensor_04 | 8 | increase | 98 | 1–156 | 156 | 0.17789 |
| sensor_04 | 8 | increase | 93 | 1–155 | 155 | 0.174786 |
| sensor_06 | 10 | decrease | 21 | 1–195 | 195 | -3.72235e-07 |
| sensor_06 | 10 | increase | 33 | 1–200 | 200 | 1.47304e-05 |
| sensor_06 | 10 | increase | 78 | 1–231 | 231 | 1.18285e-05 |
| sensor_07 | 11 | decrease | 65 | 1–153 | 153 | -0.0181767 |
| sensor_07 | 11 | decrease | 24 | 1–147 | 147 | -0.0179464 |
| sensor_08 | 12 | increase | 57 | 1–137 | 137 | 0.00158204 |
| sensor_08 | 12 | increase | 65 | 1–153 | 153 | 0.00157965 |
| sensor_09 | 13 | decrease | 65 | 1–153 | 153 | -0.127323 |
| sensor_09 | 13 | decrease | 61 | 1–185 | 185 | -0.10739 |
| sensor_09 | 13 | increase | 18 | 1–195 | 195 | 0.588818 |
| sensor_09 | 13 | increase | 97 | 1–202 | 202 | 0.578414 |
| sensor_11 | 15 | increase | 98 | 1–156 | 156 | 0.00572231 |
| sensor_11 | 15 | increase | 57 | 1–137 | 137 | 0.00535992 |
| sensor_12 | 16 | decrease | 57 | 1–137 | 137 | -0.0163364 |
| sensor_12 | 16 | decrease | 45 | 1–158 | 158 | -0.0150596 |
| sensor_13 | 17 | increase | 65 | 1–153 | 153 | 0.00170738 |
| sensor_13 | 17 | increase | 90 | 1–154 | 154 | 0.00165674 |
| sensor_14 | 18 | decrease | 65 | 1–153 | 153 | -0.178579 |
| sensor_14 | 18 | decrease | 58 | 1–147 | 147 | -0.147108 |
| sensor_14 | 18 | increase | 97 | 1–202 | 202 | 0.484829 |
| sensor_14 | 18 | increase | 18 | 1–195 | 195 | 0.483554 |
| sensor_15 | 19 | increase | 57 | 1–137 | 137 | 0.000724834 |
| sensor_15 | 19 | increase | 28 | 1–165 | 165 | 0.0007051 |
| sensor_17 | 21 | increase | 28 | 1–165 | 165 | 0.0261026 |
| sensor_17 | 21 | increase | 58 | 1–147 | 147 | 0.0259012 |
| sensor_20 | 24 | decrease | 57 | 1–137 | 137 | -0.00361263 |
| sensor_20 | 24 | decrease | 28 | 1–165 | 165 | -0.00322592 |
| sensor_21 | 25 | decrease | 45 | 1–158 | 158 | -0.00211579 |
| sensor_21 | 25 | decrease | 28 | 1–165 | 165 | -0.00201153 |

**OBSERVATION:** Tables contain source-derived values, split-level distributions, per-Unit slope direction counts, and cycle-segment summaries. **INFERENCE:** Repeated directional trends may motivate follow-up study, with uncertainty about sensor meaning and operating conditions. **UNKNOWN:** Physical failure mechanism, fault class, manufacturer limits, healthy baseline, causal relationship, maintenance history, and safety state. `BASELINE_STATUS: NOT_ESTABLISHED`. Trend direction or statistical flags are not fault diagnoses. Train has no explicit fault labels. Test has no per-Cycle RUL label; RUL is one positional value per Test Unit and not a fault class.
