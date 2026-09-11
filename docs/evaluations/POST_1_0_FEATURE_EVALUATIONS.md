# Fleet Post-1.0 Feature Evaluations

**Original record date:** 2026-08-28  
**Classification:** FUTURE EVALUATION / DEFERRED — not Fleet 1.0 requirements

This inventory preserves useful broader Fleet ideas discussed before the current 1.0 boundary was narrowed. It does not promote them into current scope. Promotion requires a separate current decision, requirement, roadmap change, or implementation-backed decision.

## Fleet 1.0 boundary at the time

The minimum product concept was:

- CIC Station exposes workers and control operations to ChatGPT.
- Vincent enrolls with CIC Station and reports worker/runtime availability.
- ChatGPT can address a named worker or publish work an eligible worker may claim.
- A worker obtains a lease before executing assigned or claimable work.
- CIC Station records lease ownership, renewal, expiration, completion, and failure.
- Vincent starts and supervises the local agent runtime, initially Codex.
- Work may direct Codex to obtain a Git repository, read its instructions, perform bounded work, validate it, and publish durable results.
- AI-provider authentication remains separate from worker enrollment and task routing.

Current Git may refine these details; `PROJECT.md`, `CURRENT_STATE.md`, current component requirements, and accepted ADRs remain authoritative.

## Project and context management

- Consider storing project roadmaps, agent instructions, operating rules, decisions, constraints, and work history in CIC Station only where a future authority model justifies it.
- Consider immutable/versioned instruction snapshots for leased work so active execution is not silently changed.
- Consider project templates, reusable work packets, dependencies, priorities, and completion criteria.

## Scheduling and orchestration

- Match unassigned work to workers by capability, OS, installed tools, resources, trust level, and load.
- Support dependencies, retries, deadlines, recurring work, priorities, and multi-stage missions.
- Reassign after worker failure only with lease/result fencing that quarantines stale results.
- Coordinate multiple workers on one project without overlapping/conflicting changes.

## Git and development workflow

- Consider managed branches/worktrees per job.
- Consider commit/test/PR/review gates before accepting results.
- Consider conflict detection, merge preparation, cleanup, and recovery workflows.
- Preserve Git commits as durable development evidence while CIC Station remains authoritative for operational state.

## Review, safety, and authority

- Consider approval policies for commands, credentials, deployment, destructive actions, merges, and external publication.
- Consider global pause, worker isolation, emergency stop, credential revocation, and incident history.
- Preserve human authority over reassignment, acceptance, deployment, and irreversible actions.
- Consider append-only event history for audit and recovery.

## User interfaces

- Consider a richer browser command center for workers, projects, jobs, leases, logs, approvals, and results.
- Treat phone-friendly/mobile clients as optional control surfaces rather than a defining requirement.
- Add live terminal/session views only where intervention or diagnosis requires them.

## Provider-neutral agents

- Maintain a stable runtime-adapter boundary for Codex and possible future providers such as Gemini, Claude, Ollama/local models, OpenCode, or custom runtimes.
- Keep CIC/Vincent job semantics separate from provider-specific sessions, authentication, approvals, and event formats.
- Allow different workers/providers without changing the operator-facing work model when practical.

## Worker lifecycle and infrastructure

- Track richer hardware, software, network, health, power, and runtime inventory.
- Evaluate wake, low-power idle, maintenance, upgrades, diagnostics, and temporary worker retirement.
- Support or evaluate Internet-connected, NATed, LAN-only, and CIC-proxied workers.
- Consider artifact distribution, software caching, and controlled Internet proxying through CIC Station.

## Evaluation rules

Before promoting any item above:

1. demonstrate a real Fleet use case that current 1.0 architecture cannot handle cleanly;
2. identify the owning boundary: CIC Station, Vincent, agent runtime, Git host, or external integration;
3. evaluate security cost, operational complexity, recovery behavior, and provider lock-in;
4. prefer interoperable protocols and small replaceable components;
5. record the promotion as a separate dated decision rather than editing this historical inventory into current authority.
