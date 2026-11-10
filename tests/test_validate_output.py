import tempfile
import unittest
from pathlib import Path

from helpers import OUTPUT, quiet, write_tsv

import validate_output as v


def kwt_row(answer, keyword="THOUGHT"):
    task = (f'<div class="kwt"><p class="original"><b>People believe the course is good.</b></p>'
            f'<p class="keyword">Słowo kluczowe: <b>{keyword}</b></p><p class="gap">The course ___ good.</p></div>')
    ans = f'<div class="answer"><b>{answer}</b></div><div class="full-sentence"><i>The course {answer} good.</i></div>'
    return [task, ans, '<div class="explanation"><p>x</p></div>', "key-word-transformation",
            "fce use-of-english key-word-transformation"]


class DetectTypeTest(unittest.TestCase):
    def test_prefix_wins_over_later_keyword(self):
        self.assertEqual(v.detect_type_from_filename("fce-use-of-english-grammar-x.tsv"), "use-of-english")
        self.assertEqual(v.detect_type_from_filename("fce-vocabulary-phrasal-verbs-x.tsv"), "vocabulary")

    def test_every_type_by_prefix(self):
        for card_type in v.EXPECTED_COLUMNS:
            self.assertEqual(v.detect_type_from_filename(f"output/fce-{card_type}-topic.tsv"), card_type)

    def test_fallback_and_unknown(self):
        self.assertEqual(v.detect_type_from_filename("my-collocations-list.tsv"), "collocations")
        self.assertIsNone(v.detect_type_from_filename("notes.tsv"))


def typing_row(scrambled, type_answer, task_type="word-order"):
    return [f'<div class="tr"><p class="word scrambled">{scrambled}</p></div>', type_answer,
            f'<div class="answer"><b>{type_answer}</b></div>', '<div class="explanation"><p>x</p></div>',
            task_type, f"fce typing {task_type}"]


class TypingTest(unittest.TestCase):
    def check(self, rows):
        with tempfile.TemporaryDirectory() as tmp:
            return v.validate_typing_logic(write_tsv(Path(tmp) / "fce-typing-t.tsv", rows))

    def test_scrambled_words_match_answer(self):
        self.assertEqual(self.check([
            typing_row("to / that / but / easier / it'd / eat out / agree / be / don't you ?",
                       "But don't you agree that it'd be easier to eat out?"),
            typing_row("saying / was / anyway / I / as / go / we .", "Anyway, as I was saying, we go."),
        ]), [])

    def test_missing_or_extra_word_is_an_error(self):
        errors = self.check([typing_row("could / go / we .", "We could always go.")])
        self.assertEqual(len(errors), 1)
        self.assertIn("rozsypanki", errors[0])

    def test_type_answer_must_be_plain_text(self):
        errors = self.check([
            typing_row("x", "<b>could always</b>", "gap-phrase"),
            typing_row("x", "could  always", "gap-phrase"),
            typing_row("x", "Don’t you think", "gap-phrase"),
        ])
        self.assertEqual(len(errors), 3)


class KwtTest(unittest.TestCase):
    def test_word_count_counts_contractions_as_two(self):
        self.assertEqual(v.count_kwt_words("is thought to be"), 4)
        self.assertEqual(v.count_kwt_words("didn't need to rewrite"), 5)
        self.assertEqual(v.count_kwt_words("the reader's attention"), 3)

    def check(self, rows):
        with tempfile.TemporaryDirectory() as tmp:
            return v.validate_use_of_english_logic(write_tsv(Path(tmp) / "fce-use-of-english-t.tsv", rows))

    def test_valid_answer(self):
        self.assertEqual(self.check([kwt_row("is thought to be")]), [])

    def test_too_long_and_missing_keyword(self):
        errors = self.check([kwt_row("is generally thought to be really"), kwt_row("is believed to be")])
        self.assertEqual(len(errors), 2)
        self.assertIn("2–5", errors[0])
        self.assertIn("słowa kluczowego", errors[1])

    def test_full_sentence_does_not_count(self):
        # Słowo kluczowe tylko w pełnym zdaniu, a nie w odpowiedzi → błąd.
        row = kwt_row("is said to be")
        row[1] += "<i>THOUGHT</i>"
        self.assertTrue(any("słowa kluczowego" in e for e in self.check([row])))


class DuplicatesTest(unittest.TestCase):
    def test_in_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = write_tsv(Path(tmp) / "fce-vocabulary-t.tsv", [["naive", "b", "e", "fce vocabulary"]] * 2)
            self.assertEqual(len(v.check_duplicates(path)), 1)

    def test_cross_file_same_type_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            files = [
                write_tsv(tmp / "fce-phrasal-verbs-a.tsv", [["give up", "m", "e", "s", "t"]]),
                write_tsv(tmp / "fce-phrasal-verbs-b.tsv", [["Give up", "m", "e", "s", "t"]]),
                write_tsv(tmp / "fce-vocabulary-c.tsv", [["give up", "b", "e", "t"]]),
            ]
            warnings = v.check_cross_file_duplicates(files)
            self.assertEqual(len(warnings), 1)
            self.assertIn("fce-phrasal-verbs-b.tsv", warnings[0])


class RepositoryDecksTest(unittest.TestCase):
    def test_all_output_files_are_valid(self):
        files = sorted(OUTPUT.glob("*.tsv"))
        self.assertTrue(files)
        invalid = [f.name for f in files if not quiet(v.validate_file, f)]
        self.assertEqual(invalid, [])

    def test_no_cross_file_duplicates(self):
        self.assertEqual(v.check_cross_file_duplicates(sorted(OUTPUT.glob("*.tsv"))), [])


if __name__ == "__main__":
    unittest.main()
