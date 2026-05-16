# Universal Axioms

These axioms apply to all routes and all tasks. No route may contradict them.

## AX-UNIV-001: Safety First

Never execute or suggest destructive actions without explicit user confirmation. This includes:
- Deleting files or directories
- Dropping database tables
- Force-pushing to shared branches
- Running commands that could affect production environments

## AX-UNIV-002: Security Awareness

Never introduce security vulnerabilities. Specifically:
- No command injection (shell=True with unsanitized input)
- No XSS vectors
- No hardcoded secrets or credentials
- No SQL injection
- Validate at system boundaries

## AX-UNIV-003: Portable Doctrine

`.agentic/` is the canonical source of truth. `.claude/` is only an adapter layer.
- Do not duplicate canonical content from `.agentic/` into `.claude/`.
- `.claude/` SKILL.md files should reference `.agentic/` files, not duplicate them.
- When updating doctrine, always update `.agentic/` first, then the adapter.

## AX-UNIV-004: Minimal Change

Prefer the smallest change that achieves the goal.
- Edit existing files rather than creating new ones when possible.
- Do not refactor or add abstractions beyond what the task requires.
- Do not add error handling for scenarios that cannot happen.

## AX-UNIV-005: Verify Before Claiming Done

Always verify work before reporting completion.
- Run validation scripts when provided.
- Run tests when provided.
- If you cannot verify, say so explicitly.
