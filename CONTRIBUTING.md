# Contributing to Fleet

This repository coordinates Fleet at the Fleet-wide and cross-component level. Component implementation contributions belong in the relevant component repository.

## Repository workflow

- `main` is the only permanent branch.
- Use a short-lived branch for each bounded change.
- Open a pull request to `main`.
- Keep PRs focused on one coherent Fleet-level objective.
- Run repository validation before merge.
- Squash merge accepted PRs.
- Delete temporary branches after merge or supersession.

## Issue placement

Create an issue here only when acceptance genuinely spans Vincent and CIC Station or concerns Fleet-level governance/integration. Otherwise use the owning component repository.

Cross-component issues should link their authoritative component issues/PRs rather than duplicating them.

## Documentation ownership

- Fleet roadmap: `docs/PROGRAM_ROADMAP.md`
- Fleet status: `docs/STATUS.md`
- Fleet governance/authority: `docs/GOVERNANCE.md`
- Fleet-level consequential decisions: `docs/decisions/`

Do not add component-specific requirements, component source code, component release notes, or duplicate component roadmaps here.

## Security

Never commit raw credentials, secrets, private keys, authentication caches, production data, private fleet state, or protected deployment configuration. See `SECURITY.md`.
