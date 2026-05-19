---
name: verify-citations
description: Verify that citations and references in any text point to real, matching sources. Catch hallucinated URLs, broken links, misattributed claims, and fabricated references. Use standalone on any draft, or as a subroutine called by for-and-against, multi-views, or risk-analysis.
---

# Verify Citations

This is a Claude Code adapter. The canonical source of truth is at `.agentic/skills/verify-citations/skill.md`.

## Required Reading

Before executing, read these files in order:

1. `.agentic/router/routes.yaml` — routing context
2. `.agentic/skills/verify-citations/skill.md` — the full workflow
3. `.agentic/skills/verify-citations/axioms.md` — skill-specific axioms
4. `.agentic/skills/verify-citations/checklist.md` — verification checklist
5. `.agentic/skills/verify-citations/output.md` — expected output format
6. `.agentic/axioms/skills/verify-citations.md` — canonical axiom definitions
7. `.agentic/axioms/universal.md` — universal axioms

## Execution

Follow the six-step workflow defined in `.agentic/skills/verify-citations/skill.md`. Verify every citation — no spot-checking. Classify into five categories, not just pass/fail. Preserve claims when possible even if a citation is broken.

## After Completion

- Verify using `.agentic/skills/verify-citations/checklist.md`
- Return output in the format defined by `.agentic/skills/verify-citations/output.md`
