# Chat Reconciliation and Temporal Precedence

This document defines how old and new ChatGPT Project history is reconciled into Fleet without allowing stale context to overwrite current Git.

## Purpose

Chat history is disposable working context. Git is durable project memory and authoritative project truth.

Reconciliation may recover useful decisions, rationale, tests, constraints, historical evidence, or future ideas that Git failed to preserve. It must not treat every old statement as current.

## Precedence order

When reconciling a thread, use the following order unless direct evidence establishes a more precise chronology:

1. current accepted Git on the authoritative repository;
2. merged implementation and test/validation evidence;
3. accepted ADRs/requirements and dated Git decisions;
4. current issues/PRs that clearly supersede older state;
5. older Git history;
6. chat history and handoff material.

Chat can reveal a later decision that Git accidentally omitted, but the burden is to establish that it was genuinely later and accepted rather than merely discussed.

## Temporal rules

- A reconciliation commit dated today does **not** make an imported 2026-07 decision newer than a conflicting accepted 2026-08 Git decision.
- Preserve the original decision/evidence date where known.
- If the original date is unknown, label it unknown instead of using the reconciliation date as semantic precedence.
- A merged/tested implementation can supersede an older intended design even if no explicit prose decision was written.
- A newer draft or brainstorm does not automatically supersede an older accepted decision.
- Old repository names, branch names, component names, and installer rules do not regain current authority when copied forward.

## Required classification

Every recovered item that is not straightforwardly current should be classified as one of:

- **CURRENT** — confirmed by current Git authority;
- **DEFERRED** — accepted concept intentionally postponed;
- **FUTURE EVALUATION** — worth considering later but not accepted scope;
- **HISTORICAL** — useful provenance/rationale, not current direction;
- **REJECTED** — explicitly not part of current direction;
- **CANDIDATE** — potentially valuable but not yet reconciled;
- **UNRESOLVED** — conflict or chronology cannot be established safely.

Uncertain legacy material defaults away from CURRENT.

## Special risk: broad Mission Control/orchestrator history

Fleet's older history contains broader orchestration concepts than the current accepted roadmap. Do not promote broad project-management, scheduling, provider, interface, audit, or remote-control ideas into Fleet 1.0 merely because they were detailed or repeatedly discussed.

Promotion to current scope requires current Git evidence: an accepted Fleet/component decision, requirement, roadmap outcome, issue/PR with clear authority, or merged implementation consistent with current architecture.

## Reconciliation procedure

For each retiring chat thread:

1. read `PROJECT.md`, `CURRENT_STATE.md`, `DECISIONS.md`, `REPOSITORIES.md`, the relevant workstream, and owning component Git;
2. extract only durable facts/decisions/evidence/future evaluations from the thread;
3. compare each item against current Git and chronology;
4. discard duplicates and stale restatements;
5. update the narrowest authoritative Git location;
6. preserve original dates/provenance where useful;
7. place broad old ideas under `docs/evaluations/` or `docs/history/` unless promoted;
8. leave unclear conflicts UNRESOLVED;
9. update `CURRENT_STATE.md` only when current state actually changed;
10. do not bulk-import raw chat transcripts.

## Completion standard

A retiring thread is reconciled only when deleting it would not remove unique current project truth or uniquely valuable historical/future-evaluation material.

The goal is not to preserve conversation. The goal is to preserve authoritative project knowledge.