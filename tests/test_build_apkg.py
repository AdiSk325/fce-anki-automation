import json
import sqlite3
import tempfile
import unittest
import zipfile
from pathlib import Path

from helpers import quiet, write_tsv

import build_apkg as b


class StableIdentifiersTest(unittest.TestCase):
    """Te wartości są już w kolekcji AnkiDroid użytkownika. Zmiana = duplikaty kart po imporcie."""

    def test_note_type_ids(self):
        expected = {
            "FCE Vocabulary": 1719399069,
            "FCE Grammar": 1591284762,
            "FCE Phrasal Verbs": 1990346138,
            "FCE Collocations": 1493849618,
            "FCE Use of English": 1515238980,
        }
        self.assertEqual({t["name"]: b.stable_id("model", t["name"]) for t in b.NOTE_TYPES.values()}, expected)

    def test_deck_id(self):
        self.assertEqual(b.stable_id("deck", "FCE Preparation::3A Multi-word verbs::2 Meanings"), 1124340297)

    def test_note_guid(self):
        self.assertEqual(b.note_guid("FCE Phrasal Verbs", "come up with (sth)"), "218ac6fee6790a4c")
        self.assertEqual(b.note_guid("FCE Vocabulary", "naive"), "f59054f99b4a32ca")


class ParseSourceTest(unittest.TestCase):
    def test_subdeck(self):
        self.assertEqual(b.parse_source("output/fce-grammar-x.tsv=1 Rules", "Root"),
                         (Path("output/fce-grammar-x.tsv"), "Root::1 Rules"))

    def test_without_subdeck(self):
        self.assertEqual(b.parse_source("output/fce-grammar-x.tsv", "Root"), (Path("output/fce-grammar-x.tsv"), "Root"))


class BuildPackageTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def open_collection(self, apkg):
        with zipfile.ZipFile(apkg) as zf:
            self.assertEqual(zf.read("media"), b"{}")
            zf.extract("collection.anki2", self.dir)
        return sqlite3.connect(self.dir / "collection.anki2")

    def test_build_counts_decks_and_guids(self):
        vocab = write_tsv(self.dir / "fce-vocabulary-t.tsv", [
            ["naive", '<div class="translation"><b>naiwny</b></div>', '<div class="example"><p>x</p></div>', "fce vocabulary t"],
            ["loyal", '<div class="translation"><b>lojalny</b></div>', '<div class="example"><p>y</p></div>', "fce vocabulary t"],
        ])
        pv = write_tsv(self.dir / "fce-phrasal-verbs-t.tsv", [
            ["look into (sth)", "<p>zbadać</p>", "<p>ex</p>", "investigate", "fce phrasal-verbs look type-3"],
        ])
        apkg = self.dir / "t.apkg"
        quiet(b.build_apkg, [(vocab, "Root::1 Words"), (pv, "Root::2 Verbs")], apkg)

        con = self.open_collection(apkg)
        self.assertEqual(con.execute("select count(*) from notes").fetchone()[0], 3)
        self.assertEqual(con.execute("select count(*) from cards").fetchone()[0], 2 * 2 + 1 * 3)
        decks = {d["name"] for d in json.loads(con.execute("select decks from col").fetchone()[0]).values()}
        self.assertEqual(decks, {"Default", "Root", "Root::1 Words", "Root::2 Verbs"})
        guids = {row[0] for row in con.execute("select guid from notes")}
        self.assertIn(b.note_guid("FCE Vocabulary", "naive"), guids)
        self.assertIn(b.note_guid("FCE Phrasal Verbs", "look into (sth)"), guids)
        tags = con.execute("select tags from notes where sfld = 'look into (sth)'").fetchone()[0]
        self.assertEqual(tags.split(), ["fce", "phrasal-verbs", "look", "type-3"])
        con.close()

    def test_invalid_tsv_stops_build(self):
        broken = write_tsv(self.dir / "fce-vocabulary-broken.tsv", [["only", "three", "columns"]])
        with self.assertRaises(ValueError):
            quiet(b.build_apkg, [(broken, "Root")], self.dir / "x.apkg")
        self.assertFalse((self.dir / "x.apkg").exists())


if __name__ == "__main__":
    unittest.main()
