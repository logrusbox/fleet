# Program Governance

## Authority model

Each kind of information has one canonical home.

| Information | Authority |
|---|---|
| Vincent product behavior/requirements | `logrusbox/vincent` |
| CIC Station product behavior/requirements | `logrusbox/cic-station` |
| Product-specific ADRs | owning product repository |
| Product-specific bugs/features/tasks | owning product repository issues |
| Product release targets | owning product repository milestones/roadmap |
| Product implementation/review evidence | owning product repository PRs/Actions |
| Cross-product roadmap | `logrusbox/vincent-program/docs/PROGRAM_ROADMAP.md` |
| Cross-product issues/integration acceptance | `logrusbox/vincent-program` issues |
| Program-level decisions | program ADRs in this repository |
| Current cross-product state | `docs/STATUS.md` |

## Issue placement rule

Use the narrowest correct owner.

- If one repository can implement and accept the work independently, create the issue there.
- If acceptance requires coordinated changes or proof across Vincent and CIC Station, create one program issue here and link the product issues/PRs that implement it.
- Do not copy product issue bodies into a program issue. Summarize the cross-product contract and link to authoritative work.
- A dependency is a link/relationship, not a duplicated issue.

## Planning metadata

Keep metadata intentionally small.

Recommended labels, when useful:

- `priority:P0`, `priority:P1`, `priority:P2`, `priority:P3`
- `stage:M0` through `stage:M8`, plus `stage:later`
- `workstream:integration`
- `workstream:security`
- `workstream:protocol`
- `workstream:release`
- `workstream:governance`
- `verification`
- `blocked`

Product repositories may use more specific workstream labels. Avoid reproducing the entire roadmap in labels.

## Work-in-progress discipline

For owner-directed development, normally keep one primary implementation objective active at a time and avoid more than two concurrent implementation issues unless parallelism is intentional and bounded.

## Pull requests

- `main` is the only permanent branch.
- Use short-lived branches for bounded changes.
- Open PRs to `main`.
- Run required CI before integration.
- Squash merge accepted PRs.
- Delete merged/superseded branches after useful work is preserved.
- Program PRs change program documentation/governance only; product code does not belong here.

## GitHub Projects

GitHub Projects v2 is intentionally not part of the authoritative workflow. The current connected automation cannot maintain Projects v2 directly, so requiring it would create a parallel manual state-tracking burden. Reconsider only if the automation boundary changes materially.

## Release and milestone boundaries

Program milestones M0-M8 are integration outcomes, not software versions. Vincent and CIC Station retain independent Semantic Versioning and release milestones in their own repositories.
