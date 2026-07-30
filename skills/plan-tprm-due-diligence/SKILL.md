---
name: plan-tprm-due-diligence
description: Build a risk-based third-party due-diligence plan that maps inherent exposures to decision-relevant evidence, reviewers, and completion criteria. Use when planning onboarding, renewal, material-change, or issue-driven diligence after the engagement has been scoped.
---

# Plan TPRM Due Diligence

## Objective

Request the smallest set of current, relevant evidence needed to test the risks
and reach a decision. Avoid one-size-fits-all questionnaires and uncontrolled
collection of sensitive reports.

## Required inputs

- Intake record, inherent-risk tier, material services, and criticality
- Applicable policy, legal, regulatory, customer, and contract requirements
- Known architecture, data flows, dependencies, and prior findings
- Decision deadline, reviewers, evidence channels, and data-handling limits

If scoping is absent, pause and route to `$scope-tprm-engagement`.

## Workflow

1. Translate each material inherent exposure into one or more review questions.
2. Select evidence using `references/diligence-planning-rules.md`; prefer direct,
   current, scoped evidence over broad attestations.
3. Mark every request `Required`, `Conditional`, or `Optional`, and explain its
   decision use. Remove requests with no decision use.
4. Define acceptable alternatives, period, scope, freshness, reviewer, and
   completion criteria before sending the request.
5. Include business, financial, legal, privacy, security, resilience,
   concentration, and fourth-party workstreams only when triggered.
6. Define secure submission, access, retention, and deletion handling for
   sensitive vendor material.
7. Sequence blockers first and identify deadline risk. Do not waive work merely
   because procurement is urgent.
8. Copy `assets/due-diligence-plan.md` and complete the plan.

## NIST alignment

Use `references/nist-alignment.md` for the informative mapping to NIST CSF 2.0
`GV.SC-05`, `GV.SC-06`, and `GV.SC-07`, with NIST SP 800-161 Rev. 1 supporting
risk-based supplier assessment and requirements.

## Output contract

Produce a traceable matrix from risk driver to review question, requested
evidence, acceptable alternative, reviewer, timing, and completion test. Include
open dependencies, escalation triggers, and explicitly excluded workstreams.

## Boundaries

- Do not review evidence, rate control effectiveness, or approve risk here.
- Do not fabricate requirements, vendor capabilities, evidence, or approval.
- Do not request full sensitive reports when a scoped summary or supervised
  review will answer the question.
- Route legal interpretations and compelled contract terms to counsel.
- Keep waivers and risk acceptance with an authorized human.

## Quality check

Confirm every request maps to a material risk or applicable requirement, every
material risk has a review path, and the plan is proportionate to criticality.
