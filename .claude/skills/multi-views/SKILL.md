---
name: multi-views
description: Research and compare multiple topics, assets, or theses side-by-side. Runs for-and-against independently per topic, then synthesizes cross-comparison with shared themes, divergences, ranking, and consolidated output. Use for multi-asset analysis, technology comparisons, strategic option evaluation, or any decision involving multiple candidates.
---

# Multi-Views

This is a Claude Code adapter. The canonical source of truth is at `.agentic/skills/multi-views/skill.md`.

## Required Reading

Before executing, read these files in order:

1. `.agentic/router/routes.yaml` — routing context
2. `.agentic/skills/multi-views/skill.md` — the full workflow
3. `.agentic/skills/multi-views/axioms.md` — skill-specific axioms
4. `.agentic/skills/multi-views/checklist.md` — verification checklist
5. `.agentic/skills/multi-views/output.md` — expected output format
6. `.agentic/axioms/skills/multi-views.md` — canonical axiom definitions
7. `.agentic/axioms/universal.md` — universal axioms

## Execution

Follow the seven-step workflow defined in `.agentic/skills/multi-views/skill.md`. Delegate per-topic research to `for-and-against`. Do not reimplement directional queries. Identify cross-cutting themes after all per-topic runs complete. Rank qualitatively — no numeric scores.

## After Completion

- Verify using `.agentic/skills/multi-views/checklist.md`
- Return output in the format defined by `.agentic/skills/multi-views/output.md`
