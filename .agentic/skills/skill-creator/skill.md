# Skill Creator

## Workflow

### Step 1: Discover Intent

Ask the user what skill they want to create or modify. Clarify:
- What should the skill do?
- When should it be triggered?
- What are its inputs and outputs?

### Step 2: Inspect Existing Skills

Inspect `.agentic/skills/` and `.claude/skills/` to see whether an existing skill matches the user's intent.

### Step 3: Decide Create vs Modify

If an existing skill matches:
- Ask the user whether to modify/append to the existing skill or create a new one.
- If modifying, identify which files need changes.

If no existing skill matches:
- Create a new skill folder at `.agentic/skills/<skill-name>/`.

### Step 4: Create or Update Canonical Files

Create or update the four required skill files in `.agentic/skills/<skill-name>/`:

#### skill.md

The main skill file. It should contain:
- A clear description of the skill's purpose
- A numbered workflow with concrete steps
- Templates for any generated output

Template:
```markdown
# <Skill Name>

<One-line description of what this skill does.>

## Workflow

### Step 1: <Step Name>
<Instructions>

### Step 2: <Step Name>
<Instructions>

...
```

#### axioms.md

Skill-specific axioms that guide behavior:
```markdown
# <Skill Name> Axioms

## AX-SKILL-<SKILL>-001: <Title>
<Description>

## AX-SKILL-<SKILL>-002: <Title>
<Description>
```

#### checklist.md

A verification checklist for the skill:
```markdown
# <Skill Name> Checklist

- [ ] Step 1 completed
- [ ] Step 2 completed
- [ ] All files created
- [ ] Validation passed
- [ ] User approved
```

#### output.md

The expected output format:
```markdown
# <Skill Name> Output

## Files Created
- <list>

## Files Modified
- <list>

## Route Changes
- <list or "none">

## Unresolved Questions
- <list or "none">
```

### Step 5: Create or Update Claude Code Adapter

Create or update `.claude/skills/<skill-name>/SKILL.md`.

The adapter should be thin — it should instruct Claude to read the canonical `.agentic/` files, not duplicate them.

Template:
```markdown
---
name: <skill-name>
description: <one-line description>
---

# <Skill Name>

Follow the canonical skill definition at `.agentic/skills/<skill-name>/skill.md`.

## Required Reading

1. Read `.agentic/router/routes.yaml` for routing context.
2. Read `.agentic/skills/<skill-name>/skill.md` for the full workflow.
3. Read `.agentic/skills/<skill-name>/axioms.md` for skill-specific axioms.
4. Read `.agentic/skills/<skill-name>/checklist.md` for the verification checklist.
5. Read `.agentic/skills/<skill-name>/output.md` for the expected output format.

## Execution

Follow the workflow defined in the canonical skill file. Verify completion using the checklist before reporting done.
```

### Step 6: Offer Route Registration

Ask the user: "Should I register this skill in `.agentic/router/routes.yaml`?"

If yes:
- Add or update a route entry in `.agentic/router/routes.yaml`.
- The route must include: description, triggers, negative_triggers, priority, intent, axiom_stack, skill, required_context, allowed_tools, disallowed_tools, verification, output_contract, guardrails, doctrine_update.

### Step 7: Return Summary

Return a summary in the format defined by `.agentic/outputs/creator-result.md`:
- Files created
- Files modified
- Route changes
- Unresolved questions
