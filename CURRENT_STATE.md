# Fleet Current State

**Verified against current default branches:** 2026-09-11  
**Component status documents last updated:** 2026-08-31

This document is the concise cross-component state needed for project re-entry. Component-specific implementation detail remains authoritative in the owning repository.

## Repository topology

- `logrusbox/fleet` — active Fleet-wide coordination, architecture, integration, governance, roadmap, and durable project-memory spine.
- `logrusbox/vincent` — active Vincent worker implementation and component documentation.
- `logrusbox/cic-station` — active CIC Station control-plane implementation repository and component documentation.

The former Fleet umbrella name `vincent-program` has been retired. Historical repository names do not regain authority merely because an old chat, issue, or document references them.

## Fleet-wide architecture state

Accepted Fleet decisions currently establish:

- `logrusbox/fleet` as the dedicated cross-component authority;
- an upstream-friendly Paperclip fork as the initial CIC Station application foundation, subject to the end-to-end foundation gate;
- Fleet-owned modular, replaceable contracts across control-plane, worker, agent runtime, transport, persistence, scheduling, source, policy, and interface boundaries;
- a modular-monolith default rather than premature microservice decomposition;
- Git as durable development/project authority and CIC Station as the future live operational orchestration authority.

The first foundation proof remains:

```text
ChatGPT -> Fleet MCP -> Paperclip-derived CIC task -> Vincent -> Codex -> durable result returned to CIC
```

## Vincent state

Vincent has an implemented installer/runtime codebase and is ahead of CIC Station in executable maturity.

Current accepted state from `logrusbox/vincent` includes:

- `main` as the canonical integration branch;
- Vincent `0.1.0` with independent Vincent/installer build identity;
- build-0023 candidate work consolidated through the August 31 QA cleanup;
- interactive installer storage/network controls, installer-media exclusion, offline Debian dependency closure, resumable first boot, rootless Podman runtime boundaries, network diagnostics/recovery, Codex companion-runtime layout, status/diagnostic surfaces, and worker state under `/var/lib/vincent`;
- provider-neutral runtime and managed-authorization work still required before 1.0;
- physical installer/runtime validation of build 0023 still pending.

Immediate Vincent gates remain:

1. prove exact-`main` build-0023 ISO and physical installer/runtime behavior;
2. complete offline-first payload and standalone READY behavior;
3. close pre-1.0 provider-boundary, authorization, execution-bounding, and credential-isolation blockers;
4. execute carried-forward laptop/workstation physical regression tests.

The large workstation is intended to remain the first useful persistent Vincent worker. The old laptop is the expendable installer/recovery target. That is temporary lab strategy, not product architecture.

## CIC Station state

CIC Station currently contains the canonical component model, requirements, architecture, security/protocol decisions, roadmaps, validation scaffolding, and issue backlog, but no implemented service/API/database/web UI yet.

Current accepted state includes:

- `logrusbox/cic-station` as the canonical public pre-release control-plane repository;
- version `0.1.0` build `0001`;
- a worker-state model that separates scheduling/availability, liveness/health, execution, and power facts;
- persistent CIC service/API/database authority required before multi-worker lease coordination;
- asymmetric worker-generated installation identity with operator-approved binding, proof-of-possession, replay-resistant bootstrap, rotation/revocation/recovery, and fail-closed server trust as the trust baseline;
- independently versioned worker protocol compatibility, idempotent retry semantics, and stale/conflicting transition rejection;
- CIC issue #25 as the pre-schema domain-model gate separating durable work items, assignments/selections, attempts, leases, and results.

Immediate CIC Station gates remain:

1. align Vincent with the accepted worker trust/protocol contract;
2. resolve CIC Station issue #25 before schema hardening;
3. implement the minimum persistent 0.1.0 service/API/database foundation;
4. prove the first managed Vincent worker through the Fleet M3 integration issue;
5. defer multi-worker lease coordination until that single-worker foundation is proven.

## Cross-component active gates

The current cross-component backlog in `logrusbox/fleet` includes:

- issue #2 — M3 first managed Vincent worker proof;
- issue #3 — native component release milestones requiring GitHub UI work;
- issue #1 — shared repository-governance enforcement; its historical `vincent-program` terminology should be treated as stale wording, not current authority.

The Fleet roadmap remains M0-M8. M0 governance/documentation establishment is complete; M1 physical Vincent proof is in progress; later milestones remain planned.

## Current blockers

- Vincent build-0023 physical acceptance has not completed.
- The persistent bounded-work Vincent proof has not completed.
- CIC Station issue #25 remains a pre-schema blocker.
- CIC Station application implementation has not begun.
- First managed-worker integration has not been proven.
- Lease clock/skew/restart semantics remain a later multi-worker design requirement.
- GitHub ruleset/merge-method/milestone settings still contain UI-only work that the connected automation cannot fully enforce.

## Next project sequence

1. Complete Vincent physical and bounded-work proof.
2. Finish required Vincent managed-worker trust/protocol/runtime boundaries.
3. Resolve CIC domain modeling and implement minimum persistent control-plane foundation.
4. Complete Fleet M3 first managed-worker proof.
5. Proceed to multi-worker lease/liveness/recovery proof.
6. Continue through the remaining Fleet roadmap only with evidence-backed promotion of scope.

## Re-entry rule

Before acting on old chat or handoff material, reconcile it against current Git using `docs/history/CHAT_RECONCILIATION.md`. A recently copied old idea is not a recent decision.