# Routing Rules

When a task does not match any route trigger, fall back to the default behavior: apply universal axioms and ask the user for clarification before proceeding.

## Route selection algorithm

1. Scan all routes for matching triggers in the user's request.
2. Filter out routes with matching negative triggers.
3. Select the highest-priority route among remaining candidates.
4. If no route matches, use default (no route) behavior.
5. If multiple routes tie on priority, present the user with a choice.

## Axiom order

Axioms are resolved in this order, with later scopes able to refine (but not contradict safety/security) earlier scopes:

1. universal
2. domain
3. job
4. skill
5. project
6. current_user_instruction

## Conflict resolution

- Default: higher scope wins.
- User instructions can override job, skill, and project axioms.
- User instructions CANNOT override safety, security, privacy, or destructive-action-guardrails.
