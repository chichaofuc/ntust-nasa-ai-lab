# NTUST NASA AI Lab — Roadmap

The project follows milestone-controlled, sequential development. M0 is ACCEPTED. M1 Governance Sync and M1 Governance Status Clarification are ACCEPTED_WITH_NOTES. M1 Dataset Profile is ACCEPTED_WITH_NOTES and M1 Domain Acceptance is ESTABLISHED. M2 FD001 Local Data Validation is ACCEPTED_WITH_NOTES. M3 Health Analysis Web MVP is ACCEPTED_WITH_NOTES / CLOSED. M4 Interactive Web UI & Source Traceability is ACCEPTED_WITH_NOTES by STUDENT-MAIN. M5 Evidence Prompt Generator is FORMAL_DISPATCH_AUTHORIZED under `M5_FD001_EVIDENCE_PROMPT_GENERATOR_001`.

## M0 — Project Governance & Environment Initialization

**Objective:** Establish project governance, file structure, Git, and GitHub synchronization.

**Deliverables:** `AGENTS.md`, `ROADMAP.md`, `WORK_ITEM.md`, `DECISIONS.md`, Git repository, GitHub repository.

**Acceptance:** All governance files exist and are complete, committed, pushed, and verified from GitHub.

**Status:** ACCEPTED by STUDENT-MAIN Brain; acceptance evidence is recorded in M1_GOVERNANCE_SYNC_001.

## M1 — Synthetic Dataset Profile

**Objective:** Analyze six synthetic CSV records using the local `synthetic_sensor.csv`.

**Deliverables:** Dataset Profile, Schema Report, Quality Report, Sensor Statistics, Initial Observations.

**Acceptance:** Every reported result is derived from the actual dataset; no analysis is fabricated.

**Status:** ACCEPTED_WITH_NOTES. M1 Domain Acceptance: ESTABLISHED by formal MAIN authorization in M2_FD001_LOCAL_DATA_VALIDATION_001.

## M2 — Data Pipeline & Sensor Analysis Engine

**Status:** ACCEPTED_WITH_NOTES by STUDENT-MAIN after Research Brain review of the final return and remote evidence.

**Objective:** Build reusable data loading, filtering, and analysis modules.

**Deliverables:** Data Loader; Engine/Cycle/Sensor Selection; Statistical Analysis; Trend Analysis; Unit Tests.

**Acceptance:** Results are reproducible and traceable to source data.

## M3 — Health Analysis Web MVP

**Status:** ACCEPTED_WITH_NOTES by STUDENT-MAIN under M3_FD001_READONLY_API_001. Read-only API implementation and Web Brain review are complete. Acceptance notes: Web Brain reviewed the source-row reconciliation program/report and Worker execution evidence but could not independently rerun reconciliation against the student's local original FD001 files. M4 remains LOCKED.

**Objective:** Develop a local interactive analysis website.

**Deliverables:** Engine Unit Selection; Cycle Selection; Sensor Selection; Trend Charts; Statistics Dashboard.

**Acceptance:** UI results match the underlying data and analysis engine.

## M4 — Interactive Web UI & Source Traceability

**Status:** ACCEPTED_WITH_NOTES by STUDENT-MAIN. Worker commit `f50062671efd1f6890a990ff19f31428fc195570`; Web Brain review PASS_WITH_NOTES. Worker-submitted browser UAT 9/9 and API/CSV/UI reconciliation 62/62 accepted as evidence. MAIN did not claim independent local reproduction.

**Objective:** Build a real, interactive browser UI on the accepted M3 FD001 read-only API, supporting Engine Unit, Cycle range, Sensor selection, trend visualization, and source-row display.

**Deliverables:** Runnable frontend; startup command and actual URL; browser/human-operation UAT trace; UI/API/original CSV row-level reconciliation; UI contract and execution evidence.

**Acceptance:** Real-browser operations prove that selections update the chart and source rows consistently, and representative train/test values match API provenance and exact original CSV physical lines. Static screenshots alone are insufficient.

## M5 — Evidence Prompt Generator

**Status:** FORMAL_DISPATCH_AUTHORIZED by STUDENT-MAIN under `M5_FD001_EVIDENCE_PROMPT_GENERATOR_001`. This is authorization for the bounded Evidence Prompt Generator only; the Own Worker implementation dispatch is a separate next step.

**Objective:** Generate a reproducible, copyable AI Prompt from the current FD001 UI selection and verified M3 API observations, including statistics, data quality, provenance, and KNOWN / INFERRED / UNKNOWN classification.

**Deliverables:** Evidence Prompt Generator section; synchronized dynamic preview; exact-copy button; evidence and provenance summaries; safety-constrained prompt; tests and browser UAT evidence.

**Scope lock:** No M3 API or M2 Data Contract changes; no raw FD001 modification; no synthetic data; no ML, fault diagnosis, RUL, failure-time/probability prediction, or unsupported extrapolation.

**Acceptance:** AC01–AC14 in the formal MAIN Work Item `M5_FD001_EVIDENCE_PROMPT_GENERATOR_001` remain unchanged and authoritative.

**Current milestone status:** M4 ACCEPTED_WITH_NOTES; M5 FORMAL_DISPATCH_AUTHORIZED.
