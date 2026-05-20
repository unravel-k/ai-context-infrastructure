---
name: perplexity-search
description: Search the web via Perplexity's API with structured results, citations, and source attribution. Supports finance, news, academic, and general search types. Use as a standalone search tool or as a data source for for-and-against, multi-views, and risk-analysis.
---

# Perplexity Search

This is a Claude Code adapter. The canonical source of truth is at `.agentic/skills/perplexity-search/skill.md`.

## Required Reading

Before executing, read these files in order:

1. `.agentic/router/routes.yaml` — routing context
2. `.agentic/skills/perplexity-search/skill.md` — the full workflow
3. `.agentic/skills/perplexity-search/axioms.md` — skill-specific axioms
4. `.agentic/skills/perplexity-search/checklist.md` — verification checklist
5. `.agentic/skills/perplexity-search/output.md` — expected output format
6. `.agentic/axioms/skills/perplexity-search.md` — canonical axiom definitions
7. `.agentic/axioms/universal.md` — universal axioms

## Prerequisites

```bash
export PERPLEXITY_API_KEY="pplx-..."
```

Get a key at https://perplexity.ai/settings/api. No SDK install needed — uses Python stdlib `requests`.

## Execution

Follow the six-step workflow defined in `.agentic/skills/perplexity-search/skill.md`. Always request citations. Match search type to query. Format output for downstream skill consumption.

## After Completion

- Verify using `.agentic/skills/perplexity-search/checklist.md`
- Return output in the format defined by `.agentic/skills/perplexity-search/output.md`
