# Workstream: Task Routing and Leases

## Current direction

Fleet distinguishes durable work items from worker selection/assignment, execution attempts, leases, and results. These concepts must not collapse into a single task row or Git branch convention.

The first managed-worker proof precedes multi-worker lease coordination.

Later multi-worker acceptance must cover:

- persistent lease ownership;
- liveness/grace behavior;
- replacement/reassignment;
- lease-generation or equivalent stale-result fencing;
- restart and recovery behavior;
- explicit clock/skew semantics before lease behavior hardens.

## Authority

CIC Station owns the live task/attempt/lease/result operational model. Fleet owns cross-component acceptance. Git owns accepted project artifacts and development truth, not live leases or heartbeats.

## Current gate

CIC Station issue #25 must resolve the work-item/assignment/attempt/lease/result relationships before the 0.1.0 schema becomes difficult to change.