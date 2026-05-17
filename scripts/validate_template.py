#!/usr/bin/env python3
"""Validate the agent-doctrine template structure and consistency."""

import os
import sys
import yaml
from pathlib import Path


TEMPLATE_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_ROUTES = []

REQUIRED_ROUTE_KEYS = [
    "description",
    "triggers",
    "negative_triggers",
    "priority",
    "intent",
    "axiom_stack",
    "skill",
    "required_context",
    "allowed_tools",
    "disallowed_tools",
    "verification",
    "output_contract",
    "guardrails",
    "doctrine_update",
]


def check(condition: bool, message: str) -> bool:
    """Check a condition and print result. Returns True if passed."""
    if condition:
        print(f"  PASS: {message}")
    else:
        print(f"  FAIL: {message}")
    return condition


def validate_routes_yaml() -> bool:
    """Validate .agentic/router/routes.yaml."""
    print("\n=== Validating routes.yaml ===")
    routes_path = TEMPLATE_ROOT / ".agentic" / "router" / "routes.yaml"
    all_ok = True

    if not routes_path.exists():
        all_ok = check(False, "routes.yaml exists")
        return all_ok
    all_ok &= check(True, "routes.yaml exists")

    with open(routes_path) as f:
        data = yaml.safe_load(f)

    all_ok &= check(data is not None, "routes.yaml parses as valid YAML")
    if data is None:
        return all_ok

    all_ok &= check("routes" in data, "routes key exists")
    all_ok &= check("defaults" in data, "defaults key exists")

    routes = data.get("routes", {})

    # Check required routes
    for route_name in REQUIRED_ROUTES:
        all_ok &= check(route_name in routes, f"route '{route_name}' exists")

    # Check each route
    for route_name, route in routes.items():
        print(f"  Route: {route_name}")
        for key in REQUIRED_ROUTE_KEYS:
            all_ok &= check(key in route, f"  has '{key}'")

        # Check axiom_stack files exist
        axiom_stack = route.get("axiom_stack", [])
        for axiom_path in axiom_stack:
            full_path = TEMPLATE_ROOT / axiom_path
            all_ok &= check(full_path.exists(), f"  axiom file exists: {axiom_path}")

        # Check skill file exists
        skill_path = route.get("skill", "")
        if skill_path:
            full_path = TEMPLATE_ROOT / skill_path
            all_ok &= check(full_path.exists(), f"  skill file exists: {skill_path}")

        # Check output_contract file exists
        output_contract = route.get("output_contract", "")
        if output_contract:
            full_path = TEMPLATE_ROOT / output_contract
            all_ok &= check(full_path.exists(), f"  output_contract exists: {output_contract}")

        # Check guardrails files exist
        guardrails = route.get("guardrails", [])
        for g in guardrails:
            full_path = TEMPLATE_ROOT / g
            all_ok &= check(full_path.exists(), f"  guardrail file exists: {g}")

        # Check triggers is non-empty
        triggers = route.get("triggers", [])
        all_ok &= check(len(triggers) > 0, f"  triggers is non-empty")

        # Check negative_triggers is a list
        negative = route.get("negative_triggers", [])
        all_ok &= check(isinstance(negative, list), f"  negative_triggers is a list")

    return all_ok


def validate_claude_skills() -> bool:
    """Validate .claude/skills/*/SKILL.md files."""
    print("\n=== Validating .claude/skills/ ===")
    skills_dir = TEMPLATE_ROOT / ".claude" / "skills"
    all_ok = True

    if not skills_dir.exists():
        all_ok = check(False, ".claude/skills/ directory exists")
        return all_ok

    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            all_ok = check(False, f"{skill_dir.name}/SKILL.md exists")
            continue

        all_ok &= check(True, f"{skill_dir.name}/SKILL.md exists")

        content = skill_md.read_text()

        # Check for YAML frontmatter
        has_frontmatter = content.startswith("---")
        all_ok &= check(has_frontmatter, f"  {skill_dir.name}: has YAML frontmatter")

        if has_frontmatter:
            # Extract frontmatter
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = yaml.safe_load(parts[1])
                all_ok &= check("name" in fm, f"  {skill_dir.name}: has 'name' field")
                all_ok &= check("description" in fm, f"  {skill_dir.name}: has 'description' field")

        # Check that adapter references .agentic/ files
        agentic_refs = ".agentic/" in content
        all_ok &= check(agentic_refs, f"  {skill_dir.name}: references .agentic/ canonical files")

    return all_ok


def main():
    print("AI Context Infrastructure Validator")
    print(f"Template root: {TEMPLATE_ROOT}")

    results = []
    results.append(("routes.yaml", validate_routes_yaml()))
    results.append(("claude skills", validate_claude_skills()))

    print("\n=== Summary ===")
    passed = all(r[1] for r in results)
    for name, ok in results:
        status = "PASS" if ok else "FAIL"
        print(f"  {status}: {name}")

    if passed:
        print("\nAll validations passed.")
        return 0
    else:
        print("\nSome validations failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
