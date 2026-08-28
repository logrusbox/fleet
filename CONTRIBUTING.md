# Contributing to the VINCENT Program Repository

This repository coordinates the VINCENT product family at the cross-product level. Product implementation contributions belong in the relevant product repository.

## Repository workflow

- `main` is the only permanent branch.
- Use a short-lived branch for each bounded change.
- Open a pull request to `main`.
- Keep PRs focused on one coherent program-level objective.
- Run repository validation before merge.
- Squash merge accepted PRs.
- Delete temporary branches after merge or supersession.

## Issue placement

Create an issue here only when acceptance genuinely spans Vincent and CIC Station or concerns program-level governance/integration. Otherwise use the owning product repository.

Cross-product issues should link their authoritative product issues/PRs rather than duplicating them.

## Documentation ownership

- Cross-product roadmap: `docs/PROGRAM_ROADMAP.md`
- Program status: `docs/STATUS.md`
- Program governance/authority: `docs/GOVERNANCE.md`
- Program-level consequential decisions: `docs/decisions/`

Do not add product-specific requirements, product source code, product release notes, or duplicate product roadmaps here.

## Security

Never commit raw credentials, secrets, private keys, authentication caches, production data, private fleet state, or protected deployment configuration. See `SECURITY.md`.
