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

The active authorization is limited to M0 governance initialization. Do not begin M1 or later milestones, analyze `synthetic_sensor.csv`, implement the website, install unrelated dependencies, or modify source data unless a new Work Item explicitly authorizes that work.
