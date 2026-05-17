---
name: for-and-against
description: Research a topic from opposing viewpoints. Query bullish/for and bearish/against perspectives independently, classify consensus vs contrarian views, and attribute every source. Use for investment theses, technology evaluations, strategic decisions, or any question where balanced perspective matters.
---

# For and Against

This is a Claude Code adapter. The canonical source of truth is at `.agentic/skills/for-and-against/skill.md`.

## Required Reading

Before executing, read these files in order:

1. `.agentic/router/routes.yaml` — routing context
2. `.agentic/skills/for-and-against/skill.md` — the full workflow
3. `.agentic/skills/for-and-against/axioms.md` — skill-specific axioms
4. `.agentic/skills/for-and-against/checklist.md` — verification checklist
5. `.agentic/skills/for-and-against/output.md` — expected output format
6. `.agentic/axioms/skills/for-and-against.md` — canonical axiom definitions
7. `.agentic/axioms/universal.md` — universal axioms

## Execution

Follow the eight-step workflow defined in `.agentic/skills/for-and-against/skill.md`. Query opposing directions independently. Attribute every claim. Verify citations before finalizing. Classify consensus vs contrarian.

## After Completion

- Verify using `.agentic/skills/for-and-against/checklist.md`
- Return output in the format defined by `.agentic/skills/for-and-against/output.md`
