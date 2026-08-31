# Fleet

`logrusbox/fleet` is the Fleet-level coordination repository for **Fleet**, a Logrus Box product for coordinating AI work across managed computers.

Fleet currently consists of two components:

- [`logrusbox/vincent`](https://github.com/logrusbox/vincent) — **Vincent**, the managed worker platform.
- [`logrusbox/cic-station`](https://github.com/logrusbox/cic-station) — **CIC Station**, the Command Information Center and central control plane.

The existing component names remain authoritative. Possible future names such as `fleet-worker` and `fleet-cic` are not adopted.

This repository holds only information that genuinely spans both component repositories or governs Fleet as a whole.

## This repository owns

- the canonical Fleet roadmap;
- cross-component issues whose acceptance requires coordinated work in more than one component repository;
- Fleet-level decisions that apply above both component repositories;
- integration milestones and cross-repository dependency/acceptance coordination;
- concise current Fleet status and governance conventions.

## This repository does not own

Component-specific implementation work remains in the repository that implements it. Do not duplicate Vincent or CIC Station requirements, bugs, feature issues, ADRs, source code, release notes, or component roadmaps here merely for visibility.

If an issue can be completed entirely in one component repository, it belongs there. Cross-component issues should link the authoritative component issues and pull requests rather than copying them.

## Start here

1. [`docs/PROGRAM_ROADMAP.md`](docs/PROGRAM_ROADMAP.md)
2. [`docs/STATUS.md`](docs/STATUS.md)
3. [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md)
4. [`docs/decisions/README.md`](docs/decisions/README.md)
5. Active issues in this repository

GitHub issues are the active Fleet backlog. GitHub Projects is intentionally not used because the current automation tooling cannot maintain Projects v2 directly without creating a parallel manual planning burden.
