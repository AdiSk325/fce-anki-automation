# GitHub Copilot Agent – FCE Anki Automation

## Cel projektu

Ten projekt służy do automatycznego generowania profesjonalnego wsadu (importu) do aplikacji **Anki** na potrzeby przygotowania do egzaminu **FCE (B2 First / First Certificate in English)**. Jako agent AI Twoja rola polega na konwersji list słów, zagadnień gramatycznych i innych materiałów edukacyjnych na gotowe do importu pliki TSV dla Anki.

## Kluczowe zasady

### 1. Format wyjściowy – Anki TSV

Wszystkie wygenerowane pliki muszą być w formacie **TSV (Tab-Separated Values)** zgodnym z importem Anki:
- Kodowanie: **UTF-8 (bez BOM)**
- Separator pól: **tabulator** (`\t`)
- Każdy wiersz = jedna karta (notatka)
- Pierwsza linia może zawierać nagłówki z tagami Anki (opcjonalnie)
- Pola tekstowe mogą zawierać HTML do formatowania

### 2. Typy kart (Note Types)

Projekt obsługuje następujące typy kart:

#### a) Vocabulary (Słownictwo)
Pola: `Front` | `Back` | `Example` | `Tags`
- **Front**: Słowo/fraza po angielsku
- **Back**: Tłumaczenie PL + definicja EN + wymowa IPA + część mowy
- **Example**: Minimum 2 przykładowe zdania z kontekstem FCE
- **Tags**: `fce vocabulary [temat] [poziom_CEFR]`

#### b) Grammar (Gramatyka)
Pola: `Rule` | `Explanation` | `Examples` | `CommonMistakes` | `Tags`
- **Rule**: Nazwa reguły gramatycznej (EN)
- **Explanation**: Wyjaśnienie po polsku z formułą/strukturą
- **Examples**: Minimum 3 przykłady z tłumaczeniem
- **CommonMistakes**: Typowe błędy z poprawną formą
- **Tags**: `fce grammar [temat_gramatyczny]`

#### c) Phrasal Verbs (Czasowniki frazowe)
Pola: `PhrasalVerb` | `Meaning` | `Examples` | `Synonyms` | `Tags`
- **PhrasalVerb**: Czasownik frazowy (EN)
- **Meaning**: Znaczenie(a) PL + EN
- **Examples**: Min. 2 zdania w kontekście FCE
- **Synonyms**: Synonimy jednowyrazowe
- **Tags**: `fce phrasal-verbs`

#### d) Collocations (Kolokacje)
Pola: `Collocation` | `Translation` | `Example` | `Type` | `Tags`
- **Collocation**: Kolokacja po angielsku
- **Translation**: Tłumaczenie PL
- **Example**: Zdanie przykładowe
- **Type**: Typ kolokacji (verb+noun, adj+noun, etc.)
- **Tags**: `fce collocations [typ]`

#### e) Use of English (Transformacje / Word Formation)
Pola: `Task` | `Answer` | `Explanation` | `Type` | `Tags`
- **Task**: Zadanie (np. zdanie z luką + słowo bazowe)
- **Answer**: Poprawna odpowiedź
- **Explanation**: Wyjaśnienie transformacji/słowotwórstwa
- **Type**: `key-word-transformation` / `word-formation` / `open-cloze` / `multiple-choice-cloze`
- **Tags**: `fce use-of-english [typ]`

### 3. Standardy jakości

- **Poziom językowy**: Wszystkie przykłady muszą odpowiadać poziomowi B2 (FCE)
- **Kontekst egzaminacyjny**: Przykłady powinny nawiązywać do typowych tematów FCE (podróże, edukacja, praca, środowisko, technologia, zdrowie, relacje, kultura)
- **Tłumaczenia**: Naturalne, idiomatyczne tłumaczenia na polski (nie dosłowne)
- **Wymowa IPA**: Zawsze w notacji IPA dla słownictwa
- **Przykłady**: Autentyczne, zróżnicowane, odpowiednie do poziomu
- **Unikaj duplikatów**: Sprawdź czy dane słowo/reguła nie powtarza się

### 4. Formatowanie HTML w kartach

Używaj HTML do formatowania treści kart:
```html
<!-- Pogrubienie kluczowych elementów -->
<b>słowo kluczowe</b>

<!-- Kursywa dla przykładów -->
<i>przykładowe zdanie</i>

<!-- Listy dla wielu znaczeń -->
<ul><li>znaczenie 1</li><li>znaczenie 2</li></ul>

<!-- Wymowa -->
<span class="ipa">/prəˌnʌnsiˈeɪʃən/</span>

<!-- Podział na sekcje -->
<div class="definition">definicja</div>
<div class="example">przykład</div>

<!-- Podświetlenie błędów -->
<span class="wrong">❌ błędna forma</span>
<span class="correct">✅ poprawna forma</span>
```

### 5. Struktura projektu

```
input/          → Pliki wejściowe (listy słów, tematy gramatyczne)
output/         → Wygenerowane pliki TSV gotowe do importu
templates/      → Szablony kart i specyfikacje formatów
scripts/        → Skrypty do walidacji i przetwarzania
docs/           → Dokumentacja projektu i workflow
```

### 6. Workflow generowania

1. Użytkownik umieszcza materiał wejściowy w `input/`
2. Agent AI przetwarza materiał zgodnie z odpowiednim promptem z `.github/prompts/`
3. Wynik zapisywany jest w `output/` w formacie TSV
4. Opcjonalnie: walidacja skryptem `scripts/validate_output.py`
5. Import do Anki

### 7. Nazewnictwo plików wyjściowych

Format: `fce-[typ]-[temat]-[data].tsv`

Przykłady:
- `fce-vocabulary-travel-2024-01-15.tsv`
- `fce-grammar-conditionals-2024-01-15.tsv`
- `fce-phrasal-verbs-mixed-2024-01-15.tsv`
- `fce-collocations-work-2024-01-15.tsv`
- `fce-use-of-english-word-formation-2024-01-15.tsv`

### 8. Tagi Anki

Hierarchia tagów:
```
fce
├── vocabulary
│   ├── travel
│   ├── education
│   ├── work
│   ├── environment
│   ├── technology
│   ├── health
│   ├── relationships
│   └── culture
├── grammar
│   ├── tenses
│   ├── conditionals
│   ├── passive
│   ├── reported-speech
│   ├── modals
│   ├── articles
│   ├── relative-clauses
│   └── wish-and-if-only
├── phrasal-verbs
├── collocations
│   ├── verb-noun
│   ├── adj-noun
│   ├── adv-adj
│   └── verb-prep
└── use-of-english
    ├── key-word-transformation
    ├── word-formation
    ├── open-cloze
    └── multiple-choice-cloze
```

### 9. Walidacja danych

Każdy wygenerowany plik powinien spełniać:
- [ ] Poprawne kodowanie UTF-8
- [ ] Poprawna liczba kolumn w każdym wierszu
- [ ] Brak pustych pól wymaganych
- [ ] Poprawne tagi
- [ ] Brak zduplikowanych kart
- [ ] Poprawny HTML (zamknięte tagi)
- [ ] Minimum wymagana liczba przykładów

### 10. Język komunikacji

- **Instrukcje dla agenta**: Polski
- **Treść kart (Front/Rule/Task)**: Angielski
- **Tłumaczenia i wyjaśnienia (Back/Explanation)**: Polski + Angielski
- **Tagi**: Angielski (lowercase, kebab-case)
