#!/usr/bin/env python3
"""
Wspólne klocki HTML do pól kart Anki w formacie projektu.

Każda funkcja zwraca gotowy HTML jednego pola (albo listę pól) zgodny
z templates/note-types.md i klasami z templates/anki-card-style.css.
Tagi i kolejność kolumn składa plik talii w decks/, bo tam zależą od tematu.

Przykład (plik talii w decks/):
    from cardlib import examples_block, meaning_fields, write_tsv
    row = ["look into (sth)", meaning_fields([...], "Type 3 …"), examples_block([...]),
           "investigate", "fce phrasal-verbs look unit-3a type-3"]
    write_tsv("fce-phrasal-verbs-x.tsv", [row])
"""

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

GAP = "<b>______</b>"
KWT_GAP = "__________________"


def type_tags(types):
    """['1', '2', 'idiom'] → 'type-1 type-2 idiom'."""
    return " ".join(f"type-{t}" if t.isdigit() else t for t in types)


def examples_block(pairs, cls="examples"):
    """Lista (zdanie EN, tłumaczenie PL) → numerowane przykłady."""
    parts = [f"<p>{i}. <i>{en}</i></p><p>   🇵🇱 <i>{pl}</i></p>" for i, (en, pl) in enumerate(pairs, 1)]
    return f'<div class="{cls}">' + "".join(parts) + "</div>"


def mistakes_block(items):
    """Lista (błędnie, poprawnie, wyjaśnienie) → pole CommonMistakes."""
    parts = []
    for j, (wrong, right, why) in enumerate(items):
        if j:
            parts.append("<hr>")
        parts.append(
            f'<p><span class="wrong">❌ {wrong}</span></p>'
            f'<p><span class="correct">✅ {right}</span></p>'
            f"<p><b>Wyjaśnienie:</b> {why}</p>"
        )
    return '<div class="mistakes">' + "".join(parts) + "</div>"


def grammar_explanation(formula, usage, tip, signal="", signal_label="🔑 Czasowniki z lekcji:"):
    """Pole Explanation karty FCE Grammar."""
    html = (
        f'<div class="formula"><b>📐 Struktura:</b><br>{formula}</div>'
        '<div class="usage"><b>📖 Użycie:</b><ul>'
        + "".join(f"<li>{u}</li>" for u in usage)
        + "</ul></div>"
    )
    if signal:
        html += f'<div class="signal-words"><b>{signal_label}</b> {signal}</div>'
    return html + f'<div class="tip"><b>💡 Wskazówka FCE:</b> {tip}</div>'


def meaning_fields(meanings, note):
    """Pole Meaning karty FCE Phrasal Verbs: lista (PL, EN) + notatka gramatyczna."""
    multi = len(meanings) > 1
    parts = []
    for i, (pl, en) in enumerate(meanings, 1):
        label = f"🇵🇱 Znaczenie {i}:" if multi else "🇵🇱 Znaczenie:"
        parts.append(f'<div class="meaning"><p><b>{label}</b> {pl}</p><p>🇬🇧 <i>{en}</i></p></div>')
    parts.append(f'<div class="grammar-note"><b>📝 Gramatyka:</b> {note}</div>')
    return "".join(parts)


def vocab_back(pos, ipa, pl, en, note=""):
    """Pole Back karty FCE Vocabulary."""
    html = (f'<div class="pos"><b>{pos}</b></div><div class="ipa">{ipa}</div>'
            f'<div class="translation"><b>🇵🇱 {pl}</b></div><div class="definition">🇬🇧 {en}</div>')
    if note:
        html += f'<div class="note"><b>💡 Uwaga:</b> {note}</div>'
    return html


def colloc_translation(pl, en, note=""):
    """Pole Translation karty FCE Collocations."""
    html = f'<div class="translation"><p><b>🇵🇱 {pl}</b></p><p>🇬🇧 <i>{en}</i></p></div>'
    if note:
        html += f'<div class="note"><b>⚠️ Uwaga:</b> {note}</div>'
    return html


def answer_block(answer):
    return f'<div class="answer"><b>{answer}</b></div>'


def uoe_explanation(why, rule=None, tip=None):
    """Pole Explanation karty FCE Use of English (Wyjaśnienie / Reguła / Wskazówka)."""
    html = f'<div class="explanation"><p><b>🇵🇱 Wyjaśnienie:</b> {why}</p>'
    if rule is not None:
        html += f'<p><b>📐 Reguła:</b> {rule}</p>'
    if tip is not None:
        html += f'<p><b>💡 Wskazówka:</b> {tip}</p>'
    return html + "</div>"


def translation_fields(pl, hint, answer, alt, expl, wrong):
    """Task, Answer, Explanation dla typu `translation` (PL → EN)."""
    task = ('<div class="tr"><p class="instruction">🇵🇱 → 🇬🇧 Przetłumacz na angielski:</p>'
            f'<p class="pl-sentence">{pl}</p><p class="keyword">Użyj: <b>{hint}</b></p></div>')
    ans = answer_block(answer)
    if alt:
        ans += f'<p class="full-sentence">✅ Też poprawnie: <i>{alt}</i></p>'
    title, body = expl
    ex = f'<div class="explanation"><p><b>📐 {title}</b> {body}</p>'
    if wrong:
        ex += f'<p><span class="wrong">❌ {wrong}</span></p>'
    return [task, ans, ex + "</div>"]


def open_cloze_fields(sentence, answer, why, rule, tip):
    """Task, Answer, Explanation dla typu `open-cloze` (luka: GAP)."""
    return [f'<div class="oc"><p>{sentence}</p></div>', answer_block(answer), uoe_explanation(why, rule, tip)]


def word_formation_fields(sentence, base, answer, formation, expl, stress=None):
    """Task, Answer, Explanation dla typu `word-formation` (opcjonalnie z akcentem)."""
    task = f'<div class="wf"><p>{sentence} (<b>{base}</b>)</p></div>'
    ans = answer_block(answer) + f'<div class="formation"><i>{formation}</i></div>'
    if stress:
        ans += f'<p class="full-sentence">🔊 Akcent: {stress}</p>'
    return [task, ans, uoe_explanation(expl)]


def kwt_fields(original, keyword, gap, answer, full, why, rule, tip):
    """Task, Answer, Explanation dla typu `key-word-transformation`."""
    task = (f'<div class="kwt"><p class="original"><b>{original}</b></p>'
            f'<p class="keyword">Słowo kluczowe: <b>{keyword}</b></p><p class="gap">{gap}</p>'
            '<p class="instruction"><i>Uzupełnij zdanie używając 2-5 słów, w tym podanego słowa kluczowego. '
            'Nie zmieniaj formy słowa kluczowego.</i></p></div>')
    ans = answer_block(answer) + f'<div class="full-sentence"><i>{full}</i></div>'
    return [task, ans, uoe_explanation(why, rule, tip)]


def rule_explanation(rule):
    return f'<div class="explanation"><p><b>📐 Reguła:</b> {rule}</p></div>'


def stress_fields(syllables, stressed, position, ipa, pl, rule):
    """Task, Answer, Explanation dla typu `word-stress` (stressed = indeks sylaby od 0)."""
    task = ('<div class="tr"><p class="instruction">Która sylaba jest akcentowana?</p>'
            f'<p class="word">{" · ".join(syllables)}</p></div>')
    marked = "·".join(f"<b><u>{s.upper()}</u></b>" if i == stressed else s for i, s in enumerate(syllables))
    ans = f'<div class="answer">{marked} – {position}. sylaba</div><p class="full-sentence">{ipa} – {pl}</p>'
    return [task, ans, rule_explanation(rule)]


def sound_g_fields(word, hard, ipa, pl, rule):
    """Task, Answer, Explanation dla typu `sound-spelling` (twarde / miękkie g)."""
    task = ('<div class="tr"><p class="instruction">Jak wymawiamy <b>g</b>: twarde /g/ czy miękkie /dʒ/?</p>'
            f'<p class="word">{word}</p></div>')
    label = "/g/ – twarde (jak w <i>get</i>)" if hard else "/dʒ/ – miękkie (jak w <i>job</i>)"
    ans = answer_block(label) + f'<p class="full-sentence">{ipa} – {pl}</p>'
    return [task, ans, rule_explanation(rule)]


def write_tsv(name, rows, output_dir=OUTPUT_DIR):
    """Zapisuje wiersze jako TSV (UTF-8 bez BOM, bez cytowania pól)."""
    path = Path(output_dir) / name
    for row in rows:
        for field in row:
            if "\t" in field or "\n" in field:
                raise ValueError(f"{name}: pole zawiera tabulator lub nową linię: {field[:60]}")
    path.write_text("".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    print(f"{path.name}: {len(rows)}")
    return path
