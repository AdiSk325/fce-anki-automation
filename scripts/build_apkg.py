#!/usr/bin/env python3
"""
Budowanie paczki Anki (.apkg) z plików TSV projektu.
Paczkę można otworzyć bezpośrednio w AnkiDroid (Android), AnkiMobile (iOS)
albo zaimportować w Anki Desktop (Plik → Importuj). Paczka zawiera gotowe
typy notatek (pola, szablony kart, CSS z templates/anki-card-style.css)
i strukturę talii, więc nie trzeba niczego konfigurować ręcznie.

Użycie:
    python build_apkg.py <plik.tsv>[=Podtalia] [...] --deck "Talia główna" -o paczka.apkg

Przykład:
    python scripts/build_apkg.py \\
        "output/fce-grammar-multi-word-verbs-3a.tsv=1 Rules" \\
        "output/fce-phrasal-verbs-multi-word-verbs-3a.tsv=2 Meanings" \\
        --deck "FCE Preparation::3A Multi-word verbs" \\
        -o output/fce-multi-word-verbs-3a.apkg

Typ notatki jest wykrywany z nazwy pliku (jak w validate_output.py)
albo ustawiany opcją --type. Identyfikatory notatek (GUID) są stałe dla
tego samego pierwszego pola, więc ponowny import poprawionej paczki
aktualizuje istniejące notatki zamiast tworzyć duplikaty.
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sqlite3
import sys
import tempfile
import time
import zipfile
from pathlib import Path

from validate_output import detect_type_from_filename, validate_file

CSS_PATH = Path(__file__).resolve().parent.parent / "templates" / "anki-card-style.css"

ANSWER_LINE = '<hr id="answer">'

SYNONYMS_TIP = '<div class="tip"><b>🔁 Synonimy:</b> {{Synonyms}}</div>'

# Typy notatek zgodne z templates/note-types.md.
# Kolumna Tags z TSV trafia do tagów notatki, a nie do pól.
NOTE_TYPES = {
    "vocabulary": {
        "name": "FCE Vocabulary",
        "fields": ["Front", "Back", "Example"],
        "templates": [
            (
                "Card 1: EN → PL",
                '<div class="front">{{Front}}</div>',
                "{{FrontSide}}" + ANSWER_LINE + "{{Back}}{{Example}}",
            ),
            (
                "Card 2: PL → EN",
                '<div class="prompt">Jak to powiedzieć po angielsku?</div>'
                '<div class="reverse reverse-vocab">{{Back}}</div>',
                '<div class="front">{{Front}}</div>' + ANSWER_LINE + "{{Back}}{{Example}}",
            ),
        ],
    },
    "grammar": {
        "name": "FCE Grammar",
        "fields": ["Rule", "Explanation", "Examples", "CommonMistakes"],
        "templates": [
            (
                "Card 1: Rule → Explanation",
                '<div class="front">{{Rule}}</div>',
                "{{FrontSide}}" + ANSWER_LINE + "{{Explanation}}{{Examples}}{{CommonMistakes}}",
            ),
            (
                "Card 2: Examples → Rule",
                '<div class="prompt">Jaka reguła / konstrukcja stoi za tymi zdaniami?</div>{{Examples}}',
                "{{FrontSide}}" + ANSWER_LINE + '<div class="front">{{Rule}}</div>{{Explanation}}',
            ),
        ],
    },
    "phrasal-verbs": {
        "name": "FCE Phrasal Verbs",
        "fields": ["PhrasalVerb", "Meaning", "Examples", "Synonyms"],
        "templates": [
            (
                "Card 1: Verb → Meaning",
                '<div class="front">{{PhrasalVerb}}</div>',
                "{{FrontSide}}" + ANSWER_LINE + "{{Meaning}}{{Examples}}" + SYNONYMS_TIP,
            ),
            (
                "Card 2: Meaning → Verb",
                '<div class="prompt">Jaki to multi-word / phrasal verb?</div>'
                '<div class="reverse">{{Meaning}}</div>',
                '<div class="back-side">{{FrontSide}}' + ANSWER_LINE
                + '<div class="front">{{PhrasalVerb}}</div>{{Examples}}' + SYNONYMS_TIP + "</div>",
            ),
            (
                "Card 3: Synonyms → Verb",
                '<div class="prompt">Multi-word / phrasal verb o znaczeniu:</div>'
                '<div class="front">{{Synonyms}}</div>',
                "{{FrontSide}}" + ANSWER_LINE
                + '<div class="front">{{PhrasalVerb}}</div>{{Meaning}}{{Examples}}',
            ),
        ],
    },
    "collocations": {
        "name": "FCE Collocations",
        "fields": ["Collocation", "Translation", "Example", "Type"],
        "templates": [
            (
                "Card 1: Collocation → Translation",
                '<div class="front">{{Collocation}}</div>',
                "{{FrontSide}}" + ANSWER_LINE
                + '{{Translation}}{{Example}}<div class="note"><b>Typ:</b> {{Type}}</div>',
            ),
            (
                "Card 2: Translation → Collocation",
                '<div class="prompt">Jaka to kolokacja?</div>'
                '<div class="reverse">{{Translation}}</div>',
                '<div class="back-side">{{FrontSide}}' + ANSWER_LINE
                + '<div class="front">{{Collocation}}</div>{{Example}}</div>',
            ),
        ],
    },
    "use-of-english": {
        "name": "FCE Use of English",
        "fields": ["Task", "Answer", "Explanation", "Type"],
        "templates": [
            (
                "Card 1: Task → Answer",
                "{{Task}}",
                "{{FrontSide}}" + ANSWER_LINE + "{{Answer}}{{Explanation}}",
            ),
        ],
    },
}

DEFAULT_DECK_CONFIG = {
    "id": 1,
    "name": "Default",
    "mod": 0,
    "usn": 0,
    "maxTaken": 60,
    "autoplay": True,
    "timer": 0,
    "replayq": True,
    "dyn": False,
    "new": {
        "bury": True,
        "delays": [1.0, 10.0],
        "initialFactor": 2500,
        "ints": [1, 4, 7],
        "order": 1,
        "perDay": 20,
        "separate": True,
    },
    "rev": {
        "bury": True,
        "ease4": 1.3,
        "fuzz": 0.05,
        "ivlFct": 1.0,
        "maxIvl": 36500,
        "minSpace": 1,
        "perDay": 200,
    },
    "lapse": {
        "delays": [10.0],
        "leechAction": 1,
        "leechFails": 8,
        "minInt": 1,
        "mult": 0.0,
    },
}

SCHEMA = """
CREATE TABLE col (
    id integer primary key, crt integer not null, mod integer not null,
    scm integer not null, ver integer not null, dty integer not null,
    usn integer not null, ls integer not null, conf text not null,
    models text not null, decks text not null, dconf text not null,
    tags text not null
);
CREATE TABLE notes (
    id integer primary key, guid text not null, mid integer not null,
    mod integer not null, usn integer not null, tags text not null,
    flds text not null, sfld integer not null, csum integer not null,
    flags integer not null, data text not null
);
CREATE TABLE cards (
    id integer primary key, nid integer not null, did integer not null,
    ord integer not null, mod integer not null, usn integer not null,
    type integer not null, queue integer not null, due integer not null,
    ivl integer not null, factor integer not null, reps integer not null,
    lapses integer not null, left integer not null, odue integer not null,
    odid integer not null, flags integer not null, data text not null
);
CREATE TABLE revlog (
    id integer primary key, cid integer not null, usn integer not null,
    ease integer not null, ivl integer not null, lastIvl integer not null,
    factor integer not null, time integer not null, type integer not null
);
CREATE TABLE graves (
    usn integer not null, oid integer not null, type integer not null
);
CREATE INDEX ix_notes_usn on notes (usn);
CREATE INDEX ix_cards_usn on cards (usn);
CREATE INDEX ix_revlog_usn on revlog (usn);
CREATE INDEX ix_cards_nid on cards (nid);
CREATE INDEX ix_cards_sched on cards (did, queue, due);
CREATE INDEX ix_revlog_cid on revlog (cid);
CREATE INDEX ix_notes_csum on notes (csum);
"""


def stable_id(kind, name):
    """Stałe ID dla typu notatki / talii, żeby kolejne paczki trafiały w te same obiekty."""
    digest = hashlib.sha1(f"fce-anki-automation:{kind}:{name}".encode("utf-8")).hexdigest()
    return (1 << 30) + int(digest[:8], 16) % (1 << 30)


def note_guid(model_name, first_field):
    return hashlib.sha1(f"{model_name}\x1f{first_field}".encode("utf-8")).hexdigest()[:16]


def strip_html(text):
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def field_checksum(text):
    return int(hashlib.sha1(strip_html(text).encode("utf-8")).hexdigest()[:8], 16)


def build_model(card_type, css, deck_id, now):
    spec = NOTE_TYPES[card_type]
    model_id = stable_id("model", spec["name"])
    fields = [
        {"name": name, "ord": i, "sticky": False, "rtl": False,
         "font": "Arial", "size": 20, "media": []}
        for i, name in enumerate(spec["fields"])
    ]
    templates = []
    req = []
    for ord_, (name, qfmt, afmt) in enumerate(spec["templates"]):
        templates.append({
            "name": name, "ord": ord_, "qfmt": qfmt, "afmt": afmt,
            "did": None, "bqfmt": "", "bafmt": "",
        })
        used = [i for i, f in enumerate(spec["fields"]) if "{{" + f + "}}" in qfmt]
        req.append([ord_, "any", used])
    model = {
        "id": model_id,
        "name": spec["name"],
        "type": 0,
        "mod": now,
        "usn": -1,
        "sortf": 0,
        "did": deck_id,
        "tmpls": templates,
        "flds": fields,
        "css": css,
        "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n"
                    "\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n"
                    "\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
        "latexPost": "\\end{document}",
        "tags": [],
        "vers": [],
        "req": req,
    }
    return model_id, model


def build_deck(name, now):
    deck_id = stable_id("deck", name)
    return deck_id, {
        "id": deck_id, "name": name, "desc": "", "mod": now, "usn": -1,
        "collapsed": False, "browserCollapsed": False, "dyn": 0, "conf": 1,
        "extendNew": 10, "extendRev": 50,
        "newToday": [0, 0], "revToday": [0, 0], "lrnToday": [0, 0], "timeToday": [0, 0],
    }


def read_tsv(path, card_type):
    expected = len(NOTE_TYPES[card_type]["fields"]) + 1
    with open(path, "r", encoding="utf-8") as f:
        rows = [row for row in csv.reader(f, delimiter="\t") if row]
    for i, row in enumerate(rows, 1):
        if len(row) != expected:
            raise ValueError(f"{path}: wiersz {i} ma {len(row)} kolumn, oczekiwano {expected}")
    return rows


def parse_source(arg, root_deck):
    """'plik.tsv=Podtalia' → (ścieżka, pełna nazwa talii)."""
    path, sep, subdeck = arg.partition("=")
    if not sep or not path.endswith(".tsv"):
        path, subdeck = arg, ""
    deck = f"{root_deck}::{subdeck}" if subdeck else root_deck
    return Path(path), deck


def build_apkg(sources, output, forced_type=None):
    # Paczka trafia prosto do Anki, więc niepoprawny TSV zatrzymuje budowanie.
    invalid = [path.name for path, _ in sources if not validate_file(path, forced_type)]
    if invalid:
        raise ValueError(f"Walidacja nie przeszła: {', '.join(invalid)}")

    now = int(time.time())
    css = CSS_PATH.read_text(encoding="utf-8")

    decks = {}
    models = {}
    notes = []
    cards = []
    next_id = now * 1000
    due = 0

    for path, deck_name in sources:
        card_type = forced_type or detect_type_from_filename(path)
        if card_type not in NOTE_TYPES:
            raise ValueError(f"Nie można wykryć typu karty z nazwy pliku: {path.name} (użyj --type)")

        # Talie nadrzędne dodajemy jawnie, żeby hierarchia była kompletna.
        parts = deck_name.split("::")
        for depth in range(1, len(parts) + 1):
            name = "::".join(parts[:depth])
            if name not in {d["name"] for d in decks.values()}:
                deck_id, deck = build_deck(name, now)
                decks[str(deck_id)] = deck
        deck_id = stable_id("deck", deck_name)

        model_id, model = build_model(card_type, css, deck_id, now)
        models.setdefault(str(model_id), model)
        template_count = len(NOTE_TYPES[card_type]["templates"])

        rows = read_tsv(path, card_type)
        for row in rows:
            fields, tags = row[:-1], row[-1].split()
            next_id += 1
            note_id = next_id
            notes.append((
                note_id, note_guid(model["name"], fields[0]), model_id, now, -1,
                " " + " ".join(tags) + " " if tags else "",
                "\x1f".join(fields), strip_html(fields[0]), field_checksum(fields[0]),
                0, "",
            ))
            for ord_ in range(template_count):
                next_id += 1
                cards.append((next_id, note_id, deck_id, ord_, now, -1,
                              0, 0, due, 0, 0, 0, 0, 0, 0, 0, 0, ""))
            due += 1
        print(f"📄 {path.name}: {len(rows)} notatek × {template_count} → talia '{deck_name}'")

    decks["1"] = build_deck("Default", now)[1] | {"id": 1}
    col_conf = {
        "activeDecks": [1], "curDeck": 1, "newSpread": 0, "collapseTime": 1200,
        "timeLim": 0, "estTimes": True, "dueCounts": True, "curModel": None,
        "nextPos": due + 1, "sortType": "noteFld", "sortBackwards": False, "addToCur": True,
    }

    with tempfile.TemporaryDirectory() as tmp:
        db_path = os.path.join(tmp, "collection.anki2")
        conn = sqlite3.connect(db_path)
        conn.executescript(SCHEMA)
        conn.execute(
            "INSERT INTO col VALUES (1, ?, ?, ?, 11, 0, 0, 0, ?, ?, ?, ?, '{}')",
            (now - now % 86400, now * 1000, now * 1000, json.dumps(col_conf),
             json.dumps(models), json.dumps(decks), json.dumps({"1": DEFAULT_DECK_CONFIG})),
        )
        conn.executemany("INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)", notes)
        conn.executemany("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", cards)
        conn.commit()
        conn.close()

        output = Path(output)
        output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(db_path, "collection.anki2")
            zf.writestr("media", "{}")

    print(f"\n✅ Zapisano: {output}")
    print(f"📊 Notatki: {len(notes)} | Karty: {len(cards)} | Talie: {len(decks) - 1}")


def main():
    parser = argparse.ArgumentParser(description="Budowanie paczki .apkg z plików TSV (FCE)")
    parser.add_argument("sources", nargs="+", help="Pliki TSV, opcjonalnie z podtalią: plik.tsv=Podtalia")
    parser.add_argument("--deck", default="FCE Preparation", help="Talia główna (domyślnie: FCE Preparation)")
    parser.add_argument("--type", choices=list(NOTE_TYPES), help="Wymuś typ karty dla wszystkich plików")
    parser.add_argument("-o", "--output", required=True, help="Ścieżka pliku .apkg")
    args = parser.parse_args()

    sources = [parse_source(arg, args.deck) for arg in args.sources]
    missing = [str(p) for p, _ in sources if not p.exists()]
    if missing:
        print(f"❌ Brak plików: {', '.join(missing)}")
        sys.exit(1)

    try:
        build_apkg(sources, args.output, args.type)
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
