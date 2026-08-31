# Fleet Agent Instructions

These instructions apply to work in `logrusbox/fleet`.

## Start order

Before consequential Fleet-level work, read:

1. `README.md`
2. `docs/PROGRAM_ROADMAP.md`
3. `docs/STATUS.md`
4. `docs/GOVERNANCE.md`
5. `docs/decisions/README.md`
6. relevant active issues/PRs in all affected repositories

Then inspect the current authoritative state of `logrusbox/vincent` and/or `logrusbox/cic-station` as needed.

## Authority boundary

- This repository owns Fleet-level planning, governance, and cross-component integration only.
- Vincent-specific requirements, ADRs, issues, implementation, tests, releases, and roadmap belong in `logrusbox/vincent`.
- CIC Station-specific requirements, ADRs, issues, implementation, tests, releases, and roadmap belong in `logrusbox/cic-station`.
- Do not duplicate component issues here merely for visibility.
- If a cross-component issue requires component work, link the authoritative component issue/PR from the Fleet issue.
- GitHub Projects v2 is intentionally not required.

## Workflow

- `main` is the only permanent branch.
- Use short-lived branches and PRs for normal changes.
- Squash merge accepted PRs.
- Delete temporary merged/superseded branches after useful work is preserved.
- Keep Fleet documents concise and derived from current component-repository authority rather than copying component documentation wholesale.

## Safety

- Never commit credentials, private keys, tokens, authentication caches, private fleet data, production configuration, or private operational data.
- Do not use this repository as a live fleet database, task execution system, or secret transport.
- Consequential component architecture belongs in the owning component ADRs unless the decision genuinely spans Fleet.
