# Specyfikacja formatów kart Anki – Szablony

## Przegląd typów notatek (Note Types)

Poniżej znajdują się specyfikacje pól dla każdego typu notatki używanego w tym projekcie.
Każdy typ odpowiada innemu rodzajowi materiału edukacyjnego FCE.

---

## 1. FCE Vocabulary

**Nazwa typu w Anki:** `FCE Vocabulary`

| Pole | Wymagane | Opis |
|------|----------|------|
| Front | ✅ | Słowo/fraza EN |
| Back | ✅ | Tłumaczenie PL + definicja EN + IPA + część mowy |
| Example | ✅ | Min. 2 przykładowe zdania z tłumaczeniem |
| Tags | ✅ | `fce vocabulary [temat]` |

**Kierunki nauki (Card Templates):**
- Card 1: Front → Back + Example (rozpoznawanie słowa)
- Card 2: Back (tylko tłumaczenie PL) → Front (aktywne przypominanie)

---

## 2. FCE Grammar

**Nazwa typu w Anki:** `FCE Grammar`

| Pole | Wymagane | Opis |
|------|----------|------|
| Rule | ✅ | Nazwa reguły EN |
| Explanation | ✅ | Wyjaśnienie PL ze strukturą/formułą |
| Examples | ✅ | Min. 3 przykłady z tłumaczeniem |
| CommonMistakes | ✅ | Min. 2 typowe błędy z poprawkami |
| Tags | ✅ | `fce grammar [temat]` |

**Kierunki nauki:**
- Card 1: Rule → Explanation + Examples + CommonMistakes
- Card 2: Examples (bez podpowiedzi) → Rule + Explanation

---

## 3. FCE Phrasal Verbs

**Nazwa typu w Anki:** `FCE Phrasal Verbs`

| Pole | Wymagane | Opis |
|------|----------|------|
| PhrasalVerb | ✅ | Czasownik frazowy EN |
| Meaning | ✅ | Znaczenia PL + EN + info gramatyczna |
| Examples | ✅ | Min. 2 przykłady z tłumaczeniem |
| Synonyms | ✅ | Synonimy jednowyrazowe |
| Tags | ✅ | `fce phrasal-verbs [czasownik]` |

**Kierunki nauki:**
- Card 1: PhrasalVerb → Meaning + Examples
- Card 2: Meaning (PL) → PhrasalVerb + Synonyms
- Card 3: Synonyms → PhrasalVerb (FCE Use of English practice)

---

## 4. FCE Collocations

**Nazwa typu w Anki:** `FCE Collocations`

| Pole | Wymagane | Opis |
|------|----------|------|
| Collocation | ✅ | Kolokacja EN |
| Translation | ✅ | Tłumaczenie PL + definicja EN |
| Example | ✅ | Min. 2 przykłady z tłumaczeniem |
| Type | ✅ | Typ kolokacji |
| Tags | ✅ | `fce collocations [typ]` |

**Kierunki nauki:**
- Card 1: Collocation → Translation + Example
- Card 2: Translation (PL) → Collocation

---

## 5. FCE Use of English

**Nazwa typu w Anki:** `FCE Use of English`

| Pole | Wymagane | Opis |
|------|----------|------|
| Task | ✅ | Treść zadania (luka/transformacja) |
| Answer | ✅ | Poprawna odpowiedź |
| Explanation | ✅ | Wyjaśnienie PL + reguła + wskazówka |
| Type | ✅ | Typ zadania |
| Tags | ✅ | `fce use-of-english [typ]` |

**Kierunki nauki:**
- Card 1: Task → Answer + Explanation

---

## Instrukcja importu do Anki

### Tworzenie typów notatek

Przed pierwszym importem musisz utworzyć odpowiednie typy notatek w Anki:

1. Otwórz Anki → **Narzędzia** → **Zarządzaj typami notatek**
2. Kliknij **Dodaj** → wybierz **Dodaj: Podstawowy**
3. Zmień nazwę na odpowiednią (np. "FCE Vocabulary")
4. Kliknij **Pola** i dodaj wymagane pola z tabeli powyżej
5. Kliknij **Karty** i skonfiguruj szablony kart

### Import pliku TSV

1. Otwórz Anki → **Plik** → **Importuj**
2. Wybierz plik `.tsv` z katalogu `output/`
3. Ustaw:
   - **Typ notatki**: odpowiedni typ (np. FCE Vocabulary)
   - **Talia**: wybierz lub utwórz odpowiednią talię
   - **Separator pól**: Tabulator
   - **Kolumna tagów**: ostatnia kolumna
4. Zmapuj pola do kolumn
5. Kliknij **Importuj**

### Sugerowane talie (Decks)

```
FCE Preparation
├── FCE::Vocabulary
├── FCE::Grammar
├── FCE::Phrasal Verbs
├── FCE::Collocations
└── FCE::Use of English
```
