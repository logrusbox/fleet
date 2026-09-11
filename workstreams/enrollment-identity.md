# Workstream: Enrollment and Identity

## Current direction

Fleet uses explicit, operator-approved enrollment between CIC Station and Vincent.

The accepted baseline includes:

- a worker-generated asymmetric installation identity;
- bootstrap authorization supplied by CIC Station;
- Vincent-initiated connection to the intended CIC Station endpoint;
- operator approval bound to the exact worker public identity;
- proof-of-possession for later connections;
- replay-resistant bootstrap behavior;
- explicit rotation, revocation, and recovery transitions;
- fail-closed CIC Station server-trust verification.

Public Internet access is not a prerequisite when CIC Station and Vincent have a mutually reachable private-network path.

## Authority boundary

CIC Station owns managed enrollment/authorization state. Vincent owns its local installation identity implementation. Fleet owns the cross-component expectation that enrollment is explicit, scoped, revocable, recoverable, and independent from Git/model-provider/human credentials.

## Current gate

Vincent implementation must align with the accepted CIC Station trust and protocol model before the first managed-worker Fleet proof.