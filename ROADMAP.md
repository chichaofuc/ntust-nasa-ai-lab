# NTUST NASA AI Lab — Roadmap

The project follows milestone-controlled, sequential development. M0 is ACCEPTED. M1 Governance Sync and M1 Governance Status Clarification are ACCEPTED_WITH_NOTES. M1 Dataset Profile is ACCEPTED_WITH_NOTES and M1 Domain Acceptance is ESTABLISHED by formal MAIN authorization. M2 FD001 Local Data Validation is ACCEPTED_WITH_NOTES by STUDENT-MAIN. M3 Health Analysis Web MVP is ACCEPTED_WITH_NOTES under M3_FD001_READONLY_API_001. M4–M5 remain LOCKED.

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

## M4 — Evidence & Traceability System

**Status:** LOCKED pending its prerequisites, acceptance, and explicit MAIN authorization.

**Objective:** Generate evidence traceable to original source data.

**Deliverables:** Evidence Schema; Source References; Statistical Evidence; Evidence Prompt Generator; Copyable AI Prompt.

**Acceptance:** Evidence accurately reflects selections and source data.

## M5 — NASA C-MAPSS FD001 Integration & Final Validation

**Status:** LOCKED pending its prerequisites, acceptance, and explicit MAIN authorization.

**Objective:** Integrate NASA C-MAPSS FD001 and complete the final Engine Health Analysis application.

**Deliverables:** FD001 Data Adapter; Full Engine/Cycle/Sensor Analysis; Final Web Application; Integration Tests; Validation Report.

**Acceptance:** All required functionality works on actual FD001 data, with reproducible and traceable results.

**Current authorization:** M0 is ACCEPTED. M1 Dataset Profile is ACCEPTED_WITH_NOTES and M1 Domain Acceptance is ESTABLISHED. M2 FD001 Local Data Validation is ACCEPTED_WITH_NOTES. M3 Health Analysis Web MVP is ACCEPTED_WITH_NOTES under M3_FD001_READONLY_API_001. M4–M5 remain LOCKED.
