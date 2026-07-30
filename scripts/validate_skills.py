"""Validate the structure and safety contract of every TPRM skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDERS = ("TODO", "[TODO", "TBD", "Lorem ipsum")
REQUIRED_BOUNDARIES = ("Do not fabricate", "authorized human")
MOJIBAKE = ("\u00e2\u20ac", "\u00c3", "\ufffd")
CSF_PATTERN = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")
NIST_MAPPINGS = {
    "scope-tprm-engagement": {"GV.SC-04", "GV.SC-06", "ID.RA-05"},
    "plan-tprm-due-diligence": {"GV.SC-05", "GV.SC-06", "GV.SC-07"},
    "review-tprm-evidence": {"GV.SC-06", "GV.SC-07", "GV.SC-09"},
    "assess-tprm-risk": {"GV.SC-03", "GV.SC-07", "GV.RM-06", "ID.RA-05"},
    "draft-tprm-contract-controls": {"GV.SC-05", "GV.SC-08", "GV.SC-10"},
    "monitor-tprm-third-parties": {"GV.SC-07", "GV.SC-08", "GV.SC-09"},
    "manage-tprm-renewal-exit": {"GV.SC-07", "GV.SC-10"},
    "govern-tprm-program": {
        "GV.SC-01",
        "GV.SC-02",
        "GV.SC-03",
        "GV.SC-04",
        "GV.SC-09",
        "GV.RR-02",
        "GV.OV-03",
    },
}
SKILL_BOUNDARIES = {
    "scope-tprm-engagement": ("Do not assess residual risk",),
    "review-tprm-evidence": (
        "Missing evidence is normally `UNKNOWN`",
        "Do not assign residual risk",
    ),
    "assess-tprm-risk": (
        "Leave approval fields unsigned",
        "Do not present the recommendation as an approval",
    ),
    "draft-tprm-contract-controls": (
        "Do not provide legal advice",
        "Do not provide legal advice, approve a contract",
    ),
    "manage-tprm-renewal-exit": ("Do not auto-renew",),
    "govern-tprm-program": (
        "Do not claim program effectiveness from document design alone",
    ),
}


def read_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening YAML frontmatter delimiter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing closing YAML frontmatter delimiter")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError("YAML frontmatter must be a mapping")
    return data, text[end + 5 :]


def read_readme_mapping(skill_name: str) -> set[str]:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    match = re.search(
        rf"^\|\s*`{re.escape(skill_name)}`\s*\|([^|]+)\|$", text, re.MULTILINE
    )
    if not match:
        return set()
    return set(CSF_PATTERN.findall(match.group(1)))


def validate_skill(directory: Path) -> list[str]:
    errors: list[str] = []
    skill_file = directory / "SKILL.md"
    agent_file = directory / "agents" / "openai.yaml"
    nist_file = directory / "references" / "nist-alignment.md"

    if not skill_file.is_file():
        return [f"{directory.name}: missing SKILL.md"]
    if not agent_file.is_file():
        errors.append(f"{directory.name}: missing agents/openai.yaml")
        return errors
    if not nist_file.is_file():
        errors.append(f"{directory.name}: missing references/nist-alignment.md")
        return errors

    try:
        frontmatter, body = read_frontmatter(skill_file)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [f"{directory.name}: invalid SKILL.md: {exc}"]

    if set(frontmatter) != {"name", "description"}:
        errors.append(
            f"{directory.name}: frontmatter must contain only name and description"
        )
    if frontmatter.get("name") != directory.name:
        errors.append(f"{directory.name}: frontmatter name must match directory")
    if not NAME_PATTERN.fullmatch(str(frontmatter.get("name", ""))):
        errors.append(f"{directory.name}: invalid lowercase hyphenated name")
    description = str(frontmatter.get("description", ""))
    if len(description) < 80 or "Use when" not in description:
        errors.append(
            f"{directory.name}: description must explain capability and 'Use when'"
        )
    if len(skill_file.read_text(encoding="utf-8").splitlines()) > 500:
        errors.append(f"{directory.name}: SKILL.md exceeds 500 lines")
    package_files = sorted(
        path
        for path in directory.rglob("*")
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}
    )
    package_text = "\n".join(path.read_text(encoding="utf-8") for path in package_files)
    normalized_package_text = re.sub(r"\s+", " ", package_text)
    for marker in PLACEHOLDERS:
        if marker.lower() in package_text.lower():
            errors.append(f"{directory.name}: unresolved placeholder {marker!r}")
    for marker in MOJIBAKE:
        if marker in package_text:
            errors.append(f"{directory.name}: possible mojibake marker {marker!r}")
    for boundary in REQUIRED_BOUNDARIES:
        if boundary.lower() not in body.lower():
            errors.append(f"{directory.name}: missing safety boundary {boundary!r}")
    for boundary in SKILL_BOUNDARIES.get(directory.name, ()):
        if boundary.lower() not in body.lower():
            errors.append(
                f"{directory.name}: missing skill-specific boundary {boundary!r}"
            )
    if not re.search(
        r"\bnot\b.{0,100}\bconformity\b", normalized_package_text, re.I
    ):
        errors.append(f"{directory.name}: missing non-conformity limitation")

    expected_nist = NIST_MAPPINGS.get(directory.name)
    if expected_nist is None:
        errors.append(f"{directory.name}: no approved NIST mapping in validator")
    else:
        skill_nist = set(CSF_PATTERN.findall(body))
        reference_nist = set(
            CSF_PATTERN.findall(nist_file.read_text(encoding="utf-8"))
        )
        readme_nist = read_readme_mapping(directory.name)
        for location, observed in (
            ("SKILL.md", skill_nist),
            ("references/nist-alignment.md", reference_nist),
            ("README.md", readme_nist),
        ):
            if observed != expected_nist:
                errors.append(
                    f"{directory.name}: {location} NIST mapping "
                    f"{sorted(observed)} != {sorted(expected_nist)}"
                )

    template_links = re.findall(r"`(assets/[^`]+\.md)`", body)
    if not template_links:
        errors.append(f"{directory.name}: SKILL.md must link to an asset template")
    for relative in template_links:
        if not (directory / relative).is_file():
            errors.append(f"{directory.name}: missing linked template {relative}")

    reference_links = re.findall(r"`(references/[^`]+\.md)`", body)
    if not reference_links:
        errors.append(f"{directory.name}: SKILL.md must link to decision rules")
    for relative in reference_links:
        if not (directory / relative).is_file():
            errors.append(f"{directory.name}: missing linked reference {relative}")

    try:
        agent = yaml.safe_load(agent_file.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{directory.name}: invalid agents/openai.yaml: {exc}")
        return errors
    interface = agent.get("interface", {})
    short = str(interface.get("short_description", ""))
    prompt = str(interface.get("default_prompt", ""))
    if not 25 <= len(short) <= 64:
        errors.append(f"{directory.name}: short_description must be 25-64 chars")
    if f"${directory.name}" not in prompt:
        errors.append(f"{directory.name}: default_prompt must name ${directory.name}")

    return errors


def main() -> int:
    if not SKILLS.is_dir():
        print("skills directory not found", file=sys.stderr)
        return 1
    directories = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    expected_directories = set(NIST_MAPPINGS)
    actual_directories = {path.name for path in directories}
    errors: list[str] = []
    if actual_directories != expected_directories:
        errors.append(
            "skills directory set differs from validator registry: "
            f"{sorted(actual_directories)} != {sorted(expected_directories)}"
        )
    errors.extend(error for path in directories for error in validate_skill(path))
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(directories)} TPRM skill packages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
