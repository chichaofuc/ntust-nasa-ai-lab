# Active Work Item

**PROJECT:** NTUST NASA AI Lab  
**CURRENT_MILESTONE:** M0  
**ACTIVE_WORK_ITEM:** WO-M0-001  
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
