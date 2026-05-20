# Perplexity Search

Search the web via Perplexity's API with structured results, citations, and source attribution. Supports general, finance, news, academic, and other search types. Can be used standalone or as a data source for for-and-against, multi-views, and risk-analysis.

## Prerequisites

Set your Perplexity API key:

```bash
export PERPLEXITY_API_KEY="pplx-..."
```

Get a key at https://perplexity.ai/settings/api.

## Workflow

### Step 1: Receive the Query

Ask the user what to search for. Clarify:
- What is the search query?
- What domain? (finance, news, general)
- Any model preference? (sonar = fast, sonar-reasoning = deep)

### Step 2: Select Model and Domain

| Query type | model | notes |
|-----------|-------|-------|
| Quick factual, prices, metrics | `sonar` | Fast, cheap |
| Complex analysis, reasoning | `sonar-reasoning` | Deep research |
| Financial data specifically | `sonar` + "Use finance context" | Perplexity auto-detects |

### Step 3: Execute the Search

```python
import requests, os

headers = {
    "Authorization": f"Bearer {os.environ['PERPLEXITY_API_KEY']}",
    "Content-Type": "application/json"
}
payload = {
    "model": "<sonar or sonar-reasoning>",
    "messages": [{"role": "user", "content": "<user query>"}]
}
r = requests.post("https://api.perplexity.ai/chat/completions",
                   headers=headers, json=payload)
data = r.json()
```

### Step 4: Parse the Response

The response contains:
- `choices[0].message.content` — the answer text
- `citations` — list of source URLs
- `model` — which model answered

### Step 5: Format with Attribution

Present results with inline citations at point of use (per AX-DOM-RESEARCH-ANALYSIS-002):

```
## Query: <original query>

<answer text>

### Sources
- [1] [URL](URL)
- [2] [URL](URL)
```

Never present a claim without its citation. If the API returns no citations for a factual claim, flag it: *(source unavailable)*.

### Step 6: Return Structured Output

Present findings in a format compatible with downstream skills (for-and-against, risk-analysis, frontend-slides).
