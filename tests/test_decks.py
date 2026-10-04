"""Pliki w decks/ muszą odtwarzać TSV z output/ bajt w bajt.

Karty z tych plików są już w kolekcji użytkownika. Jeśli test nie przechodzi,
uruchom `python decks/<plik>.py` i sprawdź w `git diff`, czy zmiana jest zamierzona.
Zmiana pierwszego pola tworzy w Anki nową notatkę.
"""
import importlib.util
import unittest

from helpers import OUTPUT, ROOT


def load_deck(path):
    spec = importlib.util.spec_from_file_location(f"deck_{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DeckSourcesTest(unittest.TestCase):
    def test_sources_reproduce_output(self):
        deck_files = sorted((ROOT / "decks").glob("*.py"))
        self.assertTrue(deck_files)
        for deck_file in deck_files:
            module = load_deck(deck_file)
            for name, rows in module.OUTPUTS.items():
                with self.subTest(deck=deck_file.name, tsv=name):
                    rendered = "".join("\t".join(r) + "\n" for r in rows)
                    self.assertEqual(rendered, (OUTPUT / name).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
