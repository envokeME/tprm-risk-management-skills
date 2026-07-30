---
name: scope-tprm-engagement
description: Scope a proposed third-party relationship, identify criticality, and assign a traceable inherent-risk tier before considering vendor controls. Use when onboarding, materially changing, or reclassifying a vendor, service provider, affiliate, contractor, or fourth-party-dependent service.
---

# Scope TPRM Engagement

## Objective

Convert intake facts into a reviewable engagement profile and proportionate
inherent-risk tier. Assess exposure before crediting certifications, contract
terms, or vendor controls.

## Required inputs

- Service, business purpose, owner, users, and lifecycle event
- Data categories, volumes, locations, retention, and processing role
- Access type, privilege, connectivity, hosting, and integration
- Business dependency, substitutability, recovery needs, and customer impact
- Countries, regulated activities, subcontractors, and known concentration
- Organization-specific tier definitions and override rules, when available

Proceed with incomplete inputs only by marking each missing item `UNKNOWN` and
showing how it could change the result.

## Workflow

1. Define the assessment unit: legal entity, service, use case, data flow, and
   lifecycle event. Split materially different services or use cases.
2. Separate supplied facts, externally verified facts, assumptions, and
   unknowns. Do not fabricate vendor facts or infer controls from reputation.
3. Rate the inherent exposure dimensions in
   `references/inherent-risk-method.md`.
4. Apply criticality and mandatory-tier overrides before any averaging.
5. Assign a provisional tier using organization policy. If policy is absent,
   use the sample four-tier model only as a clearly labeled proposal.
6. Explain the drivers, confidence, missing facts, and any plausible alternate
   tier.
7. Route to due diligence, expedited triage, enhanced review, or a documented
   low-risk path. Urgency never lowers risk.
8. Copy `assets/tprm-intake-and-tier.md` and complete every field.

## NIST alignment

Use `references/nist-alignment.md` to relate the output to NIST CSF 2.0
`GV.SC-04`, `GV.SC-06`, and `ID.RA-05`, supported by NIST SP 800-161 Rev. 1.
Treat the mapping as informative, not evidence of conformity.

## Output contract

Produce:

- assessment scope and lifecycle event;
- fact/assumption/unknown register;
- inherent-risk dimension table;
- criticality and concentration analysis;
- provisional tier, rationale, confidence, and policy basis;
- required next review and accountable owner.

## Boundaries

- Do not assess residual risk or approve the relationship in this skill.
- Do not fabricate facts, evidence, legal requirements, or approval.
- Do not treat a certificate, questionnaire answer, or contract promise as an
  inherent-risk reducer.
- Keep risk acceptance and final tier exceptions with an authorized human.
- Minimize sensitive information in the output and link to controlled records
  instead of reproducing them.

## Quality check

Confirm that another reviewer can reproduce the tier from the recorded facts,
that overrides were applied visibly, and that unknowns were not scored as
favorable.
