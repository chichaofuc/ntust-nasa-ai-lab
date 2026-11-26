# NTUST NASA AI Lab — Roadmap

The project follows milestone-controlled, sequential development. M0 is ACCEPTED. M1 Governance Sync is PASS_WITH_NOTES with MAIN acceptance PENDING. M1 Governance Status Clarification is AUTHORIZED and IN_PROGRESS_UNTIL_VERIFIED. M1 Dataset Profile is NOT_ACCEPTED and its domain acceptance is NOT_ESTABLISHED. M2 is LOCKED with release NOT_AUTHORIZED; M3–M5 are LOCKED.

## M0 — Project Governance & Environment Initialization

**Objective:** Establish project governance, file structure, Git, and GitHub synchronization.

**Deliverables:** `AGENTS.md`, `ROADMAP.md`, `WORK_ITEM.md`, `DECISIONS.md`, Git repository, GitHub repository.

**Acceptance:** All governance files exist and are complete, committed, pushed, and verified from GitHub.

**Status:** ACCEPTED by STUDENT-MAIN Brain; acceptance evidence is recorded in M1_GOVERNANCE_SYNC_001.

## M1 — Synthetic Dataset Profile

**Objective:** Analyze six synthetic CSV records using the local `synthetic_sensor.csv`.

**Deliverables:** Dataset Profile, Schema Report, Quality Report, Sensor Statistics, Initial Observations.

**Acceptance:** Every reported result is derived from the actual dataset; no analysis is fabricated.

**Status:** M1 Governance Sync is PASS_WITH_NOTES; MAIN acceptance is PENDING. The Governance Status Clarification is AUTHORIZED under M1_GOVERNANCE_STATUS_CLARIFICATION_001 and remains IN_PROGRESS_UNTIL_VERIFIED. M1 Dataset Profile is NOT_ACCEPTED; domain acceptance is NOT_ESTABLISHED. Do not execute or dispatch the profile under this clarification Work Item.

## M2 — Data Pipeline & Sensor Analysis Engine

**Status:** LOCKED; M2_RELEASE is NOT_AUTHORIZED.

**Objective:** Build reusable data loading, filtering, and analysis modules.

**Deliverables:** Data Loader; Engine/Cycle/Sensor Selection; Statistical Analysis; Trend Analysis; Unit Tests.

**Acceptance:** Results are reproducible and traceable to source data.

## M3 — Health Analysis Web MVP

**Status:** LOCKED pending its prerequisites, acceptance, and explicit MAIN authorization.

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

**Current authorization:** M0 is ACCEPTED. Governance Status Clarification M1_GOVERNANCE_STATUS_CLARIFICATION_001 is AUTHORIZED and IN_PROGRESS_UNTIL_VERIFIED. M1 Dataset Profile is NOT_ACCEPTED and domain acceptance is NOT_ESTABLISHED. M2 is LOCKED with release NOT_AUTHORIZED; M3–M5 are LOCKED.
