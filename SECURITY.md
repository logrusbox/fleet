# Security Policy

## Scope

This repository contains program-level planning and documentation only. It must not contain operational fleet state, reusable credentials, private keys, authentication caches, production secrets, or protected deployment configuration.

Security defects in Vincent belong in `logrusbox/vincent`. Security defects in CIC Station belong in `logrusbox/cic-station`. Cross-product security concerns that require coordinated changes in both products may be tracked here with links to the authoritative product issues.

## Reporting

Do not place exploitable secret material or sensitive production details in public issues. Use GitHub's private vulnerability reporting/security mechanisms for the affected product repository when appropriate.

Any credential that is accidentally committed must be treated as compromised and rotated; deleting the file alone is insufficient because Git retains history.
