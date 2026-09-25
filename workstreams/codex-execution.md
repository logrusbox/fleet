# Workstream: Codex Execution

Codex is Fleet's first supported agent runtime, not a separate Fleet product component.

## Current direction

- Vincent launches/supervises agent execution through a provider-neutral boundary.
- Fleet's first complete foundation proof uses Codex.
- Codex-specific behavior must not become the permanent CIC or Vincent domain model.
- Provider credentials remain separate from worker identity, operator identity, and ordinary project state.

## Acceptance direction

The initial path must demonstrate bounded work, interruption/failure handling, durable result reporting, and project provenance without requiring CIC Station or Vincent to become Codex-specific internally.

## Authority

Concrete runtime implementation belongs in `logrusbox/vincent`. Cross-component task/result contracts belong to the relevant Fleet/CIC/Vincent decisions.

## September 25 evidence

Vincent's supervisor now uses provider-neutral execution results with explicit
deadlines/cancellation. Optional Codex installation verifies reviewed local
artifacts before activation. No provider login or real model invocation was
performed. Full lifecycle abstraction and task/provider credential isolation
remain open component issues #38 and #48.
