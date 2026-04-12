# Konwersja czasowników frazowych na karty Anki – Phrasal Verbs

## Instrukcja

Przekonwertuj podaną listę czasowników frazowych na profesjonalny wsad do Anki w formacie TSV.

## Format wejściowy

Lista czasowników frazowych może być w dowolnym formacie:
- Prosta lista (np. "give up, look after, break down")
- Lista z tłumaczeniami
- Czasowniki pogrupowane tematycznie
- Czasownik bazowy z prośbą o wygenerowanie wariantów frazowych (np. "wszystkie phrasal verbs z GET")

## Format wyjściowy

Plik TSV z kolumnami oddzielonymi tabulatorem:

```
PhrasalVerb	Meaning	Examples	Synonyms	Tags
```

### Specyfikacja pól

**PhrasalVerb** (Czasownik frazowy):
- Forma bezokolicznikowa
- Jeśli separowalny: zaznacz `(sth)` / `(sb)` w odpowiednim miejscu
- Np. "give up (sth)", "look after (sb)", "put (sth) off"

**Meaning** (Znaczenie) – format HTML:
```html
<div class="meaning">
<p><b>🇵🇱 Znaczenie 1:</b> tłumaczenie polskie</p>
<p>🇬🇧 <i>definicja po angielsku</i></p>
</div>
<div class="meaning">
<p><b>🇵🇱 Znaczenie 2:</b> kolejne tłumaczenie (jeśli wieloznaczny)</p>
<p>🇬🇧 <i>definicja po angielsku</i></p>
</div>
<div class="grammar-note"><b>📝 Uwaga:</b> separowalny / nieseparowalny / przechodni / nieprzechodni</div>
```

**Examples** (Przykłady) – format HTML:
```html
<div class="examples">
<p>1. <i>Zdanie z <b>phrasal verb</b> w kontekście FCE.</i></p>
<p>   🇵🇱 <i>Tłumaczenie na polski.</i></p>
<p>2. <i>Drugie zdanie z <b>phrasal verb</b>.</i></p>
<p>   🇵🇱 <i>Tłumaczenie.</i></p>
</div>
```

**Synonyms** (Synonimy):
- Jednowyrazowe odpowiedniki formalne (ważne na FCE!)
- Format: synonim1, synonim2, synonim3
- Np. dla "give up" → "abandon, quit, surrender"

**Tags**:
- Format: `fce phrasal-verbs [czasownik-bazowy]`
- Np.: `fce phrasal-verbs get`, `fce phrasal-verbs take`

## Wymagania jakościowe

1. **Wszystkie znaczenia** – jeśli phrasal verb ma wiele znaczeń, uwzględnij najważniejsze (max 3)
2. **Min. 2 przykłady** na każde znaczenie
3. **Synonimy formalne** – kluczowe dla FCE (Use of English)
4. **Informacja gramatyczna** – czy separowalny, przechodni
5. **Kontekst FCE** – przykłady z typowych tematów egzaminacyjnych
6. **Poziom B2** – nie używaj phrasal verbs poniżej B1 lub powyżej C1

## Zasady generowania wariantów

Gdy użytkownik podaje czasownik bazowy (np. "GET"), wygeneruj najważniejsze phrasal verbs z tym czasownikiem na poziomie FCE:

| Czasownik bazowy | Kluczowe phrasal verbs FCE |
|------------------|---------------------------|
| GET | get along, get away, get by, get over, get through, get up to |
| TAKE | take after, take off, take on, take over, take up |
| COME | come across, come down with, come up with, come round |
| GIVE | give away, give back, give in, give out, give up |
| LOOK | look after, look for, look forward to, look into, look up |
| TURN | turn down, turn into, turn off, turn out, turn up |
| PUT | put away, put off, put on, put out, put up with |
| BREAK | break down, break in, break out, break up |
| BRING | bring about, bring back, bring up |
| SET | set off, set out, set up |

## Przykład

Wejście:
```
look after
look forward to
```

Wyjście (TSV):
```
look after (sb/sth)	<div class="meaning"><p><b>🇵🇱 Znaczenie:</b> opiekować się, zajmować się (kimś/czymś)</p><p>🇬🇧 <i>to take care of someone or something</i></p></div><div class="grammar-note"><b>📝 Uwaga:</b> nieseparowalny, przechodni (transitive, inseparable)</div>	<div class="examples"><p>1. <i>Could you <b>look after</b> my cat while I'm on holiday?</i></p><p>   🇵🇱 <i>Czy mógłbyś zaopiekować się moim kotem, gdy będę na wakacjach?</i></p><p>2. <i>She <b>looks after</b> her elderly grandmother every weekend.</i></p><p>   🇵🇱 <i>Opiekuje się swoją starszą babcią w każdy weekend.</i></p></div>	care for, take care of, tend	fce phrasal-verbs look
look forward to (sth)	<div class="meaning"><p><b>🇵🇱 Znaczenie:</b> nie móc się doczekać, cieszyć się na (coś)</p><p>🇬🇧 <i>to feel excited and happy about something that is going to happen</i></p></div><div class="grammar-note"><b>📝 Uwaga:</b> nieseparowalny + zawsze z gerund (-ing): „look forward to doing sth"</div>	<div class="examples"><p>1. <i>I'm really <b>looking forward to</b> starting university next month.</i></p><p>   🇵🇱 <i>Naprawdę nie mogę się doczekać rozpoczęcia studiów w przyszłym miesiącu.</i></p><p>2. <i>We <b>look forward to hearing</b> from you soon.</i></p><p>   🇵🇱 <i>Z niecierpliwością czekamy na wiadomość od Ciebie.</i></p></div>	anticipate, await, expect	fce phrasal-verbs look
```

## Procedura

1. Przeanalizuj listę wejściową
2. Dla każdego phrasal verb wygeneruj kompletny wiersz TSV
3. Jeśli podano czasownik bazowy, wygeneruj najważniejsze warianty FCE
4. Zapisz wynik w `output/fce-phrasal-verbs-[czasownik]-[YYYY-MM-DD].tsv`
5. Zweryfikuj format (5 kolumn TSV)
