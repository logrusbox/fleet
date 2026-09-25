# Fleet Current State

**Verified against current default branches:** 2026-09-25
**Rescan:** current default branches, open issues/PRs, and Actions results checked on 2026-09-25; no open PRs at rescan start.

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

Accepted September 25 implementation includes:

- verified embedded source and offline Python installation; safe resume preserves altered source;
- standalone local READY independent of internet, provider setup and CIC enrollment;
- explicit enrollment export from the persistent local asymmetric identity;
- strict task priority/UTC timestamp validation and deterministic ordering;
- provider-neutral execution results, explicit deadlines, cancellation and process-group cleanup;
- durable publication journaling and conservative commit/push recovery;
- exact repository authorization before preparation, execution and publication, with revocation/expiry checks;
- reviewed local provider artifacts with expected checksums and atomic runtime activation;
- independent runtime and installer version/build reporting; optional connectivity/provider observations separated from local diagnostic health.

Vincent runtime is `0.1.0` build `0030`; installer is `0.1.0` build `0027`.
170 automated tests and package/repository checks pass. The wheel was inspected
for the canonical runtime identity. Recent main ISO construction/inspection is
green; physical boot, storage, networking and useful bounded-work acceptance remain
unproven. See Vincent `docs/STATUS.md` for current exact Actions evidence.

Remaining execution gates: task/provider credential isolation (#48), full provider
lifecycle abstraction (#38), authenticated CIC enrollment/protocol (#35/#36), and
live managed-grant integration (#39). Local protected grant files are not the
complete CIC trust protocol. Process-group cleanup is not a malicious-process
security sandbox.

The large workstation remains the first persistent worker target. The old laptop
remains the expendable installer/recovery target. Neither has been accessed or
reimaged in this work.

## CIC Station state

CIC Station `0.1.0` build `0003` now has:

- ADR-0021 and a canonical work/selection/attempt/lease/result model, resolving #25;
- seven domain contract tests covering retries, fenced late results, idempotency,
  conflicting replays and ownership;
- a pinned Paperclip source commit with preserved license notice and verified
  package/lockfile hashes;
- reproducible source preparation with three real Git preservation/hash tests;
- successful frozen dependency installation, database migration static checks and
  database TypeScript compilation against the pinned foundation.

The pure reducer is not an operational database or authenticated service. No CIC
web UI, API, deployed database, Fleet MCP or real managed-worker execution is
claimed. A disposable PostgreSQL workflow is the next foundation evidence check;
local database execution was blocked by the root-only execution environment.

The asymmetric worker-trust and independently versioned retry-safe protocol
requirements remain in force. Operational authority must be transactional and
persistent before multi-worker coordination. Lease clock/skew/restart policy
remains #18 and does not follow automatically from upstream controller leases.

## Cross-component active gates

The current cross-component backlog in `logrusbox/fleet` includes:

- issue #1 — shared repository-governance enforcement;
- issue #2 — M3 first managed Vincent worker proof;
- issue #3 — native component release milestones requiring GitHub UI work;
- issue #15 — deferred evaluation of an optional organization Project; repository issues remain authoritative and Project setup retains its explicit owner gate.

The Fleet roadmap remains M0-M8. M0 governance/documentation establishment is complete; M1 physical Vincent proof is in progress; later milestones remain planned.

## Current blockers and next sequence

1. Complete physical Vincent acceptance on the authorized laptop and useful bounded
   work on the persistent workstation. No physical success is inferred from CI.
2. Select and prove task/provider isolation from worker identity and unrelated
   credentials before enabling unattended production execution.
3. Integrate the tested CIC domain with Paperclip persistence, scoped operator
   authorization and authenticated Vincent protocol.
4. Supply the authorized worker/provider environment and prove Fleet #2 end to end.
5. Resolve lease clock/restart policy before multi-worker ownership implementation.
6. Apply repository rulesets and native milestones through the available owner
   administration interface; these settings are not exposed by the connected tools.

Ordinary changes are integrated through bounded PRs after green checks. No protected
release, credential expansion, deployment or destructive hardware action has been
performed. Fleet M0-M8 promotion remains evidence based.

## Re-entry rule

Before acting on old chat or handoff material, reconcile it against current Git using `docs/history/CHAT_RECONCILIATION.md`. A recently copied old idea is not a recent decision.