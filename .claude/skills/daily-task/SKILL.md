---
name: daily-task
description: 'Tell the learner what to do today in this FCE workspace, sized to the day: a 10-15 minute task on weekdays, the Writing task or a pending Anki check at the weekend. Use when the user asks what to do today, wants a quick task, says they have a few minutes, or invokes /daily-task.'
argument-hint: 'Optional: available time today (e.g. 10 min, 1 h) or a preferred area'
user-invocable: true
---

# Daily Task

## What this skill does

Gives the learner one concrete task for today and nothing more, based on the current weekly plan and the learner's memory files. The answer should fit on a phone screen.

## Required context

Read only what is needed:

- the newest file in `plans/weekly/` (the current week plan, if it exists),
- `User/current_goals.md` (rhythm, priorities, current focus),
- `User/most_popular_mistakes.md`,
- `Status:` lines in `practice/anki-checks/*.md` and `practice/writing/tasks/*.md`.

## Procedure

1. Determine today's weekday (Europe/Warsaw) and the time the user has. If the user gives no time, assume 10–15 minutes on weekdays and 60–90 minutes at the weekend.
2. If the week plan has a task for today, give it as written (for a micro-task, paste the items into the answer so the user does not need to open the repo).
3. If there is no plan or no task for today:
   - weekday: create one micro-task in the answer (5 items: KWT, open cloze or PL → EN sentences) targeting a recorded mistake or the newest Anki deck,
   - weekend: point to the pending Writing task in `practice/writing/tasks/`; if there is none, the oldest Anki check with status `do zrobienia`.
4. Always end with a one-line reminder about daily Anki reviews and how to hand in answers (paste them in the chat).
5. When the user sends answers later, grade them with the `check-exercise` skill and update the status line or memory files as that skill describes.

## Output standard

- Polish for instructions, English for task content.
- At most one task. No lists of options.
- If an answer key is needed for self-checking, put it after a clear `Klucz` separator.
