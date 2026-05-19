# Verify Citations

Verify that citations and references in a text point to real, matching sources. Catch hallucinated URLs, broken links, misattributed claims, and fabricated references. Can be used standalone or called as a subroutine by other skills.

## Workflow

### Step 1: Receive the Draft

Accept the text or document to verify. This can be:
- Output from `for-and-against`, `multi-views`, `risk-analysis`, or any other skill
- A user-pasted article, report, or analysis
- Any text containing URLs, source references, or attribution claims

### Step 2: Extract All Citations

Scan the text and extract every citation. For each, capture:
- The URL (if present)
- The title or publication name
- The author name (if present)
- The claim it supports (the sentence or paragraph where the citation appears)

### Step 3: Verify Each Citation

For each citation, attempt verification in this order:

1. **URL resolution** — Does the URL load a real page? (HTTP 200, not 404/500)
2. **Content match** — Does the page content actually support the claim? Or is the citation irrelevant/misapplied?
3. **Title/author match** — Do the title and author at the URL match what was cited?
4. **Publication date** — Is the source from the timeframe implied by the claim?

If the `claude-skill-citation-checker` tool is available, use it for automated verification. Otherwise, use web fetch to manually verify each URL.

### Step 4: Classify Each Citation

Label every citation with one of:

| Classification | Meaning |
|---------------|---------|
| Verified | URL resolves, content matches the claim |
| Broken link | URL returns 404, 500, or does not resolve |
| Hallucinated | URL looks real but does not exist, or content is completely unrelated |
| Misattributed | URL and content exist, but author/title/date are wrong |
| Unverifiable | Paywalled, login-walled, or otherwise inaccessible |

### Step 5: Flag or Remove

- **Verified** — Leave in place. Optionally add a verification mark.
- **Broken link** — Flag: *(broken link)*. Suggest archiving or finding an alternate source.
- **Hallucinated** — Remove the citation mark. If the claim is corroborated by other verified sources, keep the claim and flag *(citation unverified)*. If no other source supports the claim, flag the claim itself.
- **Misattributed** — Correct the title/author/date. Keep the URL if it still supports the claim.
- **Unverifiable** — Flag: *(source inaccessible)*.

### Step 6: Return Verification Report

Present the results:

```
## Citation Verification Report

### Verified (N)
- [1] URL — title — claim summary
- [2] ...

### Broken Links (N)
- [3] URL — error — claim summary

### Hallucinated (N)
- [4] URL — why it fails — affected claim

### Misattributed (N)
- [5] URL — corrected: title/author → actual title/author

### Unverifiable (N)
- [6] URL — reason (paywall, login, etc.)

### Summary
N citations checked, N verified, N flagged, N removed. Overall reliability: <qualitative>.
```
