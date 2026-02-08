# Workflow – Jak korzystać z projektu

## Przegląd

Ten projekt wykorzystuje GitHub Copilot jako agenta AI do generowania profesjonalnego wsadu do Anki na potrzeby przygotowania do egzaminu FCE (B2 First).

## Krok po kroku

### 1. Przygotowanie materiału wejściowego

Umieść swoje materiały w odpowiednim katalogu:

```
input/
├── word-lists/          ← listy słów do nauki
├── grammar-topics/      ← zagadnienia gramatyczne
└── examples/            ← przykłady (do podglądu)
```

**Format wejściowy** – możesz użyć dowolnego formatu tekstowego:
- Prosta lista słów (jedno na linię)
- Lista z tłumaczeniami
- Opis tematu gramatycznego
- Skopiowany fragment podręcznika
- Notatki własne

### 2. Wybierz odpowiedni prompt

W katalogu `.github/prompts/` znajdziesz gotowe instrukcje dla Copilota:

| Prompt | Do czego służy |
|--------|---------------|
| `vocabulary.prompt.md` | Konwersja list słów |
| `grammar.prompt.md` | Generowanie kart gramatycznych |
| `phrasal-verbs.prompt.md` | Karty z czasownikami frazowymi |
| `collocations.prompt.md` | Karty z kolokacjami |
| `use-of-english.prompt.md` | Zadania Use of English |

### 3. Uruchom Copilota

#### Opcja A: GitHub Copilot Chat (VS Code)

1. Otwórz plik wejściowy w VS Code
2. Otwórz Copilot Chat (`Ctrl+Shift+I` lub `Cmd+Shift+I`)
3. Użyj polecenia z odniesieniem do promptu:
   ```
   @workspace /prompt vocabulary
   Przetworz plik input/word-lists/moja-lista.txt na karty Anki
   ```

#### Opcja B: GitHub Copilot Agent (Coding Agent)

1. Utwórz issue z opisem zadania, np.:
   ```
   Przetworz listę słów z input/word-lists/travel.txt na karty Anki vocabulary
   ```
2. Przypisz do Copilot Coding Agent
3. Agent automatycznie wygeneruje plik TSV w `output/`

#### Opcja C: Ręczne polecenie w Chat

1. Skopiuj treść odpowiedniego promptu
2. Wklej do Copilot Chat
3. Dołącz materiał wejściowy
4. Copilot wygeneruje gotowy plik TSV

### 4. Zwaliduj wynik

```bash
python scripts/validate_output.py output/fce-vocabulary-travel-2024-01-15.tsv
```

Lub zwaliduj wszystkie pliki w katalogu:
```bash
python scripts/validate_output.py output/
```

### 5. Opcjonalnie: Połącz pliki

Jeśli masz wiele plików tego samego typu:
```bash
python scripts/merge_decks.py output/fce-vocabulary-*.tsv -o output/fce-vocabulary-all.tsv
```

### 6. Importuj do Anki

1. Otwórz Anki
2. **Plik** → **Importuj**
3. Wybierz plik `.tsv` z `output/`
4. Skonfiguruj mapowanie pól (patrz `templates/note-types.md`)
5. Importuj!

## Przykładowy scenariusz

### Scenariusz: Nauka słownictwa z tematu "Environment"

```bash
# 1. Utwórz plik wejściowy
echo "pollution
renewable energy
carbon footprint
sustainability
biodiversity
deforestation
greenhouse effect
climate change
ecosystem
recycling" > input/word-lists/environment.txt

# 2. Poproś Copilota o przetworzenie (w Chat lub jako Issue)
# "Przetworz input/word-lists/environment.txt na karty vocabulary z użyciem
#  promptu .github/prompts/vocabulary.prompt.md"

# 3. Zwaliduj wynik
python scripts/validate_output.py output/fce-vocabulary-environment-2024-01-15.tsv

# 4. Importuj do Anki
```

## Wskazówki

- **Małe partie**: Lepiej przetwarzać 10-20 słów na raz niż 100
- **Sprawdzaj jakość**: Przejrzyj wygenerowane karty przed importem
- **Tagi**: Korzystaj z tagów do organizacji nauki w Anki
- **Regularne generowanie**: Twórz nowe karty regularnie, np. po każdej lekcji
- **Customizacja**: Możesz modyfikować prompty w `.github/prompts/` pod swoje potrzeby
