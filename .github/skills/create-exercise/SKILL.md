---
name: create-exercise
description: 'Create a personalized FCE exercise, practice task, worksheet, mini-test, homework set, or paper fragment. Use when the user asks to practise grammar, vocabulary, writing, speaking, listening, reading, Use of English, or wants a targeted task based on weaknesses. Save the exercise in the appropriate practice or plans folder and give clear instructions.'
argument-hint: 'Topic, paper, difficulty, number of tasks, and any weakness to target'
user-invocable: true
---

# Create Exercise

## What this skill does

This skill creates reusable learning material tailored to the user's current FCE needs and stores it in the repository.

## When to use

- The user wants to practise a topic or exam paper.
- The user asks for homework, a worksheet, a mini-test, or a drill set.
- The exercise should target known mistakes, weak areas, or a specific paper.
- The result should be saved in the repo for later revision.

## Required context

Check these sources before creating the exercise:

- `knowledge/expert_knowledge.md`
- `User/current_goals.md`
- `User/user_progress.md`
- `User/most_popular_mistakes.md`
- relevant existing files in `practice/` and `plans/`

## Procedure

1. Identify the paper, subskill, topic, level of difficulty, and whether the task is diagnostic, practice, homework, or revision.
2. Review the user's current goals and repeated mistakes so the task is genuinely personalized.
3. Create an exercise that matches the logic of B2 First rather than a generic English task.
4. Save the material in the most suitable folder:
   - `practice/grammar/`
   - `practice/vocabulary/`
   - `practice/reading-use-of-english/`
   - `practice/listening/`
   - `practice/speaking/`
   - `practice/writing/raw/` only for the user's own submission, not for generated prompts
   - `plans/mock-exams/` for larger exam simulations
5. Use a clear file name in the format `YYYY-MM-DD-short-description.md`.
6. In the chat response, explain briefly:
   - what the task trains,
   - how to complete it,
   - how the user should send answers back.
7. If the exercise is meant to reinforce memory, suggest a follow-up Anki or active recall step.

## Output standard

- Instructions for the user are in Polish.
- Exercise content is mainly in English.
- The file should be reusable without extra explanation from the chat.
- If an answer key is included, separate it clearly from the task section.

## Do not use when

- The main request is checking an already completed exercise.
- The main request is summarizing progress or updating memory.
