# Skill Creator Axioms

## AX-SKILL-SKILL-CREATOR-001: Canonical Source First

Always create or update `.agentic/skills/<skill>/` files before creating the `.claude/skills/<skill>/SKILL.md` adapter. The `.agentic/` layer is the source of truth.

## AX-SKILL-SKILL-CREATOR-002: Adapter Is Thin

The Claude Code adapter SKILL.md should be a thin pointer that references canonical `.agentic/` files. Never duplicate skill logic, workflows, or templates in the adapter.

## AX-SKILL-SKILL-CREATOR-003: Every Skill Has Four Files

Every skill folder must contain:
- `skill.md` — the workflow and procedure
- `axioms.md` — skill-specific axioms
- `checklist.md` — verification checklist
- `output.md` — expected output format

## AX-SKILL-SKILL-CREATOR-004: Route Registration

Every new skill should be offered for registration in `.agentic/router/routes.yaml`. Do not register without user confirmation.

## AX-SKILL-SKILL-CREATOR-005: Validate After Creation

After creating or modifying a skill, always offer to run validation:
- `python scripts/validate_template.py`
- `python -m pytest`
