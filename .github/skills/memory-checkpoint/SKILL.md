---
name: memory-checkpoint
description: 'Review and clean the tutor memory context for this FCE workspace. Use when context is too large, the session is drifting, memory files are outdated, duplicated, or inconsistent, or when the user wants a clean checkpoint of goals, progress, mistakes, and study state.'
argument-hint: 'Scope: full repo memory refresh or only goals/progress/mistakes'
user-invocable: true
---

# Memory Checkpoint

## What this skill does

This skill keeps the project memory compact, accurate, and useful for future tutoring sessions.

## When to use

- Session context has become noisy or unfocused.
- Memory files repeat the same information.
- Goals or progress files no longer reflect reality.
- The user wants a fresh checkpoint before a new study phase.

## Memory areas to review

- `User/current_goals.md`
- `User/user_progress.md`
- `User/most_popular_mistakes.md`
- `User/user_behavior.md`
- repo memory notes if they exist

## Procedure

1. Read the current memory files.
2. Remove duplication in meaning, not just wording.
3. Preserve stable facts and discard one-off noise.
4. Ensure goals, progress, and mistakes are aligned with current study reality.
5. If necessary, rewrite sections so they are shorter and more operational.
6. Keep entries factual, reusable, and easy to build on in future sessions.
7. If the repo state has materially changed, update repo memory notes as well.

## Output standard

- Keep memory concise.
- Prefer stable patterns over temporary details.
- Do not invent progress that is not supported by saved work.
- End by stating what the tutor should prioritize next time.
