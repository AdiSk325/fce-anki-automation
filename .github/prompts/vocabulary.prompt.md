# Konwersja listy słów na karty Anki – Vocabulary

## Instrukcja

Przekonwertuj podaną listę słów na profesjonalny wsad do Anki w formacie TSV.

## Format wejściowy

Lista słów może być w dowolnym formacie:
- Prosta lista słów (jedno słowo na linię)
- Lista z tłumaczeniami (słowo – tłumaczenie)
- Lista tematyczna (nagłówek tematu + słowa)
- Tekst z zaznaczonymi słowami do nauki

## Format wyjściowy

Plik TSV z kolumnami oddzielonymi tabulatorem:

```
Front	Back	Example	Tags
```

### Specyfikacja pól

**Front** (Przód karty):
- Słowo lub fraza po angielsku
- Jeśli słowo ma wiele form, użyj najczęstszej
- Dla phrasal verbs użyj formy bezokolicznikowej

**Back** (Tył karty) – format HTML:
```html
<div class="pos"><b>[część mowy]</b></div>
<div class="ipa">/wymowa IPA/</div>
<div class="translation"><b>🇵🇱 tłumaczenie polskie</b></div>
<div class="definition">🇬🇧 definicja po angielsku (prosta, poziom B2)</div>
```

**Example** (Przykłady) – format HTML:
```html
<div class="example">
<p>1. <i>Zdanie przykładowe po angielsku z <b>pogrubionym słowem</b>.</i></p>
<p>   🇵🇱 <i>Tłumaczenie zdania na polski.</i></p>
<p>2. <i>Drugie zdanie przykładowe z <b>pogrubionym słowem</b>.</i></p>
<p>   🇵🇱 <i>Tłumaczenie drugiego zdania.</i></p>
</div>
```

**Tags**:
- Format: `fce vocabulary [temat]`
- Temat w kebab-case, np.: `fce vocabulary travel`
- Jeśli słowo pasuje do wielu tematów, użyj najbardziej trafnego

## Wymagania jakościowe

1. **Minimum 2 zdania przykładowe** dla każdego słowa
2. **Wymowa IPA** – poprawna notacja fonetyczna
3. **Tłumaczenia** – naturalne, nie dosłowne
4. **Definicje EN** – proste, zrozumiałe na poziomie B2
5. **Przykłady** – z kontekstem FCE (typowe tematy egzaminacyjne)
6. **Część mowy** – noun / verb / adjective / adverb / phrase / idiom
7. **Kolokacje** – jeśli słowo ma ważne kolokacje, uwzględnij je w przykładach

## Przykład

Wejście:
```
accomplish
inevitable
thoroughly
```

Wyjście (TSV):
```
accomplish	<div class="pos"><b>verb</b></div><div class="ipa">/əˈkɒmplɪʃ/</div><div class="translation"><b>🇵🇱 osiągnąć, dokonać</b></div><div class="definition">🇬🇧 to succeed in doing something, especially after a lot of effort</div>	<div class="example"><p>1. <i>She managed to <b>accomplish</b> all her goals before the end of the year.</i></p><p>   🇵🇱 <i>Udało jej się osiągnąć wszystkie cele przed końcem roku.</i></p><p>2. <i>What do you hope to <b>accomplish</b> by studying abroad?</i></p><p>   🇵🇱 <i>Co masz nadzieję osiągnąć, studiując za granicą?</i></p></div>	fce vocabulary general
inevitable	<div class="pos"><b>adjective</b></div><div class="ipa">/ɪˈnevɪtəbl/</div><div class="translation"><b>🇵🇱 nieunikniony, nieuchronny</b></div><div class="definition">🇬🇧 certain to happen and impossible to avoid</div>	<div class="example"><p>1. <i>Change is an <b>inevitable</b> part of life that we all need to accept.</i></p><p>   🇵🇱 <i>Zmiana jest nieuniknioną częścią życia, którą wszyscy musimy zaakceptować.</i></p><p>2. <i>It was <b>inevitable</b> that technology would transform education.</i></p><p>   🇵🇱 <i>Było nieuniknione, że technologia zmieni edukację.</i></p></div>	fce vocabulary general
thoroughly	<div class="pos"><b>adverb</b></div><div class="ipa">/ˈθʌrəli/</div><div class="translation"><b>🇵🇱 dokładnie, gruntownie; całkowicie</b></div><div class="definition">🇬🇧 completely and with great attention to detail</div>	<div class="example"><p>1. <i>Make sure you <b>thoroughly</b> prepare for the speaking exam.</i></p><p>   🇵🇱 <i>Upewnij się, że dokładnie przygotujesz się do egzaminu ustnego.</i></p><p>2. <i>I <b>thoroughly</b> enjoyed the cultural exchange programme.</i></p><p>   🇵🇱 <i>Całkowicie podobał mi się program wymiany kulturowej.</i></p></div>	fce vocabulary general
```

## Procedura

1. Przeanalizuj listę wejściową i zidentyfikuj słowa do przetworzenia
2. Dla każdego słowa wygeneruj kompletny wiersz TSV zgodnie ze specyfikacją
3. Zapisz wynik w `output/fce-vocabulary-[temat]-[data].tsv`
4. Upewnij się, że plik jest poprawnie zakodowany w UTF-8
5. Zweryfikuj liczbę kolumn w każdym wierszu (4 kolumny)
