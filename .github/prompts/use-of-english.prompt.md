# Generowanie zadań Use of English na karty Anki

## Instrukcja

Wygeneruj karty Anki z zadaniami typu Use of English (FCE Paper 1, Parts 1-4) w formacie TSV.

## Format wejściowy

Żądanie może mieć formę:
- Typ zadania (np. "Key Word Transformation")
- Temat gramatyczny (np. "conditionals – KWT")
- Lista słów bazowych do word formation
- Konkretne struktury do przećwiczenia

## Typy zadań FCE Use of English

### Part 1: Multiple-choice cloze
- Tekst z lukami, 4 opcje do wyboru
- Testuje: kolokacje, phrasal verbs, łączniki, słownictwo

### Part 2: Open cloze
- Tekst z lukami, brak opcji
- Testuje: gramatykę, słowa funkcyjne, przyimki

### Part 3: Word formation
- Tekst z lukami + słowo bazowe
- Testuje: słowotwórstwo (prefiksy, sufiksy, konwersja)

### Part 4: Key Word Transformation
- Zdanie wyjściowe + słowo kluczowe → zdanie docelowe (2-5 słów)
- Testuje: gramatykę, słownictwo, transformacje

## Format wyjściowy

Plik TSV z kolumnami oddzielonymi tabulatorem:

```
Task	Answer	Explanation	Type	Tags
```

### Specyfikacja pól per typ zadania

---

#### Key Word Transformation (Part 4)

**Task** – format HTML:
```html
<div class="kwt">
<p class="original"><b>Zdanie oryginalne.</b></p>
<p class="keyword">Słowo kluczowe: <b>KEYWORD</b></p>
<p class="gap">Początek zdania _________________ koniec zdania.</p>
<p class="instruction"><i>Uzupełnij zdanie używając 2-5 słów, w tym podanego słowa kluczowego. Nie zmieniaj formy słowa kluczowego.</i></p>
</div>
```

**Answer**:
```html
<div class="answer"><b>odpowiedź (2-5 słów z keyword)</b></div>
<div class="full-sentence"><i>Pełne zdanie docelowe.</i></div>
```

---

#### Word Formation (Part 3)

**Task** – format HTML:
```html
<div class="wf">
<p>Zdanie z <b>______</b> (luką). (<b>SŁOWO BAZOWE</b>)</p>
</div>
```

**Answer**:
```html
<div class="answer"><b>poprawna forma słowa</b></div>
<div class="formation"><i>SŁOWO BAZOWE → prefix/suffix → ODPOWIEDŹ</i></div>
```

---

#### Open Cloze (Part 2)

**Task** – format HTML:
```html
<div class="oc">
<p>Zdanie z <b>______</b> (luką do uzupełnienia jednym słowem).</p>
</div>
```

**Answer**:
```html
<div class="answer"><b>poprawne słowo</b></div>
```

---

#### Multiple-choice Cloze (Part 1)

**Task** – format HTML:
```html
<div class="mc">
<p>Zdanie z <b>______</b> (luką).</p>
<p>A) opcja1 &nbsp; B) opcja2 &nbsp; C) opcja3 &nbsp; D) opcja4</p>
</div>
```

**Answer**:
```html
<div class="answer"><b>C) poprawna opcja</b></div>
```

---

### Wspólne pola

**Explanation** (Wyjaśnienie) – format HTML:
```html
<div class="explanation">
<p><b>🇵🇱 Wyjaśnienie:</b> Opis po polsku dlaczego ta odpowiedź jest poprawna.</p>
<p><b>📐 Reguła:</b> Nazwa reguły gramatycznej / typu kolokacji.</p>
<p><b>💡 Wskazówka:</b> Jak rozpoznać ten typ zadania na egzaminie.</p>
</div>
```

**Type**: `key-word-transformation` / `word-formation` / `open-cloze` / `multiple-choice-cloze`

**Tags**: `fce use-of-english [typ]`

## Wymagania jakościowe

1. **Realistyczne zadania** – wzorowane na prawdziwych zadaniach FCE
2. **Kontekst egzaminacyjny** – typowe tematy FCE
3. **Poziom trudności B2** – ani za łatwe, ani za trudne
4. **Wyjaśnienie transformacji** – krok po kroku
5. **KWT: 2-5 słów** w odpowiedzi, włącznie z keyword
6. **Word Formation**: poprawne prefiksy/sufiksy
7. **Jasna instrukcja** – na karcie musi być jasne, co trzeba zrobić

## Kluczowe transformacje FCE (KWT)

| Struktura | Przykład transformacji |
|-----------|----------------------|
| Active → Passive | "Someone stole..." → "...was stolen" |
| Direct → Reported | "I will go" → "she said she would go" |
| Conditional types | "I don't have" → "If I had" |
| Wish / If only | "I'm sorry I didn't" → "I wish I had" |
| Comparatives | "not as...as" → "more...than" |
| Causative | "Someone cut her hair" → "She had her hair cut" |
| Modal perfect | "Perhaps he forgot" → "He might have forgotten" |
| Used to / would | "In the past I played" → "I used to play" |
| Too / enough | "too young to" → "not old enough to" |
| Unless / provided | "If you don't" → "Unless you" |

## Kluczowe prefiksy i sufiksy (Word Formation)

| Kategoria | Prefiksy/Sufiksy |
|-----------|-----------------|
| Negation | un-, in-, im-, ir-, il-, dis-, mis-, non- |
| Noun from verb | -tion, -sion, -ment, -ance/-ence, -al, -ing |
| Noun from adj | -ness, -ity, -ence/-ance |
| Adjective | -ful, -less, -ous, -ive, -able/-ible, -al, -ic |
| Adverb | -ly |
| Person | -er, -or, -ist, -ian, -ee |
| Verb | -ise/-ize, -en, -ify |

## Przykład

Wejście:
```
Key Word Transformation – conditionals
```

Wyjście (TSV):
```
<div class="kwt"><p class="original"><b>I don't have a car, so I can't drive to work.</b></p><p class="keyword">Słowo kluczowe: <b>HAD</b></p><p class="gap">I could drive to work _________________ a car.</p><p class="instruction"><i>Uzupełnij zdanie używając 2-5 słów, w tym podanego słowa kluczowego.</i></p></div>	<div class="answer"><b>if I had</b></div><div class="full-sentence"><i>I could drive to work if I had a car.</i></div>	<div class="explanation"><p><b>🇵🇱 Wyjaśnienie:</b> Transformacja z rzeczywistej sytuacji (nie mam samochodu) na hipotetyczną (Second Conditional). „I don't have" → „if I had" = gdybym miał.</p><p><b>📐 Reguła:</b> Second Conditional: If + Past Simple, would/could + infinitive</p><p><b>💡 Wskazówka:</b> Gdy widzisz zdanie o aktualnej sytuacji z negatywnym skutkiem, pomyśl o Second Conditional.</p></div>	key-word-transformation	fce use-of-english key-word-transformation
<div class="kwt"><p class="original"><b>I'm sorry that I didn't study harder for the exam.</b></p><p class="keyword">Słowo kluczowe: <b>WISH</b></p><p class="gap">I _________________ harder for the exam.</p><p class="instruction"><i>Uzupełnij zdanie używając 2-5 słów, w tym podanego słowa kluczowego.</i></p></div>	<div class="answer"><b>wish I had studied</b></div><div class="full-sentence"><i>I wish I had studied harder for the exam.</i></div>	<div class="explanation"><p><b>🇵🇱 Wyjaśnienie:</b> Transformacja żalu o przeszłości. „I'm sorry I didn't" → „I wish I had" (+ Past Perfect). Żałuję, że nie nauczyłem się więcej.</p><p><b>📐 Reguła:</b> Wish + Past Perfect = żal o przeszłości (coś się nie stało, a chcielibyśmy, żeby się stało)</p><p><b>💡 Wskazówka:</b> „I'm sorry I didn't..." na egzaminie prawie zawsze = „I wish I had..."</p></div>	key-word-transformation	fce use-of-english key-word-transformation
```

## Procedura

1. Zidentyfikuj typ zadania i temat
2. Wygeneruj realistyczne zadania w stylu FCE
3. Dla każdego zadania wygeneruj kompletny wiersz TSV
4. Zapisz wynik w `output/fce-use-of-english-[typ]-[data].tsv`
5. Zweryfikuj format (5 kolumn TSV)
