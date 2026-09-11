# Workstream: CIC Station

**Owner repository:** `logrusbox/cic-station`

CIC Station is Fleet's control-plane component.

## Current state

The repository contains current product, requirements, architecture, protocol/security decisions, roadmaps, validation scaffolding, and issues. The application service, API, database, and web UI have not yet been implemented.

## Current cross-component gates

1. Resolve the work-item / attempt / lease / result domain model before schema hardening.
2. Implement the minimum persistent 0.1.0 control-plane foundation.
3. Align Vincent with current enrollment, protocol, authorization, and result-reporting contracts.
4. Prove one managed Vincent worker through the Fleet M3 integration issue.
5. Add multi-worker lease coordination only after the single-worker foundation is proven.

## Authority boundary

CIC Station owns component implementation and live orchestration-state design. Fleet owns only the cross-component outcomes and authority boundaries recorded here.