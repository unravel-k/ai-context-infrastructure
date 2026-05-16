# Axiom Creator Axioms

## AX-SKILL-AXIOM-CREATOR-001: Classification First

Always classify an axiom before writing it. The five classifications are:
- universal
- domain-specific
- job-specific
- skill-specific
- project-specific

## AX-SKILL-AXIOM-CREATOR-002: ID Assignment

Every axiom must have a unique ID following the convention:
- AX-UNIV-NNN for universal
- AX-DOM-<DOMAIN>-NNN for domain-specific
- AX-JOB-<JOB>-NNN for job-specific
- AX-SKILL-<SKILL>-NNN for skill-specific
- AX-PROJ-<PROJECT>-NNN for project-specific

## AX-SKILL-AXIOM-CREATOR-003: No Duplicates

Before creating a new axiom, check for existing axioms with similar intent. Ask the user whether to modify, append, or skip if a similar axiom exists.

## AX-SKILL-AXIOM-CREATOR-004: Route Integration

Offer to update `.agentic/router/routes.yaml` to include the new axiom in relevant axiom_stacks. Do not update routes without user confirmation.
