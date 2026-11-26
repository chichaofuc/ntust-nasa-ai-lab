# Historical Work Item Record — WO-M0-001

**PROJECT:** NTUST NASA AI Lab  
**CURRENT_MILESTONE:** M0  
**HISTORICAL_WORK_ITEM:** WO-M0-001
**WORK_ITEM_TYPE:** BOUNDED_WORK_ORDER  
**TARGET:** MAIN Own Worker (Codex)

## Objective

Create the governance files, initialize Git, create the authorized GitHub repository, and commit and push M0 governance.

## Input

Existing project root directory.

## Expected output

- `AGENTS.md`, `ROADMAP.md`, `WORK_ITEM.md`, and `DECISIONS.md`
- Git initialization and first commit
- Public GitHub repository `ntust-nasa-ai-lab`
- Successful push to `main`
- Remote verification evidence

## Acceptance criteria

1. All four governance files exist and contain complete governance rules.
2. Git is initialized or any existing repository is safely preserved.
3. The branch is `main`.
4. The first commit uses exactly `chore(M0): initialize AI team governance and roadmap`.
5. Public repository `ntust-nasa-ai-lab` exists.
6. The remote is correctly configured.
7. Changes are pushed to GitHub `main`.
8. Brain can access and inspect actual GitHub contents.
9. No unrelated data was modified.
10. No secrets were committed.
11. Evidence and commit SHA are returned.

## STOP_IF

Wrong project directory; existing files would be overwritten; existing repository has conflicting history; GitHub authentication or repository creation is unavailable; push fails; public repository name is unavailable; destructive action is required; or verification cannot be performed.

## RETURN_TO

STUDENT-MAIN Brain

## Status

**BLOCKED** — local governance files are committed, but GitHub repository creation, push, and remote verification could not be performed because GitHub CLI (`gh`) is unavailable. Local completion does not constitute acceptance.

## M0 Recovery Success

**Work Item:** M1_GOVERNANCE_SYNC_001
**Repository:** https://github.com/chichaofuc/ntust-nasa-ai-lab
**Visibility:** PUBLIC
**Branch:** main
**Verified main HEAD:** 16b017d69fd0b60e538032bc2c6082af558e22f2
**Evidence:** GitHub repository metadata reports public visibility and main as the default branch. GitHub main ref and commit history identify the same commit and the original required commit message. All four governance files were retrieved from GitHub main and their blob SHAs match the local files at the verified baseline commit. The original four-file M0 commit is present remotely. Baseline file blob SHAs: AGENTS.md 2db2eb112870abb2b4c71ac5bd85477da5c27405; ROADMAP.md 729db84c6fdbb00931404dc71d31698ddcfae9db; WORK_ITEM.md c5d888b0894f47d4d650f0b274895ba4f2e14c00; DECISIONS.md 33772aef18d11427a954c26be3d361031549960b.

## MAIN M0 Acceptance

**Decision:** M0_STATUS = ACCEPTED.
**Authority:** STUDENT-MAIN Brain.
**Evidence reference:** M1_GOVERNANCE_SYNC_001 and the verified M0 commit and remote files listed above. No separate MAIN decision ID was supplied.

## MAIN M1 Authorization

**Decision:** M1_STATUS = AUTHORIZED, pending governance synchronization and MAIN review/dispatch.
**Authorized Work Item:** M1_DATASET_PROFILE_001.
**Execution status:** NOT STARTED. Dataset Profile work must not begin until this governance update is pushed, remotely verified, and reviewed for dispatch by MAIN.
**M2–M5:** LOCKED.

## Historical Authorization Record — M1_DATASET_PROFILE_001

**PROJECT:** NTUST NASA AI Lab
**CURRENT_MILESTONE:** M1_SYNTHETIC_DATASET_PROFILE
**ACTIVE_WORK_ITEM:** M1_DATASET_PROFILE_001
**WORK_ITEM_TYPE:** BOUNDED_WORK_ORDER
**TARGET:** Research Own Worker (Codex)
**STATUS:** AUTHORIZED_BUT_BLOCKED_PENDING_GOVERNANCE_SYNC

This Work Item is authorized for the M1 Dataset Profile only after governance synchronization and MAIN review/dispatch. No M1 analysis has been performed under M1_GOVERNANCE_SYNC_001.

## Historical Record — M1 Governance Sync Execution and Acceptance Status

**Work Item:** M1_GOVERNANCE_SYNC_001
**Result:** PASS_WITH_NOTES.
**MAIN acceptance:** PENDING.
**Verified baseline commit:** 7e95db3494567f96bb6546df8456d150c40551eb.
**Evidence:** This commit was the expected GitHub main HEAD at clarification dispatch. Its parent is the original M0 commit 16b017d69fd0b60e538032bc2c6082af558e22f2. The current status values below are supplied by M1_GOVERNANCE_STATUS_CLARIFICATION_001; no MAIN acceptance of the Governance Sync is claimed here.

## Historical Governance Status Snapshot — before acceptance sync

M0_STATUS: ACCEPTED

M1_GOVERNANCE_SYNC:
  STATUS: PASS_WITH_NOTES
  MAIN_ACCEPTANCE: PENDING

M1_GOVERNANCE_STATUS_CLARIFICATION:
  STATUS: AUTHORIZED
  EXECUTION: IN_PROGRESS_UNTIL_VERIFIED

M1_DATASET_PROFILE:
  DOMAIN_ACCEPTANCE: NOT_ESTABLISHED
  MAIN_ACCEPTANCE: NOT_ACCEPTED

M2_STATUS: LOCKED
M2_RELEASE: NOT_AUTHORIZED

M3_M5_STATUS: LOCKED

## Historical Active Work Item Record — M1_GOVERNANCE_STATUS_CLARIFICATION_001

**PROJECT:** NTUST NASA AI Lab
**CURRENT_MILESTONE:** M1_SYNTHETIC_DATASET_PROFILE
**ACTIVE_WORK_ITEM:** M1_GOVERNANCE_STATUS_CLARIFICATION_001
**RELATED_WORK_ITEM:** M1_DATASET_PROFILE_001
**WORK_ITEM_TYPE:** BOUNDED_GOVERNANCE_UPDATE
**TARGET:** Research Own Worker (Codex)
**STATUS:** AUTHORIZED
**EXECUTION:** IN_PROGRESS_UNTIL_VERIFIED

This Work Item updates governance status only. M1 Dataset Profile remains NOT_ACCEPTED and has not been executed or dispatched. M2–M5 remain LOCKED.

## M1 Governance Acceptance Synchronization — 2026-11-26

**Work Item:** M1_GOVERNANCE_ACCEPTANCE_SYNC_001
**Prior clarification Work Item:** M1_GOVERNANCE_STATUS_CLARIFICATION_001
**Research Review:** PASS_WITH_NOTES.
**MAIN acceptance of Governance Sync:** ACCEPTED_WITH_NOTES.
**MAIN acceptance of Governance Status Clarification:** ACCEPTED_WITH_NOTES.
**Evidence commit:** 23be3089a26ea993ab4344de00aac8e759b9887f ([GitHub commit](https://github.com/chichaofuc/ntust-nasa-ai-lab/commit/23be3089a26ea993ab4344de00aac8e759b9887f)).
**Evidence reference:** M1_GOVERNANCE_STATUS_CLARIFICATION_001 and the formal MAIN decision in M1_GOVERNANCE_ACCEPTANCE_SYNC_001.

## Current Governance Status

M0_GOVERNANCE: ACCEPTED

M1_GOVERNANCE_SYNC:
  STATUS: ACCEPTED_WITH_NOTES
  MAIN_ACCEPTANCE: ACCEPTED_WITH_NOTES

M1_GOVERNANCE_STATUS_CLARIFICATION:
  STATUS: ACCEPTED_WITH_NOTES
  RESEARCH_REVIEW: PASS_WITH_NOTES
  MAIN_ACCEPTANCE: ACCEPTED_WITH_NOTES

M1_DATASET_PROFILE:
  STATUS: NOT_ACCEPTED
  DOMAIN_ACCEPTANCE: NOT_ESTABLISHED
  MAIN_ACCEPTANCE: NOT_ACCEPTED

M2_FD001_VALIDATION:
  STATUS: LOCKED
  M2_RELEASE: NOT_AUTHORIZED

M3_M5_STATUS: LOCKED

## Next Separately Authorized Work Item

**WORK_ITEM_ID:** M1_DATASET_PROFILE_001
**STATUS:** AUTHORIZED, NOT_DISPATCHED
**NEXT_STEP:** Await its own Research Brain dispatch and user-pasted Worker command.
**EXECUTION:** NOT_STARTED. Dataset Profile is not completed or accepted.

 
## Current Active Work Item — M2_FD001_LOCAL_DATA_VALIDATION_001

**PROJECT:** NTUST NASA AI Lab  
**CURRENT_MILESTONE:** M2_FD001_LOCAL_DATA_VALIDATION  
**AUTHORITY:** STUDENT-MAIN Brain  
**MAIN_DECISION:** FORMAL_AUTHORIZATION_CONFIRMED  
**AUTHORIZATION STATUS:** FORMALLY AUTHORIZED  
**TARGET:** Research Brain → Research Own Worker (Codex)  
**RETURN_TO:** STUDENT-MAIN Brain

### MAIN acceptance and prerequisite status

- M0 Governance: ACCEPTED.
- M1 Dataset Profile: ACCEPTED_WITH_NOTES.
- M1 Domain Acceptance: ESTABLISHED.
- M2 FD001 Local Data Validation: FORMALLY AUTHORIZED.
- M2 MAIN Acceptance: PENDING.

### Authorized input and scope

Only the Owner's existing local train_FD001.txt, test_FD001.txt, and RUL_FD001.txt may be used. Actual paths must be confirmed locally. Do not download, substitute, modify, move, reformat, or commit raw source files. No FD002, FD004, synthetic data, model training, website/API integration, or scope expansion is authorized.

The Work Item consists of Phase A — local file and raw data validation — followed by Phase B — Engine/Cycle/Sensor trend evidence and data quality. Phase B is authorized but strictly gated: it may begin only after Phase A passes. If Phase A does not pass, Phase B remains blocked.

### Required deliverables

1. M2_FD001_FILE_INVENTORY.md
2. M2_FD001_RAW_DATA_PROFILE.md
3. M2_FD001_DATA_QUALITY.md
4. M2_FD001_TREND_ANALYSIS.md
5. M2_FD001_DATA_CONTRACT.md
6. M2_FD001_EXECUTION_LOG.md

The complete authoritative requirements, Phase A/B acceptance gates, evidence rules, Data Contract requirements, Git rules, STOP_IF conditions, and return format are contained in the formal MAIN work order M2_FD001_LOCAL_DATA_VALIDATION_001 issued on 2026-11-26. Research Brain must include that full work order in the Worker command; it must not be reduced to a summary or reference only.

### Governance synchronization and dispatch gate

Research Brain is explicitly authorized to synchronize the four governance files (AGENTS.md, ROADMAP.md, WORK_ITEM.md, DECISIONS.md) with this MAIN decision, preserving historical records, and to remotely read back all four files. Only after successful remote readback may Research Brain create the formal Worker dispatch command. The Worker is NOT_YET_DISPATCHED until the Owner pastes that command to the Worker.

**Current execution status:** Research Own Worker NOT_YET_DISPATCHED; Phase A PENDING; Phase B LOCKED_PENDING_PHASE_A; M2 MAIN Acceptance PENDING.


---

## Active Work Item — M3_FD001_READONLY_API_001

**PROJECT:** NTUST NASA AI Lab  
**WORK_ITEM_ID:** M3_FD001_READONLY_API_001  
**CURRENT_MILESTONE:** M3_WEB_MVP  
**RELATED_WORK_ITEM:** M2_FD001_LOCAL_DATA_VALIDATION_001  
**M2_STATUS:** ACCEPTED_WITH_NOTES  
**MAIN_DECISION:** FORMAL_AUTHORIZATION_CONFIRMED  
**TARGET:** STUDENT-WEB Brain → Web Own Worker (Codex)  
**WORK_ITEM_TYPE:** BOUNDED_READONLY_API_IMPLEMENTATION  
**AUTHORITY:** STUDENT-MAIN Brain  
**RETURN_TO:** STUDENT-WEB Brain  
**COMMAND_STATUS:** CREATED_NOT_DISPATCHED

### Objective

在學生 workspace 中，使用 M2 已驗證的 NASA C-MAPSS FD001 原始資料建立唯讀 API，供後續健康分析網站讀取 Engine Unit、Cycle、Sensor 與歷史感測器數值。此工單只涵蓋 API、來源列追溯與 API 測試，不包含前端、模型訓練或 M4 Evidence Prompt 功能。

### Authorized inputs and data boundary

只允許使用 M2 工單驗證的原始檔：
- `train_FD001.txt`
- `test_FD001.txt`
- `RUL_FD001.txt`

Worker 必須先在學生 workspace 確認實際檔案路徑、檔案存在性及 SHA-256，並與 M2 已接受的檔案清單／Data Contract 對照。若路徑、雜湊或格式不一致，立即 STOP，不得自行尋找替代資料。

**明確禁止：**
- 不得讀取、合併、轉換或引用 GEN-001。
- 不得讀取、合併、轉換或引用 Ch12 合成 CSV，包括任何 synthetic sensor CSV。
- 不得以合成資料補值、測試 API、展示範例或產生測試快照。
- 不得下載其他 NASA 資料集或重新取得 FD001 檔案。
- 不得修改、移動、重命名或提交三份原始資料檔；不得提交原始資料副本。
- 不得改變 M2 Data Contract 已定義的 Unit、Cycle、Operating Settings、Sensor 欄位語義與欄位順序。

### Required API

至少實作以下唯讀 GET endpoints：

1. `GET /api/health`
   - 回報 API 狀態、資料檔可讀狀態、實際使用的資料來源識別及必要的資料驗證摘要。
   - 不得只因 Flask 啟動就回報資料健康；資料檔缺失或驗證失敗時必須明確回報 degraded/error。

2. `GET /api/catalog`
   - 回傳資料集識別、split、欄位索引／欄位名稱、Unit/Cycle/Operating Settings/Sensor 定義、欄位數及 provenance 規則。
   - 欄位 mapping 必須逐項符合 M2 Data Contract，不得自行重新命名或猜測。

3. `GET /api/units?split=train`
   - 支援 `train`、`test`，回傳該 split 真實存在的 Unit ID 清單及必要的 cycle 範圍摘要。
   - 不得從另一 split 或合成資料補出 Unit。

4. `GET /api/history?split=train&unit=1&sensor=7&start=1&end=20`
   - 支援 `train`、`test`；依 Unit、Sensor、Cycle 範圍回傳實際歷史列。
   - 回傳每筆記錄的 Unit ID、Cycle、Sensor ID／欄位、數值，以及 provenance。
   - Sensor ID 的索引基準必須在 catalog 清楚聲明，並依 M2 Data Contract 一致實作；不可默默將 0-based 與 1-based 混用。
   - Test split 的 RUL 若被提供，必須依 M2 已確認的 test Unit 順序與 RUL positional mapping 對應，並標明其來源為 `RUL_FD001.txt`；不得將 RUL 當作 test 原始列中的欄位。

### Source-row traceability — mandatory

API 每筆 history record 必須可追溯至原始檔實際列，不可只回傳轉換後 DataFrame 的列索引。

- Train record：回傳 `source_file=train_FD001.txt`、1-based physical `source_line`，以及 split、Unit ID、Cycle、Sensor 欄位識別。
- Test record：回傳 `source_file=test_FD001.txt`、1-based physical `source_line`，以及 split、Unit ID、Cycle、Sensor 欄位識別。
- RUL mapping：若回傳 RUL，提供 `source_file=RUL_FD001.txt`、1-based physical `source_line`、test Unit ID、test Unit 順序索引及 mapping 說明。
- 每筆 API 數值都必須能用「來源檔 + 原始列號 + 欄位索引」回到原始資料列並核對。若讀檔流程會過濾空白列或重新排序，必須保留原始 physical line mapping。
- 不可用推估列號、DataFrame index 或排序後索引冒充原始來源列號。

### Response contract

所有成功與錯誤回應均使用一致 JSON 格式，並在 API 文件中列出實際 schema 與範例。

- Success：至少包含 `ok: true`、`data`、`provenance` 或逐筆 provenance。
- Error：至少包含 `ok: false`、穩定的 `error.code`、可讀的 `error.message`；不得回傳 traceback、絕對路徑中的敏感資訊或原始資料全文。
- 缺值：JSON 一律使用 `null`，不得以 0、空字串、前值填補或其他 sentinel 假裝有觀測值。
- 不存在的 Unit／Cycle／Sensor 或查詢範圍：使用一致且文件化的 4xx 回應；參數格式錯誤、split 不支援、start>end 等均須明確拒絕。
- 資料檔不存在、讀取失敗、hash mismatch 或 schema mismatch：health 不得回報 healthy，history 不得靜默回傳空資料或 fallback 至其他資料集。
- API 僅提供 GET；不得新增資料寫入、刪除、更新或原始檔修改 endpoint。

### Required deliverables

1. Read-only API implementation and application entry point.
2. API contract document covering all endpoints, query parameters, success/error schema, null semantics, sensor index basis, and provenance.
3. Tests for all endpoints, validation errors, missing values, source-row mapping, and failure behavior.
4. Source-row cross-check report containing representative records from train and test (and RUL mapping if exposed), with API output compared directly against the exact original file line and column.
5. Execution log recording workspace, source paths, SHA-256 readback, commands, test results, commit SHA and changed-file list.

### Acceptance criteria

- [ ] All three source files are verified against the accepted M2 inventory/Data Contract before use.
- [ ] No GEN-001 or Ch12 synthetic CSV is accessed or mixed into API code, fixtures, tests, or outputs.
- [ ] All four required endpoints work with documented response contracts.
- [ ] Unit/Cycle/Sensor mapping matches M2 Data Contract.
- [ ] Missing observations serialize as JSON null, never fabricated numeric values.
- [ ] Every returned history row includes verifiable original source file and 1-based physical source line.
- [ ] Representative train/test API records are independently reconciled against exact raw source lines and columns; RUL positional mapping is reconciled if exposed.
- [ ] Invalid parameters, unsupported split, unknown IDs, missing files, hash mismatch and schema mismatch are handled explicitly.
- [ ] API is read-only and raw source files remain unchanged.
- [ ] Automated tests pass; actual test command and output are recorded.
- [ ] Only authorized code, tests, API contract and evidence files are committed; no raw datasets, synthetic datasets, credentials or unrelated files.
- [ ] Changes are pushed to GitHub `main`; Web Brain reads back the actual pushed files before recommending PASS.

### STOP_IF

Any source file is missing; SHA-256 differs from M2 accepted inventory; M2 Data Contract cannot resolve a field/index ambiguity; source-row mapping cannot be preserved; GEN-001 or Ch12 synthetic CSV would be required or is encountered; API requires data substitution or source modification; workspace/path is ambiguous; unrelated files would be overwritten; scope expands to frontend, model training, or M4; GitHub access/push/readback fails; or evidence cannot be independently checked.

### Dispatch and review gates

- This governance record authorizes M3 scope but does not itself dispatch the Worker.
- Web Brain must read the latest `AGENTS.md` from GitHub `main`, verify this Work Item and M2 acceptance status, then prepare the complete Worker command.
- Worker execution begins only after the Owner pastes the formal command with `COMMAND_STATUS: COMMAND_DISPATCHED`.
- Worker Return → Web Brain independent review → STUDENT-MAIN acceptance.
- No PASS or M3 completion may be claimed before actual pushed-file readback and source-row reconciliation evidence.

**Current status:** M3 FORMALLY AUTHORIZED; GOVERNANCE SYNC IN PROGRESS; Web Own Worker NOT_DISPATCHED.
