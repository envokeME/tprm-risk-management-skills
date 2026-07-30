# TPRM Risk Management Skills

An open, Markdown-first library of reusable skills for third-party risk
management (TPRM). The repository turns a defensible TPRM lifecycle into eight
small skill packages that can be copied, reviewed, adapted, and run by people
or AI agents.

The skills are designed to produce decision records, not automatic decisions.
They keep facts, assumptions, evidence, gaps, and human approvals visibly
separate.

## Skill map

| Lifecycle decision | Skill | Primary output |
|---|---|---|
| What is the engagement and how risky is it before controls? | [`scope-tprm-engagement`](skills/scope-tprm-engagement/SKILL.md) | Intake and inherent-risk tier |
| What diligence is proportionate? | [`plan-tprm-due-diligence`](skills/plan-tprm-due-diligence/SKILL.md) | Evidence request and review plan |
| What does the submitted evidence support? | [`review-tprm-evidence`](skills/review-tprm-evidence/SKILL.md) | Evidence review and gaps |
| What risk remains and what should happen? | [`assess-tprm-risk`](skills/assess-tprm-risk/SKILL.md) | Residual-risk decision record |
| Which protections should be contractual? | [`draft-tprm-contract-controls`](skills/draft-tprm-contract-controls/SKILL.md) | Requirements schedule for counsel |
| How should the relationship be watched? | [`monitor-tprm-third-parties`](skills/monitor-tprm-third-parties/SKILL.md) | Monitoring and escalation plan |
| Should it renew, or how should it end? | [`manage-tprm-renewal-exit`](skills/manage-tprm-renewal-exit/SKILL.md) | Renewal or controlled-exit record |
| How should the overall program operate? | [`govern-tprm-program`](skills/govern-tprm-program/SKILL.md) | Governance, inventory, and metrics model |

Each skill includes an informative NIST CSF 2.0 crosswalk. The principal
outcomes are:

| Skill | NIST CSF 2.0 outcomes |
|---|---|
| `scope-tprm-engagement` | GV.SC-04, GV.SC-06, ID.RA-05 |
| `plan-tprm-due-diligence` | GV.SC-05, GV.SC-06, GV.SC-07 |
| `review-tprm-evidence` | GV.SC-06, GV.SC-07, GV.SC-09 |
| `assess-tprm-risk` | GV.SC-03, GV.SC-07, GV.RM-06, ID.RA-05 |
| `draft-tprm-contract-controls` | GV.SC-05, GV.SC-08, GV.SC-10 |
| `monitor-tprm-third-parties` | GV.SC-07, GV.SC-08, GV.SC-09 |
| `manage-tprm-renewal-exit` | GV.SC-07, GV.SC-10 |
| `govern-tprm-program` | GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, GV.SC-09, GV.RR-02, GV.OV-03 |

Mappings describe how an output can support an outcome. They do not mean that
using a skill, by itself, achieves or proves conformity.

## Use a skill

Each directory under `skills/` is self-contained:

- `SKILL.md` defines when the skill applies, its workflow, decision boundaries,
  and output contract.
- `references/` contains detailed decision rules.
- `assets/` contains a copy-ready Markdown output template.
- `agents/openai.yaml` supplies discoverable interface metadata.

Example prompt:

```text
Use $scope-tprm-engagement to assess this third-party intake and assign a
defensible inherent-risk tier. State missing facts instead of guessing.
```

To install one skill in a Codex skills directory:

```powershell
Copy-Item -Recurse skills\scope-tprm-engagement `
  $env:USERPROFILE\.codex\skills\scope-tprm-engagement
```

On macOS or Linux:

```bash
cp -R skills/scope-tprm-engagement \
  "${CODEX_HOME:-$HOME/.codex}/skills/scope-tprm-engagement"
```

Restart or reload the agent after copying. Adapt tier thresholds, approval
authorities, legal requirements, and evidence standards to the organization
before production use.

## Rebuild and validate

Requirements:

- Python 3.10 or newer
- PyYAML (development validation only)

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

Validation checks package structure, YAML frontmatter, agent metadata, template
links, required safety language, and placeholder text. GitHub Actions runs the
same validator on every push and pull request.

To add a skill:

1. Copy an existing skill directory or use a compatible skill initializer.
2. Keep only `name` and `description` in `SKILL.md` frontmatter.
3. Give the skill one lifecycle decision and one primary output.
4. Add decision rules, a Markdown template, and realistic evaluation prompts.
5. Run the validator and test the skill against incomplete and conflicting
   inputs.

## Design principles

- Apply diligence proportionate to risk and criticality.
- Separate inherent risk, control evidence, and residual risk.
- Treat missing evidence as unknown, not automatically as control failure.
- Trace material conclusions to supplied evidence or an explicit assumption.
- Keep approval, legal judgment, and risk acceptance with authorized humans.
- Use organization-defined thresholds; sample tiers are starting points only.
- Collect the minimum sensitive vendor information needed for the decision.
- Use NIST CSF 2.0 outcomes as a common vocabulary and NIST SP 800-161 Rev. 1
  as the supporting C-SCRM method where applicable.

## Sources and limitations

The methods are grounded in current public guidance from NIST, CISA, and the
U.S. federal banking agencies. See [`SOURCES.md`](SOURCES.md) for scope and
applicability. Banking guidance is included as a useful regulated overlay, not
as a universal requirement.

This repository is educational and operational guidance. It is not legal
advice, an audit opinion, certification, or a substitute for an organization's
policies, counsel, regulators, or authorized risk owners.

## License

MIT. See [`LICENSE`](LICENSE).
