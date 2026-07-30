---
name: monitor-tprm-third-parties
description: Design tier-based periodic and event-driven monitoring for third-party risk, control evidence, service performance, incidents, changes, findings, concentration, and escalation. Use when onboarding an approved relationship, refreshing monitoring, responding to change, or improving ongoing oversight.
---

# Monitor TPRM Third Parties

## Objective

Detect changes that could invalidate the risk decision and route them to a
defined response before renewal or harm.

## Required inputs

- Approved scope, tier, residual risks, conditions, and risk owner
- Contract obligations, service levels, RTO/RPO, and evidence commitments
- Open findings, exceptions, review dates, dependencies, and exit triggers
- Available monitoring sources and organization escalation policy

## Workflow

1. Define the conditions that must remain true for the decision to remain valid.
2. Select periodic and event-driven indicators using
   `references/monitoring-rules.md`.
3. Set frequency from criticality, volatility, exposure, and contract—not a
   universal annual cycle.
4. Define source, owner, threshold, confidence, response time, escalation,
   evidence retention, and closure test for every signal.
5. Include incidents and recovery exercises with relevant critical suppliers.
6. Track findings, accepted risks, evidence expiry, service performance,
   financial/ownership change, data or architecture change, fourth parties, and
   concentration where triggered.
7. Define which events cause targeted review, re-tiering, full reassessment,
   suspension, incident action, or exit-plan activation.
8. Copy `assets/third-party-monitoring-plan.md` and complete it.

## NIST alignment

Use `references/nist-alignment.md` for NIST CSF 2.0 `GV.SC-07`, `GV.SC-08`, and
`GV.SC-09`, supported by NIST SP 800-161 Rev. 1 lifecycle monitoring.

## Boundaries

- Do not promise continuous monitoring when data is periodic or unavailable.
- Do not fabricate events, evidence, performance, thresholds, or approval.
- Do not silently close an alert because a vendor disputes it; record evidence
  and disposition.
- Respect lawful, contractual, privacy, and licensed-data limits.
- Keep risk acceptance and consequential action with an authorized human.

## Quality check

Confirm each material decision condition has a signal, thresholds have owners
and actions, stale evidence cannot pass unnoticed, and exit triggers are usable.
