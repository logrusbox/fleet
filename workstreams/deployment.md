# Workstream: Deployment and Recovery

## Current direction

Fleet must remain self-hostable and recoverable without a mandatory Logrus Box-operated rendezvous, registry, pairing, or relay service.

CIC Station is expected to support direct/private/tunneled connectivity modes as the product matures. Vincent workers must remain reconstructable and must not be the sole durable holder of accepted project truth.

## 1.0 acceptance direction

- repeatable CIC Station deployment and backup/restore;
- supported private-network operation;
- worker recovery/reinstall without losing durable project/control-plane truth;
- explicit operational-data and secret separation from public Git;
- destructive recovery proof for both worker and control plane before Fleet 1.0 acceptance.

## Authority

Concrete packaging/deployment mechanics belong in the owning component repositories. Fleet owns the cross-component recoverability and self-hosting requirements.

No specific local-development or production-host topology is made authoritative by this file unless current component Git records it.