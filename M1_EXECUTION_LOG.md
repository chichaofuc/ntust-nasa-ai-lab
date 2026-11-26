# M1 Execution Log — Recomputed Synthetic CSV Profile

**Work Item:** `M1_DATASET_PROFILE_001`
**Execution:** Completed for the single authorized logical dataset; returned for independent Research Brain review.
**Analysis start / finish:** 2026-11-26 19:08:30 +08:00 (Asia/Taipei).
**Project root:** `C:\Users\as555\Desktop\20261123_AI\20261123_AI`
**Branch / baseline HEAD:** `main` / `318b51a2244833a7310638847d89c8e08f431310`
**Source:** `data/synthetic_sensor.csv`.
**Source size:** 234 bytes.
**SHA-256 before / after:** `CD536B46EB628909FDC986BBAD956C24A2E50AFB287968998374BEFC62204377` / same.
**Python:** 3.13.14.
**Packages:** Python standard library only (`csv`, `hashlib`, `json`, `math`, `platform`, `re`, `statistics`, `sys`, `collections`, `datetime`, `pathlib`); no third-party packages.

## Governance and pre-execution checks

- Before local data access, fetched current GitHub `main` versions of `AGENTS.md`, `ROADMAP.md`, `WORK_ITEM.md`, and `DECISIONS.md` and checked remote `refs/heads/main`.
- Remote HEAD was `318b51a2244833a7310638847d89c8e08f431310`, equal to the authorized baseline. Governance preserves M1 as unaccepted pending profile review and M2–M5 as locked.
- Local `git branch --show-current` returned `main`; `git rev-parse HEAD` returned the baseline SHA above.
- Pre-edit `git status --short` showed only known untracked user files: `.DS_Store`, presentation files, and `data/`. No tracked modifications were present. The three reports were tracked at baseline. These known untracked items were preserved.
- The source resolved to `C:\Users\as555\Desktop\20261123_AI\20261123_AI\data\synthetic_sensor.csv`, existed, and was read successfully.

## Correction to prior report revision

The prior report revision described six expected datasets and a 1/6 input count. That was incorrect for the current authorization: six refers to data records in one CSV, not six CSV datasets. The current profile replaces that mistaken interpretation with one logical dataset containing six records. No additional datasets were searched for or created.

## Reproducible execution

PowerShell resolved `$source` as `(Resolve-Path -LiteralPath 'data\synthetic_sensor.csv').Path`, stored the following complete Python source in a single-quoted here-string, and piped it to `python - $source`. The exact executable source is included verbatim below.

```python
import csv, hashlib, json, math, platform, re, statistics, sys
from collections import Counter
from datetime import datetime
from pathlib import Path
started = datetime.now().astimezone().isoformat(timespec='seconds')
path = Path(sys.argv[1]).resolve(strict=True)
raw_before = path.read_bytes()
sha_before = hashlib.sha256(raw_before).hexdigest().upper()
text = raw_before.decode('utf-8-sig')
records = list(csv.reader(text.splitlines(), delimiter=',', strict=True))
if not records: raise ValueError('CSV is empty')
header, body = records[0], records[1:]
if any(len(row) != len(header) for row in body): raise ValueError('Malformed CSV: row width differs from header')
missing = {name: sum(not row[i].strip() for row in body) for i, name in enumerate(header)}
rows_missing = sum(any(not value.strip() for value in row) for row in body)
counts = Counter(tuple(row) for row in body)
dup_groups = [{'row': list(row), 'count': n} for row, n in counts.items() if n > 1]
dup_excess = sum(n-1 for n in counts.values() if n > 1)
dup_cols = sorted(name for name,n in Counter(header).items() if n > 1)
fields=[]
for i,name in enumerate(header):
 vals=[r[i].strip() for r in body]; present=[v for v in vals if v]
 nums=[]; all_num=bool(present); all_int=bool(present)
 for v in present:
  try:
   x=float(v)
   if not math.isfinite(x): all_num=False; all_int=False
   else:
    nums.append(x)
    if not re.fullmatch(r'[+-]?\d+',v): all_int=False
  except ValueError: all_num=False; all_int=False
 dtype='empty' if not present else ('int' if all_num and all_int else 'float' if all_num else 'string')
 stats=None
 if all_num and nums:
  stats={'count':len(nums),'min':min(nums),'max':max(nums),'mean':statistics.mean(nums),'median':statistics.median(nums),'std_sample':statistics.stdev(nums) if len(nums)>1 else None,'constant':min(nums)==max(nums)}
 fields.append({'name':name,'dtype':dtype,'missing':missing[name],'numeric_stats':stats,'constant':len(set(present))<=1 if present else True})
raw_after=path.read_bytes(); sha_after=hashlib.sha256(raw_after).hexdigest().upper()
finished=datetime.now().astimezone().isoformat(timespec='seconds')
result={'execution_started':started,'execution_finished':finished,'python':platform.python_version(),'source_path':str(path),'source_size_bytes':len(raw_before),'sha256_before':sha_before,'sha256_after':sha_after,'source_unchanged':raw_before==raw_after,'delimiter':',','data_rows':len(body),'column_count':len(header),'columns':header,'record_widths':sorted(set(map(len,body))),'fields':fields,'missing_by_column':missing,'total_missing_cells':sum(missing.values()),'rows_with_missing':rows_missing,'duplicate_rows_excess_count':dup_excess,'duplicate_row_groups':dup_groups,'duplicate_column_names':dup_cols,'constant_columns':[f['name'] for f in fields if f['constant']],'malformed_rows':0}
print(json.dumps(result,ensure_ascii=False,indent=2))
```

## Captured execution evidence

**Command:** `$code | python - $source`
**Exit code:** `0`
**stderr:** empty; no stderr output was observed.
**stdout:**

```json
{
  "execution_started": "2026-11-26T19:08:30+08:00",
  "execution_finished": "2026-11-26T19:08:30+08:00",
  "python": "3.13.14",
  "source_path": "C:\\Users\\as555\\Desktop\\20261123_AI\\20261123_AI\\data\\synthetic_sensor.csv",
  "source_size_bytes": 234,
  "sha256_before": "CD536B46EB628909FDC986BBAD956C24A2E50AFB287968998374BEFC62204377",
  "sha256_after": "CD536B46EB628909FDC986BBAD956C24A2E50AFB287968998374BEFC62204377",
  "source_unchanged": true,
  "delimiter": ",",
  "data_rows": 6,
  "column_count": 4,
  "columns": ["timestamp", "load_pct", "coolant_out_c", "oil_pressure_bar"],
  "record_widths": [4],
  "fields": [
    {"name": "timestamp", "dtype": "string", "missing": 0, "numeric_stats": null, "constant": false},
    {"name": "load_pct", "dtype": "int", "missing": 0, "numeric_stats": {"count": 6, "min": 50.0, "max": 70.0, "mean": 63.333333333333336, "median": 70.0, "std_sample": 10.327955589886445, "constant": false}, "constant": false},
    {"name": "coolant_out_c", "dtype": "int", "missing": 0, "numeric_stats": {"count": 6, "min": 78.0, "max": 84.0, "mean": 81.66666666666667, "median": 82.5, "std_sample": 2.581988897471611, "constant": false}, "constant": false},
    {"name": "oil_pressure_bar", "dtype": "float", "missing": 1, "numeric_stats": {"count": 5, "min": 3.8, "max": 4.0, "mean": 3.9, "median": 3.9, "std_sample": 0.10000000000000009, "constant": false}, "constant": false}
  ],
  "missing_by_column": {"timestamp": 0, "load_pct": 0, "coolant_out_c": 0, "oil_pressure_bar": 1},
  "total_missing_cells": 1,
  "rows_with_missing": 1,
  "duplicate_rows_excess_count": 1,
  "duplicate_row_groups": [{"row": ["2026-01-01T10:04:00", "70", "84", "3.8"], "count": 2}],
  "duplicate_column_names": [],
  "constant_columns": [],
  "malformed_rows": 0
}
```

## Interpretation rules

- Duplicate count is exact full-row tuple equality on data records, excluding header; one excess duplicate row was counted.
- A missing cell is an empty/whitespace-only field. No rows were dropped, values filled, or source cells changed.
- Numeric types and summaries are inferred from nonmissing values. Standard deviation is sample SD. `timestamp` is treated as string; no external schema was available.
- No duplicate column names, malformed-width rows, or constant fields were found.
- Column names are suggestive only. Physical meaning, validated units, equipment identity, calibration, and normal operating limits remain UNKNOWN.

## Git and remote verification

Git change and remote readback evidence is returned with the Worker execution report. No M1 acceptance is claimed.
