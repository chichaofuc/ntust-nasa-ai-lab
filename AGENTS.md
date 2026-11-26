# NTUST NASA AI Lab — Agent Governance

## Project identity

**Project:** NTUST NASA AI Lab  
**Goal:** Build a local NASA C-MAPSS FD001 Engine Health Analysis application. The planned application supports engine unit, cycle, and sensor selection; sensor trend visualization; source-data traceability; sensor statistics; evidence generation; and evidence-prompt generation.

## Authority hierarchy

1. **STUDENT / OWNER** — final authority; approves scope changes, destructive actions, milestone transitions, and external publication when required.
2. **STUDENT-MAIN Brain** — project manager; controls the roadmap and milestones, creates bounded Work Items and acceptance criteria, reviews evidence, accepts or rejects deliverables, and authorizes subsequent work.
3. **Specialized Brains** — RESEARCH Brain, DEV Brain, and QA Brain.
4. **Own Workers** — Codex, Claude, and other execution agents explicitly authorized for the active Work Item.

## Read-only boundaries

Treat original source datasets (including NASA C-MAPSS and synthetic CSV files), existing research evidence, existing project documents not assigned for modification, and user-created code outside the task scope as read-only unless an active Work Item explicitly authorizes changes. Never delete or modify source datasets, overwrite unrelated project files, perform destructive cleanup, change project scope without approval, commit secrets or credentials, execute unrelated tasks, or start a future milestone without authorization.

## Work Item governance

Every task must specify `WORK_ITEM_ID`, `TYPE`, `TARGET BRAIN / WORKER`, `CURRENT MILESTONE`, `INPUT`, `OBJECTIVE`, `EXPECTED OUTPUT`, `ACCEPTANCE CRITERIA`, `STOP_IF`, and `RETURN_TO`. Workers may execute only the scope explicitly defined by their active Work Item.

## Stop rule

Stop immediately if required input is missing, files cannot be accessed, data format differs from the expected schema, scope expansion is required, existing files may be overwritten, destructive action is required, acceptance criteria cannot be met, GitHub access is unavailable, a push fails, evidence cannot be verified, or governance instructions conflict. A stop report must contain:

```text
STOP_EVENT
WORK_ITEM_ID
CURRENT_MILESTONE
TRIGGER
OBSERVED_EVIDENCE
IMPACT
PROPOSED_ACTION
WAITING_FOR
```

## Milestone control

No Worker may start the next milestone until the previous Work Item is complete, required evidence is returned, Brain review is complete, acceptance is explicitly recorded, and MAIN authorization is issued.

## Git governance

- Use one branch, `main`, and develop sequentially. Do not run unauthorized parallel milestone work.
- Before every new dispatch, the Brain must read the latest `AGENTS.md` from GitHub `main` and instruct the Worker to follow that version. Workers must not rely only on local or cached governance when GitHub `main` is accessible.
- After authorized work, review changes and Git status, verify no unauthorized files are included, commit, push to GitHub `main`, and return the commit SHA, GitHub URLs, and evidence of pushed contents.
- The Brain must read and review the actual pushed files from GitHub before declaring PASS. If remote verification cannot be completed, status is `BLOCKED`; a local commit alone is not acceptance.

## Security

Never expose or commit secrets, tokens, or private keys. Never embed credentials in remote URLs. Prefer authenticated GitHub CLI or secure credential mechanisms, use minimum required permissions, and report authentication failures without attempting to bypass security restrictions.

## Current milestone boundary

- **M0 — ACCEPTED** by STUDENT-MAIN Brain. The M0 recovery and acceptance record is documented in M1_GOVERNANCE_SYNC_001.
- **M1 — AUTHORIZED, PENDING GOVERNANCE SYNCHRONIZATION AND MAIN REVIEW.** The active Work Item is M1_DATASET_PROFILE_001. Dataset Profile execution may begin only after this governance synchronization is pushed and verified and MAIN reviews and dispatches that Work Item. Follow its scope exactly.
- **M2–M5 — LOCKED.** Do not begin these milestones until their prerequisites are accepted and MAIN issues explicit authorization.

This authorization covers only M1 Dataset Profile under M1_DATASET_PROFILE_001 after the stated gate. It does not authorize M2 or later milestones, website work, unrelated analysis, or scope expansion. Source datasets remain read-only and must not be modified.
