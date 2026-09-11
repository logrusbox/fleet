# Fleet Decisions

This file is the compact register of durable Fleet-level decisions. Consequential architecture belongs in ADRs under `docs/decisions/`; component-specific decisions belong in the owning component repository.

## Accepted Fleet-level decisions

| ID | Decision | Status / source |
|---|---|---|
| FLEET-D001 | Fleet is the product umbrella; CIC Station and Vincent are the current product components. | Accepted; ADR-0001 and current repository structure |
| FLEET-D002 | `logrusbox/fleet` owns cross-component roadmap, architecture, integration, governance, repository inventory, and project-memory truth without duplicating component implementation truth. | Accepted; ADR-0001 |
| FLEET-D003 | `main` is the only permanent branch; normal work uses short-lived branches and PRs with squash integration. | Accepted repository governance |
| FLEET-D004 | Git is durable development/project authority; CIC Station is the future authority for live operational orchestration state. | Accepted Fleet roadmap/component architecture |
| FLEET-D005 | Vincent must remain useful standalone and reach READY without CIC Station enrollment. | Accepted Fleet/Vincent product boundary |
| FLEET-D006 | Codex is the first agent runtime, behind a provider-neutral boundary rather than a permanent architectural dependency. | Accepted ADR-0003 / Vincent requirements |
| FLEET-D007 | CIC Station begins from an upstream-friendly Paperclip foundation, but Fleet-owned contracts remain authoritative and the foundation may be reconsidered if the end-to-end proof fails. | Accepted ADR-0002 |
| FLEET-D008 | Fleet uses modular replaceable contracts; modularity does not require microservices. | Accepted ADR-0003 |
| FLEET-D009 | Generic Fleet deployments must support self-hosted/private-network operation without requiring a Logrus Box rendezvous/registry/relay service. | Accepted Fleet roadmap |
| FLEET-D010 | Active planning uses GitHub issues/PRs/repository Markdown rather than GitHub Projects v2. | Accepted ADR-0001 / governance |
| FLEET-D011 | Old chat/history cannot promote scope by itself. Current Git and accepted implementation/testing evidence take precedence; unresolved chronology stays unresolved. | Accepted project-memory policy, 2026-09-11 |
| FLEET-D012 | Historical broad Mission Control/orchestrator concepts default to HISTORICAL, FUTURE EVALUATION, CANDIDATE, or UNRESOLVED unless current Git explicitly promotes them. | Accepted project-memory policy, 2026-09-11 |

## Consequential Fleet ADRs

- `ADR-0001` — dedicated Fleet repository and cross-component authority boundary.
- `ADR-0002` — upstream-friendly Paperclip foundation and upstream strategy.
- `ADR-0003` — modular, replaceable Fleet contracts.

Read the ADR files for rationale and consequences; this register does not replace them.

## Component decisions that Fleet relies on

Fleet depends on current component decisions for details including:

- Vincent installer/runtime identity, standalone READY, provider/runtime boundary, authorization, isolation, and physical validation;
- CIC Station operator security, worker identity/enrollment trust, protocol versioning/retry semantics, worker-state modeling, persistence, work/attempt/lease/result separation, and later lease clock semantics.

Those details remain authoritative only in `logrusbox/vincent` and `logrusbox/cic-station`.

## Decision chronology rule

Decision age is determined by the original accepted decision/evidence date, not by the date an old chat is later copied into Git. Reconciliation commits must preserve known original dates or explicitly label chronology as unknown.

A conflict with unclear temporal order must be recorded as `UNRESOLVED`; do not guess which historical statement was intended to win.