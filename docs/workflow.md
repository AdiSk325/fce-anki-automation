# Workflow – codzienna praca z tutorem FCE

## Założenie

Repo ma działać jak osobista przestrzeń robocza, nie jak jednorazowy generator treści. Każda sensowna sesja z Copilotem powinna zostawić użyteczny ślad: materiał, ocenę, korektę, plan albo zapis postępu.

## Domyślny przebieg sesji

### 1. Kontekst

Przed wykonaniem zadania tutor powinien odczytać, co jest potrzebne z:

- `knowledge/expert_knowledge.md`,
- plików w `User/`,
- odpowiednich katalogów w `practice/`, `plans/`, `progress/`, `materials/`.

### 2. Praca dydaktyczna

Typowe typy sesji:

- wyjaśnienie zagadnienia gramatycznego,
- ćwiczenia z Reading and Use of English,
- Writing Part 1 lub Part 2,
- Speaking simulation,
- analiza błędów,
- planowanie tygodnia,
- generowanie lub weryfikacja fiszek Anki.

### 3. Zapis rezultatu

Po zakończeniu tutor zapisuje to, co ma wartość na przyszłość:

- materiał do `practice/`,
- plany do `plans/`,
- raporty do `progress/`,
- aktualizacje personalizacji do `User/`.

## Przykładowe workflow

### Writing

1. Tutor daje task w stylu FCE.
2. Użytkownik pisze własny tekst.
3. Tekst trafia do `practice/writing/raw/`.
4. Tutor ocenia pracę i zapisuje feedback do `practice/writing/feedback/`.
5. Wersja poprawiona trafia do `practice/writing/corrected/`.
6. Najważniejsze błędy są dopisywane do `User/most_popular_mistakes.md`.

### Reading and Use of English

1. Tutor tworzy zestaw ćwiczeń do `practice/reading-use-of-english/`.
2. Użytkownik rozwiązuje zadania.
3. Tutor sprawdza odpowiedzi i zapisuje wnioski.
4. Jeśli trzeba, tworzy zestaw naprawczy oraz fiszki Anki.

### Speaking

1. Tutor prowadzi symulację jednej części Speaking.
2. Koryguje język, zakres i organizację wypowiedzi.
3. Zapisuje kluczowe braki do `User/user_progress.md` i `User/most_popular_mistakes.md`.
4. Zleca ćwiczenie uzupełniające do `practice/speaking/` albo `practice/vocabulary/`.

### Anki cycle

1. Tutor diagnozuje, co trzeba zapamiętać.
2. Tworzy lub rozszerza zestaw fiszek w `output/`.
3. Użytkownik uczy się kart.
4. Tutor przeprowadza aktywne sprawdzenie w `practice/anki-checks/`.
5. Trudne elementy wracają do kolejnych ćwiczeń.

## Polecane polecenia startowe

```text
Sprawdź moje cele i postępy, a potem zaproponuj najrozsądniejszą sesję na dziś.
```

```text
Przygotuj mi Writing Part 2, oceń odpowiedź jak tutor FCE i zapisz komplet śladów pracy w repo.
```

```text
Na podstawie moich błędów przygotuj 15 zadań Use of English i 10 fiszek Anki do utrwalenia.
```

## Kiedy używać input/ i output/

- `input/` służy nadal jako miejsce na materiały wejściowe, listy słów, notatki lub surowe polecenia.
- `output/` pozostaje katalogiem na gotowe pliki TSV do Anki.
- Wszystko, co jest materiałem do pracy i powrotu, powinno trafiać przede wszystkim do `practice/`, `plans/`, `progress/` i `materials/`.
