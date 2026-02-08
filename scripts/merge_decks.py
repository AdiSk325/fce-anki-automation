#!/usr/bin/env python3
"""
Narzędzie do łączenia wielu plików TSV w jeden plik.
Przydatne gdy generujesz karty w partiach i chcesz je połączyć przed importem.

Użycie:
    python merge_decks.py output/fce-vocabulary-*.tsv -o output/fce-vocabulary-all.tsv
    python merge_decks.py output/ --type vocabulary -o output/fce-vocabulary-merged.tsv
"""

import argparse
import csv
from pathlib import Path
import sys


def merge_tsv_files(input_files, output_file, remove_duplicates=True):
    """Łączy wiele plików TSV w jeden."""
    all_rows = []
    seen_keys = set()
    duplicates = 0

    for filepath in input_files:
        filepath = Path(filepath)
        if not filepath.exists():
            print(f"⚠️  Pominięto (nie istnieje): {filepath}")
            continue
        if filepath.suffix != ".tsv":
            print(f"⚠️  Pominięto (nie TSV): {filepath}")
            continue

        print(f"📄 Wczytywanie: {filepath.name}")
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                if row:
                    key = row[0].strip().lower()
                    if remove_duplicates and key in seen_keys:
                        duplicates += 1
                        continue
                    seen_keys.add(key)
                    all_rows.append(row)

    if not all_rows:
        print("❌ Brak danych do zapisania")
        return False

    # Zapisz
    output_path = Path(output_file)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(all_rows)

    print(f"\n✅ Zapisano: {output_path}")
    print(f"📊 Liczba kart: {len(all_rows)}")
    if duplicates > 0:
        print(f"🔄 Usunięto duplikatów: {duplicates}")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Łączenie plików TSV Anki (FCE)"
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="Pliki TSV do połączenia lub katalog"
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Ścieżka pliku wyjściowego"
    )
    parser.add_argument(
        "--type",
        help="Filtruj po typie (np. vocabulary, grammar) - tylko przy podaniu katalogu"
    )
    parser.add_argument(
        "--keep-duplicates",
        action="store_true",
        help="Zachowaj duplikaty (domyślnie: usuwaj)"
    )

    args = parser.parse_args()

    # Zbierz pliki wejściowe
    input_files = []
    for input_path in args.inputs:
        path = Path(input_path)
        if path.is_dir():
            pattern = f"fce-{args.type}-*.tsv" if args.type else "*.tsv"
            input_files.extend(sorted(path.glob(pattern)))
        else:
            input_files.append(path)

    if not input_files:
        print("❌ Nie znaleziono plików wejściowych")
        sys.exit(1)

    print(f"📁 Znaleziono {len(input_files)} plików do połączenia\n")

    result = merge_tsv_files(
        input_files,
        args.output,
        remove_duplicates=not args.keep_duplicates
    )
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
