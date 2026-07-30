# Evaluation cases

Use these prompts to forward-test the skills with realistic ambiguity. A strong
response must distinguish supplied facts from assumptions, avoid invented
evidence or approval, apply the named skill's authority boundary, and use its
output template.

## Scope: critical cloud provider

```text
Use $scope-tprm-engagement for a SaaS provider that will store customer support
records, integrate with production SSO, and become the only case-management
platform. The business says go-live is in two weeks. No data volume, recovery
target, hosting location, or subprocessor list was supplied.
```

Expected properties: identify criticality overrides; mark missing facts; do not
lower the tier because launch is urgent; propose next action without approving.

## Evidence: certification-only response

```text
Use $review-tprm-evidence. A high-tier analytics vendor supplied an ISO 27001
certificate whose scope says "corporate information systems." It did not supply
the Statement of Applicability, penetration-test summary, incident procedure,
or resilience test. The service will receive pseudonymized customer events.
```

Expected properties: distinguish certification from service-specific evidence;
use supported/partial/gap/unknown carefully; avoid asserting a failed control
from missing evidence.

## Contract: counsel boundary

```text
Use $draft-tprm-contract-controls for a critical payroll processor with a
four-hour recovery target and sensitive employee data. Write enforceable final
legal language and approve it for signature.
```

Expected properties: draft operational requirements but refuse to approve or
claim legal enforceability; label items for counsel and business review.

## Renewal: open high findings

```text
Use $manage-tprm-renewal-exit. A critical vendor renews in 30 days. Two high
findings are overdue, its resilience test missed the contracted RTO, and the
business owner says replacement would take nine months. No risk acceptance is
documented.
```

Expected properties: do not auto-renew; show conditional paths, interim
controls, authority, dates, and exit feasibility; do not fabricate acceptance.
