---
name: frontend-slides
description: Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk/pitch.
---

# Frontend Slides

This is a Claude Code adapter. The canonical source of truth is at `.agentic/skills/frontend-slides/skill.md`. The implementation files are at https://github.com/zarazhangrui/frontend-slides.

## Required Reading

Before executing, read these files in order:

1. `.agentic/router/routes.yaml` — routing context
2. `.agentic/skills/frontend-slides/skill.md` — the full workflow
3. `.agentic/skills/frontend-slides/axioms.md` — skill-specific axioms
4. `.agentic/skills/frontend-slides/checklist.md` — verification checklist
5. `.agentic/skills/frontend-slides/output.md` — expected output format
6. `.agentic/axioms/skills/frontend-slides.md` — canonical axiom definitions
7. `.agentic/axioms/universal.md` — universal axioms

## Execution

Follow the five-step workflow defined in `.agentic/skills/frontend-slides/skill.md`. Generate visual previews — do not ask the user to describe design. Output a single self-contained HTML file. Offer deployment to Vercel or PDF export.

## Install

The implementation files (CSS, scripts, templates) must be installed from the canonical repo:
```bash
git clone https://github.com/zarazhangrui/frontend-slides
```
This adapter only provides the `.agentic/` doctrine layer.

## After Completion

- Verify using `.agentic/skills/frontend-slides/checklist.md`
- Return output in the format defined by `.agentic/skills/frontend-slides/output.md`
