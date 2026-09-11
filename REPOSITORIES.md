# Fleet Repository Inventory

This file classifies repositories and repository identities relevant to current Fleet authority. Existence alone does not make a repository current.

## Current authoritative repositories

| Repository | Classification | Purpose | Authority |
|---|---|---|---|
| `logrusbox/fleet` | **ACTIVE** | Fleet-wide product/project spine, cross-component roadmap, architecture, integration, governance, decisions, repository inventory, project memory | Fleet-wide truth only; no component source or live operational data |
| `logrusbox/vincent` | **ACTIVE** | Vincent worker distribution, installer/runtime, machine management, agent runtime adapters, diagnostics/recovery, component docs/tests/releases | Vincent component implementation and component-specific truth |
| `logrusbox/cic-station` | **BOOTSTRAP / ACTIVE AUTHORITY** | CIC Station reusable control-plane application, API/database/UI implementation, component docs/tests/releases | CIC Station component authority; application implementation has not yet begun, but the repository is canonical |

## Superseded repository identities

| Historical identity | Classification | Superseded by | Notes |
|---|---|---|---|
| `vincent-program` / prior Fleet umbrella repository name | **SUPERSEDED NAME** | `logrusbox/fleet` | The Fleet coordination repository was renamed. Old references do not restore the retired name or authority model. |
| `Gordonfive/mission-control` | **SUPERSEDED NAME** | `logrusbox/cic-station` | Current CIC Station Git records the rename to `Gordonfive/cic-station`, followed by ownership transfer to Logrus Box. |
| `Gordonfive/cic-station` | **SUPERSEDED LOCATION** | `logrusbox/cic-station` | Same current CIC Station lineage before organization transfer. |

## Historical/legacy repositories not established by current accessible Git

Older project conversations may refer to additional worker/orchestrator prototypes or repository names. They are **not authoritative by default** and must not be added here as current repositories solely from chat memory.

When a historical repository is located, classify it using one of:

- **ACTIVE** — current source/document authority;
- **BOOTSTRAP** — canonical current repository whose implementation is still being established;
- **FROZEN** — intentionally retained at a fixed state;
- **HISTORICAL** — preserved for provenance/reference only;
- **SUPERSEDED** — replaced by a named current authority;
- **EXPERIMENTAL** — active experiment without product authority.

Record its exact repository, purpose, last relevant branch/release, authoritative replacement if any, and which facts may still be imported.

## Authority rules

1. The owning component repository wins for component implementation/specification details.
2. `logrusbox/fleet` wins for Fleet-wide scope, roadmap, cross-component contracts, integration outcomes, and repository classification.
3. A repository rename or ownership transfer does not create two current authorities.
4. An old repository does not regain authority because an old chat or handoff points to it.
5. If a legacy repository conflicts with current Git and chronology is clear, current Git wins.
6. If chronology is unclear, classify the conflict as unresolved rather than importing it.

## Current branch/release notes

- All three current repositories use `main` as the only permanent branch target.
- Vincent is currently pre-1.0 and has executable installer/runtime work requiring physical validation.
- CIC Station is currently `0.1.0` build `0001`; its repository is authoritative even though service/API/database/UI implementation has not yet started.
- Fleet milestones M0-M8 are integration outcomes, not software releases.

## Repository discovery during reconciliation

If old ChatGPT Project reconciliation surfaces a repository not listed here, first verify it in Git. Do not create a classification from chat alone. Add it only after its relationship to current authority is established.