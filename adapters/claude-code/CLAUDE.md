# CLAUDE.md

This repo uses `.agentic/` as its canonical, portable source of truth for agent doctrine.

## Key Directories

- `.agentic/` — Portable doctrine: axioms, skills, router, guardrails, outputs. Framework-agnostic.
- `.claude/` — Claude Code adapters only. Thin SKILL.md files that reference `.agentic/` files. Do not duplicate canonical content here.

## For Non-Trivial Tasks

Use the routing system to load the right axioms, skill, and verification:

- `/route <task>` — Route a task through `.agentic/router/routes.yaml`
- `/skill-creator` — Create or modify a skill
- `/axiom-creator` — Create or modify an axiom

## Design Rule

**Never duplicate logic from `.agentic/` into `.claude/`.** The `.claude/` SKILL.md files are thin adapters that point to canonical `.agentic/` files. When in doubt, update `.agentic/` first.
