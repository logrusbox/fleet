# Great Parallel Work

**Purpose:** Maintain a living catalog of projects that overlap Fleet's goals or solve adjacent problems whose implementations, protocols, or ideas may inform Vincent and CIC Station.

**Last reviewed:** 2026-08-28

This is research and provenance documentation, not a roadmap or an adoption decision. Product requirements remain authoritative in the owning repositories.

## Current direction

Do not commit Fleet to a wholesale Herd fork yet. The present default is a purpose-built CIC Station core focused on ChatGPT connectivity, worker presence, assignments, claims, leases, results, and Vincent control, while selectively reusing clearly licensed code when reuse is smaller and safer than reimplementation.

A bounded Herd fork spike remains a valid evaluation. It should become the product base only if testing shows that its remote-worker, authentication, session, and provider infrastructure saves more work than removing or replacing its unrelated application layers and adding Fleet's missing job/lease model.

## Reuse classifications

| Classification | Meaning |
|---|---|
| Fork candidate | The license appears to permit a derivative, subject to its obligations; technical suitability still requires proof. |
| Selective reuse candidate | Small modules or algorithms may be imported with provenance, notices, compatibility review, and tests. |
| Ideas/specifications | Study behavior, architecture, and published interfaces; implement independently. |
| Blocked pending license | Do not copy or derive code until an unambiguous license grant is present and verified. |
| Reference only | Useful comparison, but currently a poor technical base for Fleet. |

No entry authorizes reuse by itself. Before copying code, verify the license at the exact commit or tag, file-level notices, dependency licenses, compatibility with the destination repository, and all attribution/source-disclosure obligations.

## Closest systems

### Herd

- Project: [NickGuAI/Herd](https://github.com/NickGuAI/Herd)
- License observed: AGPL-3.0-only
- Review depth: Deep source review and clean production build of public `0.0.14-beta`
- Relevant work: outbound worker WebSocket, machine pairing, provider discovery/adapters, remote agent sessions, approvals, credentials, machine inventory, API keys, web/mobile interfaces
- Gaps for Fleet: no durable push/pull work queue, lease epochs, expiry/reassignment, stale-result rejection, or ChatGPT-facing MCP server; public release repository has no behavioral test suite and appears synchronized from a separate monorepo
- Possible use: bounded fork spike or selective reuse in an AGPL-compatible CIC Station
- Current classification: Fork candidate; selective reuse candidate
- Decision status: No fork decision accepted

### Agents Anywhere

- Project: [anywhere-labs/Agents-Anywhere](https://github.com/anywhere-labs/Agents-Anywhere)
- License observed: README links to MIT, but the referenced root `LICENSE` file is absent
- Review depth: Deep source inspection; not built or run
- Relevant work: FastAPI control server, outbound connector WebSocket, device pairing, Codex-first runtime adapter, local files/shell/terminal, approvals, SQLite/PostgreSQL, desktop and mobile clients
- Gaps for Fleet: remote-session controller rather than job broker; no shared job queue, assignment/claim leases, expiry/reassignment, stale-result handling, or ChatGPT-facing MCP server
- Possible use: architecture reference; potentially a strong Vincent/CIC transport donor if its licensing is repaired
- Current classification: Blocked pending license
- Required action before reuse: obtain an actual license file and confirmation that it covers the repository and existing commits

### ADHDev

- Project: [vilmire/adhdev](https://github.com/vilmire/adhdev)
- License observed: AGPL-3.0-or-later
- Review depth: Deep source review
- Relevant work: task queue, dependencies and retries, capability-based claims, event ledger, idempotent completion fingerprints, worktrees, review/refinery gates, mission model, and `mesh_*` MCP tools
- Gaps for Fleet: public cross-machine relay/dispatch is not included; very large codebase; SQLite runtime authority rather than Fleet's Vincent/CIC protocol
- Possible use: queue, event, idempotency, review, and MCP tool-surface patterns
- Current classification: Selective reuse candidate; ideas/specifications

### Kandev

- Project: [kdlbs/kandev](https://github.com/kdlbs/kandev)
- License observed: AGPL-3.0-only
- Review depth: Deep source review
- Relevant work: task-centric UI, multi-repository worktrees, review/PR flows, executor interface, remote `agentctl`, WebSocket API, and credential lease/reissue
- Gaps for Fleet: CIC-initiated SSH/cloud runtimes rather than a permanently enrolled outbound Vincent; no Fleet-style distributed claim lease
- Possible use: executor boundary, credential lifecycle, task/worktree/PR patterns
- Current classification: Selective reuse candidate; ideas/specifications

### Codeman

- Project: [Ark0N/Codeman](https://github.com/Ark0N/Codeman)
- License observed: MIT
- Review depth: Deep source review
- Relevant work: persistent tmux sessions, local/Docker/SSH providers, terminal replay, exactly-once input using client and sequence identifiers, idle detection, reconnect recovery, push notifications, and circuit breakers
- Gaps for Fleet: central process reaches workers through SSH; not a pull-worker scheduler or durable lease authority
- Possible use: exactly-once command delivery, replay, terminal/session persistence, idle and failure recovery
- Current classification: Selective reuse candidate

### Vibe Kanban

- Project: [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)
- License observed: Apache-2.0
- Review depth: Deep source review
- Relevant work: safe multi-repository worktree creation, rollback, locking, cleanup, migration, PR and merge workflows
- Gaps for Fleet: local development orchestration rather than worker enrollment and distributed leases
- Possible use: worktree lifecycle algorithms and tests
- Current classification: Selective reuse candidate

## Agent runtimes and protocols

### OpenAI Codex

- Project: [openai/codex](https://github.com/openai/codex)
- License observed: Apache-2.0
- Relevant work: official Codex CLI/app-server behavior, authentication integration, approvals, events, and agent execution
- Possible use: prefer supported Codex interfaces over terminal scraping
- Current classification: Selective reuse candidate; primary integration reference

### Agent Client Protocol

- Project: [agentclientprotocol/agent-client-protocol](https://github.com/agentclientprotocol/agent-client-protocol)
- License observed: Apache-2.0
- Relevant work: provider-neutral JSON-RPC agent/editor interface and capability negotiation
- Possible use: inform Vincent's replaceable runtime-adapter boundary
- Current classification: Ideas/specifications; selective reuse candidate

### OpenHands

- Project: [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- License observed: MIT
- Relevant work: sandbox/runtime abstraction, event streams, agent execution, workspace handling
- Gaps for Fleet: supplies its own agent platform rather than supervising an already authenticated local Codex installation
- Current classification: Selective reuse candidate; reference only as a product base

### GitHub Agent HQ

- Project: [GitHub Agent HQ](https://github.com/features/copilot)
- License/source status: proprietary product; no reusable implementation identified
- Relevant work: multi-agent dashboard, outcome comparison, repository and pull-request integration
- Current classification: Ideas/specifications only

## Distributed jobs, leases, and delivery semantics

### BOINC

- Project: [BOINC/boinc](https://github.com/BOINC/boinc)
- License observed: LGPL-3.0
- Relevant work: workunits, host capability scheduling, deadlines, retries, result validation, redundancy, and unreliable-host handling
- Possible use: conceptual model for Fleet work items, attempts, leases, results, and late-result treatment
- Current classification: Ideas/specifications; source reuse requires careful LGPL boundary review

### Temporal

- Project: [temporalio/temporal](https://github.com/temporalio/temporal)
- License observed: MIT
- Relevant work: durable workflow history, activity heartbeats, timeouts, cancellation, retries, and idempotency
- Gaps for Fleet: substantial operational dependency for the initial product
- Current classification: Ideas/specifications; possible later integration

### NATS Server and JetStream

- Project: [nats-io/nats-server](https://github.com/nats-io/nats-server)
- License observed: Apache-2.0
- Relevant work: durable pull consumers, acknowledgement deadlines, redelivery, backpressure, and disconnected clients
- Current classification: Ideas/specifications; possible later transport

### River

- Project: [riverqueue/river](https://github.com/riverqueue/river)
- License observed: MPL-2.0
- Review depth: Discovered; deep review pending
- Relevant work: PostgreSQL-backed durable job queues, retries, uniqueness, and worker coordination
- Possible use: compare its transactional job model with CIC Station's work-item/attempt/lease design
- Current classification: Selective reuse candidate, subject to MPL file-level obligations

### Asynq

- Project: [hibiken/asynq](https://github.com/hibiken/asynq)
- License observed: MIT
- Review depth: Discovered; deep review pending
- Relevant work: distributed task queues, retries, scheduling, priorities, and worker concurrency
- Gaps for Fleet: Redis-based library, not a complete worker trust/control protocol
- Current classification: Selective reuse candidate; ideas/specifications

## Enrollment, connectivity, and machine control

### Headscale

- Project: [juanfont/headscale](https://github.com/juanfont/headscale)
- License observed: BSD-3-Clause
- Relevant work: node registration, preauthorization keys, expiry, revocation, routes, and self-hosted overlay coordination
- Possible use: optional network transport integration; enrollment ideas
- Boundary: Fleet identity and authorization must not depend on a Logrus Box-operated rendezvous service
- Current classification: Selective reuse candidate; ideas/specifications

### MeshCentral

- Project: [Ylianst/MeshCentral](https://github.com/Ylianst/MeshCentral)
- License observed: Apache-2.0
- Relevant work: outbound device agents, enrollment, inventory, status, audit history, command channels, and reverse tunnels
- Gaps for Fleet: broad remote-management/RCE platform rather than AI job broker
- Current classification: Selective reuse candidate; reference only as a product base

### Coder

- Project: [coder/coder](https://github.com/coder/coder)
- License observed: AGPL-3.0
- Review depth: Discovered; deep review pending
- Relevant work: centrally managed developer environments and agents, workspace lifecycle, templates, identity, networking, and audit
- Possible use: workspace/environment lifecycle and policy ideas
- Current classification: Fork or selective reuse candidate only after deeper scope and license review

### E2B infrastructure

- Project: [e2b-dev/infra](https://github.com/e2b-dev/infra)
- License observed: Apache-2.0
- Review depth: Discovered; deep review pending
- Relevant work: secure disposable execution environments for AI-generated code
- Possible use: future sandbox or disposable-worker architecture
- Current classification: Selective reuse candidate; ideas/specifications

### Daytona

- Project: [daytonaio/daytona](https://github.com/daytonaio/daytona)
- License observed: GitHub currently reports no repository license
- Review depth: Discovered; deep review pending
- Relevant work: secure elastic infrastructure for executing AI-generated code
- Current classification: Blocked pending license; ideas/specifications only

## General automation and execution control

### Rundeck

- Project: [rundeck/rundeck](https://github.com/rundeck/rundeck)
- License observed: Apache-2.0
- Review depth: Discovered; deep review pending
- Relevant work: authenticated job execution, node inventory, access policy, scheduling, logs, and operator controls
- Current classification: Selective reuse candidate; ideas/specifications

### AWX

- Project: [ansible/awx](https://github.com/ansible/awx)
- License observed: GitHub reports a nonstandard or unresolved repository license; file-level verification pending
- Review depth: Discovered; deep review pending
- Relevant work: inventories, credentials, job templates, execution environments, role-based access, events, and result retention
- Current classification: Ideas/specifications until licensing is verified

### Buildbot

- Project: [buildbot/buildbot](https://github.com/buildbot/buildbot)
- License observed: GPL-2.0
- Review depth: Discovered; deep review pending
- Relevant work: long-lived workers, central scheduling, builders, retries, status, and source-control-triggered execution
- Current classification: Ideas/specifications; source reuse requires GPL compatibility review

### Woodpecker CI

- Project: [woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker)
- License observed: Apache-2.0
- Review depth: Discovered; deep review pending
- Relevant work: central server with distributed agents, pipelines, repository integration, secrets, logs, and execution isolation
- Current classification: Selective reuse candidate; ideas/specifications

## Exclusions and false leads

### Herdr

- Project: [herdrdev/herdr](https://github.com/herdrdev/herdr)
- Finding: terminal multiplexer with a similar name; not the Herd remote-agent control project
- Current classification: Excluded from further Fleet-base evaluation unless its terminal handling becomes specifically relevant

## Provenance procedure

Before importing any external code into Fleet:

1. Record the upstream repository, exact commit or release tag, file paths, copyright notices, and license.
2. Confirm the destination component's license is compatible.
3. Preserve required license and NOTICE material and mark modifications where required.
4. Import the smallest coherent unit; avoid copying an entire product to obtain one subsystem.
5. Add tests that establish Fleet's expected behavior independently of upstream assumptions.
6. Keep third-party code identifiable in source history and dependency documentation.
7. Recheck licensing at public-release review; repository metadata and README claims are not sufficient when the actual license text is missing.
8. Never copy source from a project classified as ideas-only or license-unresolved.

## Intake template

Add new discoveries using:

- Project and canonical link
- Exact license observed and where verified
- Date and depth of review
- Fleet capability it resembles
- Useful code, protocol, algorithm, or product idea
- Architectural mismatches and security concerns
- Proposed action: fork, selective reuse, independent implementation, integration, defer, or reject
- Required attribution or copyleft obligations
- Decision status and follow-up owner
