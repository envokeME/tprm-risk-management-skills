# Due-diligence planning rules

## Evidence hierarchy

Prefer, in order where appropriate:

1. Direct scoped evidence: test result, configuration extract, exercise result,
   architecture or data-flow record.
2. Independent assurance: relevant SOC report, certification with scope,
   independent assessment, financial audit.
3. Controlled demonstration or interview with corroboration.
4. Policy, procedure, contract commitment, or questionnaire response.

The hierarchy is contextual: a policy can prove design but not operation.

## Common trigger-to-evidence mapping

| Trigger | Decision question | Candidate evidence |
|---|---|---|
| Sensitive data | Is collection, use, protection, retention, and deletion adequate? | Data flow, privacy schedule, control evidence, deletion method |
| Privileged access | Is access constrained and monitored? | Architecture, role model, MFA/PAM evidence, access review |
| Critical service | Can required recovery be achieved? | BIA, BCP/DR plan, recent exercise results, dependency map |
| Hosted software | Are vulnerabilities and changes managed? | Secure SDLC summary, scan/pen-test summary, remediation status |
| Material subprocessors | Are dependencies known and governed? | Subprocessor list, locations, flow-down requirements, monitoring |
| Financial dependency | Can the provider remain viable? | Financial statements, credit information, contingency options |

For SOC reports, plan to review scope, type, period, exceptions, complementary
user-entity controls, and subservice organization treatment. For ISO
certificates, review service and location scope, dates, issuer, and relevant
Statement of Applicability when available.

## Freshness

Set freshness from volatility and risk, not a universal number. Define
acceptable bridge evidence for period gaps. Require event-driven refresh when
material facts change.
