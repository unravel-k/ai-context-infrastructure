# Check Inline Citations

Scan a draft and flag every factual claim that's missing an inline citation. Verify citations are at the point of use, not deferred to footnotes or a bibliography. This skill checks citation placement and coverage — it does not verify whether the citations are real (use `verify-citations` for that).

## Workflow

### Step 1: Receive the Draft

Accept the text or document to check. This can be any output containing factual claims — research reports, analysis, articles, presentations.

### Step 2: Identify All Factual Claims

Scan the text and extract every sentence or paragraph that asserts a fact. Includes:
- Numerical claims ("revenue grew 15%")
- Causal claims ("supply crunch caused the price spike")
- Predictive claims ("demand will outpace supply by Q3")
- Comparative claims ("X outperforms Y")
- Attribution claims ("according to..." / "experts say...")
- Historical claims ("in 2020, the company launched...")

Exclude opinions clearly marked as such ("I believe...", "in my view...").

### Step 3: Check Each Claim for an Inline Citation

For each factual claim, check whether it has an inline citation:
- A parenthetical reference: `(Source, 2024)` or `[1]`
- A hyperlink on the claim text: `[claim](URL)`
- A named source in the same sentence: "According to Bloomberg..."
- A footnote/endnote marker at the claim: `claim¹`

An inline citation means the source is traceable from the claim itself without scanning the whole document.

### Step 4: Classify Each Claim

| Classification | Meaning |
|---------------|---------|
| Properly cited | Claim has an inline citation at point of use |
| Bibliography-only | Source is in a bibliography/footnotes section but not linked inline |
| Missing citation | No source provided for a factual claim |
| Unclear attribution | Vague reference ("studies show", "experts say") without specific source |

### Step 5: Check Citation Placement

For claims that have citations, verify the citation is at the point of use — the same sentence or immediately after. Flag citations that are:
- Deferred to a separate "Sources" section with no inline marker
- Clumped at paragraph end without per-claim linking
- Missing from the text but present in a footnote appendix

### Step 6: Return Coverage Report

```
## Inline Citation Coverage Report

### Properly Cited (N / M claims)
- Claim → [citation]
- ...

### Bibliography-Only (N)
- Claim — source in bibliography but not linked inline
- ...

### Missing Citations (N)
- Claim — no source found
- ...

### Unclear Attribution (N)
- Claim — "studies show" → which studies?
- ...

### Summary
N factual claims found, N properly cited (X%), N bibliography-only, N missing, N unclear.
Coverage: <qualitative>. Recommendation: <fix suggestions>.
```

Do not add citations. Do not fabricate sources. Only report what exists and what's missing.
