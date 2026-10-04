# Rutyny tutora

Dwie zaplanowane rutyny Claude (Routines) uruchamiają co tydzień świeżą sesję. Sesja wykonuje jedną z procedur poniżej i wysyła powiadomienie na telefon. Prompt rutyny tylko odsyła do tego pliku, więc zmiana działania rutyny to zwykła zmiana w repo.

| Rutyna | Kiedy (Europe/Warsaw) | Procedura |
|--------|-----------------------|-----------|
| Plan tygodnia | poniedziałek 7:44 | [Plan tygodnia](#plan-tygodnia) |
| Pakiet na weekend | piątek 16:43 | [Pakiet na weekend](#pakiet-na-weekend) |

## Wspólne zasady

- Najpierw kontekst: `CLAUDE.md`, pliki w `User/`, `plans/2026-10-04-roadmap-b2-first.md`, ostatni plik w `plans/weekly/`, statusy w `practice/anki-checks/*.md` i `practice/writing/tasks/*.md`, najnowsze notatki w `input/` (bieżący unit Empower).
- Rytm użytkownika: w tygodniu 10–15 minut dziennie (telefon), w weekend 60–90 minut. Nie planuj więcej.
- Priorytety: Writing oraz Use of English i słownictwo. Mikro-zadania celuj w `User/most_popular_mistakes.md`.
- Instrukcje po polsku, treść zadań po angielsku. Każde zadanie zawiera wyraźnie oddzielony klucz odpowiedzi, żeby dało się sprawdzić samemu na telefonie.
- Nie twórz duplikatów. Jeśli plik na ten tydzień albo nierozwiązane zadanie już istnieje, tylko przypomnij o nim.
- Na koniec: commit, PR do `main`, merge po zielonym CI (`checks`). Ostatnia wiadomość sesji to 3–5 krótkich punktów po polsku – trafiają do powiadomienia.

## Plan tygodnia

1. Ustal datę poniedziałku bieżącego tygodnia (`YYYY-MM-DD`). Jeśli `plans/weekly/YYYY-MM-DD-week.md` już istnieje, przejdź do punktu 5.
2. Utwórz `plans/weekly/YYYY-MM-DD-week.md`:
   - **Cel tygodnia** – jedno zdanie, zgodne z fazą roadmapy.
   - **Poniedziałek–piątek** – na każdy dzień: „Anki (codzienne powtórki)” plus jedno mikro-zadanie na 5–10 minut, wpisane bezpośrednio w plik (np. 5 KWT, 5 luk open cloze, 5 zdań PL → EN). Zadania opieraj na słabych punktach i słownictwie z ostatnich talii. Każdego dnia inny typ zadania.
   - **Weekend** – Writing (wskaż nierozwiązane zadanie z `practice/writing/tasks/` albo napisz, że pakiet przyjdzie w piątek) oraz najstarszy sprawdzian ze statusem `do zrobienia`.
   - **Klucz** – odpowiedzi do mikro-zadań na końcu pliku, pod nagłówkiem `## Klucz`.
3. Jeśli w ubiegłym tygodniu nic nie zostało zrobione, nie dokładaj zaległości – zaplanuj lżejszy tydzień i napisz to wprost.
4. Zaktualizuj „Bieżący nacisk” w `User/current_goals.md` tylko wtedy, gdy się zmienił.
5. Powiadomienie: cel tygodnia, zadanie na dziś i to, co czeka w weekend.

## Pakiet na weekend

1. **Writing:**
   - Jeśli w `practice/writing/tasks/` jest zadanie ze statusem `do zrobienia`, nie twórz nowego, tylko przypomnij o nim.
   - W przeciwnym razie utwórz `practice/writing/tasks/YYYY-MM-DD-<typ>-<temat>.md` z linią `**Status:** do zrobienia`. Typ wybierz na zmianę z poprzednim zadaniem (Part 1 essay ↔ Part 2: email/letter, article, report, review), a temat powiąż z bieżącym unitem Empower.
   - Format i liczba słów według `knowledge/expert_knowledge.md`. Na końcu dodaj checklistę „Zanim wyślesz” i instrukcję „wklej tekst w czacie”.
2. **Use of English:** utwórz `practice/reading-use-of-english/YYYY-MM-DD-weekend-set.md` z 6 lukami open cloze i 4 KWT, celowanymi w zarejestrowane błędy. Klucz dodaj na końcu, oddzielony.
3. **Anki:** wskaż najstarszy sprawdzian `practice/anki-checks/*.md` ze statusem `do zrobienia`.
4. Powiadomienie: co jest na weekend (Writing, zestaw UoE, sprawdzian) i ile to zajmie.

## Zmiana rutyn

Godziny i zasady zmieniasz prośbą do tutora: „zmień godzinę rutyny…” albo „w planie tygodnia dodaj…”. Godziny są ustawione w samych rutynach, a procedury w tym pliku.
