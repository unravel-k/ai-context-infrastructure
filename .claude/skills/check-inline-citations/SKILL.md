---
name: check-inline-citations
description: Scan a draft and flag every factual claim missing an inline citation. Verify citations are at the point of use, not deferred to footnotes. Reports coverage stats and missing sources, but never fabricates citations. Pairs with verify-citations (which checks if cited sources are real).
---

# Check Inline Citations

This is a Claude Code adapter. The canonical source of truth is at `.agentic/skills/check-inline-citations/skill.md`.

## Required Reading

Before executing, read these files in order:

1. `.agentic/router/routes.yaml` — routing context
2. `.agentic/skills/check-inline-citations/skill.md` — the full workflow
3. `.agentic/skills/check-inline-citations/axioms.md` — skill-specific axioms
4. `.agentic/skills/check-inline-citations/checklist.md` — verification checklist
5. `.agentic/skills/check-inline-citations/output.md` — expected output format
6. `.agentic/axioms/skills/check-inline-citations.md` — canonical axiom definitions
7. `.agentic/axioms/universal.md` — universal axioms

## Execution

Follow the six-step workflow defined in `.agentic/skills/check-inline-citations/skill.md`. Identify every factual claim. Flag missing or deferred citations. Never fabricate a source — only report what exists and what's missing.

## Relationship to verify-citations

This skill checks citation **placement** (are sources cited at the point of use?). `verify-citations` checks citation **authenticity** (are the cited sources real?). Use both for a complete citation audit.

## After Completion

- Verify using `.agentic/skills/check-inline-citations/checklist.md`
- Return output in the format defined by `.agentic/skills/check-inline-citations/output.md`
