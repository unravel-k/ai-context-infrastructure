# Dangerous Actions Guardrail

This guardrail defines actions that require explicit user confirmation before execution.

## Destructive Actions (always require confirmation)

- Deleting files or directories (rm, rmdir, del)
- Force-pushing to shared branches (git push --force)
- Dropping database tables or collections
- Killing processes
- Overwriting uncommitted changes
- Removing or downgrading packages without discussion
- Modifying CI/CD pipelines
- Sending messages to external services (Slack, email, GitHub)

## Hard-to-Reverse Actions (require confirmation)

- Amending published commits
- Resetting branches (git reset --hard)
- Force-pushing to remote
- Creating/closing/commenting on PRs or issues
- Uploading content to third-party tools

## Safe Actions (no confirmation needed)

- Reading files
- Editing files locally
- Creating new branches
- Creating new commits (not amending)
- Running tests
- Installing dependencies in a local environment
