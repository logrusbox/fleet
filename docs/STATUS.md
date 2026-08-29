# Fleet Status

**Updated:** 2026-08-29

## Product structure

**Fleet** is the product umbrella maintained by Logrus Box:

- `logrusbox/vincent` — Vincent managed worker platform.
- `logrusbox/cic-station` — CIC Station Command Information Center and control plane.
- `logrusbox/fleet` — Fleet-wide planning, integration, and governance only.

Vincent and CIC Station remain the current component names. Possible names such as `fleet-worker` and `fleet-cic` are deferred and have not been adopted.

The former organization-level GitHub Project was intentionally abandoned because the connected automation could not maintain Projects v2 state directly. Active planning uses normal GitHub issues, pull requests, labels, milestones, and repository Markdown.

## Current program state

- The program repository has been renamed from `vincent-program` to `fleet`.
- M0 governance/documentation structure is complete in the component repositories and is being consolidated into this Fleet repository for cross-component ownership.
- Vincent remains the current physical/operational gate: installer/runtime verification and standalone READY/bounded-work proof are prerequisites for the first managed-worker proof.
- CIC Station's accepted initial foundation is an upstream-friendly Paperclip fork, with generally useful changes contributed upstream and Fleet-specific Vincent/CIC behavior retained under Fleet control.\n- ADR-0003 requires replaceable module contracts across CIC, Vincent, agent runtimes, transports, scheduling, storage, policy, sources, skills, and interfaces while explicitly avoiding premature microservice decomposition.\n- The first foundation gate is a complete ChatGPT-to-CIC-to-Vincent-to-Codex result path; Harness and Herd remain selective donors and fallback evidence.
- The first managed-worker integration remains a later program gate after Vincent proves standalone operation.

## Immediate coordination priorities

1. Reconcile Vincent and CIC Station documentation so neither component repository claims ownership of the overall Fleet roadmap.
2. Move only genuinely cross-component open issues here; leave component-specific work where it is.
3. Keep component-specific releases and milestones in their component repositories.
4. Complete repository protection/settings where GitHub UI intervention is required.

## Known configuration limitation

The connected GitHub automation can manage repository contents, issues, pull requests, branches, and Actions, but cannot rename repositories, create repository rulesets, change merge-method settings, create milestones/labels directly, or manage GitHub Projects v2. Those settings remain explicit GitHub UI tasks when needed.
