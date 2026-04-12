---
name: gitflow
description: 'Prepare this FCE tutor workspace for git commits. Use when saving study materials, organizing repo changes, reviewing .gitignore relevance, grouping related edits into sensible commit batches, writing commit messages, and aligning repository snapshots with stored learning progress and memory.'
argument-hint: 'Commit scope, whether to commit now, and whether to split changes into batches'
user-invocable: true
---

# Gitflow

## What this skill does

This skill prepares or performs clean git snapshots for the study workspace while keeping repository state aligned with learning state.

## When to use

- The user wants to save study progress to git.
- There are multiple unrelated changes that should be split.
- `.gitignore` may need a quick sanity check.
- A logical study checkpoint should also be reflected in memory files.

## Procedure

1. Review changed files and identify natural commit groups.
2. Check whether generated or temporary files should stay ignored.
3. Confirm that learning state files are consistent with the saved materials.
4. If needed, suggest a commit split such as:
   - tutor configuration,
   - new exercises,
   - checked work and feedback,
   - progress and memory updates.
5. Write short, specific commit messages tied to actual changes.
6. If the user asked to commit, use non-interactive git commands only.
7. Never rewrite unrelated history unless explicitly requested.

## Commit message standard

- Use factual messages.
- Prefer messages that reflect learning milestones or repo structure changes.
- Avoid vague messages like `update files`.

## Memory alignment rule

Before or alongside a commit, check whether `User/` and relevant progress files need a small update so that the repository snapshot and the learning snapshot make sense together.
