# Git / CIC Station Authority Boundary

Fleet intentionally separates durable development/project truth from live operational orchestration state.

## Git authority

Git is authoritative for accepted source, committed documentation, requirements, ADRs, integration history, releases, and project artifacts that are designed to live in repositories.

A Git commit may be referenced by CIC Station as provenance, but Git is not the live control-plane database.

## CIC Station authority

CIC Station is authoritative for managed operational state once implemented, including enrollment/authorization, worker identity bindings, health/liveness observations, work/attempt/result/audit records within its domain, leases, reassignment, and managed operational policy.

## Vincent authority

Vincent is authoritative for its local worker implementation and local runtime facts it produces. In managed mode it reports those facts through the versioned Fleet worker protocol and obeys only currently valid, scoped CIC Station authority.

Vincent must still have a standalone READY lifecycle without CIC enrollment.

## Codex / agent runtime boundary

Codex is an execution runtime, not a project/control-plane authority. It receives bounded work through the Vincent provider/runtime adapter boundary and produces results/evidence. Provider-specific credentials and state do not become CIC worker identity or ordinary project/Git state.

## Provenance chain

Where Git is the project authority, Fleet should preserve a traceable relationship among:

```text
CIC work item
  -> execution attempt
  -> worker / lease generation
  -> agent-runtime execution
  -> result/report
  -> durable project artifact / commit / PR evidence
```

The exact schema is owned by CIC Station and component protocol decisions. This document defines only the cross-component authority boundary.

## Failure rule

If Git and CIC disagree, first determine whether the disagreement concerns durable project truth or live operational state. Do not resolve the conflict by forcing one system to own the other's domain.

Stale operational results must not overwrite newer accepted project state, and stale Git metadata must not be treated as a valid current lease or heartbeat.