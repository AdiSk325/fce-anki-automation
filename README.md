# FCE Tutor Workspace

To repo nie jest już tylko generatorem fiszek. To kompletna, osobista przestrzeń do przygotowania do egzaminu Cambridge B2 First, w której GitHub Copilot działa jako tutor, trener egzaminacyjny, recenzent prac i opiekun spersonalizowanego systemu nauki.

## Cel projektu

Jedyny główny cel projektu to pomoc w skutecznym przygotowaniu i zdaniu egzaminu B2 First. Oznacza to połączenie w jednym miejscu:

- wiedzy eksperckiej o egzaminie,
- codziennej pracy z tutorem AI,
- trwałej pamięci o postępach i błędach,
- archiwum ćwiczeń i materiałów,
- modułu Anki do powtórek słownictwa, gramatyki i Use of English.

## Jak działa tutor

Domyślny agent projektu pracuje w trybie:

1. analizuje kontekst bieżącej nauki,
2. wykonuje zadanie dydaktyczne,
3. zapisuje postępy, błędy i nowe ustalenia.

W praktyce oznacza to, że po każdej sensownej sesji repo może zostać zaktualizowane o:

- nowe ćwiczenia,
- ocenę writingu lub speakingu,
- wnioski o najczęstszych błędach,
- aktualny plan nauki,
- materiały Anki do dalszej pracy.

## Struktura projektu

```text
fce-anki-automation/
├── .github/
│   ├── copilot-instructions.md
│   └── prompts/
├── User/
│   ├── current_goals.md
│   ├── most_popular_mistakes.md
│   ├── user_behavior.md
│   └── user_progress.md
├── knowledge/
│   └── expert_knowledge.md
├── practice/
│   ├── anki-checks/
│   ├── grammar/
│   ├── listening/
│   ├── reading-use-of-english/
│   ├── speaking/
│   ├── vocabulary/
│   └── writing/
│       ├── corrected/
│       ├── feedback/
│       └── raw/
├── plans/
│   ├── mock-exams/
│   └── weekly/
├── progress/
│   ├── assessments/
│   └── reports/
├── materials/
│   ├── lesson-notes/
│   └── reference/
├── input/
├── output/
├── scripts/
├── templates/
└── docs/
```

## Szybki start

### 1. Zacznij od pracy z tutorem

Przykładowe polecenia do Copilot Chat:

```text
Przeanalizuj moje cele, błędy i aktualny progress, a potem przygotuj mi plan nauki na 7 dni pod FCE.
```

```text
Przeprowadź ze mną Writing Part 1. Najpierw daj task, potem oceń mój tekst i zapisz raw, feedback i corrected do odpowiednich katalogów.
```

```text
Przygotuj mi 12 zadań Use of English celowanych w moje najczęstsze błędy i zapisz je do practice/reading-use-of-english/.
```

```text
Weź ten odcinek podcastu z transkrypcją i przygotuj pełny pakiet: słówka + grammar + listening B2 First z answer key.
```

### 2. Używaj Anki jako modułu powtórek

Moduł Anki nadal działa i jest wspierany przez istniejące prompty oraz skrypty walidacyjne. Tutor może generować fiszki, zlecać ich naukę i później sprawdzać aktywne użycie materiału.

### 3. Archiwizuj realną pracę

- własne teksty zapisuj w `practice/writing/raw/`,
- wspólne poprawki w `practice/writing/corrected/`,
- oceny i komentarze w `practice/writing/feedback/`,
- testy i zestawy ćwiczeń w odpowiednich katalogach `practice/`,
- plany nauki w `plans/`,
- raporty postępu w `progress/`.

## Najważniejsze pliki startowe

- [docs/workflow.md](docs/workflow.md)
- [docs/study-system.md](docs/study-system.md)
- [docs/skills-guide.md](docs/skills-guide.md)
- [knowledge/expert_knowledge.md](knowledge/expert_knowledge.md)
- [docs/fce-topics.md](docs/fce-topics.md)
- [docs/anki-import-guide.md](docs/anki-import-guide.md)
- [templates/note-types.md](templates/note-types.md)

## Moduł Anki

Obsługiwane typy materiałów:

- vocabulary,
- grammar,
- phrasal verbs,
- collocations,
- use of english.

Promptów do generowania fiszek nadal używa się z katalogu `.github/prompts/`, a gotowe pliki można walidować skryptem `scripts/validate_output.py` i łączyć `scripts/merge_decks.py`.

## Workflow podcast -> pakiet FCE

Repo obsługuje teraz pełny workflow oparty na transkrypcjach podcastów:

- pobranie transkrypcji do `input/podcast-transcripts/` przez `scripts/fetch_podcast_transcript.py`,
- przygotowanie notatki słownictwa do `materials/podcast-notes/`,
- przygotowanie ćwiczenia gramatycznego do `practice/grammar/`,
- przygotowanie ćwiczenia Listening B2 First + answer key (z referencjami do linii transkrypcji) do `practice/listening/`.

Do tego workflow możesz użyć skilla `podcast-episode-agent` albo promptu `.github/prompts/podcast-episode-workflow.prompt.md`.

## Oficjalna podstawa wiedzy

Ekspercka wiedza agenta została oparta na oficjalnych materiałach Cambridge dotyczących B2 First, podsumowanych w [knowledge/expert_knowledge.md](knowledge/expert_knowledge.md). Ten plik jest źródłem referencyjnym dla struktury egzaminu, typów zadań i oczekiwań wobec kandydata.

## Licencja

Projekt edukacyjny do użytku osobistego.
