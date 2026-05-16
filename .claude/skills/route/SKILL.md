---
name: route
description: Use to route a task through `.agentic/router/routes.yaml` before executing it. Use for non-trivial tasks involving file edits, skill creation, axiom creation, refactors, debugging, code review, architecture, or doctrine updates.
---

# Route

This is a Claude Code adapter for the `.agentic/router/routes.yaml` routing system.

## Procedure

1. **Read the routes file.** Read `.agentic/router/routes.yaml` to load all available routes.

2. **Match the task to a route.** Compare the user's request against the `triggers` and `negative_triggers` of each route. Select the best match by priority.

3. **Read the axiom stack.** Read every file listed in the matched route's `axiom_stack`. These axioms govern behavior for this task.

4. **Read the skill file.** Read the file referenced by the route's `skill` key. Follow its workflow.

5. **Follow verification and output contract.** Use the `verification` strategy and format output according to the `output_contract`.

6. **Honor the guardrails.** Read the guardrail files referenced in the route. Do not perform dangerous actions without confirmation.

7. **Ask before mutating doctrine.** Unless the user explicitly requested creation or update of doctrine files (skills, axioms, routes, guardrails), ask before modifying any file under `.agentic/`.

## Default Behavior (No Route Match)

If no route matches the user's request:
- Apply universal axioms from `.agentic/axioms/universal.md`
- Fall back to general-purpose assistance
- Ask the user for clarification if needed
