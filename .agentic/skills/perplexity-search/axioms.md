# Perplexity Search Axioms

See `.agentic/axioms/skills/perplexity-search.md` for the canonical axiom definitions.

## AX-SKILL-PERPLEXITY-SEARCH-001: Always Return Citations

Perplexity's API returns citations by default. Always present them with the answer. Never strip or ignore source URLs. The citations are the point — the answer is secondary.

## AX-SKILL-PERPLEXITY-SEARCH-002: Match Model to Task

Use `sonar` for quick factual queries (prices, metrics, headlines). Use `sonar-reasoning` for analysis requiring depth. Wrong model wastes time or produces shallow results.

## AX-SKILL-PERPLEXITY-SEARCH-003: Preserve Structure for Downstream Use

Format output so it can be consumed by for-and-against, risk-analysis, or multi-views directly. Preserve citations and structure. Don't flatten into prose that downstream skills must re-parse.
