---
name: progress-feedback
description: 'Summarize the user progress, study patterns, results, strengths, weaknesses, and next priorities for B2 First. Use when the user asks for feedback, progress review, diagnosis, confidence check, learning recommendations, or wants a clear picture of what to study next.'
argument-hint: 'Time range, paper focus, or ask for full progress review'
user-invocable: true
---

# Progress Feedback

## What this skill does

This skill produces a clear progress snapshot from the repo and turns it into actionable recommendations.

## When to use

- The user asks how they are doing.
- The user wants a summary of strengths and weaknesses.
- The user wants next-step recommendations.
- The repo contains enough recent material to draw conclusions.

## Required context

Check as relevant:

- `User/current_goals.md`
- `User/user_progress.md`
- `User/most_popular_mistakes.md`
- `User/user_behavior.md`
- recent materials in `practice/`, `plans/`, and `progress/`

## Procedure

1. Summarize current status by paper or skill area.
2. Separate stable strengths from temporary wins.
3. Identify the highest-value weak points affecting exam performance.
4. Recommend concrete next exercises, not vague advice.
5. If useful, create or update a report in `progress/reports/`.
6. If goals have changed, update `User/current_goals.md`.

## Output format

The response should usually contain:

- current level snapshot,
- strongest areas,
- weakest areas,
- priority order,
- recommended next exercises,
- optional weekly focus.

## Do not use when

- The user mainly wants a new exercise created.
- The user mainly wants an existing exercise checked.
