---
name: draft-tprm-contract-controls
description: Translate documented third-party risks and operating requirements into a prioritized security, privacy, resilience, incident, subcontractor, and exit requirements schedule for counsel review. Use when preparing, negotiating, renewing, or amending a supplier agreement after risk requirements are known.
---

# Draft TPRM Contract Controls

## Objective

Turn risk decisions into measurable supplier obligations and customer
responsibilities without claiming legal enforceability or approving language.

## Required inputs

- Scoped service, data flow, tier, and criticality
- Evidence gaps, residual risks, treatment decisions, and required outcomes
- Standard clauses, negotiation positions, applicable law/policy, and counsel
- Business service levels, RTO/RPO, incident needs, and exit dependencies

## Workflow

1. Trace each proposed requirement to a risk, policy, law, customer commitment,
   or operational dependency.
2. Classify it `Must`, `Should`, or `Negotiable`; identify the authorized owner
   of any fallback.
3. Draft measurable outcomes using `references/contract-control-rules.md`.
4. Cover only triggered domains: data use and security, access, assurance and
   audit, incident notice and cooperation, vulnerabilities, resilience,
   subprocessors and flow-down, regulatory access, records, termination,
   deletion, and exit assistance.
5. Define evidence, notification window, remediation time, approval right,
   survival, and consequence where relevant.
6. Separate supplier obligations, customer responsibilities, and shared
   dependencies.
7. Mark legal, privacy, insurance, liability, and jurisdiction questions for
   counsel. Never state that draft text is enforceable.
8. Copy `assets/contract-requirements-schedule.md` and complete it.

## NIST alignment

Use `references/nist-alignment.md` for NIST CSF 2.0 `GV.SC-05`, `GV.SC-08`, and
`GV.SC-10`. NIST SP 1305 also supports using CSF outcomes and Target Profiles
to communicate supplier requirements.

## Boundaries

- Do not provide legal advice, approve a contract, or sign for any party.
- Do not fabricate legal requirements, negotiated positions, vendor facts,
  evidence, or approval.
- Do not copy proprietary clauses without permission.
- Preserve material unresolved departures in the risk decision record.
- Keep final legal judgment, fallback approval, and acceptance with counsel and
  an authorized human.

## Quality check

Confirm every material clause has a source, owner, measurable outcome, fallback,
and review route; eliminate vague obligations that cannot be tested.
