# Axiom Creator

## Workflow

### Step 1: Discover the Axiom

Ask the user for the axiom or principle they want to add. Clarify:
- What is the rule or principle?
- Why is it important?
- When should it apply?

### Step 2: Classify the Axiom

Ask the user to classify it as one of:
- **universal** — applies to all tasks and routes
- **domain-specific** — applies to a specific domain (engineering, security, ai-agents, etc.)
- **job-specific** — applies to a specific job or role
- **skill-specific** — applies to a specific skill
- **project-specific** — applies only to the current project

### Step 3: Select Target Location

Based on classification:

| Classification     | Target File                                      |
|-------------------|--------------------------------------------------|
| universal         | `.agentic/axioms/universal.md`                   |
| domain-specific   | `.agentic/axioms/domains/<domain>.md`            |
| job-specific      | `.agentic/axioms/jobs/<job>.md`                  |
| skill-specific    | `.agentic/axioms/skills/<skill>.md`              |
| project-specific  | `.agentic/axioms/projects/<project>.md`          |

### Step 4: Inspect Target File

If the target file exists, read it. Look for existing axioms with similar intent or wording.

### Step 5: Handle Duplicates

If a similar axiom exists:
- Ask the user whether to **modify** the existing axiom, **append** to it, or **skip** creation.
- If modifying, preserve the existing axiom ID.
- If appending, add a sub-point to the existing axiom.

If no similar axiom exists:
- Proceed to create a new axiom.

### Step 6: Assign an Axiom ID

Axiom IDs follow this convention:

| Classification     | ID Format                  | Example                    |
|-------------------|----------------------------|----------------------------|
| universal         | AX-UNIV-NNN                | AX-UNIV-006                |
| domain-specific   | AX-DOM-<DOMAIN>-NNN        | AX-DOM-ENGINEERING-004     |
| job-specific      | AX-JOB-<JOB>-NNN           | AX-JOB-REVIEWER-001        |
| skill-specific    | AX-SKILL-<SKILL>-NNN       | AX-SKILL-DEPLOYER-001      |
| project-specific  | AX-PROJ-<PROJECT>-NNN      | AX-PROJ-MYAPP-001          |

Determine the next available NNN by counting existing axioms of that type.

### Step 7: Write the Axiom

Append to the target file using this template:

```markdown
## AX-<TYPE>-NNN: <Title>

<One or two sentences describing the rule.>

<Optional: rationale or context.>
```

### Step 8: Offer Route Integration

Ask: "Should I update `.agentic/router/routes.yaml` to include this axiom in any route's axiom_stack?"

If yes:
- Identify which route(s) should include the axiom.
- Add the axiom file path to the route's `axiom_stack` list.
- Do not update routes without user confirmation.

### Step 9: Return Summary

Return a summary containing:
- Classification (universal / domain-specific / job-specific / skill-specific / project-specific)
- File changed (target file path)
- Axiom ID (the assigned ID)
- Route changes (which routes were updated, or "none")
- Unresolved questions
