# Podcast Episode -> FCE Learning Package

Zbuduj kompletny pakiet nauki na bazie transkrypcji odcinka podcastu.

## Input

- URL odcinka z transkrypcją
- (opcjonalnie) podtyp listening B2 First: `part-1`, `part-2`, `part-3`, `part-4`

## Required workflow

1. Pobierz transkrypcję:
   - uruchom `python3 /home/runner/work/fce-anki-automation/fce-anki-automation/scripts/fetch_podcast_transcript.py <URL>`
2. Zapisz pełny materiał do repo:
   - transcript: `input/podcast-transcripts/YYYY-MM-DD-episode-slug.md`
   - vocabulary: `materials/podcast-notes/YYYY-MM-DD-episode-slug-vocabulary.md`
   - grammar: `practice/grammar/YYYY-MM-DD-episode-slug-grammar.md`
   - listening task: `practice/listening/YYYY-MM-DD-episode-slug-listening-task.md`
   - listening answers: `practice/listening/YYYY-MM-DD-episode-slug-listening-answers.md`

## Vocabulary output requirements

Dla każdego słowa/frazy:

- **Item** (EN)
- **Definition** (EN, B2-friendly)
- **Example** (EN, natural sentence)
- **Translation** (PL)

## Grammar output requirements

- Wybierz zagadnienie najbardziej obecne w transkrypcji.
- Dodaj krótkie uzasadnienie wyboru.
- Przygotuj ćwiczenie celowane i klucz odpowiedzi.

## Listening output requirements

- Zadanie musi odzwierciedlać logikę B2 First Listening.
- Arkusz odpowiedzi ma zawierać:
  - poprawną odpowiedź,
  - krótkie uzasadnienie,
  - odwołanie do numerów linii transkrypcji.

## Language policy

- Instrukcje i meta-komentarze: po polsku.
- Treść zadań i przykłady językowe: po angielsku.
