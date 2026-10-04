import json
import re
import unittest

from helpers import ROOT

from validate_output import count_kwt_words

SETS = ROOT / "apps" / "pieciominutowka" / "sets"
KINDS = {"cloze", "kwt", "write"}
FILENAME = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.json$")


class QuizSetsTest(unittest.TestCase):
    """Zestawy Pięciominutówki muszą mieć format, który rozumie strona (docs/pieciominutowka.md)."""

    def test_sets_exist(self):
        self.assertTrue(list(SETS.glob("*.json")))

    def test_every_set(self):
        for path in sorted(SETS.glob("*.json")):
            with self.subTest(set=path.name):
                self.assertRegex(path.name, FILENAME)
                data = json.loads(path.read_text(encoding="utf-8"))
                for field in ("title", "created", "items"):
                    self.assertIn(field, data)
                items = data["items"]
                self.assertTrue(items)
                ids = [item["id"] for item in items]
                self.assertEqual(len(ids), len(set(ids)), "powtórzone id zadania")
                for item in items:
                    self.check_item(item)

    def check_item(self, item):
        with self.subTest(item=item.get("id")):
            self.assertIn(item.get("kind"), KINDS)
            for field in ("id", "label", "instruction", "explain"):
                self.assertTrue(item.get(field), f"brak pola {field}")
            answers = item.get("answers")
            self.assertTrue(answers and all(isinstance(a, str) and a.strip() for a in answers))
            if item["kind"] in ("cloze", "kwt"):
                self.assertEqual(item.get("text", "").count("{gap}"), 1, "luka {gap} musi wystąpić raz")
            if item["kind"] == "cloze":
                for answer in answers:
                    self.assertEqual(len(answer.split()), 1, f"open cloze to jedno słowo: {answer!r}")
            if item["kind"] == "kwt":
                keyword = item.get("keyword", "")
                self.assertTrue(keyword and keyword == keyword.upper())
                self.assertTrue(item.get("source"))
                for answer in answers:
                    self.assertIn(keyword.lower(), answer.lower().split())
                    self.assertTrue(2 <= count_kwt_words(answer) <= 5, f"KWT 2–5 słów: {answer!r}")
            if item["kind"] == "write":
                self.assertTrue(item.get("source"))


if __name__ == "__main__":
    unittest.main()
