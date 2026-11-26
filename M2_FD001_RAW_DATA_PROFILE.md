# M2 FD001 Raw Data Profile

Phase A: `PASS_WITH_NOTES`
Note: RUL has 100 values and Test first-occurrence Unit order is 1..100, so positional coverage is one-to-one. RUL rows have no Unit ID key; semantic row identity is not cross-key-verifiable from these files.

## Raw row and column counts

| File | Physical lines | Blank | Nonblank | Parsed rows | Parsed columns | Bad lines |
|---|---|---|---|---|---|---|
| train_FD001.txt | 20631 | 0 | 20631 | 20631 | 26 | 0 |
| test_FD001.txt | 13096 | 0 | 13096 | 13096 | 26 | 0 |
| RUL_FD001.txt | 100 | 0 | 100 | 100 | 1 | 0 |

Parsing: strict ASCII; each nonblank physical line is one record; whitespace tokenization; each value must parse to a finite float; widths must be 26/26/1. Raw physical lines are distinct from parsed rows. No line was silently skipped except blank lines (none found).

## Unit and Cycle checks

Unit IDs are split-local trajectory identifiers. Train/Test IDs each span 1–100 and first occur in ascending order. Every Unit Cycle begins at 1, increases strictly, and is contiguous. IDs in separate splits do not establish the same physical engine. Test final observed Cycle is not a failure Cycle.

| Split | Units | Rows | Cycles per Unit min | median | mean | max | Last Cycle min | Last Cycle max |
|---|---|---|---|---|---|---|---|---|
| Train | 100 | 20631 | 128 | 199.0 | 206.31 | 362 | 128 | 362 |
| Test | 100 | 13096 | 31 | 133.5 | 130.96 | 303 | 31 | 303 |

### Train Unit ranges

| Unit | First Cycle | Last Cycle | Rows |
|---|---|---|---|
| 1 | 1 | 192 | 192 |
| 2 | 1 | 287 | 287 |
| 3 | 1 | 179 | 179 |
| 4 | 1 | 189 | 189 |
| 5 | 1 | 269 | 269 |
| 6 | 1 | 188 | 188 |
| 7 | 1 | 259 | 259 |
| 8 | 1 | 150 | 150 |
| 9 | 1 | 201 | 201 |
| 10 | 1 | 222 | 222 |
| 11 | 1 | 240 | 240 |
| 12 | 1 | 170 | 170 |
| 13 | 1 | 163 | 163 |
| 14 | 1 | 180 | 180 |
| 15 | 1 | 207 | 207 |
| 16 | 1 | 209 | 209 |
| 17 | 1 | 276 | 276 |
| 18 | 1 | 195 | 195 |
| 19 | 1 | 158 | 158 |
| 20 | 1 | 234 | 234 |
| 21 | 1 | 195 | 195 |
| 22 | 1 | 202 | 202 |
| 23 | 1 | 168 | 168 |
| 24 | 1 | 147 | 147 |
| 25 | 1 | 230 | 230 |
| 26 | 1 | 199 | 199 |
| 27 | 1 | 156 | 156 |
| 28 | 1 | 165 | 165 |
| 29 | 1 | 163 | 163 |
| 30 | 1 | 194 | 194 |
| 31 | 1 | 234 | 234 |
| 32 | 1 | 191 | 191 |
| 33 | 1 | 200 | 200 |
| 34 | 1 | 195 | 195 |
| 35 | 1 | 181 | 181 |
| 36 | 1 | 158 | 158 |
| 37 | 1 | 170 | 170 |
| 38 | 1 | 194 | 194 |
| 39 | 1 | 128 | 128 |
| 40 | 1 | 188 | 188 |
| 41 | 1 | 216 | 216 |
| 42 | 1 | 196 | 196 |
| 43 | 1 | 207 | 207 |
| 44 | 1 | 192 | 192 |
| 45 | 1 | 158 | 158 |
| 46 | 1 | 256 | 256 |
| 47 | 1 | 214 | 214 |
| 48 | 1 | 231 | 231 |
| 49 | 1 | 215 | 215 |
| 50 | 1 | 198 | 198 |
| 51 | 1 | 213 | 213 |
| 52 | 1 | 213 | 213 |
| 53 | 1 | 195 | 195 |
| 54 | 1 | 257 | 257 |
| 55 | 1 | 193 | 193 |
| 56 | 1 | 275 | 275 |
| 57 | 1 | 137 | 137 |
| 58 | 1 | 147 | 147 |
| 59 | 1 | 231 | 231 |
| 60 | 1 | 172 | 172 |
| 61 | 1 | 185 | 185 |
| 62 | 1 | 180 | 180 |
| 63 | 1 | 174 | 174 |
| 64 | 1 | 283 | 283 |
| 65 | 1 | 153 | 153 |
| 66 | 1 | 202 | 202 |
| 67 | 1 | 313 | 313 |
| 68 | 1 | 199 | 199 |
| 69 | 1 | 362 | 362 |
| 70 | 1 | 137 | 137 |
| 71 | 1 | 208 | 208 |
| 72 | 1 | 213 | 213 |
| 73 | 1 | 213 | 213 |
| 74 | 1 | 166 | 166 |
| 75 | 1 | 229 | 229 |
| 76 | 1 | 210 | 210 |
| 77 | 1 | 154 | 154 |
| 78 | 1 | 231 | 231 |
| 79 | 1 | 199 | 199 |
| 80 | 1 | 185 | 185 |
| 81 | 1 | 240 | 240 |
| 82 | 1 | 214 | 214 |
| 83 | 1 | 293 | 293 |
| 84 | 1 | 267 | 267 |
| 85 | 1 | 188 | 188 |
| 86 | 1 | 278 | 278 |
| 87 | 1 | 178 | 178 |
| 88 | 1 | 213 | 213 |
| 89 | 1 | 217 | 217 |
| 90 | 1 | 154 | 154 |
| 91 | 1 | 135 | 135 |
| 92 | 1 | 341 | 341 |
| 93 | 1 | 155 | 155 |
| 94 | 1 | 258 | 258 |
| 95 | 1 | 283 | 283 |
| 96 | 1 | 336 | 336 |
| 97 | 1 | 202 | 202 |
| 98 | 1 | 156 | 156 |
| 99 | 1 | 185 | 185 |
| 100 | 1 | 200 | 200 |

### Test last observed Cycle and RUL positional mapping

RUL has no Unit ID. Pairing below uses row index against Test Unit first-occurrence order; count and order match, but semantic ID cannot be independently cross-keyed from RUL.

| Test Unit | Last observed Cycle | Rows | RUL row 1-based | RUL value |
|---|---|---|---|---|
| 1 | 31 | 31 | 1 | 112 |
| 2 | 49 | 49 | 2 | 98 |
| 3 | 126 | 126 | 3 | 69 |
| 4 | 106 | 106 | 4 | 82 |
| 5 | 98 | 98 | 5 | 91 |
| 6 | 105 | 105 | 6 | 93 |
| 7 | 160 | 160 | 7 | 91 |
| 8 | 166 | 166 | 8 | 95 |
| 9 | 55 | 55 | 9 | 111 |
| 10 | 192 | 192 | 10 | 96 |
| 11 | 83 | 83 | 11 | 97 |
| 12 | 217 | 217 | 12 | 124 |
| 13 | 195 | 195 | 13 | 95 |
| 14 | 46 | 46 | 14 | 107 |
| 15 | 76 | 76 | 15 | 83 |
| 16 | 113 | 113 | 16 | 84 |
| 17 | 165 | 165 | 17 | 50 |
| 18 | 133 | 133 | 18 | 28 |
| 19 | 135 | 135 | 19 | 87 |
| 20 | 184 | 184 | 20 | 16 |
| 21 | 148 | 148 | 21 | 57 |
| 22 | 39 | 39 | 22 | 111 |
| 23 | 130 | 130 | 23 | 113 |
| 24 | 186 | 186 | 24 | 20 |
| 25 | 48 | 48 | 25 | 145 |
| 26 | 76 | 76 | 26 | 119 |
| 27 | 140 | 140 | 27 | 66 |
| 28 | 158 | 158 | 28 | 97 |
| 29 | 171 | 171 | 29 | 90 |
| 30 | 143 | 143 | 30 | 115 |
| 31 | 196 | 196 | 31 | 8 |
| 32 | 145 | 145 | 32 | 48 |
| 33 | 50 | 50 | 33 | 106 |
| 34 | 203 | 203 | 34 | 7 |
| 35 | 198 | 198 | 35 | 11 |
| 36 | 126 | 126 | 36 | 19 |
| 37 | 121 | 121 | 37 | 21 |
| 38 | 125 | 125 | 38 | 50 |
| 39 | 37 | 37 | 39 | 142 |
| 40 | 133 | 133 | 40 | 28 |
| 41 | 123 | 123 | 41 | 18 |
| 42 | 156 | 156 | 42 | 10 |
| 43 | 172 | 172 | 43 | 59 |
| 44 | 54 | 54 | 44 | 109 |
| 45 | 152 | 152 | 45 | 114 |
| 46 | 146 | 146 | 46 | 47 |
| 47 | 73 | 73 | 47 | 135 |
| 48 | 78 | 78 | 48 | 92 |
| 49 | 303 | 303 | 49 | 21 |
| 50 | 74 | 74 | 50 | 79 |
| 51 | 144 | 144 | 51 | 114 |
| 52 | 189 | 189 | 52 | 29 |
| 53 | 164 | 164 | 53 | 26 |
| 54 | 121 | 121 | 54 | 97 |
| 55 | 113 | 113 | 55 | 137 |
| 56 | 136 | 136 | 56 | 15 |
| 57 | 160 | 160 | 57 | 103 |
| 58 | 176 | 176 | 58 | 37 |
| 59 | 94 | 94 | 59 | 114 |
| 60 | 147 | 147 | 60 | 100 |
| 61 | 159 | 159 | 61 | 21 |
| 62 | 232 | 232 | 62 | 54 |
| 63 | 155 | 155 | 63 | 72 |
| 64 | 168 | 168 | 64 | 28 |
| 65 | 71 | 71 | 65 | 128 |
| 66 | 147 | 147 | 66 | 14 |
| 67 | 71 | 71 | 67 | 77 |
| 68 | 187 | 187 | 68 | 8 |
| 69 | 54 | 54 | 69 | 121 |
| 70 | 152 | 152 | 70 | 94 |
| 71 | 68 | 68 | 71 | 118 |
| 72 | 131 | 131 | 72 | 50 |
| 73 | 112 | 112 | 73 | 131 |
| 74 | 137 | 137 | 74 | 126 |
| 75 | 88 | 88 | 75 | 113 |
| 76 | 205 | 205 | 76 | 10 |
| 77 | 162 | 162 | 77 | 34 |
| 78 | 72 | 72 | 78 | 107 |
| 79 | 101 | 101 | 79 | 63 |
| 80 | 133 | 133 | 80 | 90 |
| 81 | 213 | 213 | 81 | 8 |
| 82 | 162 | 162 | 82 | 9 |
| 83 | 73 | 73 | 83 | 137 |
| 84 | 172 | 172 | 84 | 58 |
| 85 | 34 | 34 | 85 | 118 |
| 86 | 110 | 110 | 86 | 89 |
| 87 | 56 | 56 | 87 | 116 |
| 88 | 68 | 68 | 88 | 115 |
| 89 | 177 | 177 | 89 | 136 |
| 90 | 146 | 146 | 90 | 28 |
| 91 | 234 | 234 | 91 | 38 |
| 92 | 150 | 150 | 92 | 20 |
| 93 | 244 | 244 | 93 | 85 |
| 94 | 133 | 133 | 94 | 55 |
| 95 | 89 | 89 | 95 | 128 |
| 96 | 97 | 97 | 96 | 137 |
| 97 | 134 | 134 | 97 | 82 |
| 98 | 121 | 121 | 98 | 59 |
| 99 | 97 | 97 | 99 | 117 |
| 100 | 198 | 198 | 100 | 20 |

RUL rows: 100. Integer value range: 7–145. It provides one value per Test Unit by positional rule, not a separate value for each Test Cycle and not a fault-class label.

## Raw column index (0-based)

Files have no header; canonical names are positional labels, not proof of physical meaning.

| Index | Canonical field | Category | Type | Semantic status | Evidence / limitation |
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

## Label semantics

Train/Test contain no explicit fault class. Train has observed trajectories through each Unit's last supplied Cycle; files alone do not prove a physical failure at the last row. `last_observed_cycle - cycle` is computable but is true failure RUL only under that endpoint assumption. Test has no per-Cycle label. RUL_FD001 has 100 values; positional coverage is one-to-one with Test Unit first-occurrence order 1..100. The RUL file has no Unit key, so semantic row association remains a positional-contract limitation.
