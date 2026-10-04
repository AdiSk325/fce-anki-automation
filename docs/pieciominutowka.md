# Pięciominutówka – zestawy na telefon

Aplikacja na krótkie zestawy w formacie B2 First, otwierana w aplikacji Claude na telefonie albo na claude.ai.

- Link: https://claude.ai/artifact/VxakPzW5TXhT9fjtKv352t (prywatny, widzi go tylko właściciel).
- Kod strony: `apps/pieciominutowka/page.html`.
- Zestawy: `apps/pieciominutowka/sets/<YYYY-MM-DD-slug>.json`. Każdy plik to kopia dokumentu z bazy aplikacji.

## Jak to działa

1. Tutor dodaje zestaw: zapisuje plik JSON w repo i wgrywa ten sam dokument do bazy aplikacji.
2. Użytkownik rozwiązuje zestaw na telefonie. Odpowiedzi jednoznaczne (luki, KWT, szyk) sprawdza strona. Tłumaczenia oznaczone `review: true`, które nie pasują do klucza, czekają na tutora.
3. Każde podejście trafia do kolekcji `attempts`. Gdy użytkownik napisze w czacie „sprawdź Pięciominutówkę”, tutor czyta podejścia, ocenia według `check-exercise`, zapisuje komentarz w aplikacji i wynik w repo (`practice/reading-use-of-english/`).

## Dane

Baza aplikacji ma dwie kolekcje.

### `sets/<id>`

`id` = nazwa pliku bez `.json`, np. `2026-10-04-quick-test`.

| Pole | Znaczenie |
|------|-----------|
| `title` | nazwa zestawu na liście (po polsku) |
| `created` | data ISO 8601, zwykle dzień, na który zestaw jest przeznaczony. Na liście „Do zrobienia” zestawy idą od najwcześniejszego, a w „Zrobione” od ostatnio rozwiązanego |
| `minutes` | szacowany czas |
| `focus` | krótki opis tematu (opcjonalnie) |
| `intro` | jedno-dwa zdania przed startem (opcjonalnie) |
| `items` | lista zadań, patrz niżej |

Zadanie (`items[]`):

| Pole | Znaczenie |
|------|-----------|
| `id` | unikalne w zestawie, np. `q1` |
| `kind` | `cloze` (jedno słowo w luce), `kwt` (Part 4), `write` (całe zdanie: szyk, tłumaczenie) |
| `label` | nagłówek po angielsku w nazewnictwie egzaminu, np. `Part 4 · Key word transformation` |
| `instruction` | polecenie po polsku |
| `source` | zdanie wyjściowe (KWT, zadania `write`) |
| `keyword` | słowo w ramce, tylko `kwt`, wielkimi literami |
| `text` | zdanie z jedną luką `{gap}` (`cloze`, `kwt`) |
| `answers` | akceptowane odpowiedzi; pierwsza jest pokazywana jako klucz |
| `review` | `true`, gdy odpowiedź spoza klucza ma ocenić tutor (tłumaczenia) |
| `explain` | wyjaśnienie po polsku, widoczne po sprawdzeniu |

Porównanie ignoruje wielkość liter, interpunkcję, rodzaj apostrofu i pisownię `canceled`/`cancelled`. Skróty `n't`, `'ve`, `'re`, `'m`, `'ll` są równoważne pełnym formom (`I've` = `I have`), więc w `answers` wystarczy jedna wersja. `'s` i `'d` są niejednoznaczne, więc obie formy trzeba podać osobno. W luce można wpisać całe zdanie: strona sama obetnie część, która jest już wydrukowana.

### `attempts/<auto-id>`

Zapisuje je strona. Pola: `setId`, `setTitle`, `items` (kopia zadań z chwili rozwiązania), `answers` (`{id: tekst}`), `auto` (`{id: ok | wrong | review | empty}`), `score`, `pending`, `total`, `startedAt`, `finishedAt`, `durationSec`, `by`.

Tutor dopisuje do podejścia pole `tutor` (zwykłe `update`, bez zmiany pozostałych pól):

```json
{
  "tutor": {
    "note": "Krótki komentarz po polsku do całego zestawu.",
    "gradedAt": "2026-10-04T13:00:00Z",
    "items": { "q5": { "verdict": "ok", "note": "Poprawne, choć Past Perfect brzmi naturalniej." } }
  }
}
```

`verdict` w `tutor.items` nadpisuje ocenę automatu, więc wynik na stronie zmienia się od razu.

## Procedury dla tutora

Narzędzia: `ArtifactData` (baza aplikacji) i `Artifact` (strona). W sesji bez tych narzędzi (np. w rutynie bez dostępu do artefaktów) zapisz zestaw tylko w repo i napisz w podsumowaniu, że czeka na wgranie do aplikacji.

**Nowy zestaw**

1. Zapisz `apps/pieciominutowka/sets/<YYYY-MM-DD-slug>.json` według tabel powyżej. Zadania celuj w `User/most_popular_mistakes.md` i najnowsze talie; nie dubluj mikro-zadań z bieżącego planu tygodnia.
2. `python -m unittest tests.test_quiz_sets` (z katalogu `tests/` albo przez `discover`) sprawdza format, w tym 2–5 słów w KWT.
3. `ArtifactData` → `set`, `collection: "sets"`, `doc_id` = nazwa pliku, `file_path` = ten plik.
4. Podaj użytkownikowi link do aplikacji.

**Sprawdzenie podejścia**

1. `ArtifactData` → `query` na `attempts` z `order_by: finishedAt desc`, `limit: 5`.
2. Oceń odpowiedzi `review` i błędne według `check-exercise`.
3. `ArtifactData` → `update` podejścia z polem `tutor` (z `if_version` z odczytu).
4. Zapisz zadania, odpowiedzi i wynik w `practice/reading-use-of-english/<data>-<slug>.md`, zaktualizuj `User/`, potem PR i merge zgodnie z polityką Git.

**Zmiana strony**

Edytuj `apps/pieciominutowka/page.html`, potem `Artifact` → `read` z linkiem powyżej i `publish` z `url` oraz tym plikiem. Bez `url` powstałby nowy artefakt z innym linkiem. Nie zmieniaj nazw kolekcji ani pól, bo stare podejścia przestaną się wyświetlać.
