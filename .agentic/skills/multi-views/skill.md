# Multi-Views

Research multiple topics, assets, or theses side-by-side. Delegates to `for-and-against` per topic, then synthesizes cross-topic comparison — shared themes, divergences, ranking, and a consolidated output.

## Workflow

### Step 1: Receive Topics

Ask the user what topics, assets, or theses to compare. Clarify each one:
- What is the topic? (e.g., "copper", "e-comm vs retail", "TypeScript vs Rust for infra")
- What is the shared frame? (e.g., "investment outlook 2026", "technology choice", "strategic decision")

Confirm the full list before proceeding.

### Step 2: Run For-and-Against Per Topic

For each topic, execute the `for-and-against` skill independently. Do not run topics in parallel if they share dependencies or if running sequentially allows learning from earlier findings. If topics are fully independent, parallel is acceptable.

Each per-topic run produces:
- For (bullish/supportive) views with source attribution
- Against (bearish/opposing) views with source attribution
- Consensus vs contrarian classification
- Why/How/Who/When context per view

### Step 3: Collect Per-Topic Outputs

Collect all per-topic reports. Preserve all source attributions. Do not summarize away detail yet — the cross-comparison needs the raw views.

### Step 4: Identify Cross-Cutting Themes

Scan across all topics for:

- **Shared catalysts** — Factors that affect multiple topics in the same direction (e.g., "falling rates help both copper and lithium")
- **Divergent factors** — Factors that help one topic but hurt another (e.g., "strong USD hurts copper, but lithium has local supply contracts")
- **Correlated vs independent** — Are the topics' fates linked or decoupled?
- **Contrarian overlaps** — Views that are consensus for one topic but contrarian for another

### Step 5: Build Comparison Table

Create a side-by-side comparison:

| Dimension | Topic A | Topic B | Topic C |
|-----------|---------|---------|---------|
| Bullish strength | (qualitative) | (qualitative) | (qualitative) |
| Bearish strength | (qualitative) | (qualitative) | (qualitative) |
| Consensus view | (summary) | (summary) | (summary) |
| Key catalyst | (what + when) | (what + when) | (what + when) |
| Key risk | (what) | (what) | (what) |

### Step 6: Rank and Synthesize

Rank the topics ordinally — no fabricated scores, just qualitative ordering:

- **Strongest for case:** Topic X (why — direct reason)
- **Weakest for case:** Topic Y (why — direct reason)
- **Strongest against case:** Topic Z (why — direct reason)
- **Most balanced:** Topic W (why — direct reason)

### Step 7: Consolidated Output

Produce the final output:

1. **Per-topic summaries** (condensed from for-and-against outputs, sources preserved with inline citations at point of use)
2. **Cross-cutting themes** (shared catalysts, divergences, correlations)
3. **Comparison table** (side-by-side)
4. **Ranking** (qualitative ordering with direct reasons)
5. **Overall synthesis** — if this is an investment or decision context, state which topics have the strongest qualitative profile and why. Do not fabricate conclusions.
