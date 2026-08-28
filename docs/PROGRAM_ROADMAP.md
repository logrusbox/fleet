# Fleet Program Roadmap

This is the canonical cross-component roadmap for Fleet. Component-specific implementation details remain in the Vincent and CIC Station roadmaps.

## Fleet structure

- **Fleet** is the product.
- **CIC Station** is Fleet's Command Information Center and central control plane.
- **Vincent** is Fleet's managed worker platform.
- The existing component names remain authoritative; `fleet-cic` and `fleet-worker` are possible future names only.

## Program principles

- Vincent remains a useful standalone worker platform.
- CIC Station governs managed-fleet enrollment, authorization, assignments, leases, approvals, health, operational configuration, and coordination after explicit enrollment.
- Workers and the control plane are replaceable; durable authoritative work must not depend on one machine or chat thread.
- Git repositories preserve durable source, requirements, ADRs, issues, PR evidence, and releases; CIC Station stores operational fleet state once implemented.
- Product/release evidence is required before declaring milestones complete.
- Generic Vincent and CIC Station releases must support independent self-hosted deployments without requiring a Logrus Box-operated rendezvous, registry, pairing, or relay service.
- Public Internet access is not a prerequisite for Vincent/CIC Station enrollment when the two components have a mutually reachable private network path.

## Program milestones

| Milestone | Outcome | Current state |
|---|---|---|
| M0 | Canonical product, requirements, ADR, roadmap, status, repository-boundary, and governance model established | Complete |
| M1 | Vincent installer and standalone READY path physically proven on heterogeneous hardware; large workstation usable as persistent worker | In progress |
| M2 | Vincent completes bounded real work from an operator-selected source, publishes verified results, maintains itself, and preserves installer/software version separation | Not complete |
| M3 | First managed-worker CIC Station model proven through persistent service/database authority with decentralized enrollment, scoped authorization, inventory, bounded work-item/attempt execution, result reporting, revocation, and managed operational configuration | Planned |
| M4 | Two-worker coordination proves persistent lease ownership, liveness/grace behavior, stale-result protection, replacement, and recovery | Planned |
| M5 | CIC Station operational hardening plus responsive phone-capable web UI, deployment/recovery workflows, and supported direct/private/tunneled connectivity modes proven | Planned |
| M6 | CIC Station passes its formal-release audit and ships the reusable public application source under the accepted release license with self-hosted packaging and release process | Planned |
| M7 | Multi-project and multi-agent/provider scheduling/identity policy proven with project isolation, capability matching, centrally assigned worker network/egress policy, and managed software/source delivery where required | Planned |
| M8 | Full destructive recovery proves workers and CIC Station can be reconstructed from durable/protected external state; 1.0 Fleet acceptance criteria satisfied | Planned |

## Current execution strategy

- Complete Vincent physical installer/runtime verification from exact accepted `main` source.
- Keep the large workstation online as the first useful persistent Vincent worker and use it for real development work when practical.
- Use the old laptop as the expendable physical installer/recovery test target for repeated clean installs and failure-path tests.
- Do not destroy the productive workstation merely for symmetry; deliberately rebuild it later at the worker-impermanence/recovery acceptance gate.
- Begin CIC Station application/domain-model work with the minimum persistent service/API/database foundation from the start; do not make Git the authoritative live lease/heartbeat database.
- Resolve CIC Station work-item/attempt/lease/result modeling and multidimensional worker-state semantics before database schemas harden.
- Implement managed enrollment from the accepted decentralized model: CIC Station supplies its reachable endpoint plus a single-use bootstrap authorization; Vincent initiates the connection and binds its worker-generated asymmetric identity to that CIC Station.
- Preserve same-subnet/private-address enrollment and make CIC Station reachability independent from public Internet/provider/package-source availability.
- Treat CIC Station as the managed operational-policy authority after enrollment, including direct/proxied/restricted network mode and future managed software/source delivery.

## Program planning model

Fleet deliberately uses ordinary GitHub repositories, issues, pull requests, milestones, labels, and repository Markdown rather than GitHub Projects v2.

- `logrusbox/fleet` holds only Fleet-wide and cross-component work.
- `logrusbox/vincent` owns Vincent-specific work.
- `logrusbox/cic-station` owns CIC Station-specific work.
- Component release targeting uses repository milestones in the relevant component repository.
- Cross-component program stage uses M0-M8 in this roadmap and, when useful, Fleet issue metadata/labels.
- PRs are implementation/review evidence; issues are planning/work anchors.
- Do not create duplicate Fleet issues merely to mirror component issues.

## Cross-component acceptance rules

A program milestone is complete only when:

1. required implementation exists in the owning component repositories;
2. automated validation passes;
3. applicable physical/integration proof has been performed;
4. authoritative results are durable outside the tested worker;
5. relevant requirements/ADRs/status/roadmaps are updated in their owning repositories;
6. cross-component compatibility/authority boundaries are coherent;
7. no unresolved safety or ownership contradiction remains.

## Deferred capabilities

Unscheduled future ideas belong in GitHub issues in the repository that owns them. Promote an item into this roadmap only when it becomes a concrete cross-component milestone outcome.
