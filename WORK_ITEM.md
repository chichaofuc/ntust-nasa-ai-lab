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
**COMMAND_STATUS:** COMMAND_DISPATCHED (historical dispatch state; Worker execution and review are complete)

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

**Current status:** M2 ACCEPTED_WITH_NOTES; M3 ACCEPTED_WITH_NOTES and CLOSED by STUDENT-MAIN; Web Own Worker execution SUCCESS as reported and reviewed by Web Brain; M4–M5 LOCKED.


## M3 MAIN Acceptance and Closure — M3_FD001_READONLY_API_001

**MAIN DECISION:** ACCEPTED_WITH_NOTES  
**WORKER EXECUTION:** SUCCESS (Worker Return as relayed by STUDENT-WEB Brain)  
**WEB BRAIN REVIEW:** PASS_WITH_NOTES  
**MAIN ACCEPTANCE:** ACCEPTED_WITH_NOTES  
**WORK ITEM STATUS:** CLOSED  
**FINAL REPORTED REMOTE HEAD:** 6572ddfeec2c728b17cde424c11d91a2c7ba9aec  
**IMPLEMENTATION COMMIT:** 84ddd697aef5af67678b0e850779a6bc67983684  
**EXECUTION-LOG COMMIT:** 6572ddfeec2c728b17cde424c11d91a2c7ba9aec  
**DISPATCH BASE:** f2f26d531d80e6afe4a6f134ca70a7906b2c2065

### Acceptance basis

MAIN accepts the M3 read-only API deliverable based on the STUDENT-WEB Brain's independent remote review report, which states that it read the eight delivered files and checked the implementation, API contract, automated tests, source-row reconciliation report/program, execution log, commit ancestry, and changed-file scope.

Reviewed items reported by Web Brain:
- Required GET endpoints: /api/health, /api/catalog, /api/units, and /api/history.
- Success/error response contract, JSON null semantics, validation behavior, and read-only method restrictions.
- Sensor ID 1-based mapping; Sensor 7 maps to sensor_07 and raw column index 11, per the reviewed M2 contract.
- Per-record original source file and 1-based physical source_line provenance.
- 17 automated tests reported passing.
- 40/40 Train/Test source-row matches reported, supported by reconciliation code and report.
- Two commits with the reported parent-child relationship and eight delivered files; Web Brain reported no unauthorized changes.

### Acceptance notes and evidence limitation

1. Web Brain reviewed the reconciliation program and its 40-row report but could not directly access the student's local train_FD001.txt, test_FD001.txt, and RUL_FD001.txt to rerun the raw-source comparison. MAIN therefore accepts the delivered reconciliation evidence as reviewed evidence, not as a fresh independent MAIN- or Web-Brain-executed raw-data verification.
2. MAIN's decision relies on the Web Brain's reported remote readback and review. This record does not claim that MAIN independently reran the API tests or accessed the student's local raw data.
3. M3 acceptance covers the bounded read-only API deliverable only. It does not accept or authorize frontend integration, Evidence Prompt generation, M4, or M5.

### Next milestone boundary

M3_FD001_READONLY_API_001 is CLOSED. M4 Evidence & Traceability System and M5 FD001 Integration & Final Validation remain LOCKED pending their prerequisites and separate explicit MAIN authorization.


## Active Work Item — M4_FD001_INTERACTIVE_WEB_UI_001

**PROJECT:** NTUST NASA AI Lab  
**WORK_ITEM_ID:** M4_FD001_INTERACTIVE_WEB_UI_001  
**CURRENT_MILESTONE:** M4_INTERACTIVE_WEB_UI_AND_SOURCE_TRACEABILITY  
**RELATED_WORK_ITEM:** M3_FD001_READONLY_API_001  
**M3_STATUS:** ACCEPTED_WITH_NOTES / CLOSED  
**MAIN_DECISION:** FORMAL_AUTHORIZATION_CONFIRMED  
**TARGET:** STUDENT-WEB Brain → Web Own Worker (Codex)  
**WORK_ITEM_TYPE:** BOUNDED_INTERACTIVE_FRONTEND_IMPLEMENTATION_AND_BROWSER_UAT  
**AUTHORITY:** STUDENT-MAIN Brain  
**RETURN_TO:** STUDENT-WEB Brain  
**COMMAND_STATUS:** CREATED_NOT_DISPATCHED

### Objective

在學生 workspace 中，以 M3 已驗收的 FD001 唯讀 API 為唯一資料介面，建立可由真實瀏覽器操作的互動式 Engine Health Analysis 網頁。使用者可選擇 Engine Unit、Cycle 範圍及 Sensor，查看感測器趨勢圖及對應的來源資料列，並能追溯每筆顯示資料至 API provenance 與原始 FD001 CSV 的實際列/欄。

### Authorized inputs and dependencies

- M3 已驗收的唯讀 API、API contract、測試及 provenance 定義；Web Brain 必須先從 GitHub `main` 讀取實際檔案並確認其啟動/整合方式。
- M2 已接受的 FD001 Data Contract 與來源檔清單。
- 學生 workspace 中已核驗的 `train_FD001.txt`、`test_FD001.txt`、必要時 `RUL_FD001.txt`。只可讀取，不得修改、移動、重新命名或提交原始資料。

若 M3 API 的實際路由、啟動方式、回應欄位或 provenance 與本工單理解不同，先 STOP 並回報差異，不得猜測或另建一套替代 API。

### Authorized scope

1. 建立可啟動的互動式前端，與 M3 API 整合；不得以硬編碼資料、合成資料或直接由前端另讀 CSV 取代 API。
2. Engine Unit 選單：由 API 的實際 Unit 清單載入；切換 Unit 後，Cycle 範圍及資料必須同步更新。
3. Cycle 範圍選擇：可指定起訖 Cycle，遵守所選 Unit 的有效範圍，拒絕 start > end 或超出有效範圍的輸入。
4. Sensor 選單：依 API catalog / M2 Data Contract 建立，清楚呈現 Sensor ID 與欄位名稱；遵守 M3 的 1-based Sensor ID 規則，不得自行改成 0-based。
5. 趨勢圖：依目前 split、Unit、Cycle 範圍、Sensor 的 API 回應繪製；圖上點數、Cycle、數值須能與來源資料列逐筆核對。明確標示 split、Unit、Sensor、Cycle 範圍及單位（若來源未定義單位則不得自行添加）。
6. 來源資料列：顯示與圖表相同查詢的逐筆資料，至少包含 Cycle、Sensor ID/欄位、數值、source_file、source_line；若 API 有回傳其他 provenance 欄位，可一併呈現。source_line 必須保留 M3 定義的原始檔 1-based physical line 語義。
7. 操作狀態：載入中、無資料、API 錯誤、參數錯誤及資料檔不可用時，需有清楚且不誤導的畫面狀態；不得用舊資料冒充新選擇結果。
8. 提供可複製的啟動命令、必要環境/套件說明、實際啟動後 URL、停止方式及 API base URL 設定方式。URL/port 必須以實際執行結果記錄，不得預先捏造為已驗證。

### Data and scope exclusions

- 唯一資料來源是 M3 FD001 API；不得以 mock、fixture、靜態 JSON、合成資料或 Ch12/GEN-001 作為展示、瀏覽器測試或正式頁面資料。
- 不得由前端直接讀取原始 CSV 作為圖表資料；原始 CSV 僅供受控的 API/CSV 對照驗證。
- 不得修改 M3 API 的資料語義、M2 Data Contract、來源檔或既有 API contract。若需 API 變更，STOP 並提出獨立變更需求。
- 不包含模型訓練、故障診斷結論、預測 RUL、M5 最終整合或其他未授權功能。
- 本工單不要求 Evidence Prompt Generator；不得以其為由擴張範圍。

### Required deliverables

1. 可執行的前端程式、必要設定及入口頁面。
2. `M4_FD001_WEB_UI_CONTRACT.md`：頁面控制項、狀態流、API endpoint/參數對應、圖表與資料列欄位、錯誤處理及啟動設定。
3. `M4_FD001_STARTUP_AND_URL.md`：實際工作目錄、環境需求、安裝命令、啟動命令、實際 URL/port、API base URL、停止命令及成功啟動證據。
4. `M4_FD001_BROWSER_UAT.md`：真實瀏覽器或人工操作測試紀錄，包含瀏覽器/版本、時間、URL、逐步操作、預期/實際結果、通過/失敗、Console/Network 錯誤觀察及測試證據位置。
5. `M4_FD001_API_CSV_UI_RECONCILIATION.md`：代表性查詢的 UI 顯示值、瀏覽器 Network/API JSON、API provenance、原始 CSV 精確 physical line 與欄位值的逐筆對照；至少涵蓋 train 與 test、不同 Unit、不同 Sensor 及 Cycle 範圍。若因原始檔無法存取而不能對照，必須 STOP/標記 BLOCKED，不得以推測值替代。
6. 自動化前端測試（若適用）及實際執行命令/結果；自動化測試不能取代真實瀏覽器或人工操作 UAT。
7. 執行紀錄：workspace、Git base/commit、變更檔清單、啟動/測試命令、實際 URL、瀏覽器操作證據、API/CSV 對照結果、原始檔未變更證據。

### Mandatory real-browser / human-operation UAT

必須實際啟動 API 與前端，並在真實瀏覽器中操作（可使用 Playwright/Selenium 等真實瀏覽器自動化，或由人員依步驟操作並記錄）。至少完成：

- 開啟實際啟動 URL，確認頁面載入及 API 健康狀態。
- 選擇至少兩個不同 Engine Unit，確認 Unit 切換後 Cycle 有效範圍、圖表及來源資料列更新。
- 調整 Cycle 起訖範圍，確認圖表點與表格列只涵蓋該範圍。
- 切換至少兩個 Sensor，確認 Sensor 欄位映射正確、圖表及表格同步更新。
- 分別驗證 train 與 test split（若 UI 提供 split 選擇；若不提供，須在 UAT 說明實際支援範圍並提出決策，不得自行假設）。
- 驗證無效範圍、空結果或 API 錯誤時的 UI 狀態；不得保留舊結果造成誤判。
- 至少選取 train/test 的代表性資料點，從畫面追到 Network/API JSON 的 source_file/source_line，再對照原始 CSV 同一 physical line 與 sensor 欄位值。

證據必須包含可稽核的操作軌跡（逐步人工操作紀錄，或 Playwright/Selenium trace/log/影片等）及必要畫面。**靜態截圖、設計稿、單純 HTTP/API 測試、或僅聲稱「可操作」均不足以通過 UAT。** 截圖只能作為操作軌跡的補充。

### Acceptance criteria

- [ ] 使用者可在真實啟動的頁面選擇 Engine Unit、Cycle 起訖範圍及 Sensor。
- [ ] 控制項資料來自 M3 API/catalog；不使用合成或硬編碼業務資料。
- [ ] 趨勢圖與來源資料表由同一組 API 查詢結果產生，切換條件後同步更新且不殘留舊資料。
- [ ] 圖表每個點可對應到表格列；Cycle、Sensor、數值及 provenance 一致。
- [ ] source_file/source_line 保留 M3 定義，且代表性 train/test 資料列可對照原始 CSV 精確列與欄。
- [ ] 真實瀏覽器或人工操作 UAT 完成，含至少兩個 Unit、兩個 Sensor、Cycle 範圍變更及錯誤/空狀態測試。
- [ ] 提供實際啟動命令與實際可開啟 URL/port；由執行紀錄證明，不得只提供範例 URL。
- [ ] 提供 API JSON、畫面值及 CSV 原始列逐筆對照證據；train/test 均有代表案例。
- [ ] 自動化測試與 UAT 命令/結果完整記錄；無未解決的 Console/Network 錯誤。
- [ ] 原始資料、M3 API contract 及 M2 Data Contract 未被未授權修改；無 GEN-001/Ch12 synthetic data。
- [ ] 只提交授權的前端、測試、文件及證據；推送至 GitHub `main`，Web Brain 讀回實際檔案並審查後才可推薦 PASS。

### STOP_IF

M3 API 檔案/啟動方式/契約無法確認；M2 Data Contract 或欄位映射不清；本機原始 FD001 檔案缺失或無法核對；需要修改 M3 API 或原始資料；需使用合成/替代資料；無法啟動真實瀏覽器 UAT；無法取得實際 URL/操作證據/API-CSV 對照；工作目錄不明；可能覆寫無關檔案；GitHub 讀取、push 或 readback 失敗；或工作範圍擴張至模型訓練、診斷或 M5。

### Dispatch and review gates

- 本工單為 MAIN 正式授權，**不等同 Worker 已派發或開始執行**。
- Web Brain 必須先讀取 GitHub `main` 最新 `AGENTS.md`、本工單、M3 API 實際檔案/API contract，以及 M2 Data Contract/驗收紀錄；確認依賴可用後，才可建立完整 Worker 命令。
- Web Brain 準備命令後，狀態仍為 `CREATED_NOT_DISPATCHED`。只有 Owner 將正式命令貼給 Web Own Worker 並標記 `COMMAND_DISPATCHED`，Worker 才可開始。
- Worker Return → Web Brain 獨立複審（讀回實際 push 檔案、核對瀏覽器操作軌跡與 API/CSV 對照）→ STUDENT-MAIN 最終驗收。
- 不得以靜態截圖或 Worker 自述取代實際 UAT 證據；未滿足任一必要驗收條件不得宣告 PASS。

**Current status:** M3 ACCEPTED_WITH_NOTES / CLOSED; M4 FORMALLY AUTHORIZED / CREATED_NOT_DISPATCHED; M5 LOCKED.
