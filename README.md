# FCE Anki Automation 🎓🃏

Automatyczne generowanie profesjonalnego wsadu do **Anki** na potrzeby przygotowania do egzaminu **FCE (B2 First)** z wykorzystaniem **GitHub Copilot** jako agenta AI.

## 🎯 Cel projektu

Projekt umożliwia szybką konwersję materiałów edukacyjnych (listy słów, zagadnienia gramatyczne, czasowniki frazowe, kolokacje, zadania Use of English) na gotowe do importu pliki TSV dla aplikacji Anki.

**Kluczowa idea**: Wykorzystanie GitHub Copilot (i innych agentów AI) z precyzyjnymi, szczegółowymi instrukcjami do automatycznego generowania wysokiej jakości fiszek.

## 📁 Struktura projektu

```
fce-anki-automation/
├── .github/
│   ├── copilot-instructions.md        # 📋 Główne instrukcje dla Copilota
│   └── prompts/                        # 🤖 Prompty dla agentów AI
│       ├── vocabulary.prompt.md        #    → Konwersja list słów
│       ├── grammar.prompt.md           #    → Generowanie kart gramatycznych
│       ├── phrasal-verbs.prompt.md     #    → Czasowniki frazowe
│       ├── collocations.prompt.md      #    → Kolokacje
│       └── use-of-english.prompt.md    #    → Zadania Use of English
├── templates/
│   ├── note-types.md                   # 📝 Specyfikacja typów notatek Anki
│   └── anki-card-style.css             # 🎨 Style CSS dla kart
├── input/
│   ├── word-lists/                     # 📥 Listy słów do przetworzenia
│   ├── grammar-topics/                 # 📥 Tematy gramatyczne
│   └── examples/                       # 📖 Przykładowe pliki wejściowe
├── output/                             # 📤 Wygenerowane pliki TSV
├── scripts/
│   ├── validate_output.py              # ✅ Walidacja plików TSV
│   └── merge_decks.py                  # 🔗 Łączenie plików TSV
└── docs/
    ├── workflow.md                     # 📘 Jak korzystać z projektu
    ├── fce-topics.md                   # 📚 Lista tematów FCE
    └── anki-import-guide.md            # 📖 Przewodnik importu do Anki
```

## 🚀 Szybki start

### 1. Przygotuj materiał wejściowy

Umieść swoją listę słów lub opis tematu w katalogu `input/`:

```bash
echo "accomplish
inevitable
thoroughly
sustainable
approximately" > input/word-lists/general-b2.txt
```

### 2. Użyj GitHub Copilot do generowania kart

**Opcja A – Copilot Chat (VS Code):**
```
Przetworz plik input/word-lists/general-b2.txt na karty Anki
zgodnie z instrukcjami z .github/prompts/vocabulary.prompt.md
i zapisz wynik w output/
```

**Opcja B – Copilot Coding Agent (GitHub Issue):**
Utwórz issue z opisem zadania – agent automatycznie wygeneruje plik TSV.

### 3. Zwaliduj wynik

```bash
python scripts/validate_output.py output/fce-vocabulary-general-2024-01-15.tsv
```

### 4. Importuj do Anki

Otwórz Anki → **Plik** → **Importuj** → wybierz wygenerowany plik `.tsv`

Szczegółowy przewodnik: [docs/anki-import-guide.md](docs/anki-import-guide.md)

## 🤖 Typy kart

| Typ | Prompt | Opis |
|-----|--------|------|
| **Vocabulary** | `vocabulary.prompt.md` | Słowo EN → Tłumaczenie PL + IPA + definicja + przykłady |
| **Grammar** | `grammar.prompt.md` | Reguła → Formuła + wyjaśnienie + typowe błędy |
| **Phrasal Verbs** | `phrasal-verbs.prompt.md` | Czasownik frazowy → Znaczenia + synonimy formalne |
| **Collocations** | `collocations.prompt.md` | Kolokacja → Tłumaczenie + typ + przykłady |
| **Use of English** | `use-of-english.prompt.md` | Zadanie FCE → Odpowiedź + wyjaśnienie |

## 📋 Dokumentacja

- [Workflow – jak korzystać z projektu](docs/workflow.md)
- [Tematy FCE – kompletna lista](docs/fce-topics.md)
- [Przewodnik importu do Anki](docs/anki-import-guide.md)
- [Specyfikacja typów notatek](templates/note-types.md)

## 🛠️ Narzędzia

### Walidacja plików TSV
```bash
# Waliduj pojedynczy plik
python scripts/validate_output.py output/fce-vocabulary-travel.tsv

# Waliduj wszystkie pliki w katalogu
python scripts/validate_output.py output/

# Waliduj z podaniem typu
python scripts/validate_output.py output/moj-plik.tsv --type vocabulary
```

### Łączenie plików
```bash
# Połącz wszystkie pliki vocabulary w jeden
python scripts/merge_decks.py output/fce-vocabulary-*.tsv -o output/fce-vocabulary-all.tsv
```

## 📖 Przykładowe pliki wejściowe

W katalogu `input/examples/` znajdziesz przykłady:
- `vocabulary-travel.txt` – lista słów z tematu podróży
- `grammar-conditionals.txt` – temat: tryby warunkowe
- `phrasal-verbs-get.txt` – phrasal verbs z GET
- `collocations-make-do.txt` – kolokacje MAKE vs DO
- `use-of-english-kwt.txt` – Key Word Transformation

## 📄 Licencja

Projekt edukacyjny do użytku osobistego.