---
name: axiom-creator
description: Use when creating, updating, classifying, or registering axioms, principles, doctrine rules, or route axiom stacks.
---

# Axiom Creator

This is a Claude Code adapter. The canonical source of truth is at `.agentic/skills/axiom-creator/skill.md`.

## Required Reading

Before executing, read these files in order:

1. `.agentic/router/routes.yaml` — routing context and route definition
2. `.agentic/skills/axiom-creator/skill.md` — the full workflow
3. `.agentic/skills/axiom-creator/axioms.md` — skill-specific axioms
4. `.agentic/skills/axiom-creator/checklist.md` — verification checklist
5. `.agentic/skills/axiom-creator/output.md` — expected output format
6. `.agentic/axioms/skills/axiom-creator.md` — canonical axiom definitions
7. `.agentic/axioms/universal.md` — universal axioms

## Execution

Follow the workflow defined in `.agentic/skills/axiom-creator/skill.md`. Do not deviate from the nine-step workflow.

## Classification

The five axiom classifications are:
- universal → `.agentic/axioms/universal.md`
- domain-specific → `.agentic/axioms/domains/<domain>.md`
- job-specific → `.agentic/axioms/jobs/<job>.md`
- skill-specific → `.agentic/axioms/skills/<skill>.md`
- project-specific → `.agentic/axioms/projects/<project>.md`

## After Completion

- Verify using `.agentic/skills/axiom-creator/checklist.md`
- Return output in the format defined by `.agentic/skills/axiom-creator/output.md`
- Offer to run `python scripts/validate_template.py`
