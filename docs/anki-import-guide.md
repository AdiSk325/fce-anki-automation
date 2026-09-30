# Importowanie do Anki – Szczegółowy przewodnik

Moduł Anki jest częścią większego systemu nauki w tym repo. Najlepiej używać go w cyklu: tutor diagnozuje brak, generuje materiał, użytkownik uczy się fiszek, a następnie tutor sprawdza aktywne użycie w `practice/anki-checks/`.

## Wymagania

- **Anki** (wersja 2.1+): https://apps.ankiweb.net/ albo **AnkiDroid** (Android) / **AnkiMobile** (iOS)
- Pliki `.tsv` wygenerowane przez ten projekt albo gotowa paczka `.apkg`

## Najprostsza droga: paczka `.apkg` (także na telefon)

Paczka `.apkg` zawiera od razu typy notatek (pola, szablony kart, CSS z `templates/anki-card-style.css`, łącznie z trybem nocnym) i strukturę talii. Nie trzeba niczego konfigurować ręcznie, więc to najlepsza opcja dla AnkiDroid.

### Budowanie paczki

```bash
python scripts/build_apkg.py \
  "output/fce-grammar-multi-word-verbs-3a.tsv=1 Rules" \
  "output/fce-phrasal-verbs-multi-word-verbs-3a.tsv=2 Meanings" \
  "output/fce-use-of-english-multi-word-verbs-3a-translation.tsv=3 Translation" \
  --deck "FCE Preparation::3A Multi-word verbs" \
  -o output/fce-multi-word-verbs-3a.apkg
```

- Każdy plik TSV może mieć własną podtalię (`plik.tsv=Podtalia`); bez `=` trafia do talii z `--deck`.
- Typ notatki jest wykrywany z nazwy pliku, tak jak w `validate_output.py`.
- Przed budowaniem zwaliduj pliki TSV (`validate_output.py`).
- Notatki mają stałe identyfikatory (GUID liczony z pierwszego pola), więc po poprawkach wystarczy zbudować paczkę ponownie i zaimportować ją jeszcze raz. Anki zaktualizuje istniejące notatki i zachowa historię powtórek. Zmiana treści pierwszego pola tworzy nową notatkę.

### Import na Androidzie (AnkiDroid)

1. Pobierz plik `.apkg` na telefon, np. z GitHuba (plik w `output/` → **Download raw file**) albo z załącznika w czacie.
2. Stuknij pobrany plik i wybierz **AnkiDroid** (albo w AnkiDroid: menu **⋮** → **Importuj** → wskaż plik).
3. Talia pojawi się na liście, np. `FCE Preparation › 3A Multi-word verbs` z podtaliami.
4. Jeśli korzystasz z AnkiWeb, zsynchronizuj AnkiDroid, żeby karty pojawiły się też na komputerze.

### Import w Anki Desktop

**Plik** → **Importuj** → wybierz `.apkg`, potem zsynchronizuj z AnkiWeb, żeby karty trafiły na telefon.

### Uwaga o istniejących typach notatek

Jeśli w Anki istnieje już ręcznie utworzony typ notatki o tej samej nazwie (np. `FCE Phrasal Verbs`), Anki doda typ z paczki pod nazwą z plusem (`FCE Phrasal Verbs+`). Karty działają normalnie. Kolejne paczki z tego repo trafiają już w ten sam typ z plusem, bo mają stałe ID.

## Ręczny import TSV (Anki Desktop)

Poniższe kroki są potrzebne tylko przy imporcie plików `.tsv` bez paczki `.apkg`.

## Przygotowanie Anki

### Krok 1: Utwórz talie (Decks)

Zalecana struktura talii:

```
FCE Preparation
├── FCE::Vocabulary
├── FCE::Grammar
├── FCE::Phrasal Verbs
├── FCE::Collocations
└── FCE::Use of English
```

Aby utworzyć talię z podtaliami:
1. Kliknij **Utwórz talię**
2. Wpisz nazwę z `::` jako separatorem, np. `FCE Preparation::Vocabulary`

### Krok 2: Utwórz typy notatek (Note Types)

Dla każdego typu karty musisz utworzyć odpowiedni typ notatki:

#### FCE Vocabulary
1. **Narzędzia** → **Zarządzaj typami notatek** → **Dodaj**
2. Wybierz **Klonuj: Podstawowy** → Nazwij: `FCE Vocabulary`
3. Kliknij **Pola** i ustaw:
   - `Front` (domyślne)
   - `Back` (domyślne)
   - Dodaj: `Example`
4. Kliknij **Karty** i ustaw szablon:

**Przód:**
```html
<div class="front">{{Front}}</div>
```

**Tył:**
```html
<div class="front">{{Front}}</div>
<hr id="answer">
{{Back}}
<br><br>
{{Example}}
```

#### FCE Grammar
Pola: `Rule`, `Explanation`, `Examples`, `CommonMistakes`

**Przód:**
```html
<div class="front">{{Rule}}</div>
```

**Tył:**
```html
<div class="front">{{Rule}}</div>
<hr id="answer">
{{Explanation}}
<br><br>
{{Examples}}
<br><br>
{{CommonMistakes}}
```

#### FCE Phrasal Verbs
Pola: `PhrasalVerb`, `Meaning`, `Examples`, `Synonyms`

**Przód:**
```html
<div class="front">{{PhrasalVerb}}</div>
```

**Tył:**
```html
<div class="front">{{PhrasalVerb}}</div>
<hr id="answer">
{{Meaning}}
<br><br>
{{Examples}}
<br><br>
<div class="tip"><b>Synonimy:</b> {{Synonyms}}</div>
```

#### FCE Collocations
Pola: `Collocation`, `Translation`, `Example`, `Type`

#### FCE Use of English
Pola: `Task`, `Answer`, `Explanation`, `Type`

### Krok 3: Dodaj styl CSS

Dla każdego typu notatki:
1. Kliknij **Karty** w edytorze typu notatki
2. W sekcji **Styl** wklej zawartość pliku `templates/anki-card-style.css`

## Import pliku TSV

### Krok 1: Otwórz import
**Plik** → **Importuj** → wybierz plik `.tsv`

### Krok 2: Konfiguracja importu

| Ustawienie | Wartość |
|-----------|---------|
| Typ notatki | Odpowiedni typ (np. FCE Vocabulary) |
| Talia | Odpowiednia talia (np. FCE Preparation::Vocabulary) |
| Separator pól | Tabulator |
| Zezwól na HTML | ✅ Tak |
| Aktualizuj istniejące | Według preferencji |

### Krok 3: Mapuj pola

Upewnij się, że kolumny z pliku TSV są zmapowane do odpowiednich pól:

**Vocabulary:**
| Kolumna | Pole |
|---------|------|
| 1 | Front |
| 2 | Back |
| 3 | Example |
| 4 | Tags |

**Grammar:**
| Kolumna | Pole |
|---------|------|
| 1 | Rule |
| 2 | Explanation |
| 3 | Examples |
| 4 | CommonMistakes |
| 5 | Tags |

### Krok 4: Import
Kliknij **Importuj** i sprawdź liczbę zaimportowanych kart.

## Wskazówki dotyczące nauki

### Ustawienia powtórek
Zalecane ustawienia dla przygotowania do FCE:
- **Nowe karty dziennie**: 15-20
- **Maksymalne powtórki dziennie**: 100-150
- **Interwał nauki**: 1min, 10min (domyślne)
- **Graduating interval**: 1 dzień
- **Easy interval**: 4 dni

### Strategia nauki
1. **Codziennie**: Przeglądaj zaplanowane powtórki
2. **Co tydzień**: Dodawaj nowe karty z kolejnych tematów
3. **Po każdej sesji z tutorem**: Sprawdź, czy z nowych błędów lub braków nie trzeba dodać kolejnych kart
4. **Przed egzaminem**: Skup się na kartach z najgorszymi statystykami
5. **Custom Study**: Użyj filtrowanej talii do intensywnej nauki konkretnego tematu

### Tagi i filtrowanie
Dzięki systemowi tagów możesz tworzyć filtrowane talie:
- `tag:fce tag:grammar tag:conditionals` – tylko conditionals
- `tag:fce tag:vocabulary tag:travel` – tylko słownictwo z podróży
- `tag:fce tag:use-of-english` – wszystkie zadania Use of English

## Integracja z tutorem

- Po przerobieniu talii poproś tutora o aktywne sprawdzenie bez podpowiedzi.
- Trudne słowa i struktury warto od razu przerobić także w writingu, speakingu albo Use of English.
- Jeśli jakaś karta jest stale trudna, tutor powinien przygotować dodatkowy zestaw ćwiczeń zamiast tylko zwiększać liczbę powtórek.
