---
name: study-plan
description: 'Build a realistic FCE study plan, weekly schedule, sprint, revision cycle, or mock-exam roadmap based on current goals, progress, and repeated mistakes. Use when the user asks for a plan, roadmap, schedule, revision priorities, or wants to rebalance work across papers.'
argument-hint: 'Time horizon, available time, and whether to focus on one paper or full exam balance'
user-invocable: true
---

# Study Plan

## What this skill does

This skill turns saved progress and current priorities into a practical learning plan.

## When to use

- The user asks for a weekly plan or revision schedule.
- Current work is unbalanced across papers.
- The user wants a mock-exam plan or a recovery plan after weak results.

## Required context

- `User/current_goals.md`
- `User/user_progress.md`
- `User/most_popular_mistakes.md`
- recent files in `practice/` and `progress/`

## Procedure

1. Identify the highest-value priorities.
2. Balance productive and receptive skills.
3. Include active practice, review, and correction.
4. Include Anki only where it genuinely supports the plan.
5. Save reusable plans in `plans/weekly/` or `plans/mock-exams/`.
6. Update `User/current_goals.md` if the priorities become sharper.

## Output standard

- Make the plan realistic.
- Prefer a manageable plan the user can complete over an idealized plan they will abandon.
- Every plan should include at least one checkpoint.
