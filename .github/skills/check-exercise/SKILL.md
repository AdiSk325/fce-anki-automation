---
name: check-exercise
description: 'Check a completed FCE exercise, writing task, speaking response, grammar drill, vocabulary task, Use of English set, or mock fragment. Use when the user sends answers and wants correction, scoring, explanation, strengths and weaknesses, plus repository updates with conclusions.'
argument-hint: 'Exercise file or answer source, task type, and whether to save feedback'
user-invocable: true
---

# Check Exercise

## What this skill does

This skill evaluates completed work, gives correction and feedback, and saves useful conclusions back into the repo.

## When to use

- The user has completed an exercise and wants it checked.
- The user wants errors explained, not just marked.
- The result should update progress and repeated mistakes.
- The checked work has archival value.

## Required context

Review:

- the original exercise file,
- `User/user_progress.md`,
- `User/most_popular_mistakes.md`,
- related earlier attempts in `practice/` if they exist.

## Procedure

1. Identify what type of task is being checked and what success looks like.
2. Compare the user's answers against the task requirements or answer key.
3. Give corrections with brief explanations focused on exam usefulness.
4. Separate findings into:
   - what is correct,
   - what is weak,
   - what is repeatedly problematic,
   - what to practise next.
5. Save the feedback in the appropriate place:
   - writing feedback in `practice/writing/feedback/`
   - corrected writing in `practice/writing/corrected/`
   - checked answer sets or review notes in the same `practice/` area as the original task
6. Update `User/most_popular_mistakes.md` if the same type of mistake appears again.
7. Update `User/user_progress.md` if the attempt shows a meaningful change in ability.
8. End with one concrete next task or repair exercise.

## Output standard

- Feedback is practical and specific.
- Polish is used for explanation to the user.
- English is used where the original task content needs to be quoted or corrected.
- If scoring is approximate, state that clearly.

## Special case: writing

If the task is writing, also follow the standards already defined in `copilot-instructions.md` for raw, feedback, and corrected versions.
