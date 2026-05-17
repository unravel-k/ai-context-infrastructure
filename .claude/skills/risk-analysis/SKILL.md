---
name: risk-analysis
description: Evaluate the impact and likelihood of viewpoints to build a qualitative risk profile across sides of a bet or decision. Use when the user asks for risk assessment, odds evaluation, chance profiling, or impact-likelihood analysis of competing views.
---

# Risk Analysis

This is a Claude Code adapter. The canonical source of truth is at `.agentic/skills/risk-analysis/skill.md`.

## Required Reading

Before executing, read these files in order:

1. `.agentic/router/routes.yaml` — routing context
2. `.agentic/skills/risk-analysis/skill.md` — the full workflow
3. `.agentic/skills/risk-analysis/axioms.md` — skill-specific axioms
4. `.agentic/skills/risk-analysis/checklist.md` — verification checklist
5. `.agentic/skills/risk-analysis/output.md` — expected output format
6. `.agentic/axioms/skills/risk-analysis.md` — canonical axiom definitions
7. `.agentic/axioms/universal.md` — universal axioms

## Execution

Follow the seven-step workflow defined in `.agentic/skills/risk-analysis/skill.md`. Evaluate impact first, then likelihood. Every "why" must be a direct reason about that side. Use qualitative labels only. Preserve source attribution throughout.

## After Completion

- Verify using `.agentic/skills/risk-analysis/checklist.md`
- Return output in the format defined by `.agentic/skills/risk-analysis/output.md`
