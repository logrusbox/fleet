# Workstream: CIC Station

**Owner repository:** `logrusbox/cic-station`

CIC Station is Fleet's control-plane component.

## Current state

The repository now includes the tested Fleet work domain (ADR-0021), exact Paperclip foundation pin, reproducible preparation and database-foundation checks. The operational service/API/database integration and web UI remain unimplemented.

## Current cross-component gates

1. Enforce the accepted work-item / attempt / lease / result model transactionally in the Paperclip adapter.
2. Implement the minimum persistent 0.1.0 control-plane foundation.
3. Align Vincent with current enrollment, protocol, authorization, and result-reporting contracts.
4. Prove one managed Vincent worker through the Fleet M3 integration issue.
5. Add multi-worker lease coordination only after the single-worker foundation is proven.

## Authority boundary

CIC Station owns component implementation and live orchestration-state design. Fleet owns only the cross-component outcomes and authority boundaries recorded here.