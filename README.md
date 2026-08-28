# VINCENT Program

`logrusbox/vincent-program` is the program-level coordination repository for the VINCENT product family maintained by Logrus Box.

It exists to hold only information that genuinely spans more than one product repository or governs the product family as a whole.

## Product repositories

- [`logrusbox/vincent`](https://github.com/logrusbox/vincent) — Vincent worker platform: installer, runtime, diagnostics, updates, provider adapters, worker-side protocols, tests, requirements, ADRs, product roadmap, issues, and releases.
- [`logrusbox/cic-station`](https://github.com/logrusbox/cic-station) — CIC Station control plane: service/API/database/UI, enrollment, authorization, fleet coordination, leases, operational policy, tests, requirements, ADRs, product roadmap, issues, and releases.

## This repository owns

- the canonical cross-product program roadmap;
- cross-product issues whose acceptance requires coordinated work in more than one product repository;
- program-level decisions that genuinely apply above both product repositories;
- integration milestones and cross-repository dependency/acceptance coordination;
- concise current program status and governance conventions.

## This repository does not own

Product-specific implementation work remains in the product repository that implements it. Do not duplicate Vincent or CIC Station requirements, bugs, feature issues, ADRs, source code, release notes, or product roadmaps here merely for visibility.

If an issue can be completed entirely in one product repository, it belongs there. Cross-product issues should link the authoritative product issues/PRs rather than copying them.

## Start here

1. [`docs/PROGRAM_ROADMAP.md`](docs/PROGRAM_ROADMAP.md)
2. [`docs/STATUS.md`](docs/STATUS.md)
3. [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md)
4. [`docs/decisions/README.md`](docs/decisions/README.md)
5. active issues in this repository

GitHub issues are the active program backlog. GitHub Projects is intentionally not used because the current automation tooling cannot maintain Projects v2 directly without creating a parallel manual planning burden.
