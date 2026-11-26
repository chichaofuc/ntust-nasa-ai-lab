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

## Current Active Work Item

**PROJECT:** NTUST NASA AI Lab
**CURRENT_MILESTONE:** M1_SYNTHETIC_DATASET_PROFILE
**ACTIVE_WORK_ITEM:** M1_DATASET_PROFILE_001
**WORK_ITEM_TYPE:** BOUNDED_WORK_ORDER
**TARGET:** Research Own Worker (Codex)
**STATUS:** AUTHORIZED_BUT_BLOCKED_PENDING_GOVERNANCE_SYNC

This Work Item is authorized for the M1 Dataset Profile only after governance synchronization and MAIN review/dispatch. No M1 analysis has been performed under M1_GOVERNANCE_SYNC_001.
