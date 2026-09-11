# Fleet Chat Reconciliation Ledger

Purpose: concise audit index for Project-wide ChatGPT history reconciliation. This file records which identifiable conversations have been checked against current Git and whether deletion is safe. It is not a transcript archive and does not create product authority.

Status meanings:

- **RECONCILED** — available conversation material was checked against current Git and any durable gap was preserved.
- **PARTIAL** — recognizable thread/context was available, but the platform did not expose the complete transcript to this reconciliation session; do not treat the thread as safe to delete solely from this entry.
- **UNAVAILABLE** — known thread exists but substantive content was not available enough to reconcile.

| Approx. date | Conversation / recognizable title | Major subjects | Status | Git action / preservation | Unresolved | Safe to retire? |
|---|---|---|---|---|---|---|
| 2026-08-25 | Fleet continuation after Vincent/Mission Control split (title not exposed) | Vincent worker/control-plane split; GitBoy/codex-worker-platform retirement; migration/history preservation | PARTIAL | Current Fleet/Vincent authority already preserves component split; Vincent Git contains migration commits. | Complete transcript/title not exposed. | No |
| 2026-08-26 | Vincent ISO Rebuild and Repository Continuation — Do the Work | ISO rebuild, installer acceptance, worker identity/enrollment, heartbeat/lease client, crash-safe state, cold shutdown | PARTIAL | Current Vincent requirements/status supersede implementation details; historical build evidence remains in Vincent Git/history. | Complete transcript not exposed. | No |
| 2026-08-26 | Mission Control repository/runtime discussions (title not exposed) | Private Git repository vs future runtime/service; Vincent↔control-plane relationship | PARTIAL | Current Fleet/CIC repository and authority boundaries supersede older repository model. | Exact thread boundaries/titles unavailable. | No |
| 2026-08-27 | CIC-station QA review and cleanup approval | CIC QA, obvious cleanup, owner approval gates | PARTIAL | Current CIC source/tests/issues/PRs are authoritative; no unique current Fleet-wide gap identified. | Full QA transcript not exposed. | No |
| 2026-08-27 | Vincent QA review and cleanup approval | Vincent QA, cleanup, authority gates | PARTIAL | Current Vincent source/tests/history/status are authoritative; no unique Fleet-wide gap identified. | Full QA transcript not exposed. | No |
| 2026-08-27 | Next Project Steps | branch consolidation, next execution sequence | PARTIAL | Superseded by current `main`-only governance and current roadmap/state. | Full transcript not exposed. | No |
| 2026-08-27 | Alpha Beta Versioning Scheme | prototype/pre-alpha/alpha/beta terminology | PARTIAL | Current component SemVer/build identities are authoritative; no durable Fleet-wide gap found. | Full transcript not exposed. | No |
| 2026-08-27 | Codex Device Sign In | provider device-code/interactive authorization; provider account/profile assignment | PARTIAL | Preserved in Vincent requirements VIN-REQ-0046..0050 and CIC requirements MC-REQ-0037..0042. | Full transcript not exposed. | No |
| 2026-08-27 | Worker Power Management | low-power idle/wake while remaining dispatchable | RECONCILED | Preserved as FUTURE EVALUATION in `docs/evaluations/POST_1_0_FEATURE_EVALUATIONS.md`; abrupt-power recovery remains current Vincent requirement. | Promotion into current requirement requires a new decision/use case. | Yes for recovered durable content; transcript access caveat remains |
| 2026-08-27 | Sci Fi Command Center Names | Mission Control→CIC Station rename; branch consolidation; CIC meaning | PARTIAL | Current naming preserved: Fleet umbrella, CIC Station control plane, Vincent worker; `Command Information Center` in README/PROJECT lineage. | Full transcript not exposed. | No |
| 2026-08-27 | Mission Control fleet-control planning (title not exposed) | assignments, status, audit, web/API direction | PARTIAL | Current CIC requirements preserve bounded assignments, audit, browser UI/API, persistence. | Exact thread/title and full transcript unavailable. | No |
| 2026-08-28 | Evaluate the roadmap/known issues/ADR/future requests (title shown as New chat) | architecture re-evaluation; whether design still matches goal | PARTIAL | Current Fleet spine, ADRs, roadmap, component requirements, issues supersede old planning state. | Full transcript not exposed. | No |
| 2026-08-28 | Brainstorm Vincent Enrollment | NAT, LAN-only enrollment, human-readable handshake, CIC proxy/managed network config | RECONCILED | Current FLEET-D009 and ADR-0002 preserve private/LAN enrollment and no vendor rendezvous dependency; deferred CIC-proxy/cache concepts preserved in post-1.0 evaluation. | Detailed future proxy design intentionally deferred. | Yes for recovered durable content; transcript access caveat remains |
| 2026-08-28 | Plan GitHub Project Structure | Logrus Box organization; repo ownership/namespace; application access | PARTIAL | Current repositories under `logrusbox` and Fleet repository inventory establish present authority. | Full transcript not exposed; company/legal identity outside Fleet technical authority. | No |
| 2026-08-28 | Plan Local CIC Station Development | local CIC development with Codex worker; no changes yet | PARTIAL | Current roadmap/state preserves local-before-deployment implementation sequencing where still applicable; CIC implementation remains unstarted. | Full transcript not exposed. | No |
| 2026-08-28 | Choose Herd Or Vincent | build-vs-adopt analysis; Herd license; Fleet naming; CIC expansion | RECONCILED | ADR-0002 records Paperclip foundation with Harness/Herd donors; DECISIONS preserves Fleet/CIC/Vincent boundary and modularity. | Earlier temporary Herd-first recommendation was superseded by Paperclip decision dated 2026-08-29. | Yes for recovered durable content; transcript access caveat remains |
| 2026-08-28 | Similar Products Comparison | central remote AI-worker management; Herd/OpenHands and alternatives; free/self-hosted fit | PARTIAL | ADR-0002/0003 preserve selected foundation/donor conclusions. | Per-product comparison details not fully available; only durable selected conclusions recovered. | No |
| 2026-08-28 | Evaluate Scientific Agent Skills | Scientific Agent Skills, K-Dense BYOK/KADY, OpenHands Agent Canvas and possible donors | UNAVAILABLE | No promotion made. Current architecture allows selective donors behind Fleet-owned contracts. | Substantive per-project findings were not exposed by available history retrieval. | No |
| 2026-08-28 | Review Herd Fork Options | Paperclip vs Harness/Herd, borrowing code, contribute-vs-fork, modular design | RECONCILED | ADR-0002 selects upstream-friendly Paperclip fork, Harness/Herd selective donors; ADR-0003 records modular replaceable contracts. | Exact product-version provenance still must be checked at reuse time. | Yes for recovered durable content; transcript access caveat remains |
| 2026-08-28 | Fleet VPS Requirements | expected personal deployment size; one CIC VPS; website/static hosting considerations | PARTIAL | ADR-0003 preserves smallest-practical deployment topology and one-VPS viability; no fixed infrastructure count promoted. | Full transcript not exposed. | No |
| 2026-08-31 | Project Status Update | overall Fleet status | PARTIAL | Superseded by `CURRENT_STATE.md` verified 2026-09-11 and current component status/issues. | Full transcript not exposed. | No |
| 2026-09-03 | Assessing PAIR Impact | NVIDIA PAIR/personal AI router impact on Fleet value proposition | UNAVAILABLE | No Git change; external product does not alter current authority without a deliberate decision. | Substantive thread content was not exposed in this session. | No |
| 2026-09-11 | Fleet Project — Full Conversation History Reconciliation | Project-wide durable-memory audit | ACTIVE | Created this ledger and restored the 2026-08-28 deferred feature inventory to Git on reconciliation branch. | Continue until all Project conversations are fully exposed/reconciled or explicitly recorded unavailable. | No |

## Current reconciliation findings

Already preserved correctly in current Git:

- Fleet / CIC Station / Vincent product boundary and naming;
- Git versus CIC operational-authority boundary;
- Paperclip foundation with Harness/Herd as selective donors;
- modular replaceable contracts without mandatory microservices;
- provider-neutral runtime boundary with Codex first;
- explicit/revocable worker enrollment, asymmetric worker identity, protocol compatibility, leases, stale-result fencing, and conservative reassignment;
- Vincent standalone READY and provider-local interactive/device authorization;
- private/LAN/self-hosted operation without a Logrus Box rendezvous dependency;
- current installer/runtime, validation, and recovery authority in Vincent;
- current CIC domain requirements and pre-schema gate in CIC Station.

Recovered gap preserved during this audit:

- the 2026-08-28 post-1.0 idea inventory, including low-power/wake behavior, richer scheduling, branch/worktree automation, richer review/audit/UI features, and NAT/LAN/CIC-proxy infrastructure concepts, now lives under `docs/evaluations/POST_1_0_FEATURE_EVALUATIONS.md` as non-current future evaluation material.

## Access limitation

This reconciliation session can see Project-provided conversation summaries/context and can retrieve some older conversational facts, but it does not have a direct API that enumerates and opens every ChatGPT Project thread as a complete transcript. Therefore rows marked PARTIAL or UNAVAILABLE are intentionally not declared safe to retire. The Fleet ChatGPT Project as a whole must not be declared fully reconciled while those rows remain.
