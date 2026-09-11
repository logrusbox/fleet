# Fleet Project Truth

Fleet is the Logrus Box product for coordinating AI work across managed computers.

## Product boundary

Fleet currently consists of two product components:

- **CIC Station** (`logrusbox/cic-station`) — the Command Information Center and central control plane.
- **Vincent** (`logrusbox/vincent`) — the managed worker platform.

**Codex** is the first supported agent runtime executed through Vincent. It is not a third Fleet product component and must remain behind the provider/runtime boundary defined by Fleet architecture.

`logrusbox/fleet` is the cross-component project authority. It contains no runtime implementation and no live fleet operational data.

## What Fleet is solving

Fleet provides a durable path from an operator or ChatGPT-facing interface through CIC Station to one or more explicitly enrolled Vincent workers, where bounded work is executed by an agent runtime and authoritative results are returned to durable project state.

The current foundation direction is an upstream-friendly Paperclip-derived CIC Station application, with Fleet-owned contracts defining the behavior that must remain stable even if an upstream or borrowed implementation changes.

## Fleet 1.0 scope

Fleet 1.0 is the acceptance outcome represented by milestones M1-M8 in `docs/PROGRAM_ROADMAP.md`. The intended system includes:

- a physically proven, recoverable Vincent installer and standalone READY lifecycle;
- bounded useful work on Vincent before managed-fleet integration;
- explicit CIC Station enrollment, worker identity, authorization, inventory, and revocation;
- persistent work-item, attempt, result, audit, liveness, and operational state in CIC Station;
- durable lease/reassignment behavior for multiple workers, including stale-result fencing and recovery;
- a usable CIC Station web/API surface and supported private/direct/tunneled connectivity modes;
- a reusable self-hosted CIC Station release process;
- multi-project and multi-agent/provider scheduling and isolation behind explicit contracts;
- destructive recovery proof showing that workers and the control plane can be reconstructed from durable protected state.

The exact component release sequencing remains owned by the component repositories. The Fleet roadmap owns only cross-component outcomes.

## Current architecture principles

1. **Fleet-owned contracts outrank imported internals.** Paperclip, Harness, Herd, Codex, and future dependencies are implementations or donors, not architectural authorities.
2. **Modular does not mean microservices.** CIC Station should default to the smallest practical deployment topology, including a modular monolith, until an operational boundary justifies separation.
3. **Vincent remains independently useful.** A fresh Vincent installation must reach standalone READY without CIC Station enrollment or private Fleet credentials.
4. **Enrollment is explicit and revocable.** Managed authority begins only after an operator-approved enrollment flow that binds CIC Station to the worker identity.
5. **Agent runtimes are replaceable.** Codex is first, not permanent architecture.
6. **Durable technical truth is external to workers.** A worker may be rebuilt or replaced without losing accepted source, project artifacts, or control-plane authority.
7. **Private operation must not require a Logrus Box service.** Generic Vincent/CIC Station deployments must support self-hosting and private-network enrollment without a vendor rendezvous or relay dependency.

## Authority boundary: Git versus CIC Station

Git and CIC Station have different authoritative roles.

### Git owns durable development truth

Git repositories own:

- source code;
- committed product/project documentation;
- accepted requirements and ADRs;
- integration history and pull-request evidence;
- releases and durable project artifacts that are intended to live in Git.

A merged commit is evidence of accepted repository state. Git must not be used as the live heartbeat, lease, enrollment-session, or task-execution database.

### CIC Station owns live operational orchestration state

Once implemented, CIC Station owns operational state such as:

- operator and worker enrollment/authorization state;
- worker identity bindings and inventory;
- liveness/health observations;
- work items, assignments/selections, execution attempts, results, and audit state within its domain;
- leases, lease generations, reassignment, and stale-result rejection;
- operational policy and managed configuration.

Task-to-attempt-to-worker-to-result provenance must remain traceable to durable project outputs and accepted Git state where Git is the project authority, without collapsing operational state into Git.

## Security and recovery principles

- Separate human, worker, Git, and model-provider authentication domains.
- Never place reusable secrets, private worker credentials, private fleet state, or production configuration in public Git.
- Use least privilege, explicit authorization, revocation, replay-resistant enrollment, fail-closed server trust, and versioned protocol compatibility.
- Preserve recovery paths for workers, CIC Station state, and project outputs before treating the system as production-ready.
- Physical/destructive operations and credential expansion retain explicit operator gates unless a later accepted decision changes them.

## Explicit 1.0 non-goals

The following are not current merely because they existed in older Mission Control/orchestrator discussions:

- a generalized project-management suite beyond what current Fleet milestones require;
- arbitrary remote-shell control of workers;
- Git as a live scheduler/lease/heartbeat database;
- mandatory multi-provider support before the Codex path works end to end;
- speculative microservice decomposition;
- mandatory mobile/native control applications;
- any historical feature that has not been promoted by current Git authority.

Well-developed historical ideas belong under `docs/evaluations/` or `docs/history/` until a current decision explicitly promotes them.

## Where truth lives

- Fleet-wide product truth: this repository.
- Fleet current cross-component state: `CURRENT_STATE.md`.
- Small durable Fleet decisions and ADR index: `DECISIONS.md` and `docs/decisions/`.
- Repository classification/authority: `REPOSITORIES.md`.
- Cross-component roadmap: `docs/PROGRAM_ROADMAP.md`.
- Component implementation truth: the owning component repository.
- Active work: GitHub issues and pull requests in the owning repository.

Do not reconstruct Fleet from chat history when Git can answer the question.