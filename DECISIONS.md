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
