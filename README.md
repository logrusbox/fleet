# Fleet

`logrusbox/fleet` is the cross-component project authority and durable project-memory spine for **Fleet**, a Logrus Box product for coordinating AI work across managed computers.

Fleet currently consists of:

- [`logrusbox/vincent`](https://github.com/logrusbox/vincent) — **Vincent**, the managed worker platform.
- [`logrusbox/cic-station`](https://github.com/logrusbox/cic-station) — **CIC Station**, the Command Information Center and central control plane.

Codex is the first supported agent runtime used through Vincent. It is not a third Fleet product component.

## Start here

For project re-entry or consequential Fleet-wide work, read in this order:

1. [`PROJECT.md`](PROJECT.md) — current product truth, scope, architecture, authority boundaries, and non-goals.
2. [`CURRENT_STATE.md`](CURRENT_STATE.md) — concise current cross-component implementation/gate status.
3. [`DECISIONS.md`](DECISIONS.md) — compact durable Fleet decision register and ADR index.
4. [`REPOSITORIES.md`](REPOSITORIES.md) — current/superseded repository classification and authority.
5. [`docs/PROGRAM_ROADMAP.md`](docs/PROGRAM_ROADMAP.md) — canonical Fleet M0-M8 cross-component roadmap.
6. the relevant file under [`workstreams/`](workstreams/) and Fleet ADR/interface documentation.
7. the owning component repository's current docs/source/tests/issues/PRs.

Do not reconstruct Fleet from chat history when Git can answer the question. Old chats are reconciled under [`docs/history/CHAT_RECONCILIATION.md`](docs/history/CHAT_RECONCILIATION.md).

## This repository owns

- Fleet definition and 1.0 cross-component scope;
- cross-component architecture and authority boundaries;
- the canonical Fleet roadmap and current Fleet state;
- repository inventory and historical/superseded repository classification;
- Fleet-level ADRs/decisions and integration outcomes;
- cross-component contracts/interfaces at the level needed to keep components coherent;
- current workstream summaries and scoped handoffs;
- durable project-memory and chat-reconciliation rules;
- Fleet-wide governance.

## This repository does not own

Component-specific implementation work remains in the repository that implements it. Do not duplicate Vincent or CIC Station requirements, source, detailed architecture, installer/runtime behavior, database/schema internals, bugs, release notes, or component roadmaps here merely for visibility.

If a work item can be completed entirely in one component repository, it belongs there. Cross-component issues should link authoritative component issues and pull requests rather than copy them.

This repository also does not contain live fleet operational data, worker secrets, production configuration, or task/lease/heartbeat state.

## Planning model

GitHub issues are the active planning/work anchors. Pull requests are implementation/review evidence. Component release targets remain component-owned. Fleet milestones M0-M8 are integration outcomes rather than software versions.

GitHub Projects v2 is intentionally not required because it would create a parallel manual planning surface that the current automation cannot maintain directly.

## Historical scope rule

Detailed old Mission Control/generalized orchestrator ideas are not current Fleet scope merely because they were previously designed. Preserve useful material under `docs/evaluations/` or `docs/history/` unless current Git explicitly promotes it.