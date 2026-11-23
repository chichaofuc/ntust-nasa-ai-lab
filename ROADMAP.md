# NTUST NASA AI Lab — Roadmap

The project follows milestone-controlled, sequential development. M1–M5 must not begin until the prior Work Item has been completed, reviewed, accepted by MAIN, and explicitly authorized.

## M0 — Project Governance & Environment Initialization

**Objective:** Establish project governance, file structure, Git, and GitHub synchronization.

**Deliverables:** `AGENTS.md`, `ROADMAP.md`, `WORK_ITEM.md`, `DECISIONS.md`, Git repository, GitHub repository.

**Acceptance:** All governance files exist and are complete, committed, pushed, and verified from GitHub.

## M1 — Synthetic Dataset Profile

**Objective:** Analyze six synthetic CSV records using the local `synthetic_sensor.csv`.

**Deliverables:** Dataset Profile, Schema Report, Quality Report, Sensor Statistics, Initial Observations.

**Acceptance:** Every reported result is derived from the actual dataset; no analysis is fabricated.

## M2 — Data Pipeline & Sensor Analysis Engine

**Objective:** Build reusable data loading, filtering, and analysis modules.

**Deliverables:** Data Loader; Engine/Cycle/Sensor Selection; Statistical Analysis; Trend Analysis; Unit Tests.

**Acceptance:** Results are reproducible and traceable to source data.

## M3 — Health Analysis Web MVP

**Objective:** Develop a local interactive analysis website.

**Deliverables:** Engine Unit Selection; Cycle Selection; Sensor Selection; Trend Charts; Statistics Dashboard.

**Acceptance:** UI results match the underlying data and analysis engine.

## M4 — Evidence & Traceability System

**Objective:** Generate evidence traceable to original source data.

**Deliverables:** Evidence Schema; Source References; Statistical Evidence; Evidence Prompt Generator; Copyable AI Prompt.

**Acceptance:** Evidence accurately reflects selections and source data.

## M5 — NASA C-MAPSS FD001 Integration & Final Validation

**Objective:** Integrate NASA C-MAPSS FD001 and complete the final Engine Health Analysis application.

**Deliverables:** FD001 Data Adapter; Full Engine/Cycle/Sensor Analysis; Final Web Application; Integration Tests; Validation Report.

**Acceptance:** All required functionality works on actual FD001 data, with reproducible and traceable results.

**Current authorization:** M0 only. Do not start M1–M5 under Work Item `WO-M0-001`.
