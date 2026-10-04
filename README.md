# FCE Tutor Workspace

Osobista przestrzeń do przygotowania do egzaminu Cambridge B2 First. Tutorem jest Claude (Claude Code): planuje naukę, tworzy ćwiczenia i talie Anki z Twoich materiałów, ocenia prace i pamięta postępy w plikach `User/`. Repo jest jednocześnie archiwum całej pracy.

## Jak wygląda tydzień

| Kiedy | Co robisz | Skąd wiesz co |
|-------|-----------|---------------|
| Pn–Pt, 10–15 min | Anki w AnkiDroid + jedno mikro-zadanie | Plan tygodnia w `plans/weekly/`, powiadomienie w poniedziałek rano albo `/daily-task` w czacie |
| Weekend, 60–90 min | Writing + sprawdzian po Anki albo zestaw Use of English | Pakiet na weekend, powiadomienie w piątek po południu |
| Po lekcji z lektorem | Zrzuty stron z Empower i notatek → nowa talia Anki | Prośba w czacie, np. „zrób fiszki z tego materiału” |

Rutyny i ich procedury: [docs/routines.md](docs/routines.md). Długi plan do egzaminu: [plans/2026-10-04-roadmap-b2-first.md](plans/2026-10-04-roadmap-b2-first.md).

## Najczęstsze sytuacje

**Nowy materiał z podręcznika lub lekcji.** Wyślij zrzuty ekranu, razem z kolorowymi zaznaczeniami i dopiskami. Tutor porówna je z istniejącymi taliami, przygotuje karty (znaczenia, zdania do tłumaczenia, zadania w stylu egzaminu) i zbuduje paczkę `.apkg` w `output/`. Paczkę otwierasz na telefonie w AnkiDroid ([instrukcja](docs/anki-import-guide.md)). Ponowny import poprawionej paczki aktualizuje karty i zachowuje historię powtórek.

**Writing.** Zadania są w `practice/writing/tasks/`. Tekst wklejasz w czacie. Ocena według 4 kryteriów Cambridge trafia do `practice/writing/feedback/`, a wersja poprawiona do `practice/writing/corrected/`.

**Sprawdzian po Anki.** Pliki w `practice/anki-checks/` mają w nagłówku status (`do zrobienia` / `sprawdzony`). Odpowiedzi wklejasz w czacie.

**„Co dziś?”** Napisz `/daily-task` – dostaniesz jedno zadanie dopasowane do dnia.

## Komendy (skille)

| Komenda | Do czego |
|---------|----------|
| `/daily-task` | jedno zadanie na dziś |
| `/create-exercise` | nowe ćwiczenie lub test |
| `/check-exercise` | sprawdzenie odpowiedzi lub writingu, zapis błędów |
| `/anki-cycle` | fiszki → nauka → sprawdzian |
| `/study-plan` | plan tygodnia albo sprintu |
| `/progress-feedback` | podsumowanie postępów i priorytety |
| `/memory-checkpoint` | porządek w pamięci tutora |
| `/podcast-episode-agent` | odcinek podcastu → słówka, gramatyka, listening |
| `/gitflow` | porządne commity |

Szczegóły: [docs/skills-guide.md](docs/skills-guide.md).

## Struktura

```text
User/            pamięć tutora: cele, postępy, błędy, sposób pracy
knowledge/       fakty o egzaminie B2 First (źródła Cambridge)
plans/           roadmapa i plany tygodnia
practice/        ćwiczenia, writing (tasks/raw/feedback/corrected), sprawdziany po Anki
progress/        raporty i diagnozy
input/           materiały źródłowe (notatki ze zrzutów, listy słów, transkrypcje)
materials/       notatki z lekcji i podcastów
decks/           źródła talii Anki (Python) → generują output/*.tsv
output/          talie TSV i gotowe paczki .apkg
scripts/         walidacja, budowa paczek, cardlib, podcasty
tests/           testy uruchamiane też w CI
templates/       typy notatek Anki, CSS kart, szablon feedbacku do writingu
docs/            przewodniki (workflow, import Anki, skille, rutyny)
.claude/skills/  skille tutora (.github/skills to dowiązanie dla Copilota)
```

## Dla agenta

Instrukcje pracy są w [CLAUDE.md](CLAUDE.md) (oraz [.github/copilot-instructions.md](.github/copilot-instructions.md) dla Copilota). Skrypty korzystają tylko z biblioteki standardowej Pythona:

```bash
python -m unittest discover -s tests          # testy (też w CI na każdym PR)
python scripts/validate_output.py output/     # walidacja wszystkich talii
python decks/ability_achievement_3a.py        # regeneracja TSV ze źródła talii
python scripts/build_apkg.py "output/fce-x.tsv=Podtalia" --deck "FCE Preparation::Temat" -o output/fce-x.apkg
```

## Licencja

Projekt edukacyjny do użytku osobistego.
