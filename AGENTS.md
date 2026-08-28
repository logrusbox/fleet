# VINCENT Program Agent Instructions

These instructions apply to work in `logrusbox/vincent-program`.

## Start order

Before consequential program work, read:

1. `README.md`
2. `docs/PROGRAM_ROADMAP.md`
3. `docs/STATUS.md`
4. `docs/GOVERNANCE.md`
5. `docs/decisions/README.md`
6. relevant active issues/PRs in all affected repositories

Then inspect the current authoritative state of `logrusbox/vincent` and/or `logrusbox/cic-station` as needed.

## Authority boundary

- This repository owns cross-product program planning and integration only.
- Vincent-specific requirements, ADRs, issues, implementation, tests, releases, and roadmap belong in `logrusbox/vincent`.
- CIC Station-specific requirements, ADRs, issues, implementation, tests, releases, and roadmap belong in `logrusbox/cic-station`.
- Do not duplicate product issues here merely for visibility.
- If a cross-product issue requires product work, link the authoritative product issue/PR from the program issue.
- GitHub Projects v2 is intentionally not required.

## Workflow

- `main` is the only permanent branch.
- Use short-lived branches and PRs for normal changes after initial bootstrap.
- Squash merge accepted PRs.
- Delete temporary merged/superseded branches after useful work is preserved.
- Keep program documents concise and derived from current product-repository authority rather than copying product documentation wholesale.

## Safety

- Never commit credentials, private keys, tokens, authentication caches, private fleet data, production configuration, or private operational data.
- Do not use this repository as a live fleet database, task execution system, or secret transport.
- Consequential product architecture belongs in the owning product ADRs unless the decision genuinely spans both products.
