# Workstream: Vincent

**Owner repository:** `logrusbox/vincent`

Vincent is Fleet's managed worker platform and must also remain useful when it is not enrolled in CIC Station.

## Current state

- Installer/runtime code exists.
- Physical validation of the current build-0023 path remains pending.
- The standalone READY lifecycle and offline-first payload path still have open work.
- Provider-neutral execution, managed authorization, bounded execution, and separation of worker/runtime credentials remain pre-1.0 gates.

## Current cross-component gates

1. Complete exact-main physical installer/runtime validation.
2. Prove useful bounded standalone work.
3. Align the worker with current CIC Station enrollment and protocol contracts.
4. Prove the first managed-worker path under Fleet M3.

## Authority boundary

Installer, runtime, networking, diagnostics, update, provider-adapter, and physical-test details remain authoritative in `logrusbox/vincent`. This file records only Fleet-visible integration state.

## September 25 implementation update

Offline payload/local READY, bounded provider invocation, publication recovery,
repository grant enforcement, reviewed local provider installation and independent
runtime/installer provenance are implemented with automated tests. Physical
acceptance, task credential isolation and authenticated CIC integration remain
open. Component `docs/STATUS.md` is the detailed evidence authority.
