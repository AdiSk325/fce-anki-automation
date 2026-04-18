---
name: podcast-episode-agent
description: 'Build a full FCE learning package from a podcast transcript: download transcript, create vocabulary note, grammar exercise, and B2 First listening task with answer key and source references.'
argument-hint: 'Episode URL, optional listening task subtype, and target difficulty'
user-invocable: true
---

# Podcast Episode Agent

## What this skill does

This skill creates a complete learning package from one podcast episode transcript and stores all reusable artifacts in the repository.

## When to use

- The user provides a podcast episode URL with transcript.
- The user asks for transcript-based vocabulary and exam practice.
- The user wants a B2 First listening worksheet plus answer key with references to source transcript lines.

## Required context

Review before work:

- `knowledge/expert_knowledge.md`
- `User/current_goals.md`
- `User/user_progress.md`
- `User/most_popular_mistakes.md`
- existing files in `practice/listening/`, `practice/grammar/`, `practice/vocabulary/`, `materials/`

## Procedure

1. Download transcript from the episode URL:
   - run from repo root: `python scripts/fetch_podcast_transcript.py <URL>` (Python 3 required)
   - output goes to `input/podcast-transcripts/YYYY-MM-DD-episode-slug.md`
2. Read the downloaded transcript and identify:
   - topic and core message,
   - highlighted/new lexical items,
   - grammar pattern especially visible in the episode.
3. Create vocabulary note markdown in:
   - `materials/podcast-notes/YYYY-MM-DD-episode-slug-vocabulary.md`
   - for each item include: word/phrase, EN definition, EN example, PL translation.
4. Create grammar exercise markdown in:
   - `practice/grammar/YYYY-MM-DD-episode-slug-grammar.md`
   - choose the most relevant grammar focus from the transcript and build a targeted exercise.
5. Create B2 First listening task in:
   - worksheet: `practice/listening/YYYY-MM-DD-episode-slug-listening-task.md`
   - answer key: `practice/listening/YYYY-MM-DD-episode-slug-listening-answers.md`
6. In answer key include explicit source references:
   - point to numbered transcript lines from `input/podcast-transcripts/...` for each answer.
7. Keep language standards:
   - operational instructions in Polish,
   - task content in English,
   - naming in english lowercase/kebab-case where possible.
8. Update `User/user_progress.md` if this introduces a meaningful new practice block.

## Output standard

### Vocabulary note structure

- Episode metadata (url, date, topic)
- Table or list with fields:
  - item
  - definition (EN)
  - example (EN)
  - translation (PL)
- Short “next step” for converting into Anki cards

### Grammar exercise structure

- Why this grammar point fits this episode
- Clear instructions
- Exercise set
- Answer key section

### Listening package structure

- Part type aligned with B2 First listening logic
- Instructions and scoring guidance
- Questions section
- Separate answer key file with:
  - correct answer,
  - short explanation,
  - transcript line reference(s)

## Do not use when

- The user only asks to check a finished exercise.
- The user does not provide an episode URL and does not want transcript-based work.
