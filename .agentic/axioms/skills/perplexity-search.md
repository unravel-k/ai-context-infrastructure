# Perplexity Search Axioms

## AX-SKILL-PERPLEXITY-SEARCH-001: Always Return Citations

Every search must request and return citations (`return_citations=True`). Never present Perplexity results without source attribution. The citations are the point — the answer is secondary.

## AX-SKILL-PERPLEXITY-SEARCH-002: Select the Right Search Type

Match the search type to the query: finance for market data, news for current events, academic for papers, general for everything else. Wrong search type degrades result quality.

## AX-SKILL-PERPLEXITY-SEARCH-003: Preserve Structure for Downstream Use

Format output so it can be consumed by for-and-against, risk-analysis, or multi-views directly. Preserve citations, sources, and structure. Don't flatten into prose that downstream skills must re-parse.
