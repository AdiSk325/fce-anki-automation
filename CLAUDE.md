# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This is a personal AI-powered tutoring workspace for Cambridge B2 First (FCE) exam preparation. It is not a software application — it is a structured learning archive where an AI tutor (agent) manages exercises, writing feedback, Anki flashcards, and progress memory across sessions.

The full role specification for the AI tutor is defined in `.github/copilot-instructions.md`. Read it before every substantive session.

## Scripts

All scripts use Python stdlib only (no dependencies to install).

```bash
# Download a podcast transcript from URL
python scripts/fetch_podcast_transcript.py <URL>

# Validate one or more Anki TSV files
python scripts/validate_output.py output/fce-*.tsv
python scripts/validate_output.py output/  # validates all TSVs in directory

# Validate with explicit type
python scripts/validate_output.py output/file.tsv --type vocabulary

# Merge multiple TSV files into one deck
python scripts/merge_decks.py output/*.tsv -o output/merged.tsv
```

Supported `--type` values for validation: `vocabulary`, `grammar`, `phrasal-verbs`, `collocations`, `use-of-english`.

## Architecture

### Session Flow

Every tutor session follows a mandatory three-step wrapper:

1. **Context** — Read relevant files from `knowledge/`, `User/`, and the applicable `practice/` subdirectory before acting.
2. **Action** — Perform the pedagogical task.
3. **Save** — Write any output that has lasting value to the repo, and update `User/` files if the session revealed something new about the user's progress, mistakes, or behavior.

### Persistent Memory (`User/`)

Four files hold operational state about the learner. These are the primary personalization source and must be kept current:

| File | Holds |
|------|-------|
| `current_goals.md` | Active study priorities and targets |
| `user_progress.md` | Achievements, diagnostic results, confidence levels |
| `most_popular_mistakes.md` | Recurring language and exam technique errors |
| `user_behavior.md` | How the user learns best; what task formats work |

Update these files after any session that reveals a new pattern. Do not duplicate information across files.

### Anki Module

TSV files in `output/` follow strict schemas defined in `templates/note-types.md`. Five card types are supported, each with its own column set:

| Type | Columns |
|------|---------|
| `FCE Vocabulary` | Front, Back, Example, Tags |
| `FCE Grammar` | Rule, Explanation, Examples, CommonMistakes, Tags |
| `FCE Phrasal Verbs` | PhrasalVerb, Meaning, Examples, Synonyms, Tags |
| `FCE Collocations` | Collocation, Translation, Example, Type, Tags |
| `FCE Use of English` | Task, Answer, Explanation, Type, Tags |

Format: TSV, UTF-8 without BOM. Always validate with `validate_output.py` before treating a file as ready to import.

The Anki cycle is: diagnose gaps → generate TSV → validate → user studies in Anki → create active recall check in `practice/anki-checks/` → grade check → update memory.

### File Naming Convention

All exercise and material files use `YYYY-MM-DD-descriptive-slug.md`. This enables chronological sorting and links between related files (e.g., a repair drill created the day after a diagnostic).

### Directory Routing

| What | Where |
|------|-------|
| User's raw writing submissions | `practice/writing/raw/` |
| Writing feedback | `practice/writing/feedback/` |
| Corrected/model versions | `practice/writing/corrected/` |
| Grammar, vocabulary, reading/UoE, speaking, listening exercises | `practice/<type>/` |
| Active recall tests post-Anki | `practice/anki-checks/` |
| Podcast transcripts (downloaded) | `input/podcast-transcripts/` |
| Vocabulary notes from podcasts | `materials/podcast-notes/` |
| Weekly schedules and sprint plans | `plans/weekly/` |
| Progress reports and assessments | `progress/` |
| Ready-to-import Anki TSV files | `output/` |
| Source word lists and raw inputs | `input/` |

### Skills

Eight reusable skills live in `.github/skills/` and cover the most common multi-step workflows. Prefer a skill over improvising a process from scratch when one fits:

| Skill | Use when |
|-------|---------|
| `/create-exercise` | Generating a new exercise, worksheet, or test |
| `/check-exercise` | Grading completed work and logging errors to memory |
| `/anki-cycle` | Running the full Anki learn→check loop |
| `/progress-feedback` | Synthesizing a progress report and next priorities |
| `/memory-checkpoint` | Cleaning and consolidating `User/` files |
| `/gitflow` | Creating logical commits that reflect study milestones |
| `/study-plan` | Building weekly or sprint plans |
| `/podcast-episode-agent` | Podcast URL → transcript + vocab notes + grammar exercise + listening exercise |

### Prompt Templates

`.github/prompts/` holds nine templates for generating TSV card sets and running specific session types. The five TSV-generating prompts (`vocabulary`, `grammar`, `phrasal-verbs`, `collocations`, `use-of-english`) produce output ready for `validate_output.py`.

## Language Convention

- Instructions and feedback to the user: **Polish**
- Exercise content, model answers, and exam material: **English**
- File names, tags, task type labels: **English, lowercase, kebab-case**

## Key Reference Files

Read these to understand exam structure and current learner state before creating exercises or plans:

- `knowledge/expert_knowledge.md` — authoritative Cambridge B2 First exam facts; always prefer this over general knowledge when stating exam specifics
- `User/current_goals.md` — what the user is working toward right now
- `User/most_popular_mistakes.md` — personalize exercises against these
- `docs/workflow.md` — canonical session flow with worked examples
- `docs/anki-import-guide.md` — full Anki setup and import steps
