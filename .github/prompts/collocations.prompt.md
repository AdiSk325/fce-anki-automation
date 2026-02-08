# Konwersja kolokacji na karty Anki – Collocations

## Instrukcja

Przekonwertuj podaną listę kolokacji lub temat na profesjonalny wsad do Anki w formacie TSV.

## Format wejściowy

Kolokacje mogą być podane jako:
- Lista kolokacji (np. "make a decision, take responsibility")
- Temat (np. "kolokacje z MAKE i DO")
- Typ kolokacji (np. "verb + noun collocations for work")
- Tekst z prośbą o wyodrębnienie kolokacji

## Format wyjściowy

Plik TSV z kolumnami oddzielonymi tabulatorem:

```
Collocation	Translation	Example	Type	Tags
```

### Specyfikacja pól

**Collocation** (Kolokacja):
- Kolokacja po angielsku
- Pogrubienie elementów kluczowych nie jest potrzebne (to pole Front)

**Translation** (Tłumaczenie) – format HTML:
```html
<div class="translation">
<p><b>🇵🇱 tłumaczenie polskie</b></p>
<p>🇬🇧 <i>definicja/objaśnienie po angielsku</i></p>
</div>
<div class="note"><b>⚠️ Uwaga:</b> Typowe pułapki / różnice PL-EN (opcjonalnie)</div>
```

**Example** (Przykład) – format HTML:
```html
<div class="example">
<p>1. <i>Zdanie z <b>kolokacją</b> w kontekście FCE.</i></p>
<p>   🇵🇱 <i>Tłumaczenie zdania.</i></p>
<p>2. <i>Drugie zdanie z <b>kolokacją</b>.</i></p>
<p>   🇵🇱 <i>Tłumaczenie.</i></p>
</div>
```

**Type** (Typ kolokacji):
- `verb+noun` – np. make a decision
- `adj+noun` – np. heavy rain
- `adv+adj` – np. highly unlikely
- `verb+prep` – np. depend on
- `verb+adv` – np. strongly disagree
- `noun+noun` – np. rush hour
- `noun+verb` – np. alarm goes off

**Tags**:
- Format: `fce collocations [typ]`
- Np.: `fce collocations verb-noun`, `fce collocations adj-noun`

## Wymagania jakościowe

1. **Min. 2 przykłady** dla każdej kolokacji
2. **Tłumaczenie naturalne** – idiomatyczne, nie dosłowne
3. **Kontekst FCE** – przykłady z typowych tematów egzaminacyjnych
4. **Uwagi o typowych błędach** – np. "make a decision" nie "do a decision"
5. **Poziom B2** – kolokacje istotne na egzaminie FCE

## Kolokacje kluczowe dla FCE

Gdy użytkownik prosi o kolokacje tematyczne, uwzględnij te najczęstsze na FCE:

### MAKE vs DO
| MAKE | DO |
|------|-----|
| make a decision | do homework |
| make a mistake | do research |
| make progress | do your best |
| make an effort | do damage |
| make a complaint | do a favour |
| make an appointment | do business |
| make friends | do exercise |

### Kolokacje tematyczne FCE
- **Praca**: apply for a job, earn a living, meet a deadline
- **Edukacja**: pass an exam, take a course, do research
- **Podróże**: catch a flight, book accommodation, go sightseeing
- **Zdrowie**: catch a cold, keep fit, lose weight
- **Relacje**: make friends, keep in touch, have an argument

## Przykład

Wejście:
```
make a decision
do your best
```

Wyjście (TSV):
```
make a decision	<div class="translation"><p><b>🇵🇱 podjąć decyzję</b></p><p>🇬🇧 <i>to decide something, especially after thinking for a long time</i></p></div><div class="note"><b>⚠️ Uwaga:</b> Nigdy „do a decision"! Po polsku „podjąć decyzję" – używamy MAKE, nie DO.</div>	<div class="example"><p>1. <i>It's time to <b>make a decision</b> about which university to attend.</i></p><p>   🇵🇱 <i>Czas podjąć decyzję o tym, na którą uczelnię pójść.</i></p><p>2. <i>She found it difficult to <b>make a decision</b> under pressure.</i></p><p>   🇵🇱 <i>Trudno jej było podjąć decyzję pod presją.</i></p></div>	verb+noun	fce collocations verb-noun
do your best	<div class="translation"><p><b>🇵🇱 dać z siebie wszystko, starać się jak najlepiej</b></p><p>🇬🇧 <i>to try as hard as you can to achieve something</i></p></div>	<div class="example"><p>1. <i>Just <b>do your best</b> in the exam and don't worry about the result.</i></p><p>   🇵🇱 <i>Po prostu daj z siebie wszystko na egzaminie i nie martw się o wynik.</i></p><p>2. <i>We'll <b>do our best</b> to finish the project on time.</i></p><p>   🇵🇱 <i>Damy z siebie wszystko, żeby skończyć projekt na czas.</i></p></div>	verb+noun	fce collocations verb-noun
```

## Procedura

1. Przeanalizuj listę wejściową lub temat
2. Zidentyfikuj kolokacje do przetworzenia
3. Dla każdej kolokacji wygeneruj kompletny wiersz TSV
4. Zapisz wynik w `output/fce-collocations-[temat]-[data].tsv`
5. Zweryfikuj format (5 kolumn TSV)
