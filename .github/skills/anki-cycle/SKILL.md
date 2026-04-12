---
name: anki-cycle
description: 'Run the full Anki learning cycle for FCE: diagnose what should become cards, generate or extend flashcards, validate TSV output, assign review use, and create follow-up active recall checks. Use when the user wants to learn with Anki as part of a broader study workflow.'
argument-hint: 'Topic, source material, card type, and whether to add follow-up checks'
user-invocable: true
---

# Anki Cycle

## What this skill does

This skill treats Anki as one stage in the tutoring system rather than a standalone output generator.

## When to use

- The user wants new cards from current weaknesses or source notes.
- A lesson or checked exercise produced material worth memorizing.
- The user wants follow-up exercises after learning cards.

## Required context

Review:

- `templates/note-types.md`
- relevant prompt files in `.github/prompts/`
- `docs/anki-import-guide.md`
- `User/most_popular_mistakes.md`
- relevant source material in `input/`, `practice/`, or `materials/`

## Procedure

1. Decide what belongs in flashcards and what should stay as active practice only.
2. Choose the right Anki note type.
3. Generate or update TSV material in `output/`.
4. Validate with `scripts/validate_output.py` when relevant.
5. Tell the user how the cards fit into the current study plan.
6. Create a follow-up check in `practice/anki-checks/` when the cards are intended for real retention.
7. If the cards come from repeated mistakes, update memory so the tutor knows why these cards exist.

## Important rule

Do not stop at card creation if the user clearly needs transfer into active use. Add a recall, gap-fill, speaking, or writing follow-up when appropriate.
