# Codex Orchestra Legacy Project Reconciliation

Status: complete historical reconciliation record  
Reconciliation date: 2026-09-11  
Authority: current `logrusbox/fleet`, `logrusbox/vincent`, and `logrusbox/cic-station` Git outrank this record.

## Purpose

This file records durable knowledge recovered from the older ChatGPT Project variously called Codex Orchestra, Codex Orchestrator, and Mission Control. It is a coverage/provenance ledger, not a restored architecture specification.

Legacy material is classified using `docs/history/CHAT_RECONCILIATION.md`. Nothing becomes current merely because it appears here.

## Conversation coverage

The Codex Orchestra legacy ChatGPT Project contains 10 conversations. All 10 were identified and evaluated during this reconciliation:

| Approx. date | Conversation | Primary material | Outcome | Git preservation | Retirement |
|---|---|---|---|---|---|
| 2026-07-31 | Codex Integration with ChatGPT | Linux-first open-source orchestration; ChatGPT directing Codex workers through a coordinator | **HISTORICAL / CURRENT rationale** | Current Fleet Git already preserves provider/runtime separation and CIC-mediated control | safe |
| 2026-07-31 | Mission Control Proposal | reusable orchestration system; Git as source of truth; human-controlled coordination | **HISTORICAL / CURRENT rationale** | Current `PROJECT.md`, `AGENTS.md`, roadmap and ADRs already preserve accepted principles | safe |
| 2026-07-31 | Mission Control Architecture | Project DNA; restoring project intent rather than only code/environment | **HISTORICAL / CURRENT rationale** | Current Fleet project-memory spine preserves Git-as-durable-memory principle; Project DNA survives conceptually in durable product/project docs | safe |
| 2026-08-03 | Codex Token Usage | single coordinator watching Git and triggering designated workers; ChatGPT chooses worker rather than coordinator deciding autonomously | **HISTORICAL / FUTURE EVALUATION** | Current architecture preserves CIC as control plane and explicit scheduling contracts; exact historical Git-watcher mechanism is not current | safe |
| 2026-08-22 | ChatGPT On Phone | extensive Codex-worker platform requirements and handoff/specification generation | **HISTORICAL** | Durable worker/platform concepts were subsequently migrated into Vincent/Fleet documentation and implementation | safe |
| 2026-08-24 | Full project roadmap | public Vincent/private Mission Control split; migration from legacy repositories; ISO workstream | **HISTORICAL / CURRENT lineage** | Current repository authority is Fleet/Vincent/CIC Station; legacy split and migration are provenance only | safe |
| 2026-08-25 | Fictional Robot Names | Vincent naming; creation of Vincent and Mission Control repositories; repository-role split | **HISTORICAL** | Current names and repository authority are independently established in Git | safe |
| 2026-08-25 | Migration Verification Report | migration acceptance gate; exact accepted Vincent migration commit; test/history preservation | **HISTORICAL evidence** | Current Vincent Git is authoritative; accepted migration evidence explains lineage but does not override newer implementation | safe |
| 2026-08-25 | ISO work blocked | exact-commit gate before ISO testing; build validation, secret scan, destructive-media identification and authorization | **HISTORICAL / CURRENT safety rationale** | Current Vincent installer validation and operator-gate requirements supersede exact old build instructions | safe |
| 2026-08-25 | Roadmap storage status | requirement that roadmap and handoff live in Git before chat Project deletion; consolidation then resume ISO testing | **CURRENT project-memory rationale** | Current Fleet Git project-memory spine directly implements this principle | safe |

Additional recoverable legacy details appeared in summarized Project context associated with these conversations, including Mission Control roadmap/architecture discussion, legacy repository-history migration, and Vincent ISO build/testing material. Those details were evaluated for durable concepts below rather than preserved as separate conversations.

## Durable knowledge recovered

### CURRENT — confirmed independently by current Git

The legacy Project contains early rationale for several principles now established by current Fleet Git:

- Git is durable development/project authority; chat is disposable context.
- Fleet separates the control plane from managed workers.
- Vincent is the worker platform, not the control plane.
- Codex is an agent runtime and must not become permanent architecture.
- workers must be replaceable/recoverable rather than owning unique project truth;
- managed worker authority must be explicit, scoped, revocable, and distinct from human/Git/provider credentials;
- physical/destructive installer actions retain explicit operator safety gates;
- human judgment remains in control of consequential coordination decisions.

These are not imported from chat as new decisions; current Git already establishes them.

### HISTORICAL — useful provenance

The architecture evolved through several names and repository arrangements before current Fleet authority:

1. broad **Mission Control / Codex Orchestra** concepts described a reusable Linux-first AI-assisted software-development coordinator;
2. **GitBoy** and **codex-worker-platform** were predecessor worker/orchestration identities used during experimentation;
3. the worker platform was renamed **Vincent** and split from a private **Mission Control** control-plane repository;
4. Mission Control was renamed **CIC Station**;
5. **Fleet** became the product umbrella and `logrusbox/fleet` the cross-component authority;
6. current component authority settled on `logrusbox/vincent` and `logrusbox/cic-station`.

Old repository names and branches are provenance only. Current `REPOSITORIES.md` determines present authority.

### HISTORICAL — installer and migration lessons

Legacy Vincent/worker work established several costly lessons that should not be rediscovered casually:

- ISO work must use an exact accepted source state rather than an arbitrary staging checkout or stale branch.
- build/test evidence should be captured explicitly, including final exit status, payload/manifest verification, secret scanning, and obsolete-name scanning.
- destructive flashing requires identifying the exact removable target and obtaining authorization for that target.
- installer/first-boot behavior must be physically proven on real hardware; generated ISO success alone is insufficient.
- networking and DNS failures on test laptops can masquerade as installer/runtime failures and require explicit diagnostic separation.
- worker identity must not be baked into reusable installer media.
- cold shutdown/reboot/network interruption must be treated as normal recovery scenarios, not exceptional laboratory conditions.

Current Vincent requirements and tests govern the exact implementation; these bullets preserve only the historical lesson.

## FUTURE EVALUATION — legacy ideas not promoted to Fleet 1.0

The old Project explored broader capabilities than current Fleet 1.0. The following remain potentially useful but are not current requirements unless separately promoted by current Git:

- generalized project-state and roadmap management inside the control plane;
- coordinator-managed activation/deactivation and capacity allocation across many projects;
- richer provider/agent routing beyond the current replaceable-runtime contract;
- automated restoration of an entire multi-project development environment from durable manifests;
- phone-first/native control surfaces;
- generalized scheduling/maintenance windows;
- broad audit/history UX beyond current operational provenance requirements;
- remote terminal/desktop control;
- a generalized `fleet recover` / control-plane reconstruction workflow beyond currently accepted recovery milestones.

Each requires a fresh evaluation against current Fleet architecture before promotion.

## REJECTED or superseded directions

The following legacy patterns must not be restored as current architecture:

- Git as the live lease, heartbeat, enrollment-session, or execution-state database;
- a worker owning unique project authority or irreplaceable orchestration state;
- mandatory provider-specific architecture centered permanently on Codex;
- broad Mission Control functionality being treated as Fleet 1.0 merely because it was previously detailed;
- old repository/branch names regaining authority;
- superseded Vincent installer instructions overriding current Vincent requirements or physical-test gates;
- arbitrary remote-shell capability as a Fleet 1.0 requirement.

## UNRESOLVED

No legacy statement reviewed here establishes a later accepted decision that conflicts with current Git. No conversation-coverage gap remains: the owner confirmed that the Project contains exactly the 10 conversations listed above.

## Completion assessment

All 10 conversations in the Codex Orchestra legacy ChatGPT Project have been reconciled. Deleting the Project would not remove unique current truth or uniquely valuable historical/future-evaluation material: current principles are represented in authoritative Git, and useful provenance, failure lessons, and future possibilities are preserved here without restoring obsolete architecture.

**The Codex Orchestra legacy ChatGPT Project is safe to retire and delete.**