---
name: skill-creator
description: Use when creating, updating, or registering agent skills, playbooks, checklists, or Claude Code skill adapters.
---

# Skill Creator

This is a Claude Code adapter. The canonical source of truth is at `.agentic/skills/skill-creator/skill.md`.

## Required Reading

Before executing, read these files in order:

1. `.agentic/router/routes.yaml` — routing context and route definition
2. `.agentic/skills/skill-creator/skill.md` — the full workflow
3. `.agentic/skills/skill-creator/axioms.md` — skill-specific axioms
4. `.agentic/skills/skill-creator/checklist.md` — verification checklist
5. `.agentic/skills/skill-creator/output.md` — expected output format
6. `.agentic/axioms/skills/skill-creator.md` — canonical axiom definitions
7. `.agentic/axioms/universal.md` — universal axioms

## Execution

Follow the workflow defined in `.agentic/skills/skill-creator/skill.md`. Do not deviate from the seven-step workflow.

## After Completion

- Verify using `.agentic/skills/skill-creator/checklist.md`
- Return output in the format defined by `.agentic/skills/skill-creator/output.md`
- Offer to run `python scripts/validate_template.py`
