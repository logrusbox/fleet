# VINCENT Program Status

**Updated:** 2026-08-28

## Repository structure

The VINCENT product family is now organized under the Logrus Box GitHub organization:

- `logrusbox/vincent` — Vincent worker product.
- `logrusbox/cic-station` — CIC Station control-plane product.
- `logrusbox/vincent-program` — cross-product planning, integration, and program governance only.

The former organization-level GitHub Project was intentionally abandoned because the connected automation could not maintain Projects v2 state directly. Active planning now uses normal GitHub issues, PRs, labels, milestones, and repository Markdown that can be maintained through the same automation surface used for development.

## Current program state

- M0 governance/documentation structure is complete in the product repositories and is being consolidated into this program repository for cross-product ownership.
- Vincent remains the current physical/operational gate: installer/runtime verification and standalone READY/bounded-work proof are prerequisites for the first managed-worker proof.
- CIC Station implementation may proceed within its accepted product/security/protocol boundaries while avoiding schema decisions that depend on unresolved domain-model work.
- The first managed-worker integration remains a later program gate after Vincent proves standalone operation.

## Immediate coordination priorities

1. Finish this repository bootstrap and move canonical cross-product roadmap ownership here.
2. Reconcile Vincent and CIC Station documentation so neither product repository claims ownership of the overall program roadmap.
3. Move only genuinely cross-product open issues here; leave product-specific work where it is.
4. Keep product-specific releases/milestones in the product repositories.
5. Complete repository protection/settings where GitHub UI intervention is required.

## Known configuration limitation

The connected GitHub automation can manage repository contents, issues, PRs, branches, and Actions, but cannot currently create repository rulesets, change merge-method settings, create milestones/labels directly, or manage GitHub Projects v2. Those settings remain explicit GitHub UI tasks when needed.
