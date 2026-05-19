# Verify Citations Axioms

See `.agentic/axioms/skills/verify-citations.md` for the canonical axiom definitions.

## AX-SKILL-VERIFY-CITATIONS-001: Verify Every Citation

Every citation in the draft must be checked. No spot-checking. No sampling. Every URL, every source reference, every attribution claim.

## AX-SKILL-VERIFY-CITATIONS-002: Classify, Don't Just Filter

Classify each citation into one of five categories: verified, broken link, hallucinated, misattributed, unverifiable. This gives the user a complete picture, not just a pass/fail.

## AX-SKILL-VERIFY-CITATIONS-003: Preserve the Claim When Possible

If a citation is hallucinated but the claim is corroborated by other verified sources, preserve the claim and flag the citation. Only remove a claim if no verified source supports it.

## AX-SKILL-VERIFY-CITATIONS-004: Tool Integration

Use `claude-skill-citation-checker` if available. If not, manually verify URLs via web fetch. If neither is available, flag all citations as unverifiable and report the limitation.
