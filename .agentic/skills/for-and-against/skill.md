# For and Against

Research a topic from opposing viewpoints. Query the supportive (bullish/for) and opposing (bearish/against) perspectives independently, then synthesize with source attribution and consensus/contrarian classification.

## Workflow

### Step 1: Receive the Topic

Ask the user what topic they want a balanced view on. Clarify:
- What instrument, industry, decision, or question is being evaluated?
- Is there a specific timeframe or scope?

### Step 2: Discover Available Tools

Before querying, check what tools are available:
- MCP servers (data APIs, financial data, news)
- Web search tools
- Any other data sources in the environment

Prefer specialized data tools over general web search. If multiple tools are available, use the most relevant ones first.

### Step 3: Query the "For" Direction

Query supporting / bullish / positive viewpoints. This is a separate, independent query.

Example phrasings:
- "What are the bullish arguments for [topic]?"
- "What evidence supports [position]?"
- "Why might [topic] outperform / succeed?"

For each viewpoint collected, also capture the Why, How, Who, When context if available (per AX-DOM-RESEARCH-ANALYSIS-006). Do not fabricate missing dimensions.

Collect all viewpoints with their sources intact.

### Step 4: Query the "Against" Direction

Query opposing / bearish / negative viewpoints. This must be a SEPARATE query, not combined with Step 3.

Example phrasings:
- "What are the bearish arguments against [topic]?"
- "What evidence contradicts [position]?"
- "Why might [topic] underperform / fail?"

For each viewpoint collected, also capture the Why, How, Who, When context if available (per AX-DOM-RESEARCH-ANALYSIS-006). Do not fabricate missing dimensions.

Collect all viewpoints with their sources intact.

### Step 5: Classify Views

If the data includes multiple viewpoints on the same sub-topic:

- **Consensus:** The majority or most frequently expressed view. Mark clearly.
- **Contrarian:** Views that go against the consensus. Mark clearly.

If there is no clear majority, state that views are mixed and no single consensus exists.

### Step 6: Attribute Every Source

For every viewpoint, provide source attribution. Use whichever is available:

| Available Info         | Attribution Format                    |
|-----------------------|---------------------------------------|
| URL + Title           | `[Title](URL)`                        |
| Title + Author        | `Title — Author`                      |
| Title only            | `Title`                               |
| Author only           | `Author`                              |

Citations must be **inline at the point of use** — the same sentence or immediately after the claim. Do not defer citations to a bibliography section. Every claim-sentence that asserts a fact must carry its source directly (per AX-DOM-RESEARCH-ANALYSIS-002).

Never present a claim without attribution. If no source is available, flag it: *(source unavailable)*.

### Step 7: Verify Citations

Delegate to the `verify-citations` skill. Run it against the draft output to catch hallucinated URLs, broken links, misattributed claims, or fabricated references. Do not proceed to synthesis until all citations are verified, flagged, or removed per the verify-citations workflow.

### Step 8: Synthesize the Output

Present the findings in this structure:

```
## For (Bullish / Supportive)

### Viewpoint A
- Claim and evidence
- Source: [attribution]

### Viewpoint B
- Claim and evidence
- Source: [attribution]

## Against (Bearish / Opposing)

### Viewpoint A
- Claim and evidence
- Source: [attribution]

### Viewpoint B
- Claim and evidence
- Source: [attribution]

## Consensus vs Contrarian

| Viewpoint              | Classification | Held By            |
|------------------------|----------------|---------------------|
| Bullish on X           | Consensus      | Source A, Source B  |
| Bearish on X           | Contrarian     | Source C            |

## Summary

A brief synthesis weighing the strength of evidence on both sides. Do not fabricate a conclusion — if the evidence leans one way, say so. If it is balanced, say so.
```
