# ADR-0002: Use an upstream-friendly Paperclip fork as Fleet's initial application foundation

- **Status:** Accepted
- **Date:** 2026-08-29
- **Scope:** Fleet, CIC Station, and the Vincent/CIC integration boundary

## Context

Fleet needs more than remote command execution. ChatGPT must be able to create and resume projects, preserve context and instructions, create and delegate work, monitor execution, approve actions, and retrieve durable results from managed Vincent workers.

Paperclip already provides much of that application layer: projects, goals, tasks, delegation, approvals, budgets, activity history, multiple agent adapters, and an experimental remote runner protocol. Harness has a stronger directly relevant runtime-host and job-lease model. Herd has useful remote-machine, session, approval, and Codex-control infrastructure.

Building CIC Station independently would duplicate substantial working application functionality. Building from Harness plus Herd would require integrating two products before Fleet acquires the higher-level project and task experience already present in Paperclip.

## Decision

Fleet will begin with an upstream-friendly fork of [Paperclip](https://github.com/paperclipai/paperclip) as the initial CIC Station application foundation.

The implementation strategy is:

1. Keep the fork close enough to upstream Paperclip to receive and evaluate upstream changes.
2. Contribute generally useful fixes and features upstream when they are acceptable to Paperclip maintainers.
3. Keep Fleet-specific behavior modular where practical so it does not require unnecessary divergence.
4. Preserve Vincent as Fleet's independently controlled worker distribution, machine-management, enrollment, and recovery layer.
5. Use Harness as the primary reference or selective donor for capability matching, renewable leases, lease generations, draining, loss-of-lease behavior, and stale-result fencing.
6. Use Herd as a selective donor for remote-machine connections, live agent sessions, approvals, and Codex control when Paperclip's runner is insufficient.
7. Add other dependencies or borrowed subsystems only for demonstrated requirements and only after exact-version license and provenance review.

The first foundation gate is one complete proof:

```text
ChatGPT -> Fleet MCP -> Paperclip-derived CIC task -> Vincent -> Codex -> durable result returned to CIC
```

This decision selects the initial direction, not an irreversible permanent base. If the proof demonstrates that Paperclip's company-oriented domain model or runner architecture creates more cost than retained value, Fleet will reconsider the foundation before deep divergence.

## Fleet-specific boundary

The following remain Fleet-owned unless an upstream project independently adopts compatible abstractions:

- Vincent installation image and worker appliance;
- CIC-generated enrollment and Vincent-initiated identity binding;
- physical worker inventory, health, network policy, and power management;
- same-subnet and disconnected/private-network enrollment;
- CIC proxy and managed operational configuration;
- ChatGPT-facing Fleet MCP tools;
- Fleet's authoritative job-attempt, lease, reassignment, and result-acceptance rules;
- Fleet branding and its simplified personal-fleet operating model.

## Upstream contribution policy

Prefer upstream contributions for generally useful behavior such as runner reliability, reconnect/replay, lease safety, capability advertisement, provider-neutral adapters, Codex app-server integration, security fixes, tests, and documentation.

Do not make Fleet's required behavior dependent on upstream acceptance or scheduling. When an upstream contribution is rejected or incompatible with Fleet's requirements, retain a clearly documented Fleet implementation.

## Legal and provenance requirements

Paperclip and Harness were observed under MIT licenses; Herd was observed under AGPL-3.0-only. Every reuse decision must be verified at the exact source commit, preserve required copyright/license notices, record modified files and provenance, and confirm compatibility with the destination component's release license.

## Consequences

- Fleet gains a mature project/task/governance layer and a plausible remote-runner starting point.
- CIC Station becomes a distribution or maintained fork rather than a greenfield application unless the foundation gate fails.
- Upstream synchronization and divergence management become ongoing engineering responsibilities.
- Vincent remains a distinct Fleet component rather than being replaced by Paperclip's runner.
- Harness and Herd are no longer competing primary foundations for the first spike; they remain important donors and fallback evidence.
