# Great Parallel Work

**Purpose:** Maintain a living catalog of projects that overlap Fleet's goals or solve adjacent problems whose implementations, protocols, or ideas may inform Vincent and CIC Station.

**Last reviewed:** 2026-08-28

This is research and provenance documentation, not a roadmap or an adoption decision. Product requirements remain authoritative in the owning repositories.

## Current direction

Do not commit Fleet to a wholesale fork yet. The present default is a purpose-built CIC Station core focused on ChatGPT connectivity, worker presence, assignments, claims, leases, results, and Vincent control, while selectively reusing clearly licensed code when reuse is smaller and safer than reimplementation.

Two bounded fork spikes now merit direct comparison. Harness is the strongest discovered CIC control-plane candidate because it already models runtime hosts, capability matching, claims, renewable leases, lease generations, and stale-completion fencing. Herd remains the strongest remote-worker/session candidate. Neither should become the product base until a spike proves that retained code exceeds the cost of removing unrelated layers and filling Fleet-specific enrollment, identity, ChatGPT, and Vincent gaps.

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

### Harness

- Project: [majiayu000/harness](https://github.com/majiayu000/harness)
- License observed: MIT
- Review depth: Deep source inspection at `8904d1bea9509851eb812c3bcf9f1a4d9b7f6b4c`; not built or run
- Relevant work: persistent runtime-host registration and heartbeat, host lifecycle and draining, capability-based job claims, renewable job leases, lease generations and proofs, idempotent renewal identifiers, expiry, stale-completion rejection, completion evidence, project cache, Codex/Claude/OpenCode adapters, policy, review, observability, and dashboarding
- Particularly close behavior: host heartbeat is separate from job lease; a worker that loses a lease receives `must_stop`; stale or wrong-generation completion is rejected; lease TTL is bounded and configurable
- Gaps for Fleet: no Vincent-style worker daemon or outbound enrollment connector was found; the repository exposes server-side runtime-host APIs but not the per-machine installation, one-time marriage, asymmetric worker identity, or ChatGPT-facing relationship CIC requires
- Risks to verify: its own reliability audit describes historical dual-lease and supervision hazards; determine which remain at the evaluated commit before adopting the scheduler
- Possible use: first CIC fork spike; alternatively reuse the runtime-host/job-lease model and tests while building Vincent enrollment and transport independently
- Current classification: Highest-priority fork candidate; selective reuse candidate
- Decision status: No fork decision accepted

### Paperclip

- Project: [paperclipai/paperclip](https://github.com/paperclipai/paperclip)
- License observed: MIT
- Review depth: Deep source inspection at `ad474abece709bdb0db47f83977780e1ce672817`; not built or run
- Relevant work: central goals, projects, issues, delegation, permissions, approvals, budgets, task dependencies, atomic checkout, execution locks, heartbeat wakeups, orphan recovery, persistent agent sessions, and adapters for several agent runtimes
- Runner work: the experimental Rust `paperclip-runnerd` implements a WebSocket runner protocol, Codex app-server provider, short-lived connection leases, one-use bootstrap tickets, command idempotency, durable outbox, reconnect/replay, and semantic action authorization
- Gaps for Fleet: the primary product models an AI company and is much broader than Fleet 1.0; built-in adapters normally execute near the Paperclip server, while the runner's initial supported topology is still intentionally narrow rather than a finished Vincent workstation fleet
- Possible use: task/context/governance donor and strong reference for a durable Vincent runner protocol; consider a spike, but prefer selective reuse over a wholesale product fork
- Current classification: Selective reuse candidate; secondary fork candidate

### K-Dense BYOK and Kady

- Project: [K-Dense-AI/k-dense-byok](https://github.com/K-Dense-AI/k-dense-byok)
- License observed: MIT
- Review depth: Source and documentation inspection at `7b3e89502176d347117c2e5af38d47bd528d9fb5`; not built or run
- Terminology: Kady is the research agent inside K-Dense BYOK, not a separate control-plane project
- Relevant work: ordinary-folder local projects, parallel chat tabs and specialist sub-agents, durable/reconnectable live turns, queued steering messages, provider-neutral OpenRouter/subscription/Ollama selection, MCP tools, project budgets, remote Modal compute, structured workflow templates, and a provenance-rich living lab notebook
- Gaps for Fleet: single-user local research workspace rather than a central authority for enrolled physical workers, job claims, renewable leases, reassignment, and stale-result fencing
- Possible use: project workspace and artifact organization, portable provider configuration, run recovery, budget display, auditable work logs, workflow templates, and specialist delegation patterns
- Current classification: Selective reuse candidate; reference only as a CIC base

### RunDiffusion Agents

- Project: [rundiffusion/RunDiffusion-Agents](https://github.com/rundiffusion/RunDiffusion-Agents)
- License observed: Apache-2.0
- Review depth: Source inspection; not deployed or run
- Relevant work: Docker Compose agent farm, per-tenant isolation, reverse-proxy routes, configuration and version pins, secrets policy, health checks, recovery, and hosted terminal/UI routes for several agent tools
- Gaps for Fleet: deployment kit for containerized agent services, not a durable job scheduler, workstation enrollment service, or lease authority
- Possible use: future CIC/Vincent deployment, tenancy, routing, configuration, and recovery reference
- Current classification: Selective reuse candidate; reference only as a product base

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
- Relevant work: Agent Canvas control-center UI, registry and switching across local/remote/cloud Agent Servers, sandbox/runtime abstraction, event streams, multiple provider agents including Codex, workspace handling, API/client separation, and scheduled or webhook automations
- Repository note: the separate [OpenHands/agent-canvas](https://github.com/OpenHands/agent-canvas) repository is archived and its work moved into OpenHands
- Gaps for Fleet: users select backends and operate conversations; the backends are not automatically treated as one schedulable worker pool with assignment/claim leases and stale-result fencing
- Current classification: Selective reuse candidate; reference only as a product base

### Cotal

- Project: [Cotal-AI/Cotal](https://github.com/Cotal-AI/Cotal)
- License observed: Apache-2.0
- Review depth: Deep source inspection at `ae9f61643816ffe544f7e20d9edde2b5fe816c53`; not built or run
- Relevant work: NATS/JetStream-backed unicast, multicast and anycast messaging; durable delivery, presence, JWT/ACLs, remote managers and manager leases, remote launch specifications, MCP tools, and a Codex app-server connector that can wake idle Codex sessions and steer active ones
- Delivery behavior: messages are acknowledged only after a successful agent turn, allowing redelivery after failure or restart
- Gaps for Fleet: durable agent messaging and anycast are not an authoritative work-item/attempt/result lease model; it does not by itself define expiry, reassignment, or acceptance rules for late results
- Possible use: Vincent-to-CIC transport or protocol donor, especially for Codex app-server integration; adopting it also introduces NATS/JetStream operations
- Current classification: Selective reuse candidate; possible transport integration

### Scientific Agent Skills

- Project: [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
- License observed: repository MIT; individual skills explicitly carry their own license metadata and must be checked independently
- Review depth: Repository structure and documentation inspection; individual skills not audited
- Relevant work: a large, versioned, installable library of `SKILL.md` capability packages compatible with several agent hosts; project/user install scopes, reproducible pinning, metadata, validation, and per-skill attribution
- Gaps for Fleet: capability content, not worker discovery, scheduling, execution authority, or transport
- Possible use: define a portable CIC/Vincent capability-package convention and let projects pin approved skills by version; scientific skills themselves are optional project payloads, not CIC core
- Current classification: Ideas/specifications; selective reuse only after per-skill license review

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
