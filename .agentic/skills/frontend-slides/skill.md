# Frontend Slides

Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. This skill references the canonical implementation at https://github.com/zarazhangrui/frontend-slides.

## Workflow

### Step 1: Discover Intent

Ask the user:
- What is the presentation about?
- Is there an existing PowerPoint to convert, or should it be built from scratch?
- What emotional tone should the slides convey? (e.g., impressed, excited, calm, urgent)

### Step 2: Plan Content

If building from scratch, outline the slide structure:
- Title slide
- Key message slides (3-7)
- Supporting evidence slides (data, charts, quotes)
- Closing slide

If converting from PPTX, run `scripts/extract-pptx.py` on the uploaded file to extract text, images, and speaker notes.

### Step 3: Style Discovery

Generate 3 visual previews with different style presets from `STYLE_PRESETS.md`. Let the user compare and pick one. Do not ask the user to describe design preferences in words — let them choose visually.

### Step 4: Generate

Produce a single self-contained HTML file using:
- The chosen style preset
- `viewport-base.css` for responsive layout
- `html-template.md` for slide structure and navigation
- `animation-patterns.md` for CSS/JS animations

The output is a single HTML file that works in any modern browser with no build step.

### Step 5: Offer Deployment

Ask the user whether to deploy:
- Run `scripts/deploy.sh` to publish to Vercel for a shareable URL
- Run `scripts/export-pdf.sh` to convert slides to a PDF

## Required Files (from canonical repo)

| File | Role |
|------|------|
| `SKILL.md` | Core workflow, rules, and prompts |
| `STYLE_PRESETS.md` | 12 curated visual themes |
| `viewport-base.css` | Responsive CSS framework |
| `html-template.md` | HTML structure, JS navigation |
| `animation-patterns.md` | CSS/JS animation library |
| `scripts/extract-pptx.py` | PPTX content extraction |
| `scripts/deploy.sh` | Vercel deployment |
| `scripts/export-pdf.sh` | PDF export via Playwright |

## Attribution

Canonical implementation: [frontend-slides](https://github.com/zarazhangrui/frontend-slides) by zarazhangrui.
