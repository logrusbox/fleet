# ADR-0001: Use a dedicated Fleet repository for cross-component planning and integration authority

**Status:** Accepted  
**Decision date:** 2026-08-28  
**Amended:** 2026-08-28 — product umbrella renamed from VINCENT Program to Fleet.

## Context

Vincent and CIC Station are separate components with independent source trees, requirements, ADRs, roadmaps, issues, releases, and implementation lifecycles. Cross-component planning previously lived in CIC Station because a shared planning surface was needed. An organization-level GitHub Project was evaluated but rejected after setup because the connected automation cannot maintain Projects v2 fields, views, statuses, or workflows directly without imposing a manual parallel planning burden on the owner.

Fleet is the product umbrella. CIC Station is its Command Information Center and central control plane; Vincent is its managed worker platform. Their current names remain authoritative.

## Decision

Use three repositories under the Logrus Box organization:

- `logrusbox/vincent` — Vincent component authority.
- `logrusbox/cic-station` — CIC Station component authority.
- `logrusbox/fleet` — Fleet-level cross-component roadmap, integration issues, status, and ADRs.

The Fleet repository owns only cross-component concerns. If an issue, requirement, ADR, or roadmap item can be owned and accepted entirely by one component repository, it remains there.

GitHub issues are the active planning/work anchors. Pull requests are implementation/review evidence. Component release targets remain component-repository milestones and roadmaps. Fleet milestones M0-M8 remain integration outcomes rather than software versions.

Names such as `fleet-cic` and `fleet-worker` are possible future conventions but are not adopted by this decision.

## Rationale

A dedicated Fleet repository removes the artificial rule that CIC Station owns planning for Vincent while keeping the planning surface accessible to the automation that manages normal GitHub repositories and issues. The narrow ownership rule prevents the third repository from becoming a duplicate backlog or documentation mirror.

## Consequences

- The canonical cross-component roadmap belongs to Fleet.
- CIC Station and Vincent link to the Fleet roadmap rather than owning editable copies.
- Cross-component work is represented once here and links authoritative component issues and pull requests.
- Component-specific issues and implementation remain in their component repositories.
- GitHub Projects v2 is not required for normal Fleet operation.
- The Fleet repository contains no component implementation code or operational fleet data.
