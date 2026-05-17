# Research & Analysis Domain Axioms

## AX-DOM-RESEARCH-ANALYSIS-001: Full Attribution

Every factual claim must carry a source attribution. Use the richest attribution available:
- URL + title (preferred)
- Title + author
- Title only or author only (minimum)

Never present a factual claim without attribution. If no source is available, flag it explicitly: *(source unavailable)*.

## AX-DOM-RESEARCH-ANALYSIS-002: In-Text Citation

Sources must be cited in-text at the point of use, not only in a bibliography or footnotes section. The reader should be able to trace any claim to its source without scanning the entire document.

## AX-DOM-RESEARCH-ANALYSIS-003: Preserve Rich Evidence

For rich output formats (HTML, PDF, markdown), preserve and embed relevant evidentiary media:
- Price charts, data visualizations
- Tables with source data
- Diagrams that support the analysis

Images and tables must be placed inline at the relevant position in the output, not appended at the end.

## AX-DOM-RESEARCH-ANALYSIS-004: Interactive Citations

For interactive output formats (HTML), implement hover-on-citation behavior: when the user hovers over a citation, display a snippet from the original source. This enables the reader to verify claims without leaving the document.

## AX-DOM-RESEARCH-ANALYSIS-005: Verified Citations

Citations must be verified against original sources before finalizing output. Use automated citation-checking tools (e.g., `claude-skill-citation-checker`) to catch hallucinated or fabricated references. Remove or flag any citation that cannot be verified.
