# Fleet Status

**Updated:** 2026-08-28

## Product structure

**Fleet** is the product umbrella maintained by Logrus Box:

- `logrusbox/vincent` — Vincent managed worker platform.
- `logrusbox/cic-station` — CIC Station Command Information Center and control plane.
- `logrusbox/fleet` — Fleet-wide planning, integration, and governance only.

Vincent and CIC Station remain the current component names. Possible names such as `fleet-worker` and `fleet-cic` are deferred and have not been adopted.

The former organization-level GitHub Project was intentionally abandoned because the connected automation could not maintain Projects v2 state directly. Active planning uses normal GitHub issues, pull requests, labels, milestones, and repository Markdown.

## Current program state

- M0 governance/documentation structure is complete in the component repositories and is being consolidated into this Fleet repository for cross-component ownership.
- Vincent remains the current physical/operational gate: installer/runtime verification and standalone READY/bounded-work proof are prerequisites for the first managed-worker proof.
- CIC Station implementation may proceed within its accepted product/security/protocol boundaries while avoiding schema decisions that depend on unresolved domain-model work.
- The first managed-worker integration remains a later program gate after Vincent proves standalone operation.

## Immediate coordination priorities

1. Complete the GitHub repository slug rename from `vincent-program` to `fleet`.
2. Reconcile Vincent and CIC Station documentation so neither component repository claims ownership of the overall Fleet roadmap.
3. Move only genuinely cross-component open issues here; leave component-specific work where it is.
4. Keep component-specific releases and milestones in their component repositories.
5. Complete repository protection/settings where GitHub UI intervention is required.

## Known configuration limitation

The connected GitHub automation can manage repository contents, issues, pull requests, branches, and Actions, but cannot rename repositories, create repository rulesets, change merge-method settings, create milestones/labels directly, or manage GitHub Projects v2. Those settings remain explicit GitHub UI tasks when needed.
