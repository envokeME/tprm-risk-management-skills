---
name: manage-tprm-renewal-exit
description: Reassess a third-party relationship for renewal or plan a controlled termination covering continuity, transition, access, integrations, records, data return and deletion, and residual dependencies. Use when approaching renewal, non-renewal, replacement, emergency termination, or service decommissioning.
---

# Manage TPRM Renewal and Exit

## Objective

Prevent automatic renewal on stale risk facts and prevent termination from
creating unmanaged operational, security, data, legal, or concentration risk.

## Required inputs

- Current scope, tier, decision, conditions, contract, and notice dates
- Monitoring history, incidents, performance, findings, and current evidence
- Business need, alternatives, transition time, dependencies, and recovery plan
- Data, access, integrations, assets, records, legal holds, and subprocessors

## Workflow

1. Select `Renewal reassessment`, `Planned exit`, or `Emergency exit`.
2. For renewal, compare current facts with the prior decision using
   `references/renewal-exit-rules.md`. Trigger re-scoping for material change.
3. Check conditions, overdue findings, assurance freshness, service/resilience
   performance, incidents, contract departures, concentration, and exit
   feasibility.
4. Recommend renew, conditional renew, defer, non-renew, or terminate; preserve
   authorized decision fields.
5. For exit, inventory data, access, identities, keys, integrations, assets,
   dependencies, records, and surviving obligations.
6. Sequence continuity, transition, access revocation, data return/deletion,
   evidence, financial/legal closure, and post-exit monitoring.
7. Define emergency compensating actions when notice or transition cannot be
   completed normally.
8. Copy `assets/renewal-or-exit-record.md` and complete the applicable sections.

## NIST alignment

Use `references/nist-alignment.md` for NIST CSF 2.0 `GV.SC-07` and `GV.SC-10`,
supported by NIST SP 800-161 Rev. 1 lifecycle and disposal guidance.

## Boundaries

- Do not auto-renew because replacement is difficult or a deadline is near.
- Do not fabricate completion, deletion, access revocation, evidence, or
  approval.
- Do not destroy records subject to contract, law, investigation, or legal hold.
- Route legal notice, retention, dispute, and termination rights to counsel.
- Keep renewal, risk acceptance, and termination authority with an authorized human decision-maker.

## Quality check

Confirm the recommendation uses current evidence and the exit plan leaves no
unowned access, integration, data copy, dependency, record, or open obligation.
