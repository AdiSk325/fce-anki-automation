# FCE Anki Automation - Automatyczne generowanie fiszek do nauki FCE

Narzędzie do automatycznego generowania fiszek Anki dla słówek z egzaminu FCE (First Certificate in English) przy użyciu lokalnego modelu językowego Ollama (llama3).

## 📋 Spis treści

- [Wymagania](#wymagania)
- [Instalacja Ollama](#instalacja-ollama)
- [Instalacja projektu](#instalacja-projektu)
- [Konfiguracja Anki](#konfiguracja-anki)
- [Użycie](#użycie)
- [Struktura plików](#struktura-plików)
- [Troubleshooting](#troubleshooting)

## 🎯 Wymagania

Przed rozpoczęciem upewnij się, że masz zainstalowane:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Ollama** - Lokalne środowisko do uruchamiania modeli AI
- **Anki** - Program do nauki z fiszkami [Download Anki](https://apps.ankiweb.net/)

## 🚀 Instalacja Ollama

### Windows / macOS / Linux

1. Pobierz i zainstaluj Ollama ze strony: https://ollama.com/

2. Po instalacji uruchom terminal/wiersz polecenia i pobierz model llama3:

```bash
ollama run llama3
```

3. Poczekaj, aż model się pobierze (może to zająć kilka minut, w zależności od połączenia internetowego).

4. Po pobraniu możesz przetestować model wpisując dowolne pytanie. Aby zakończyć test, wpisz `/bye`.

5. Sprawdź, czy Ollama działa poprawnie:

```bash
ollama list
```

Powinieneś zobaczyć model `llama3` na liście.

## 📦 Instalacja projektu

1. Sklonuj repozytorium lub pobierz pliki projektu:

```bash
git clone https://github.com/AdiSk325/fce-anki-automation.git
cd fce-anki-automation
```

2. (Opcjonalnie, ale zalecane) Stwórz wirtualne środowisko Python:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt
```

## 📚 Konfiguracja Anki

Aby poprawnie zaimportować wygenerowane fiszki do Anki, musisz stworzyć odpowiedni typ notatki.

### Tworzenie typu notatki

1. Uruchom Anki i otwórz swoją talię (lub stwórz nową).

2. Przejdź do **Narzędzia** → **Zarządzaj typami notatek** (Tools → Manage Note Types).

3. Kliknij **Dodaj** (Add) i wybierz **Cloze**.

4. Nazwij nowy typ np. `FCE Vocabulary Cloze`.

5. Kliknij **Pola** (Fields) i upewnij się, że masz następujące pola w dokładnie tej kolejności:
   - **Text** (domyślnie powinno być)
   - **Translation** (kliknij "Dodaj" aby dodać to pole)
   - **Definition** (kliknij "Dodaj" aby dodać to pole)
   - **Word** (kliknij "Dodaj" aby dodać to pole)

6. Opcjonalnie możesz dostosować szablony kart:

   **Front Template:**
   ```html
   {{cloze:Text}}
   <hr>
   <div style="color: #666; font-size: 14px;">{{Definition}}</div>
   ```

   **Back Template:**
   ```html
   {{cloze:Text}}
   <hr>
   <div style="margin-top: 10px; color: #444;">
     <strong>Tłumaczenie:</strong> {{Translation}}
   </div>
   <div style="margin-top: 5px; color: #666;">
     <strong>Definicja:</strong> {{Definition}}
   </div>
   <div style="margin-top: 5px; color: #888; font-size: 12px;">
     <strong>Słowo:</strong> {{Word}}
   </div>
   ```

7. Kliknij **Zapisz** (Save) i zamknij okna konfiguracji.

## 🎮 Użycie

### Krok 1: Przygotuj listę słówek

Otwórz plik `slowka.txt` (lub stwórz go, jeśli nie istnieje) i dodaj słowa lub frazy, które chcesz nauczyć się do FCE. Każde słowo/fraza powinno być w osobnej linii:

```
resilient
inevitable
to pull off
breakthrough
overwhelming
```

**Uwaga:** Plik `slowka.txt` jest domyślnie w `.gitignore`, więc Twoje osobiste słówka nie będą commitowane do repozytorium.

### Krok 2: Uruchom skrypt

Upewnij się, że Ollama jest uruchomiona (model llama3 musi być dostępny). Następnie uruchom skrypt:

```bash
python fce_local_generator.py
```

Skrypt:
1. Odczyta słowa z pliku `slowka.txt`
2. Połączy się z lokalnym modelem llama3 przez Ollama
3. Wygeneruje dla każdego słowa:
   - Zdanie przykładowe z formatowaniem Cloze `{{c1::słowo}}`
   - Polskie tłumaczenie całego zdania
   - Polską definicję/wyjaśnienie słowa
4. Zapisze wszystko do pliku `import_to_anki.csv`

### Krok 3: Importuj do Anki

1. W Anki przejdź do **Plik** → **Importuj** (File → Import).

2. Wybierz plik `import_to_anki.csv`.

3. W oknie importu ustaw:
   - **Typ:** `FCE Vocabulary Cloze` (lub jak nazwałeś swój typ notatki)
   - **Talia:** Wybierz talię, do której chcesz dodać fiszki
   - **Separator pól:** Średnik (;)
   - **Dopasowanie pól:** Upewnij się, że pola są poprawnie dopasowane:
     - Pole 1 → Text
     - Pole 2 → Translation
     - Pole 3 → Definition
     - Pole 4 → Word

4. Kliknij **Importuj** (Import).

5. Gotowe! Możesz teraz uczyć się swoich nowych fiszek.

## 📁 Struktura plików

```
fce-anki-automation/
├── fce_local_generator.py   # Główny skrypt generujący fiszki
├── requirements.txt          # Zależności Python
├── slowka.txt               # Twoja lista słówek (ignorowana przez git)
├── import_to_anki.csv       # Wygenerowany plik CSV (ignorowany przez git)
├── .gitignore               # Pliki ignorowane przez git
└── README.md                # Ta dokumentacja
```

## 🔧 Troubleshooting

### Problem: "Błąd połączenia z Ollama"

**Rozwiązanie:**
- Upewnij się, że Ollama jest uruchomiona. Możesz to sprawdzić wpisując `ollama list` w terminalu.
- Sprawdź, czy model `llama3` jest pobrany: `ollama run llama3`
- Jeśli problem nadal występuje, zrestartuj Ollama.

### Problem: "Plik 'slowka.txt' nie został znaleziony"

**Rozwiązanie:**
- Utwórz plik `slowka.txt` w głównym katalogu projektu.
- Dodaj do niego słowa (jedno słowo/fraza na linię).

### Problem: Błędy parsowania JSON

**Rozwiązanie:**
- Skrypt zawiera funkcję `clean_json_string`, która automatycznie naprawia większość problemów.
- Jeśli błąd nadal występuje, spróbuj ponownie uruchomić skrypt - czasami model może zwrócić nieprawidłowy format.

### Problem: Fiszki nie importują się poprawnie do Anki

**Rozwiązanie:**
- Sprawdź, czy typ notatki ma wszystkie wymagane pola: Text, Translation, Definition, Word.
- Upewnij się, że podczas importu wybrałeś średnik (;) jako separator.
- Sprawdź, czy pola są poprawnie dopasowane podczas importu.

### Problem: Model generuje odpowiedzi w złym języku

**Rozwiązanie:**
- Prompt w skrypcie jest zaprojektowany tak, aby generować polskie tłumaczenia i definicje.
- Jeśli mimo to otrzymujesz odpowiedzi w innym języku, spróbuj ponownie uruchomić skrypt.
- Możesz również edytować prompt w pliku `fce_local_generator.py` w funkcji `generate_flashcard()`.

## 📝 Licencja

Ten projekt jest dostępny jako open source. Możesz go swobodnie używać i modyfikować.

## 🤝 Wkład

Jeśli chcesz przyczynić się do rozwoju projektu:
1. Fork repozytorium
2. Stwórz branch dla swojej funkcjonalności
3. Commit swoich zmian
4. Wyślij Pull Request

## 📧 Kontakt

Jeśli masz pytania lub sugestie, stwórz Issue w repozytorium GitHub.

---

**Powodzenia w nauce do FCE! 🎓**