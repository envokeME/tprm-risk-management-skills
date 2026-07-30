# Contributing

Contributions should make TPRM decisions more traceable, proportionate, and
reproducible.

## Change requirements

- Give each skill one clear lifecycle decision and one primary output.
- Keep `SKILL.md` under 500 lines and use imperative instructions.
- Keep only `name` and `description` in its YAML frontmatter.
- Cite public primary sources for material method changes.
- Distinguish guidance from legal, regulatory, contractual, and policy
  requirements.
- Never include confidential vendor records, personal data, credentials, or
  proprietary reports in examples.
- Include a copy-ready Markdown template and at least one evaluation case.
- Preserve human approval for risk acceptance and legal conclusions.

## Validate

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

Pull requests should explain the decision problem, the evidence for the change,
and any limits or assumptions.
