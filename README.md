# Agent Doctrine Template

Drop-in infrastructure for building agent doctrine. Install it into any repo, then use `/skill-creator` and `/axiom-creator` to build your own axioms, principles, guardrails, and reusable skills. The bundled analysis skills are **examples** showing what you can build — the real product is the creator meta-skills and the `.agentic/` doctrine layer.

---

## What is this?

Most Claude Code setups are ad-hoc — a flat `CLAUDE.md`, maybe a few skills. This template gives you a **structured doctrine layer** that grows with your project:

```
You install the template.
       │
       ▼
You create axioms via /axiom-creator.
  ("Every PR must include a test plan.")
       │
       ▼
You create skills via /skill-creator.
  ("PR review workflow: read diff → check axioms → run tests → report")
       │
       ▼
You register the skill in routes.yaml.
  (Now "review this PR" triggers your skill with your axioms.)
       │
       ▼
Your agent runs with guardrails, principles,
and verification — all defined by you.
```

The `.agentic/` layer is portable — it's not tied to Claude Code. If you switch agent platforms later, the doctrine moves with you. Only the thin `.claude/` adapter layer is platform-specific.

---

## Why context infrastructure matters

### Without it

Claude Code starts fresh each session. You repeat the same instructions. You forget to mention a guardrail. A skill works differently depending on who invoked it. Your team has no shared doctrine — Alice's Claude acts one way, Bob's another. Over time, the `CLAUDE.md` becomes a graveyard of stale notes.

### With it

| Component | Why it matters |
|-----------|---------------|
| **Axioms** | Principles that survive sessions. Universal axioms (`AX-UNIV`) fire on every task — safety, security, portable doctrine. Domain axioms (`AX-DOM`) fire on relevant tasks. Job, skill, and project axioms narrow further. No more "I forgot to tell Claude not to force-push." |
| **Skills** | Reusable workflows with built-in verification. Every skill has the same four-file structure (`skill.md`, `axioms.md`, `checklist.md`, `output.md`), so they compose. Run skill A, feed its output to skill B, verify both with their checklists. |
| **Router** | Auto-selects the right axioms and skill for a task. "Bull vs bear copper" → loads research-analysis domain axioms + for-and-against skill + verification strategy. No manual `--remember-to` flags. |
| **Guardrails** | Hard stops. Dangerous actions always require confirmation. Doctrine files can't be mutated without asking. These fire regardless of which route, skill, or axiom stack is active. |
| **Output contracts** | Every skill produces structured, predictable output. Risk-analysis output feeds directly into frontend-slides. No parsing guesswork. |

### The problem this solves

**Doctrine drift.** Without infrastructure, your agent principles are in your head, in a chat transcript, or scattered across multiple `CLAUDE.md` files. They decay. The template gives doctrine a home — version-controlled, structured, and portable. When you switch agent platforms, `.agentic/` moves with you. Only the thin `.claude/` adapter layer is Claude Code-specific.

---

## Quick start

```bash
# Install into your repo
python scripts/install_claude.py --target /path/to/your/repo

# Or install as a Claude Code plugin
# (after adding the marketplace, or from local path)
claude --plugin-dir /path/to/agent-doctrine-template
```

Then inside Claude Code in your repo:

```
/skill-creator    →  Build your first skill
/axiom-creator    →  Add your first axiom
```

---

## Architecture

```
.agentic/   ←  Portable doctrine. Source of truth. Framework-agnostic.
.claude/    ←  Claude Code adapter only. Thin SKILL.md files that point to .agentic/
```

**Rule:** never duplicate logic from `.agentic/` into `.claude/`. The adapter says "go read these canonical files" — it does not copy them.

### What's inside `.agentic/`

| Directory | Purpose |
|-----------|---------|
| `router/` | `routes.yaml` maps tasks to axiom stacks, skills, and verification |
| `axioms/` | Principles organized by scope: universal, domain, job, skill, project |
| `skills/` | Reusable workflows — each has skill.md, axioms.md, checklist.md, output.md |
| `guardrails/` | Safety rules (dangerous actions, doctrine mutation) |
| `outputs/` | Output contract templates for consistent results |

### Axiom scopes and conflict resolution

```
universal → domain → job → skill → project → user instruction
```

Higher scope wins by default. **Safety, security, privacy, and destructive-action guardrails can never be overridden** — not even by user instruction.

---

## Creator skills (the core)

### `/skill-creator`

Build a reusable skill from scratch:

1. Describe what the skill should do
2. Skill-creator generates the four canonical files (`skill.md`, `axioms.md`, `checklist.md`, `output.md`)
3. Generates the `.claude/` adapter
4. Offers to register it in `routes.yaml`

Every skill follows the same structure, so they're composable and verifiable.

### `/axiom-creator`

Add a principle to your doctrine:

1. Describe the rule or principle
2. Classify it: universal, domain, job, skill, or project
3. Axiom-creator assigns an ID (`AX-DOM-ENGINEERING-004`) and writes it to the right file
4. Offers to add it to any route's axiom stack

This is how doctrine grows — incrementally, with IDs, without drift.

### `/route <task>`

Routes any non-trivial task through `routes.yaml`. Loads the right axioms, skill, output contract, and verification strategy before execution.

---

## Example skills (what you can build)

These are **examples** built with the creator skills above. They demonstrate what the infrastructure produces, but the creators are the product.

**`/for-and-against`** — Research a topic from opposing viewpoints. Queries bullish/for and bearish/against independently. Classifies consensus vs contrarian views. Verifies citations. Attributes every source. Captures Why/How/Who/When context. Chains into risk-analysis.

**`/risk-analysis`** — Consume views and evaluate impact + likelihood per side. Build a qualitative risk profile. No fake percentages. Every "why" is a direct reason about that specific side, never a comparison. Designed to chain after for-and-against.

**`/frontend-slides`** — Generate animation-rich HTML presentations from scratch or PPTX. Visual style previews — pick by seeing. Single self-contained HTML file. Built by [zarazhangrui](https://github.com/zarazhangrui/frontend-slides).

### Example chain (all three composed)

```
/for-and-against "copper supply 2026"   →  research with sources
/risk-analysis                           →  risk profile from that research
/frontend-slides                        →  presentation from the analysis
```

---

## Example axiom domain: Research & Analysis

Shipped as an example of what doctrine looks like. All six axioms are built around **trust through transparency**:

1. **Full Attribution** — Every claim carries source (URL + title preferred)
2. **In-Text Citation** — Sources at point of use, not buried in footnotes
3. **Preserve Rich Evidence** — Charts, tables, images embedded inline
4. **Interactive Citations** — HTML: hover a citation to see the original snippet
5. **Verified Citations** — Automated checks catch hallucinated references (uses [claude-skill-citation-checker](https://github.com/PHY041/claude-skill-citation-checker) by PHY041)
6. **Why, How, Who, When** — Every view explains catalyst, mechanism, stakeholders + game theory, and timeline

---

## Installation

### Via Python installer (recommended)

```bash
python scripts/install_claude.py --target /path/to/your/repo
```

| Flag | Effect |
|------|--------|
| `--force` | Overwrite existing files |
| `--dry-run` | Preview without writing |

The installer copies `.agentic/`, `.claude/skills/`, and a `CLAUDE.md` bootstrap. Existing `CLAUDE.md` is preserved unless you `--force`.

### Via Claude Code plugin

```bash
# Local development
claude --plugin-dir /path/to/agent-doctrine-template

# From marketplace (once published)
/plugin marketplace add unravel-k/context-engine
/plugin install agent-doctrine-template
```

---

## Updating

```bash
python scripts/install_claude.py --target /path/to/your/repo --dry-run  # preview
python scripts/install_claude.py --target /path/to/your/repo --force    # apply
```

---

## Testing

```bash
python -m pytest                    # 38 tests: install, routes, contracts
python scripts/validate_template.py # Structure-only validation
```

---

## Directory structure

```
.agentic/
  router/          # routes.yaml — maps tasks to axiom stacks + skills
  axioms/          # Principles by scope (universal, domains/, jobs/, skills/, projects/)
  skills/          # Reusable skill definitions (each has 4 canonical files)
  outputs/         # Output contract templates
  guardrails/      # Safety and doctrine-mutation rules

.claude/
  skills/          # Thin Claude Code adapters (point to .agentic/ files)

.claude-plugin/
  plugin.json      # Claude Code plugin manifest

adapters/
  claude-code/     # CLAUDE.md bootstrap copied into target repos

scripts/
  install_claude.py    # Installer (Python stdlib only)
  validate_template.py # Structure validator
```

---

## Credits

- [frontend-slides](https://github.com/zarazhangrui/frontend-slides) — HTML presentation skill by **zarazhangrui**
- [claude-skill-citation-checker](https://github.com/PHY041/claude-skill-citation-checker) — Citation verification by **PHY041**
