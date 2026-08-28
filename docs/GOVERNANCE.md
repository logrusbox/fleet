# Fleet Governance

## Authority model

Each kind of information has one canonical home.

| Information | Authority |
|---|---|
| Vincent behavior and requirements | `logrusbox/vincent` |
| CIC Station behavior and requirements | `logrusbox/cic-station` |
| Component-specific ADRs | owning component repository |
| Component-specific bugs, features, and tasks | owning component repository issues |
| Component release targets | owning component repository milestones/roadmap |
| Component implementation/review evidence | owning component repository pull requests and Actions |
| Fleet roadmap | `logrusbox/fleet/docs/PROGRAM_ROADMAP.md` |
| Cross-component issues and integration acceptance | `logrusbox/fleet` issues |
| Fleet-level decisions | Fleet ADRs in this repository |
| Current Fleet state | `docs/STATUS.md` |

## Issue placement rule

Use the narrowest correct owner.

- If one repository can implement and accept the work independently, create the issue there.
- If acceptance requires coordinated changes or proof across Vincent and CIC Station, create one Fleet issue here and link the component issues and pull requests that implement it.
- Do not copy component issue bodies into a Fleet issue. Summarize the cross-component contract and link to authoritative work.
- A dependency is a link or relationship, not a duplicated issue.

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

Component repositories may use more specific workstream labels. Avoid reproducing the entire roadmap in labels.

## Work-in-progress discipline

For owner-directed development, normally keep one primary implementation objective active at a time and avoid more than two concurrent implementation issues unless parallelism is intentional and bounded.

## Pull requests

- `main` is the only permanent branch.
- Use short-lived branches for bounded changes.
- Open pull requests to `main`.
- Run required CI before integration.
- Squash merge accepted pull requests.
- Delete merged or superseded branches after useful work is preserved.
- Fleet pull requests change Fleet documentation and governance only; component code does not belong here.

## GitHub Projects

GitHub Projects v2 is intentionally not part of the authoritative workflow. The current connected automation cannot maintain Projects v2 directly, so requiring it would create a parallel manual state-tracking burden. Reconsider only if the automation boundary changes materially.

## Release and milestone boundaries

Fleet milestones M0-M8 are integration outcomes, not software versions. Vincent and CIC Station retain independent Semantic Versioning and release milestones in their own repositories.
