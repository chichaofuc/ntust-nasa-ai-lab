# Decision Log — NTUST NASA AI Lab

## D001 — Milestone-controlled workflow

**Project:** NTUST NASA AI Lab  
**Decision:** The project uses a milestone-controlled workflow M0–M5.  
**Status:** APPROVED  
**Authority:** Student Owner

## D002 — Main branch

**Decision:** The project uses one main branch named `main`.  
**Status:** APPROVED

## D003 — Sequential development

**Decision:** The next Work Item cannot begin until the previous Work Item is verified, accepted, and authorized by MAIN.  
**Status:** APPROVED

## D004 — Read-only source and unrelated files

**Decision:** Original datasets and unrelated user files are read-only.  
**Status:** APPROVED

## D005 — Verifiable evidence

**Decision:** Workers must provide verifiable evidence of execution.  
**Status:** APPROVED

## D006 — Synthetic data planned for M1

**Decision:** M1 uses six synthetic CSV records from the student's local `synthetic_sensor.csv`.  
**Status:** PLANNED

## D007 — Final data target

**Decision:** The final data target is NASA C-MAPSS FD001.  
**Status:** PLANNED

## D008 — GitHub synchronization and review

**Decision:** GitHub synchronization is part of the governance workflow. Brain acceptance must rely on actual remote contents, not only local claims.  
**Status:** APPROVED

## D009 — M0 recovery synchronization success

**Decision:** The original M0 governance commit is present on GitHub main and all four governance files were remotely retrieved and verified against the local baseline.
**Status:** VERIFIED
**Authority:** STUDENT-MAIN Brain
**Work Item:** M1_GOVERNANCE_SYNC_001
**Evidence:** Repository https://github.com/chichaofuc/ntust-nasa-ai-lab; baseline commit 16b017d69fd0b60e538032bc2c6082af558e22f2; remote main ref and four remote file reads.

## D010 — M0 acceptance

**Decision:** M0_STATUS is ACCEPTED.
**Status:** ACCEPTED
**Authority:** STUDENT-MAIN Brain
**Work Item:** M1_GOVERNANCE_SYNC_001
**Evidence:** The MAIN decision supplied in M1_GOVERNANCE_SYNC_001 and verified M0 commit 16b017d69fd0b60e538032bc2c6082af558e22f2. No separate MAIN decision ID was supplied.

## D011 — M1 authorization

**Decision:** M1 is authorized only under M1_DATASET_PROFILE_001; Dataset Profile execution remains blocked until governance synchronization is pushed, remotely verified, and reviewed/dispatched by MAIN.
**Status:** AUTHORIZED_BUT_BLOCKED_PENDING_GOVERNANCE_SYNC
**Authority:** STUDENT-MAIN Brain
**Work Items:** M1_GOVERNANCE_SYNC_001; M1_DATASET_PROFILE_001
**Evidence:** The MAIN decision supplied in M1_GOVERNANCE_SYNC_001. Dataset Profile analysis has not been performed under this governance-sync Work Item.

## D012 — M2–M5 remain locked

**Decision:** M2–M5 remain LOCKED until their prerequisites are accepted and MAIN issues explicit authorization for the relevant Work Item.
**Status:** LOCKED
**Authority:** STUDENT-MAIN Brain
**Work Item:** M1_GOVERNANCE_SYNC_001
**Evidence:** The MAIN milestone controls supplied in M1_GOVERNANCE_SYNC_001.

## D013 — M1 Governance Sync status

**Decision:** M1_GOVERNANCE_SYNC_001 is PASS_WITH_NOTES; MAIN acceptance remains PENDING.
**Status:** PASS_WITH_NOTES / MAIN_ACCEPTANCE_PENDING
**Authority:** STUDENT-MAIN Brain
**Work Item:** M1_GOVERNANCE_STATUS_CLARIFICATION_001
**Evidence:** Verified baseline commit 7e95db3494567f96bb6546df8456d150c40551eb and this dispatched status-clarification Work Item. PASS_WITH_NOTES does not constitute MAIN acceptance.

## D014 — M1 Governance Status Clarification authorization

**Decision:** M1_GOVERNANCE_STATUS_CLARIFICATION_001 is AUTHORIZED and remains IN_PROGRESS_UNTIL_VERIFIED.
**Status:** AUTHORIZED
**Authority:** STUDENT-MAIN Brain
**Work Item:** M1_GOVERNANCE_STATUS_CLARIFICATION_001
**Evidence:** The authorization and execution status supplied in this Work Item.

## D015 — M1 Dataset Profile acceptance status

**Decision:** M1 Dataset Profile domain acceptance is NOT_ESTABLISHED and MAIN acceptance is NOT_ACCEPTED. No Dataset Profile execution is recorded by this Work Item.
**Status:** NOT_ESTABLISHED / NOT_ACCEPTED
**Authority:** STUDENT-MAIN Brain
**Work Item:** M1_DATASET_PROFILE_001
**Related Work Item:** M1_GOVERNANCE_STATUS_CLARIFICATION_001
**Evidence:** The required status supplied in M1_GOVERNANCE_STATUS_CLARIFICATION_001. No analysis evidence or acceptance artifact was supplied.

## D016 — M2–M5 remain locked

**Decision:** M2_STATUS is LOCKED; M2_RELEASE is NOT_AUTHORIZED; M3–M5 remain LOCKED.
**Status:** LOCKED
**Authority:** STUDENT-MAIN Brain
**Work Item:** M1_GOVERNANCE_STATUS_CLARIFICATION_001
**Evidence:** The explicit MAIN status in this dispatched Work Item.

## D017 — Record MAIN governance acceptance decisions

**Decision:** M0 Governance remains ACCEPTED. M1 Governance Sync is ACCEPTED_WITH_NOTES. M1 Governance Status Clarification is ACCEPTED_WITH_NOTES, with Research Review PASS_WITH_NOTES and MAIN acceptance ACCEPTED_WITH_NOTES. M1 Dataset Profile remains NOT_ACCEPTED; M1 Domain Acceptance remains NOT_ESTABLISHED. M2 FD001 Validation is LOCKED, M2_RELEASE is NOT_AUTHORIZED, and M3–M5 remain LOCKED.
**Status:** RECORDED
**Authority:** STUDENT-MAIN Brain
**Work Items:** M1_GOVERNANCE_ACCEPTANCE_SYNC_001; M1_GOVERNANCE_STATUS_CLARIFICATION_001; M1_DATASET_PROFILE_001
**Evidence:** Clarification commit 23be3089a26ea993ab4344de00aac8e759b9887f; Research Review PASS_WITH_NOTES and MAIN acceptance decision supplied in M1_GOVERNANCE_ACCEPTANCE_SYNC_001. M1_DATASET_PROFILE_001 is separately authorized but awaits its own Research Brain dispatch; no Dataset Profile completion is claimed.


## D018 — M1 Dataset Profile acceptance and domain acceptance

**Decision:** M1 Dataset Profile is ACCEPTED_WITH_NOTES and M1 Domain Acceptance is ESTABLISHED.  
**Status:** ACCEPTED_WITH_NOTES / ESTABLISHED  
**Authority:** STUDENT-MAIN Brain  
**Work Item:** M2_FD001_LOCAL_DATA_VALIDATION_001  
**Evidence:** Formal MAIN authorization and acceptance statement supplied on 2026-11-26. This decision supersedes the earlier pending/not-accepted status snapshots for current governance state; historical records remain preserved.

## D019 — M2 FD001 Local Data Validation authorization

**Decision:** M2_FD001_LOCAL_DATA_VALIDATION_001 is FORMALLY AUTHORIZED. Phase A local file/raw data validation is mandatory. Phase B Engine/Cycle/Sensor trend evidence and data quality is explicitly authorized only after Phase A passes. M2 MAIN Acceptance remains PENDING until independent Research Brain review and MAIN decision.  
**Status:** FORMALLY_AUTHORIZED / PHASE_A_PENDING / PHASE_B_LOCKED_PENDING_PHASE_A  
**Authority:** STUDENT-MAIN Brain  
**Work Item:** M2_FD001_LOCAL_DATA_VALIDATION_001  
**Evidence:** Complete formal MAIN work order issued on 2026-11-26. Inputs are limited to the Owner's existing local train_FD001.txt, test_FD001.txt, and RUL_FD001.txt. No data download/substitution, raw-source modification/commit, model training, website/API integration, or scope expansion is authorized.


## D020 — M2 FD001 Local Data Validation acceptance

**Decision:** M2_FD001_LOCAL_DATA_VALIDATION_001 is ACCEPTED_WITH_NOTES. Phase A and Phase B deliverables, the revised R1–R3 items, and the M2 Data Contract are accepted with notes based on the Research Brain final review and its reported GitHub remote readback.  
**Status:** ACCEPTED_WITH_NOTES / CLOSED  
**Authority:** STUDENT-MAIN Brain  
**Work Item:** M2_FD001_LOCAL_DATA_VALIDATION_001  
**Final reported commit:** 599330b39b9a484ec89115e21ea5977dd1d5be71  
**Evidence basis:** Research Brain final Return and independent review as reported to MAIN. This record does not claim a separate independent MAIN-side source-file verification.

## D021 — M3 FD001 Read-only API authorization

**Decision:** M3_FD001_READONLY_API_001 is FORMALLY AUTHORIZED. Web Brain may coordinate and prepare the bounded Worker dispatch command after governance synchronization and remote readback. Worker execution is not yet dispatched.  
**Status:** FORMALLY_AUTHORIZED / CREATED_NOT_DISPATCHED  
**Authority:** STUDENT-MAIN Brain  
**Related Work Item:** M2_FD001_LOCAL_DATA_VALIDATION_001  
**Scope:** Read-only API in the student's workspace using only the three M2-verified FD001 original files; required endpoints are /api/health, /api/catalog, /api/units, and /api/history. API responses must define success/error behavior, represent missing values as JSON null, and provide original source-file plus 1-based physical source-line provenance.  
**Data exclusion:** GEN-001 and all Ch12 synthetic CSV files are explicitly prohibited from API implementation, fixtures, tests, examples, and outputs.  
**Gate:** The Web Brain must read the latest AGENTS.md from GitHub main and verify synchronized governance before issuing the formal Worker command. M4–M5 remain LOCKED.
