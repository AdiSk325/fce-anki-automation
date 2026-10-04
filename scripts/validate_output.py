#!/usr/bin/env python3
"""
Walidator plików TSV wygenerowanych dla Anki.
Sprawdza poprawność formatu, kodowania i kompletność danych.

Użycie:
    python validate_output.py <plik.tsv> [--type vocabulary|grammar|phrasal-verbs|collocations|use-of-english]
    python validate_output.py output/  (waliduje wszystkie pliki TSV w katalogu)
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path

# Definicja oczekiwanych kolumn per typ
EXPECTED_COLUMNS = {
    "vocabulary": {"count": 4, "names": ["Front", "Back", "Example", "Tags"]},
    "grammar": {"count": 5, "names": ["Rule", "Explanation", "Examples", "CommonMistakes", "Tags"]},
    "phrasal-verbs": {"count": 5, "names": ["PhrasalVerb", "Meaning", "Examples", "Synonyms", "Tags"]},
    "collocations": {"count": 5, "names": ["Collocation", "Translation", "Example", "Type", "Tags"]},
    "use-of-english": {"count": 5, "names": ["Task", "Answer", "Explanation", "Type", "Tags"]},
}

# Prawidłowe prefiksy tagów per typ
VALID_TAG_PREFIXES = {
    "vocabulary": "fce vocabulary",
    "grammar": "fce grammar",
    "phrasal-verbs": "fce phrasal-verbs",
    "collocations": "fce collocations",
    "use-of-english": "fce use-of-english",
}


def detect_type_from_filename(filename):
    """Wykrywa typ karty na podstawie nazwy pliku: najpierw prefiks fce-<typ>-, potem dowolne wystąpienie."""
    name = Path(filename).stem.lower()
    for card_type in EXPECTED_COLUMNS:
        if name.startswith(f"fce-{card_type}-") or name == f"fce-{card_type}":
            return card_type
    for card_type in EXPECTED_COLUMNS:
        if card_type in name:
            return card_type
    return None


# Skróty liczone na egzaminie jako dwa słowa (didn't = did not). Końcówka 's bywa dopełniaczem,
# więc liczy się jako jedno słowo.
TWO_WORD_CONTRACTIONS = re.compile(r"(n't|'ll|'ve|'re|'d|'m)$", re.IGNORECASE)


def count_kwt_words(text):
    """Liczy słowa odpowiedzi KWT według zasad Cambridge (skróty = dwa słowa)."""
    words = [w.strip(".,;:!?()[]{}\"") for w in text.split()]
    return sum(2 if TWO_WORD_CONTRACTIONS.search(w) else 1 for w in words if w)


def validate_utf8(filepath):
    """Sprawdza poprawność kodowania UTF-8."""
    errors = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            f.read()
    except UnicodeDecodeError as e:
        errors.append(f"Błąd kodowania UTF-8: {e}")
    return errors


def validate_tsv_structure(filepath, card_type):
    """Sprawdza strukturę pliku TSV."""
    errors = []
    warnings = []
    expected = EXPECTED_COLUMNS.get(card_type)

    if not expected:
        errors.append(f"Nieznany typ karty: {card_type}")
        return errors, warnings

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        rows = list(reader)

    if not rows:
        errors.append("Plik jest pusty")
        return errors, warnings

    for i, row in enumerate(rows, 1):
        # Sprawdź liczbę kolumn
        if len(row) != expected["count"]:
            errors.append(
                f"Wiersz {i}: oczekiwano {expected['count']} kolumn, znaleziono {len(row)}"
            )
            continue

        # Sprawdź czy wymagane pola nie są puste
        for j, field in enumerate(row):
            if not field.strip():
                errors.append(
                    f"Wiersz {i}: puste pole '{expected['names'][j]}'"
                )

        # Sprawdź tagi (ostatnia kolumna)
        tags = row[-1].strip()
        expected_prefix = VALID_TAG_PREFIXES.get(card_type, "fce")
        if not tags.startswith(expected_prefix):
            warnings.append(
                f"Wiersz {i}: tag '{tags}' nie zaczyna się od '{expected_prefix}'"
            )

    return errors, warnings


def validate_use_of_english_logic(filepath):
    """Sprawdza podstawową logikę kart Use of English."""
    errors = []

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, row in enumerate(reader, 1):
            if len(row) != EXPECTED_COLUMNS["use-of-english"]["count"]:
                continue

            task, answer, _, task_type, _ = row

            if task_type.strip() != "key-word-transformation":
                continue

            keyword_match = re.search(
                r'<p class="keyword">\s*Słowo kluczowe:\s*<b>([^<]+)</b>',
                task,
                re.IGNORECASE,
            )
            if not keyword_match:
                errors.append(
                    f"Wiersz {i}: nie można odczytać słowa kluczowego w zadaniu KWT"
                )
                continue

            keyword = keyword_match.group(1).strip()
            # Sama odpowiedź to pole .answer; pełne zdanie (.full-sentence) nie wlicza się do limitu słów.
            answer_match = re.search(r'<div class="answer">(.*?)</div>', answer, re.IGNORECASE | re.DOTALL)
            answer_text = re.sub(r"<[^>]+>", " ", answer_match.group(1) if answer_match else answer)
            answer_text = re.sub(r"\s+", " ", answer_text).strip()
            answer_words = {word.strip(".,;:!?()[]{}\"'").upper() for word in answer_text.split()}

            if keyword.upper() not in answer_words:
                errors.append(
                    f"Wiersz {i}: odpowiedź KWT nie zawiera słowa kluczowego '{keyword}'"
                )

            word_count = count_kwt_words(answer_text)
            if not 2 <= word_count <= 5:
                errors.append(
                    f"Wiersz {i}: odpowiedź KWT '{answer_text}' ma {word_count} słów (dozwolone 2–5)"
                )

    return errors


def validate_html(filepath):
    """Podstawowa walidacja HTML w polach."""
    warnings = []
    tag_names = ["b", "i", "div", "ul", "li", "p", "span", "code"]

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, row in enumerate(reader, 1):
            for j, field in enumerate(row):
                for tag in tag_names:
                    open_count = len(re.findall(rf"<{tag}[\s>]", field, re.IGNORECASE))
                    close_count = len(re.findall(rf"</{tag}>", field, re.IGNORECASE))
                    if open_count > 0 and close_count == 0:
                        warnings.append(
                            f"Wiersz {i}, pole {j+1}: możliwy niezamknięty tag <{tag}>"
                        )

    return warnings


def check_duplicates(filepath):
    """Sprawdza duplikaty (na podstawie pierwszej kolumny)."""
    warnings = []
    seen = {}

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, row in enumerate(reader, 1):
            if row:
                key = row[0].strip().lower()
                if key in seen:
                    warnings.append(
                        f"Wiersz {i}: duplikat '{row[0]}' (pierwszy w wierszu {seen[key]})"
                    )
                else:
                    seen[key] = i

    return warnings


def check_cross_file_duplicates(tsv_files, forced_type=None):
    """Szuka tego samego pierwszego pola w różnych plikach jednego typu.

    build_apkg.py liczy GUID notatki z typu i pierwszego pola, więc taki duplikat
    w dwóch paczkach skleiłby się w Anki w jedną notatkę.
    """
    warnings = []
    seen = {}
    for tsv_file in sorted(tsv_files):
        card_type = forced_type or detect_type_from_filename(tsv_file)
        if not card_type:
            continue
        with open(tsv_file, "r", encoding="utf-8") as f:
            for i, row in enumerate(csv.reader(f, delimiter="\t"), 1):
                if not row:
                    continue
                key = (card_type, row[0].strip().lower())
                if key in seen and seen[key][0] != tsv_file.name:
                    first_file, first_row = seen[key]
                    warnings.append(
                        f"{tsv_file.name} wiersz {i}: '{row[0]}' jest już w {first_file} (wiersz {first_row})"
                    )
                else:
                    seen.setdefault(key, (tsv_file.name, i))
    return warnings


def validate_file(filepath, card_type=None):
    """Główna funkcja walidacji pliku."""
    filepath = Path(filepath)

    if not filepath.exists():
        print(f"❌ Plik nie istnieje: {filepath}")
        return False

    if not filepath.suffix == ".tsv":
        print(f"⚠️  Pominięto (nie TSV): {filepath}")
        return True

    # Wykryj typ karty
    if not card_type:
        card_type = detect_type_from_filename(filepath)
    if not card_type:
        print(f"⚠️  Nie można wykryć typu karty z nazwy pliku: {filepath.name}")
        print("   Użyj --type aby określić typ ręcznie")
        return False

    print(f"\n{'='*60}")
    print(f"📄 Walidacja: {filepath.name}")
    print(f"   Typ: {card_type}")
    print(f"{'='*60}")

    all_errors = []
    all_warnings = []

    # 1. Kodowanie UTF-8
    utf8_errors = validate_utf8(filepath)
    all_errors.extend(utf8_errors)

    # 2. Struktura TSV
    if not utf8_errors:
        struct_errors, struct_warnings = validate_tsv_structure(filepath, card_type)
        all_errors.extend(struct_errors)
        all_warnings.extend(struct_warnings)

    # 3. HTML
    if not utf8_errors:
        html_warnings = validate_html(filepath)
        all_warnings.extend(html_warnings)

    # 4. Logika kart Use of English
    if not utf8_errors and card_type == "use-of-english":
        logic_errors = validate_use_of_english_logic(filepath)
        all_errors.extend(logic_errors)

    # 5. Duplikaty
    if not utf8_errors:
        dup_warnings = check_duplicates(filepath)
        all_warnings.extend(dup_warnings)

    # Raport
    if all_errors:
        print(f"\n❌ BŁĘDY ({len(all_errors)}):")
        for error in all_errors:
            print(f"   • {error}")

    if all_warnings:
        print(f"\n⚠️  OSTRZEŻENIA ({len(all_warnings)}):")
        for warning in all_warnings:
            print(f"   • {warning}")

    if not all_errors and not all_warnings:
        print(f"\n✅ Plik jest poprawny!")

    # Statystyki
    if not utf8_errors:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            row_count = sum(1 for _ in reader)
        print(f"\n📊 Statystyki:")
        print(f"   Liczba kart: {row_count}")

    return len(all_errors) == 0


def main():
    parser = argparse.ArgumentParser(
        description="Walidator plików TSV dla Anki (FCE)"
    )
    parser.add_argument(
        "path",
        help="Ścieżka do pliku TSV lub katalogu z plikami TSV"
    )
    parser.add_argument(
        "--type",
        choices=list(EXPECTED_COLUMNS.keys()),
        help="Typ karty (jeśli nie można wykryć z nazwy pliku)"
    )

    args = parser.parse_args()
    path = Path(args.path)

    if path.is_dir():
        tsv_files = list(path.glob("*.tsv"))
        if not tsv_files:
            print(f"Brak plików TSV w katalogu: {path}")
            sys.exit(1)

        results = []
        for tsv_file in sorted(tsv_files):
            result = validate_file(tsv_file, args.type)
            results.append(result)

        cross_warnings = check_cross_file_duplicates(tsv_files, args.type)
        print(f"\n{'='*60}")
        if cross_warnings:
            print(f"⚠️  DUPLIKATY MIĘDZY PLIKAMI ({len(cross_warnings)}):")
            for warning in cross_warnings:
                print(f"   • {warning}")
        print(f"📋 PODSUMOWANIE: {sum(results)}/{len(results)} plików poprawnych")
        sys.exit(0 if all(results) else 1)
    else:
        result = validate_file(path, args.type)
        sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
