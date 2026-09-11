# Fleet Documentation Index

The top-level project spine is the primary re-entry path:

1. [`../PROJECT.md`](../PROJECT.md)
2. [`../CURRENT_STATE.md`](../CURRENT_STATE.md)
3. [`../DECISIONS.md`](../DECISIONS.md)
4. [`../REPOSITORIES.md`](../REPOSITORIES.md)

Additional Fleet-wide documentation:

- [`PROGRAM_ROADMAP.md`](PROGRAM_ROADMAP.md) — canonical M0-M8 cross-component roadmap.
- [`GOVERNANCE.md`](GOVERNANCE.md) — repository/planning governance.
- [`decisions/`](decisions/) — consequential Fleet ADRs.
- [`interfaces/AUTHORITY_BOUNDARY.md`](interfaces/AUTHORITY_BOUNDARY.md) — Git/CIC/Vincent/Codex authority separation.
- [`history/CHAT_RECONCILIATION.md`](history/CHAT_RECONCILIATION.md) — temporal precedence for retiring chat history.
- [`evaluations/`](evaluations/) — future/historical concepts that are not current authority.
- [`../workstreams/`](../workstreams/) — concise cross-component workstream state.
- [`../handoffs/`](../handoffs/) — active scoped handoffs only.

Component implementation documentation remains authoritative in:

- `logrusbox/vincent`
- `logrusbox/cic-station`

Do not duplicate component requirements, implementation detail, or transient status in Fleet merely for visibility.