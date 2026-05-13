# Agent Workflow Contract

This repository uses an issue-first workflow. These instructions apply to all
agentic coding tools and human contributors working in this repo.

## Non-Negotiable Workflow

No implementation work may start without a GitHub issue.

Every unit of work must follow this sequence:

1. Plan the work.
2. Create or identify the GitHub issue.
3. Create a dedicated branch for that issue.
4. Implement only the scoped issue work.
5. Run the relevant validation.
6. Push the branch to GitHub.
7. Open a pull request linked to the issue.

Do not skip steps. Do not batch unrelated issues into one branch or PR.

## Issue Requirements

Before editing files, confirm the issue exists and has enough detail to act on.
If it does not, update the issue or create a new one before continuing.

Each issue should include:

- Goal
- Scope
- Acceptance criteria
- Validation plan
- Known dependencies or blockers

Use one issue per independently reviewable change.

## Branch Rules

Create one branch per issue from the current target branch, normally
`origin/main`.

Branch naming:

```text
issue-<number>-short-description
```

Examples:

```text
issue-3-agent-workflow
issue-7-v0-rag-agent
```

Do not branch from a local branch containing unrelated or unmerged work unless
the user explicitly approves stacking PRs.

## Implementation Rules

Keep changes tightly scoped to the issue.

Do not:

- Revert unrelated user changes.
- Include opportunistic refactors.
- Edit generated or dependency output unless the issue requires it.
- Mix documentation, infrastructure, and feature work unless the issue covers
  that exact combined scope.

If new requirements appear while working, create a follow-up issue instead of
expanding the branch silently.

## Validation Rules

Run the narrowest meaningful validation for the change before pushing.

Examples:

- Documentation-only change: `git diff --check`
- Astro blog change: `ASTRO_TELEMETRY_DISABLED=1 npm run build`
- Python lab code: the relevant unit tests plus any documented smoke test
- Docker lab change: the relevant `docker compose` command or a documented
  reason it was not run

If validation cannot be run, document the reason in the PR.

## Commit Rules

Commits must be intentional and signed when repository rules require it.

Commit messages should be short and scoped:

```text
Add agent workflow contract
Scaffold v0 lab structure
Implement v0 RAG retrieval
```

Avoid committing local secrets, real credentials, generated caches, or build
outputs.

## Pull Request Rules

Every completed branch must be pushed and opened as a PR.

PR titles must reference the issue:

```text
[#<issue>] Short description
```

PR bodies must include:

- Linked issue using `Closes #<issue>` or `Refs #<issue>`
- Summary of changes
- Validation performed
- Known limitations or follow-up issues

Draft PRs are acceptable while work is incomplete. Ready PRs must have passing
validation or a clearly documented blocker.

## Safety Rules For Lab Work

The AI red-team lab is intentionally vulnerable. Keep it isolated.

Do not add:

- Real credentials
- Real cloud resources without explicit issue scope and approval
- Host filesystem mounts containing personal data
- Host network mode for vulnerable services
- Third-party probing workflows without written authorization

Vulnerable behavior must be limited to owned lab targets.

## Conflict Handling

If local state conflicts with this workflow, stop and resolve the workflow
first.

Examples:

- If there is no issue, create one.
- If on the wrong branch, create or switch to the issue branch.
- If unrelated files are modified, do not stage them.
- If a PR would include another unmerged PR, ask before stacking.
- If GitHub rejects a push, fix the repository rule violation before opening
  or updating the PR.

The workflow is part of the work product. A change is not complete until the PR
exists and links back to the issue.
