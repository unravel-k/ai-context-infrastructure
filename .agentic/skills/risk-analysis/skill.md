# Risk Analysis

Evaluate the impact and likelihood of each viewpoint from input data (e.g., for-and-against output, research, or user-provided views). Build a qualitative risk profile showing the relative chances of success across different sides of a bet or decision.

## Workflow

### Step 1: Receive Input Views

Accept views from any source:
- Output from `for-and-against` skill
- User-provided arguments
- Research data, web search results
- MCP or data API output

If the input is already structured (e.g., for-and-against output), preserve the original attribution. If unstructured, ask the user to clarify which sides are being evaluated.

### Step 2: Identify the Sides

List each distinct side of the bet or decision. A "side" is a discrete outcome or position (e.g., "bullish on XYZ", "bearish on XYZ", "XYZ stays flat").

### Step 3: Extract Views Per Side

For each side, extract the individual viewpoints that support it. Each view should have:
- The claim or argument
- The source (preserved from input, with inline citation at point of use per AX-DOM-RESEARCH-ANALYSIS-002)
- The Why, How, Who, When context if available (per AX-DOM-RESEARCH-ANALYSIS-006)
- Any supporting evidence

If the input views lack Why/How/Who/When context, note this as a limitation in the risk profile — views without mechanism or stakeholder context carry higher uncertainty.

### Step 4: Evaluate Impact

For each view, assess: **If this view is correct, how much does it move the outcome?**

Use qualitative labels:

| Impact      | Meaning                                      |
|-------------|----------------------------------------------|
| Critical    | Alone could decide the bet                    |
| High        | Substantially shifts odds                     |
| Medium      | Moves the needle somewhat                     |
| Low         | Minor factor                                  |
| Negligible  | Trivial, unlikely to change anything          |

Explain **why** this impact level was chosen. Where available, use the How and Who context (mechanism and stakeholder incentives) to justify the magnitude of effect. The explanation must reference the magnitude of effect, not the likelihood of the view being true.

### Step 5: Evaluate Likelihood

For each view, assess: **How probable is it that this view is correct?**

Use qualitative labels:

| Likelihood  | Meaning                                      |
|-------------|----------------------------------------------|
| Very High   | Overwhelming evidence / near-certain          |
| High        | Strong evidence, more likely than not          |
| Medium      | Plausible, evidence is mixed                  |
| Low         | Weak evidence, unlikely                       |
| Very Low    | Little to no evidence, speculative            |

Explain **why** this likelihood was chosen. Where available, use the Why and When context (catalyst rationale and timeline) to justify the probability. The explanation must be about the evidence for **this specific side** — not a comparison to other sides. Do not say "less likely than side B." Say "the evidence for this claim is weak because X, Y, Z."

### Step 6: Build the Risk Profile

Create a qualitative profile comparing the sides:

```
## Risk Profile

### Side A: <label>
- Aggregate impact: <qualitative> (explain why — based on the sum of impact-weighted views)
- Aggregate likelihood: <qualitative> (explain why — based on the strength of evidence for this side)
- Chance of success: <qualitative> (explain why — based on impact × likelihood of views supporting this side)
- Key risk: <the view that could most undermine this side>

### Side B: <label>
- Aggregate impact: <qualitative>
- Aggregate likelihood: <qualitative>
- Chance of success: <qualitative>
- Key risk: <the view that could most undermine this side>
```

### Step 7: Qualitative Summary

State which side has the better qualitative chance of success and why. If sides are close, say so. Do not assign numeric probabilities. Use phrases like:

- "Side A has a stronger qualitative profile because..."
- "The evidence leans toward Side B due to..."
- "Sides are roughly balanced; the key differentiator is..."

Every "why" in this summary must be a direct reason about that side, not a comparison. "Side A's chance is stronger because its supporting views have high impact and high likelihood" — not "Side A is better because Side B is weak."
