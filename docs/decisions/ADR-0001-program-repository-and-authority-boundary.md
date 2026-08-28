# ADR-0001: Use a dedicated program repository for cross-product planning and integration authority

**Status:** Accepted
**Decision date:** 2026-08-28

## Context

Vincent and CIC Station are separate products with independent source trees, requirements, ADRs, roadmaps, issues, releases, and implementation lifecycles. Cross-product planning previously lived in CIC Station because a shared planning surface was needed. An organization-level GitHub Project was evaluated but rejected after setup because the connected automation cannot maintain Projects v2 fields, views, statuses, or workflows directly without imposing a manual parallel planning burden on the owner.

## Decision

Use three repositories under the Logrus Box organization:

- `logrusbox/vincent` — Vincent product authority.
- `logrusbox/cic-station` — CIC Station product authority.
- `logrusbox/vincent-program` — program-level cross-product roadmap, integration issues, program status, and program ADRs.

The program repository owns only cross-product concerns. If an issue, requirement, ADR, or roadmap item can be owned and accepted entirely by one product repository, it remains there.

GitHub issues are the active planning/work anchors. Pull requests are implementation/review evidence. Product release targets remain product-repository milestones/roadmaps. Program milestones M0-M8 remain integration outcomes rather than software versions.

## Rationale

A dedicated program repository removes the artificial rule that CIC Station owns planning for Vincent, while keeping the planning surface fully accessible to the same automation that manages normal GitHub repositories and issues. The narrow ownership rule prevents the third repository from becoming a duplicate backlog or documentation mirror.

## Consequences

- The canonical cross-product program roadmap moves from CIC Station to this repository.
- CIC Station and Vincent link to the program roadmap rather than owning editable copies.
- Cross-product work is represented once here and links authoritative product issues/PRs.
- Product-specific issues and implementation remain in their product repositories.
- GitHub Projects v2 is not required for normal program operation.
- The program repository contains no product implementation code or operational fleet data.
