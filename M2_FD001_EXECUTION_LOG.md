# M2 FD001 Execution Log

**Work Item:** `M2_FD001_LOCAL_DATA_VALIDATION_001`
**Execution date/time:** 2026-11-26, 19:37–20:02 Asia/Taipei (UTC+08:00); final reproducible run 20:02:25–20:02:28.
**Project root:** `C:\Users\as555\Desktop\20261123_AI\20261123_AI`
**OS:** Microsoft Windows 10.0.26100, AMD64.
**Shell:** PowerShell 7.6.9.
**Python:** 3.13.14.
**Third-party packages:** None. Python standard library only.
**Governance HEAD:** `1964c1deec490f38f8c16b1897cd2013808eeba6`.

## Authorization and governance preflight

The complete formal MAIN work order was included in the Owner-pasted Research Worker command. It authorizes M2 FD001 Local Data Validation; M0 is accepted, M1 is ACCEPTED_WITH_NOTES with domain acceptance established, M2 is authorized with Phase A as a gate for Phase B, and M3–M5 remain locked.

Before local FD001 data access, GitHub `main` was checked at `1964c1deec490f38f8c16b1897cd2013808eeba6`; the four current governance files were fetched. Their verified Blob SHAs were:

| File | Blob SHA |
|---|---|
| `AGENTS.md` | `c5203cadd06a6189da7a009ac0ca430cec5989f0` |
| `ROADMAP.md` | `b7cfae55b700925ea017c56bdd9b2af8dd524700` |
| `WORK_ITEM.md` | `6d8e0efced936bf5d53f1041808c3e73175edd98` |
| `DECISIONS.md` | `d31df675979603245dd448334ee1f794796302a4` |

The repository previously contained historical M2-LOCKED/not-accepted records; the current governance sections record M2 authorization and M1 acceptance. These historical/current differences were preserved and not edited by this Worker. The local branch was at `54c2373665d18ec6e517ee349f85b54f6018e748`, behind remote. Fetch showed four remote commits, all limited to the four governance files. With tracked local files clean, local `main` was fast-forwarded to the verified governance baseline `1964c1deec490f38f8c16b1897cd2013808eeba6`. Known untracked user files (`.DS_Store`, presentation files, and `data/`) were left untouched. The six required M2 report files did not exist before execution.

## Inputs and integrity

Only these local trusted files were used:

| File | Absolute path | Size (bytes) | SHA-256 before | SHA-256 after |
|---|---|---:|---|---|
| `train_FD001.txt` | `C:\Users\as555\Desktop\20261123_AI\20261123_AI\data\FD001\train_FD001.txt` | 3515356 | `963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8` | `963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8` |
| `test_FD001.txt` | `C:\Users\as555\Desktop\20261123_AI\20261123_AI\data\FD001\test_FD001.txt` | 2228855 | `3CDA7109CE17BAFB5443F2AC926CFCF88154B941B8C4CF95EB55D1DDD6F52851` | `3CDA7109CE17BAFB5443F2AC926CFCF88154B941B8C4CF95EB55D1DDD6F52851` |
| `RUL_FD001.txt` | `C:\Users\as555\Desktop\20261123_AI\20261123_AI\data\FD001\RUL_FD001.txt` | 429 | `A19C8EC94931949D0485BDC35118206E9C81C4547B422EFB9CF86F4CEDDBCECA` | `A19C8EC94931949D0485BDC35118206E9C81C4547B422EFB9CF86F4CEDDBCECA` |

All files decoded as ASCII, were nonempty, ended with a newline, and parsed as whitespace-delimited numeric data. No source was modified or staged.

## Phase A results and gate

**PHASE_A_STATUS: PASS_WITH_NOTES.** Train has 20,631 parsed rows × 26 columns; Test has 13,096 × 26; RUL has 100 × 1. Raw physical line counts equal parsed records for all three files; no blank lines, width errors, unparseable values, or nonfinite values occurred. Train and Test each contain 100 split-local Unit IDs, 1–100, in first-occurrence order. All observed per-Unit cycles begin at 1, increase strictly, and are contiguous. No duplicate Unit-Cycle records were found.

RUL has 100 integer values (range 7–145) and Test Unit first-occurrence order is 1–100, supporting complete one-to-one positional coverage. **Note:** RUL rows contain no Unit identifier; semantic row identity cannot be cross-keyed from these three files alone. The contract therefore records row-order alignment as positional and retains this limitation. Phase B proceeded only after recording this Phase A result and note.

Raw index mapping is 0-based: 0 Unit ID, 1 Cycle, 2–4 operating-setting slots, 5–25 sensor slots 01–21. Operating-setting physical meanings are inferred from layout; sensor physical names/units are unknown. The source files have no header. Train/Test contain no fault-class label; Test contains no per-Cycle RUL label. The endpoint of a Train trajectory is not itself proof of a physical failure event.

## Phase B method and results

The reproducible script computes per-sensor Train/Test distributions; exact constant status; 1.5×IQR descriptive flags separately by split; per-Unit Train OLS slopes against that Unit's Cycle; equal-Unit early/middle/late segment means for Train and Test; per-sensor slope-direction counts; per-Unit slope extremes; and a positional Test/RUL table. It does not join Unit timelines, smooth, normalize, delete, or impute observations. Tukey flags are statistical review candidates only. Baselines and physical fault thresholds are not established.

Six sensors (`sensor_01`, `sensor_05`, `sensor_10`, `sensor_16`, `sensor_18`, `sensor_19`) are exactly constant in both Train and Test. Full per-sensor statistics, Unit-specific evidence, Cycle summaries, and data-quality tables are in the corresponding reports.

## Reproducibility and captured execution

- Script: `M2_FD001_analysis.py` (included with the authorized reports; complete reproducible source).
- Commands: `python -m py_compile .\M2_FD001_analysis.py`; `python .\M2_FD001_analysis.py`.
- Final analysis command exit code: `0`.
- stderr: empty.
- stdout from the final analysis run (JSON values reproduced; nested object whitespace is compacted for readability):

```json
{
  "execution_started": "2026-11-26T20:02:25+08:00",
  "execution_finished": "2026-11-26T20:02:28+08:00",
  "python": "3.13.14",
  "phase_a_status": "PASS_WITH_NOTES",
  "phase_a_note": "RUL has 100 values and Test first-occurrence Unit order is 1..100, so positional coverage is one-to-one. RUL rows have no Unit ID key; semantic row identity is not cross-key-verifiable from these files.",
  "phase_b_status": "COMPLETED_AFTER_PHASE_A_PASS_WITH_NOTES",
  "files": {
    "train_FD001.txt": {"path": "C:\\Users\\as555\\Desktop\\20261123_AI\\20261123_AI\\data\\FD001\\train_FD001.txt", "bytes": 3515356, "sha256_before": "963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8", "sha256_after": "963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8", "physical_lines": 20631, "blank_lines": 0, "parsed_rows": 20631, "columns": 26, "parse_errors": 0},
    "test_FD001.txt": {"path": "C:\\Users\\as555\\Desktop\\20261123_AI\\20261123_AI\\data\\FD001\\test_FD001.txt", "bytes": 2228855, "sha256_before": "3CDA7109CE17BAFB5443F2AC926CFCF88154B941B8C4CF95EB55D1DDD6F52851", "sha256_after": "3CDA7109CE17BAFB5443F2AC926CFCF88154B941B8C4CF95EB55D1DDD6F52851", "physical_lines": 13096, "blank_lines": 0, "parsed_rows": 13096, "columns": 26, "parse_errors": 0},
    "RUL_FD001.txt": {"path": "C:\\Users\\as555\\Desktop\\20261123_AI\\20261123_AI\\data\\FD001\\RUL_FD001.txt", "bytes": 429, "sha256_before": "A19C8EC94931949D0485BDC35118206E9C81C4547B422EFB9CF86F4CEDDBCECA", "sha256_after": "A19C8EC94931949D0485BDC35118206E9C81C4547B422EFB9CF86F4CEDDBCECA", "physical_lines": 100, "blank_lines": 0, "parsed_rows": 100, "columns": 1, "parse_errors": 0}
  },
  "train": {"rows": 20631, "units": 100, "unit_ids": [1, 100], "cycle_count": [128, 362], "last_cycle": [128, 362], "cycles_contiguous": true, "duplicate_rows": 0, "duplicate_unit_cycle": 0},
  "test": {"rows": 13096, "units": 100, "unit_ids": [1, 100], "cycle_count": [31, 303], "last_cycle": [31, 303], "cycles_contiguous": true, "duplicate_rows": 0, "duplicate_unit_cycle": 0},
  "rul": {"rows": 100, "range": [7, 145], "positional_test_alignment": true, "has_unit_key": false},
  "sensors": {"count": 21, "train_exact_constants": ["sensor_01", "sensor_05", "sensor_10", "sensor_16", "sensor_18", "sensor_19"], "test_exact_constants": ["sensor_01", "sensor_05", "sensor_10", "sensor_16", "sensor_18", "sensor_19"], "train_tukey_flags_total": 5406, "test_tukey_flags_total": 3436},
  "reports": ["M2_FD001_FILE_INVENTORY.md", "M2_FD001_RAW_DATA_PROFILE.md", "M2_FD001_DATA_QUALITY.md", "M2_FD001_TREND_ANALYSIS.md", "M2_FD001_DATA_CONTRACT.md"]
}
```

## Deliverables and current status

The script produced the first five required reports. This execution log completes the sixth. Detailed analysis labels physical sensor meaning as UNKNOWN where unsupported. `BASELINE_STATUS: NOT_ESTABLISHED`; descriptive trends and statistical flags are not fault diagnosis. M2 acceptance remains pending independent Research Brain review.

The compile step generated `__pycache__/M2_FD001_analysis.cpython-313.pyc`; it is outside the commit allowlist and will not be staged. Raw source files are excluded from Git. Git commit, push, and remote readback evidence will be added after change review.

## Initial commit and independent remote readback

The first deliverable commit was pushed to the existing `main` branch:

- Commit: `9a163a85570d717888b4f38bb148330d123b25fc`
- URL: https://github.com/chichaofuc/ntust-nasa-ai-lab/commit/9a163a85570d717888b4f38bb148330d123b25fc
- Parent: `1964c1deec490f38f8c16b1897cd2013808eeba6`
- Push result: `1964c1d..9a163a8 main -> main`.
- Remote `refs/heads/main` resolved to `9a163a85570d717888b4f38bb148330d123b25fc`.
- GitHub commit metadata lists exactly the six reports and `M2_FD001_analysis.py`; no source data or unrelated files were committed.

After push, each report was independently fetched from GitHub `main`. Its remote Git Blob SHA matched the local commit's Git Blob SHA:

| File | Remote Git Blob SHA | GitHub |
|---|---|---|
| `M2_FD001_FILE_INVENTORY.md` | `6b0202edef49e99725b259c1284cea6dfd4d7674` | https://github.com/chichaofuc/ntust-nasa-ai-lab/blob/main/M2_FD001_FILE_INVENTORY.md |
| `M2_FD001_RAW_DATA_PROFILE.md` | `3b58fab41dff764716d9650134538d385684d896` | https://github.com/chichaofuc/ntust-nasa-ai-lab/blob/main/M2_FD001_RAW_DATA_PROFILE.md |
| `M2_FD001_DATA_QUALITY.md` | `4c91e3897d4969a0163fcfadcdb55e0fd965e9bf` | https://github.com/chichaofuc/ntust-nasa-ai-lab/blob/main/M2_FD001_DATA_QUALITY.md |
| `M2_FD001_TREND_ANALYSIS.md` | `bd7377b7d5bc8d662aae96c532aff7be725500dc` | https://github.com/chichaofuc/ntust-nasa-ai-lab/blob/main/M2_FD001_TREND_ANALYSIS.md |
| `M2_FD001_DATA_CONTRACT.md` | `05a617f80efc562430718ec90ea8f9a16b01daac` | https://github.com/chichaofuc/ntust-nasa-ai-lab/blob/main/M2_FD001_DATA_CONTRACT.md |
| `M2_FD001_EXECUTION_LOG.md` | `969a9336931f585338f4f2c3c403321620c017ec` | https://github.com/chichaofuc/ntust-nasa-ai-lab/blob/main/M2_FD001_EXECUTION_LOG.md |

The readback verified each fetched path and content was served at the expected report path. Raw data remain excluded. A Python bytecode cache created by `py_compile` is untracked and excluded from all commits; pre-existing untracked user files and the `data/` directory were not staged or modified.

This log update records the post-push verification and will be committed separately, then all six files will be fetched and verified again against the final `main` commit.
