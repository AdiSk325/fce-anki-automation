# Konwersja zagadnień gramatycznych na karty Anki – Grammar

## Instrukcja

Przekonwertuj podane zagadnienie gramatyczne na profesjonalny zestaw kart Anki w formacie TSV.

## Format wejściowy

Zagadnienie gramatyczne może być podane jako:
- Nazwa tematu (np. "Second Conditional")
- Lista reguł do przetworzenia
- Fragment podręcznika lub notatek
- Pytanie o konkretną strukturę gramatyczną

## Format wyjściowy

Plik TSV z kolumnami oddzielonymi tabulatorem:

```
Rule	Explanation	Examples	CommonMistakes	Tags
```

### Specyfikacja pól

**Rule** (Reguła):
- Nazwa reguły gramatycznej po angielsku
- Krótka, konkretna, łatwa do zidentyfikowania
- Np. "Second Conditional – Structure" / "Present Perfect vs Past Simple – Usage"

**Explanation** (Wyjaśnienie) – format HTML:
```html
<div class="formula"><b>📐 Struktura:</b><br>[wzór/formuła gramatyczna]</div>
<div class="usage"><b>📖 Użycie:</b>
<ul>
<li>Kiedy używamy (po polsku)</li>
<li>Dodatkowe informacje o użyciu</li>
</ul>
</div>
<div class="signal-words"><b>🔑 Słowa sygnałowe:</b> [lista słów]</div>
<div class="tip"><b>💡 Wskazówka:</b> [porady dla zdającego FCE]</div>
```

**Examples** (Przykłady) – format HTML:
```html
<div class="examples">
<p>1. <i>Zdanie po angielsku z <b>pogrubioną strukturą</b>.</i></p>
<p>   🇵🇱 <i>Tłumaczenie na polski.</i></p>
<p>2. <i>Drugie zdanie z <b>pogrubioną strukturą</b>.</i></p>
<p>   🇵🇱 <i>Tłumaczenie.</i></p>
<p>3. <i>Trzecie zdanie z <b>pogrubioną strukturą</b>.</i></p>
<p>   🇵🇱 <i>Tłumaczenie.</i></p>
</div>
```

**CommonMistakes** (Typowe błędy) – format HTML:
```html
<div class="mistakes">
<p><span class="wrong">❌ Błędna forma / zdanie</span></p>
<p><span class="correct">✅ Poprawna forma / zdanie</span></p>
<p><b>Wyjaśnienie:</b> Dlaczego to jest błąd (po polsku).</p>
<hr>
<p><span class="wrong">❌ Kolejny typowy błąd</span></p>
<p><span class="correct">✅ Poprawna forma</span></p>
<p><b>Wyjaśnienie:</b> Dlaczego.</p>
</div>
```

**Tags**:
- Format: `fce grammar [temat-gramatyczny]`
- Temat w kebab-case
- Np.: `fce grammar conditionals`, `fce grammar tenses`, `fce grammar passive`

## Wymagania jakościowe

1. **Minimum 3 zdania przykładowe** dla każdej reguły
2. **Minimum 2 typowe błędy** dla każdej reguły
3. **Formuła gramatyczna** – jasna i kompletna
4. **Wyjaśnienia po polsku** – zrozumiałe, z odniesieniem do polskich odpowiedników
5. **Kontekst FCE** – przykłady powinny nawiązywać do tematów egzaminacyjnych
6. **Słowa sygnałowe** – kluczowe dla rozpoznania struktury w zadaniach
7. **Wskazówki egzaminacyjne** – praktyczne porady dla zdającego FCE

## Zasady podziału na karty

Każde zagadnienie gramatyczne powinno zostać podzielone na **logiczne karty**:

| Temat | Sugerowane karty |
|-------|------------------|
| Conditionals | Osobna karta dla: Zero, First, Second, Third, Mixed |
| Tenses | Osobna karta dla każdego czasu + karty porównawcze |
| Passive | Karta per czas + karta na transformacje |
| Reported Speech | Zasady ogólne + zmiany czasów + wyjątki |
| Modals | Osobna karta per modal verb + karta porównawcza |
| Relative Clauses | Defining vs Non-defining + zaimki + omitting |

## Przykład

Wejście:
```
Second Conditional
```

Wyjście (TSV, 2 karty):
```
Second Conditional – Structure	<div class="formula"><b>📐 Struktura:</b><br><code>If + Past Simple, would + infinitive</code><br><code>Would + infinitive + if + Past Simple</code></div><div class="usage"><b>📖 Użycie:</b><ul><li>Sytuacje hipotetyczne, wyobrażone, mało prawdopodobne w teraźniejszości lub przyszłości</li><li>Rady i sugestie (If I were you...)</li><li>Marzenia i życzenia dotyczące teraźniejszości</li></ul></div><div class="signal-words"><b>🔑 Słowa sygnałowe:</b> if, would, were, could, might</div><div class="tip"><b>💡 Wskazówka FCE:</b> W Use of English Part 4 (Key Word Transformation) Second Conditional pojawia się bardzo często. Pamiętaj o „were" zamiast „was" w formalnym angielskim.</div>	<div class="examples"><p>1. <i>If I <b>had</b> more free time, I <b>would travel</b> around Europe.</i></p><p>   🇵🇱 <i>Gdybym miał więcej wolnego czasu, podróżowałbym po Europie.</i></p><p>2. <i>If she <b>spoke</b> better English, she <b>would apply</b> for the job abroad.</i></p><p>   🇵🇱 <i>Gdyby mówiła lepiej po angielsku, złożyłaby podanie o pracę za granicą.</i></p><p>3. <i>I <b>would buy</b> a bigger flat if I <b>earned</b> more money.</i></p><p>   🇵🇱 <i>Kupiłbym większe mieszkanie, gdybym zarabiał więcej.</i></p></div>	<div class="mistakes"><p><span class="wrong">❌ If I would have more time, I would travel.</span></p><p><span class="correct">✅ If I had more time, I would travel.</span></p><p><b>Wyjaśnienie:</b> Po „if" w Second Conditional nigdy nie używamy „would". Używamy Past Simple.</p><hr><p><span class="wrong">❌ If I was you, I would study harder.</span></p><p><span class="correct">✅ If I were you, I would study harder.</span></p><p><b>Wyjaśnienie:</b> W formalnym angielsku (i na egzaminie FCE) używamy „were" dla wszystkich osób w Second Conditional.</p></div>	fce grammar conditionals
Second Conditional – Special Uses	<div class="formula"><b>📐 Specjalne zastosowania:</b><br><code>If I were you, I would...</code> (rada)<br><code>If + Past Simple, could/might + infinitive</code> (mniejsza pewność)</div><div class="usage"><b>📖 Użycie:</b><ul><li><b>Rada:</b> „If I were you" = „Gdybym był na Twoim miejscu"</li><li><b>could w wyniku:</b> wyrażenie możliwości, nie pewności</li><li><b>might w wyniku:</b> jeszcze mniejsza pewność niż would</li></ul></div><div class="signal-words"><b>🔑 Słowa sygnałowe:</b> if I were you, could, might, would be able to</div><div class="tip"><b>💡 Wskazówka FCE:</b> „If I were you" to bardzo przydatna fraza w Writing Part 2 (letter/email z radą) i Speaking Part 3.</div>	<div class="examples"><p>1. <i><b>If I were you</b>, I <b>would choose</b> the environmental science course.</i></p><p>   🇵🇱 <i>Gdybym był na twoim miejscu, wybrałbym kurs o naukach środowiskowych.</i></p><p>2. <i>If we <b>saved</b> enough money, we <b>could afford</b> a trip to Japan.</i></p><p>   🇵🇱 <i>Gdybyśmy zaoszczędzili dość pieniędzy, moglibyśmy pozwolić sobie na wycieczkę do Japonii.</i></p><p>3. <i>If he <b>trained</b> every day, he <b>might win</b> the competition.</i></p><p>   🇵🇱 <i>Gdyby trenował codziennie, mógłby wygrać zawody.</i></p></div>	<div class="mistakes"><p><span class="wrong">❌ If I were you, I will study more.</span></p><p><span class="correct">✅ If I were you, I would study more.</span></p><p><b>Wyjaśnienie:</b> W Second Conditional używamy „would", nie „will". „Will" to First Conditional (realne sytuacje).</p><hr><p><span class="wrong">❌ If I would be you, I would change jobs.</span></p><p><span class="correct">✅ If I were you, I would change jobs.</span></p><p><b>Wyjaśnienie:</b> Nigdy „If I would be you". Zawsze „If I were you".</p></div>	fce grammar conditionals
```

## Procedura

1. Zidentyfikuj główne zagadnienie gramatyczne
2. Podziel je na logiczne podtematy (każdy = osobna karta)
3. Dla każdej karty wygeneruj kompletny wiersz TSV
4. Zapisz wynik w `output/fce-grammar-[temat]-[data].tsv`
5. Zweryfikuj poprawność formatu (5 kolumn TSV)
