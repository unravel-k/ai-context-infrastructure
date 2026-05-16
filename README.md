# Agent Doctrine Template

A portable, reusable template for agent-doctrine systems, with a Claude Code adapter layer.

## Architecture

This template enforces a strict separation between portable doctrine and platform-specific adapters:

- **`.agentic/`** — Portable source of truth. Contains axioms, skills, router, guardrails, and output contracts. Framework-agnostic and reusable across any agent platform.
- **`.claude/`** — Claude Code adapter layer only. Contains thin `SKILL.md` files that reference canonical `.agentic/` files. Never duplicates logic.
- **`adapters/`** — Platform-specific bootstrap files (e.g., `CLAUDE.md` for Claude Code).

### Design Rule

**Never duplicate logic from `.agentic/` into `.claude/`.** The `.claude/` adapter files are thin pointers that direct Claude to read the canonical `.agentic/` source files. When updating doctrine, always modify `.agentic/` first.

## Installation

Install into a target repository:

```bash
python scripts/install_claude.py --target /path/to/your/repo
```

Options:
- `--force` — Overwrite existing files
- `--dry-run` — Preview what would be installed without writing files

## Usage in Claude Code

After installation, start Claude Code in the target repo and use these slash commands:

- `/route <task>` — Route any non-trivial task through `.agentic/router/routes.yaml` to load the correct axioms, skill, and verification strategy.
- `/skill-creator` — Create or modify a skill (workflow + axioms + checklist + output + adapter).
- `/axiom-creator` — Create or modify an axiom (classify, assign ID, integrate into route stacks).

## Updating

When the template is updated upstream, re-run the installer to pull in changes:

```bash
python scripts/install_claude.py --target /path/to/your/repo --force
```

The installer preserves existing files by default. Use `--force` to overwrite.

Files you create locally (custom skills, axioms, routes) are in the same directories — use `--dry-run` first to preview what will be overwritten.

## Testing

Run the test suite:

```bash
python -m pytest
```

Validate template structure without running tests:

```bash
python scripts/validate_template.py
```

## Directory Structure

```
.agentic/
  router/          # Task routing rules
  axioms/          # Universal, domain, job, skill, project axioms
  skills/          # Portable skill definitions
  outputs/         # Output contract templates
  guardrails/      # Safety and mutation guardrails

.claude/
  skills/          # Claude Code SKILL.md adapters (thin wrappers)

adapters/
  claude-code/     # CLAUDE.md bootstrap for Claude Code

scripts/
  install_claude.py    # Template installer
  validate_template.py # Structure validator
```
