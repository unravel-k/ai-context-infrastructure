# Doctrine Mutation Guardrail

This guardrail governs changes to the `.agentic/` doctrine layer.

## Rules

1. **Ask before mutating.** Do not create, modify, or delete any file under `.agentic/axioms/`, `.agentic/skills/`, `.agentic/router/`, `.agentic/guardrails/`, or `.agentic/outputs/` without explicit user confirmation, unless the user's request clearly implies a creation or update operation (e.g., "create a new skill", "add an axiom").

2. **Use the creators.** Prefer using the `/skill-creator` or `/axiom-creator` routes rather than directly editing doctrine files. The creator workflows include validation and consistency checks.

3. **Follow ID conventions.** When adding axioms, always assign IDs following the convention: AX-{SCOPE}-{QUALIFIER}-{NNN}.

4. **Update routes when needed.** When adding a new skill or axiom, offer to update `.agentic/router/routes.yaml` to maintain consistency.

5. **Validate after changes.** Run `python scripts/validate_template.py` after any doctrine mutation to ensure the template remains valid.

6. **Never remove safety axioms.** AX-UNIV-001 (Safety First) and AX-UNIV-002 (Security Awareness) must never be removed or weakened.
