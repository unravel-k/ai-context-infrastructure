# Agent Doctrine Template

Drop-in infrastructure for building agent doctrine. Install it into any repo, then use `/skill-creator` and `/axiom-creator` to build your own axioms, principles, guardrails, and reusable skills. The bundled analysis skills are **examples** showing what you can build — the real product is the creator meta-skills and the `.agentic/` doctrine layer.

---

## What is this?

Think of your agent as a new team member. Without onboarding, they wing it — sometimes brilliantly, sometimes they force-push to main at 2am.

This template is the **onboarding infrastructure**. You define the constitution (axioms), the playbooks (skills), the dispatch rules (router), and the safety boundaries (guardrails). Your agent consults them every session. They're version-controlled, so they improve over time.

```
Your repo before:                    Your repo after:
┌─────────────┐                     ┌──────────────────────────────┐
│ CLAUDE.md   │                     │ CLAUDE.md  (bootstrap)       │
│ (flat file) │                     │ .agentic/   (the constitution)│
└─────────────┘                     │   axioms/   (principles)     │
                                    │   skills/   (playbooks)      │
                                    │   router/   (dispatch rules) │
                                    │   guardrails/ (safety)       │
                                    │ .claude/    (adapter layer)  │
                                    └──────────────────────────────┘
```

The `.agentic/` layer is portable — not tied to Claude Code. Switch platforms later, the doctrine moves with you. Only the thin `.claude/` adapter layer is Claude Code-specific.

---

## Why context infrastructure matters

### The five problems it solves

**1. You repeat yourself.** Every session you remind the agent: "don't force-push, attribute sources, run tests after changes." With axioms, you say it once. Universal axioms fire on every task, automatically.

**2. Your team has no shared doctrine.** Alice's Claude reviews PRs one way, Bob's another. With the template, the doctrine lives in the repo — one source of truth, version-controlled, reviewed like code.

**3. Skills drift.** A skill that worked last month now skips a step because someone edited the markdown and forgot to update the checklist. Every skill here has four locked files: `skill.md` (workflow), `axioms.md` (principles), `checklist.md` (verification), `output.md` (contract). They can't drift independently.

**4. Tasks hit the wrong context.** "Review this PR" loads a code-review skill — or does it? Without a router, the agent guesses. `routes.yaml` matches tasks to the right axioms, skill, and verification. No guessing.

**5. No safety net.** A well-intentioned `rm -rf` or `git push --force` slips through. Guardrails are hard stops — they fire regardless of which route, skill, or axiom stack is active. They can't be overridden by user instruction.

### How the pieces fit together

```
User asks: "Is copper a good bet for 2026?"

     ┌──────────────────────────────┐
     │  ROUTER (routes.yaml)       │
     │  "good bet" → for-and-against│
     └──────────┬───────────────────┘
                │ loads
     ┌──────────▼───────────────────┐
     │  AXIOM STACK                 │
     │  universal.md                │  ← always
     │  research-analysis.md        │  ← matched by domain
     │  for-and-against.md          │  ← matched by skill
     └──────────┬───────────────────┘
                │ feeds into
     ┌──────────▼───────────────────┐
     │  SKILL (for-and-against)    │
     │  8-step research workflow    │
     │  output → structured report  │
     └──────────┬───────────────────┘
                │ can chain into
     ┌──────────▼───────────────────┐
     │  NEXT SKILL (risk-analysis)  │
     │  consumes report → profile   │
     └──────────────────────────────┘

Every step protected by guardrails.
Every output verified by checklist.
```

---

## Quick start

```bash
# Option A: Python installer
python scripts/install_claude.py --target /path/to/your/repo

# Option B: Claude Code marketplace
# (inside Claude Code — no terminal needed)
/plugin marketplace add unravel-k/ai-context-infrastructure
/plugin install agent-doctrine-template
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

### Via Claude Code marketplace

From inside Claude Code:
```
/plugin marketplace add unravel-k/ai-context-infrastructure
/plugin install agent-doctrine-template
```

Or for local development:
```bash
claude --plugin-dir /path/to/agent-doctrine-template
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
  plugin.json        # Claude Code plugin manifest
  marketplace.json   # Marketplace registry

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
