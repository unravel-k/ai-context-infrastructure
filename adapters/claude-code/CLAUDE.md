# CLAUDE.md

This repo uses `.agentic/` as its canonical, portable source of truth for agent doctrine.

## Key Directories

- `.agentic/` — Portable doctrine: axioms, skills, router, guardrails, outputs. Framework-agnostic.
- `.claude/` — Claude Code adapters only. Thin SKILL.md files that reference `.agentic/` files. Do not duplicate canonical content here.

## Implicit Routing (automatic)

Before processing any non-trivial request, scan `.agentic/router/routes.yaml` for matching routes:

1. Compare the user's request against every route's `triggers`.
2. Filter out any route with a matching `negative_triggers` hit.
3. If a route matches, load its `axiom_stack` files, read its `skill` file, follow its `verification` and `output_contract`, and honor its `guardrails`.
4. If no route matches, proceed with universal axioms from `.agentic/axioms/universal.md`.

Do this automatically — the user should not need to invoke `/route` explicitly. They can just say "bull vs bear case for copper" and the router matches `for-and-against`.

## Explicit Slash Commands

- `/route <task>` — Manually route a task (if automatic matching fails)
- `/skill-creator` — Create or modify a skill
- `/axiom-creator` — Create or modify an axiom

## Design Rule

**Never duplicate logic from `.agentic/` into `.claude/`.** The `.claude/` SKILL.md files are thin adapters that point to canonical `.agentic/` files. When in doubt, update `.agentic/` first.
