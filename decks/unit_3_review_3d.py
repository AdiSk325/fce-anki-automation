#!/usr/bin/env python3
"""Talia 3D – opis danych (Seattle Snapshot) i powtórka przed Unit 3 Review and extension.

Źródło: Empower B2, unit 3D (tekst *Fitness: Seattle Snapshot* z zaznaczeniami i dopiskami,
ćwiczenia b–d) oraz strona *Unit 3 Review and extension* (Grammar, Vocabulary, Wordpower *up*).
Karty ćwiczą ten sam materiał na innych zdaniach niż Review, żeby Review zostało
prawdziwym sprawdzianem po nauce.

Uruchom z katalogu repo: python decks/unit_3_review_3d.py
Nadpisuje pliki TSV w output/. Nie zmieniaj pierwszych pól istniejących wierszy –
od nich zależy GUID notatki w Anki (zmiana = nowa karta i utrata historii powtórek).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cardlib import (GAP, colloc_translation, examples_block, grammar_explanation,  # noqa: E402
                     meaning_fields, mistakes_block, typing_fields, uoe_explanation, vocab_back,
                     write_tsv)

T = "unit-3-review unit-3d"

# Reguły powtarzane w wyjaśnieniach kart.
R = {
    "adj": "<b>a / an + przymiotnik + rzeczownik</b>: <i>a slight decrease</i>. Przymiotnik opisuje rzeczownik.",
    "adv": "<b>czasownik + przysłówek</b>: <i>decreased slightly</i>. Przysłówek (zwykle <i>-ly</i>) opisuje czasownik i stoi po nim.",
    "swap": "<i>There was a <b>slight decrease</b> in X</i> = <i>X <b>decreased slightly</b></i>. Przymiotnik + rzeczownik zamienia się w czasownik + przysłówek.",
    "in": "<b>an increase / a decrease / a boost in</b> sth. <i>of</i> tylko przed liczbą: <i>an increase of 10%</i>.",
    "steady": "<b>remain steady</b>: po <i>remain</i> (jak po <i>be</i>) stoi przymiotnik, nie przysłówek.",
    "ppc": "<b>have / has been + -ing</b>: czynność trwa do teraz albo dopiero co się skończyła i widać jej ślady; liczy się samo działanie i to, jak długo trwa.",
    "pps": "<b>have / has + imiesłów</b>: liczy się skończony rezultat albo liczba (ile, ile razy); także z <i>yet / already</i>.",
    "stative": "Czasowniki stanu (<i>know, be, have</i> = posiadać, <i>like, see</i> = widzieć) nie mają formy ciągłej: tylko Present Perfect Simple.",
    "type2": "Type 2 (rozdzielny): zaimek <b>musi</b> stać w środku: <i>pick <b>it</b> up</i>, <i>look <b>it</b> up</i>.",
    "type34": "Type 3 i 4 (nierozdzielny): nic nie wchodzi do środka, dopełnienie stoi na końcu: <i>look down on <b>me</b></i>, <i>put up with <b>it</b></i>.",
    "up-end": "<b>up</b> = „do końca, całkowicie”: <i>drink up, use up, eat up, clear up</i>.",
    "word": "<b>word is getting out (that …)</b>: <i>word</i> bez przedimka znaczy „wieść”.",
    "up-more": "<b>up</b> = „głośniej, mocniej” (<i>speak up, turn the music up</i>) albo „razem” (<i>add up</i>).",
    "up-idiom": "Tu <b>up</b> nie ma osobnego znaczenia: cały czasownik trzeba znać jako jedno słowo.",
    "ability": "<b>have the ability / the potential + to</b> + bezokolicznik · <b>be skilled at</b> + <i>-ing</i> · <b>have a talent for</b> + rzeczownik / <i>-ing</i>.",
    "adj-noun": "<b>an outstanding / exceptional / extraordinary</b> + rzeczownik nazywający osobę: <i>can cook very well</i> → <i>is an extraordinary cook</i>.",
    "wf": "Najpierw ustal, jakiej części mowy wymaga luka (osoba, rzecz, przymiotnik), potem dobierz końcówkę.",
}


def grammar(rule, formula, usage, signal, tip, examples, mistakes, extra=""):
    return [rule, grammar_explanation(formula, usage, tip, signal=signal, signal_label="🔑 Słowa-sygnały:"),
            examples_block(examples), mistakes_block(mistakes), f"fce grammar {T} {extra}".strip()]


def pv(verb, meanings, note, examples, synonyms, base, extra=""):
    return [verb, meaning_fields(meanings, note), examples_block(examples), synonyms,
            f"fce phrasal-verbs {base} {T} wordpower-up {extra}".strip()]


def colloc(item, pl, en, examples, ctype, note="", extra=""):
    return [item, colloc_translation(pl, en, note), examples_block(examples, "example"), ctype,
            f"fce collocations {ctype.replace('+', '-')} {T} {extra}".strip()]


def vocab(front, pos, ipa, pl, en, examples, note="", extra=""):
    return [front, vocab_back(pos, ipa, pl, en, note), examples_block(examples, "example"),
            f"fce vocabulary {T} {extra}".strip()]


def typing(task_type, fields, why, rule, topic):
    return [*fields, uoe_explanation(why, R[rule]), task_type, f"fce typing {task_type} {T} {topic}"]


def gap(sentence, answer, hint, pl, why, rule, topic, alt=None):
    """Luka: wpisujesz brakujące słowo albo zwrot."""
    n = len(answer.split())
    full = sentence.replace(GAP, f"<b>{answer}</b>")
    return typing("gap-phrase",
                  typing_fields("⌨️ Wpisz brakujące słowa:", sentence, answer, full, pl=pl, alt=alt,
                                hint=f"{hint} · {n} {'słowo' if n == 1 else 'słowa'}"),
                  why, rule, topic)


def order(context, scrambled, answer, pl, why, rule, topic):
    """Słowa kursywą z Review 1a: wpisujesz tylko ułożony fragment."""
    full = context.replace(GAP, f"<b>{answer}</b>")
    return typing("word-order",
                  typing_fields("⌨️ Ułóż słowa w dobrej kolejności i wpisz sam ten fragment:", scrambled, answer, full,
                                pl=pl, body_cls="word scrambled", context=context),
                  why, rule, topic)


def fix(wrong, answer, pl, why, rule, topic, alt=None):
    return typing("error-correction",
                  typing_fields("⌨️ W zdaniu jest jeden błąd. Wpisz całe poprawne zdanie:", wrong, answer, answer,
                                pl=pl, alt=alt, body_cls="wrong-sentence"),
                  why, rule, topic)


def rewrite(original, word, start, answer, pl, why, rule, topic, alt=None):
    """Zdanie do przepisania z podanym słowem (jak Review 2a) albo inną ramą (3D)."""
    return typing("rewrite",
                  typing_fields("⌨️ Napisz to samo inaczej. Wpisz całe zdanie:", original, answer, answer, pl=pl, alt=alt,
                                hint=f"Użyj: <b>{word}</b> · Zacznij od: <b>{start} …</b>"),
                  why, rule, topic)


def tr(pl, hint, answer, why, rule, topic, alt=None):
    return typing("translation",
                  typing_fields("🇵🇱 → 🇬🇧 Przetłumacz i wpisz całe zdanie:", pl, answer, answer, alt=alt,
                                hint=f"Użyj: <b>{hint}</b>"),
                  why, rule, topic)


# ---------------------------------------------------------------- Grammar (zrozumienie)
GRAMMAR = [
    grammar(
        "Describing data: adjective + noun vs verb + adverb",
        "<code>there is / was / has been + a / an + przymiotnik + rzeczownik + in + …</code><br>"
        "<code>podmiot + czasownik + przysłówek</code>",
        ["Tę samą zmianę opisujesz dwiema ramami: <i>There was a <b>slight decrease</b> in participation.</i> = <i>Participation <b>decreased slightly</b>.</i> Przeplatanie obu ram ratuje opis danych przed monotonią.",
         "<b>Znaczenie:</b> <b>slight</b> = mała · <b>gradual</b> = powolna, stopniowa · <b>dramatic</b> = duża i nagła · <b>significant</b> = duża, ważna · <b>noticeable</b> / <b>obvious</b> = wyraźnie widoczna.",
         "<b>Przysłówki:</b> slight<b>ly</b>, gradual<b>ly</b>, significant<b>ly</b>, obvious<b>ly</b>; uwaga na pisownię: noticeabl<b>e</b> → noticeabl<b>y</b>, dramatic → dramatic<b>ally</b>.",
         "Po rzeczowniku przyimek <b>in</b>: <i>an increase <b>in</b> the number of members</i>. Rzeczowniki: <i>increase, decrease, boost</i> (wyraźny wzrost); czasowniki: <i>increase, decrease, drop</i>.",
         "<b>Brak zmiany:</b> <i>has <b>remained steady</b></i> (przymiotnik!) albo <i>hasn't increased or dropped below 60%</i>.",
         "<b>This</b> na początku zdania odsyła <b>wstecz</b>, do tego, co właśnie opisano: <i>This was because a new gym opened nearby.</i> · <i>This is the result of a stable group of members.</i>"],
        "increase · decrease · drop · boost · remain steady · over the four-year period",
        "W raporcie i rozprawce tak opisujesz trendy. Zamiana przymiotnik + rzeczownik ↔ czasownik + przysłówek to też typowa parafraza w Use of English Part 4.",
        [("After the first two years, there was <b>a gradual decrease in</b> the number of members using the pool.",
          "Po pierwszych dwóch latach nastąpił stopniowy spadek liczby członków korzystających z basenu."),
         ("Last year, participation <b>decreased dramatically</b>.", "W zeszłym roku uczestnictwo gwałtownie spadło."),
         ("Participation in individual gym programmes <b>has remained steady</b> over the four-year period.",
          "Uczestnictwo w indywidualnych programach utrzymuje się na stałym poziomie przez całe cztery lata."),
         ("Numbers in those classes <b>have increased noticeably</b>.", "Liczba osób na tych zajęciach zauważalnie wzrosła.")],
        [("There was a slightly decrease in membership.", "There was a slight decrease in membership.",
          "Przed rzeczownikiem stoi przymiotnik, nie przysłówek."),
         ("Participation has remained steadily.", "Participation has remained steady.",
          "Po <i>remain</i> przymiotnik, tak jak po <i>be</i>."),
         ("There was a noticeable increase of the number of members.", "There was a noticeable increase in the number of members.",
          "Wzrost <b>in</b> czegoś; <i>of</i> tylko przed liczbą (<i>an increase of 10%</i>).")],
        "describing-data writing"),
    grammar(
        "Present perfect simple vs present perfect continuous",
        "<code>have / has + imiesłów bierny</code> (I've finished)<br>"
        "<code>have / has + been + -ing</code> (I've been sorting)",
        ["<b>Continuous</b> = patrzysz na samą <b>czynność</b>: trwa do teraz albo dopiero co się skończyła i widać jej ślady. <i>What have you <b>been doing</b>? There are things all over the floor.</i>",
         "<b>Simple</b> = patrzysz na <b>rezultat</b>: coś jest skończone albo policzone. <i>I've <b>written</b> three emails.</i> · <i>I haven't <b>finished</b> yet.</i>",
         "<b>How long?</b> → zwykle Continuous (<i>I've been learning English for years</i>). <b>How many / how much?</b> → Simple (<i>I've read two chapters</i>).",
         "<b>Czasowniki stanu</b> (<i>know, be, have</i> = posiadać, <i>like, see</i> = widzieć) tylko w Simple: <i>I've <b>known</b> her for years</i>, <i>I haven't <b>seen</b> you for ages</i>.",
         "Po polsku to zwykle czas teraźniejszy („uczę się od roku”) albo przeszły („co robiłeś?”). Po angielsku most między przeszłością a teraz buduje zawsze <i>have</i>."],
        "for · since · all day · recently · these days · yet · already · how long · how many",
        "W open cloze luka to często samo <b>been</b>. W Part 4 sprawdź w drugim zdaniu, czy masz pełną strukturę: <i>have + been + -ing</i>.",
        [("I've <b>been sorting</b> things out, but I haven't quite <b>finished</b> yet.",
          "Porządkuję rzeczy (od jakiegoś czasu), ale jeszcze nie całkiem skończyłem."),
         ("She's <b>been writing</b> emails since nine o'clock. She's <b>written</b> twelve so far.",
          "Pisze maile od dziewiątej. Jak dotąd napisała dwanaście."),
         ("I haven't <b>seen</b> you for ages. What have you <b>been doing</b>?",
          "Nie widziałem cię od wieków. Co porabiasz?"),
         ("We've <b>known</b> each other since primary school.", "Znamy się od podstawówki.")],
        [("I am learning English for three years.", "I've been learning English for three years.",
          "Czynność zaczęła się w przeszłości i trwa do teraz: Present Perfect, nie Present Continuous."),
         ("I've been knowing her since 2015.", "I've known her since 2015.",
          "<i>know</i> to czasownik stanu, więc nie ma formy ciągłej."),
         ("She's been writing three emails this morning.", "She's written three emails this morning.",
          "Podana liczba = rezultat, więc Simple.")],
        "present-perfect"),
    grammar(
        "Wordpower: what does 'up' add to a verb?",
        "<code>czasownik + up</code> → (a) do końca · (b) razem · (c) głośniej · albo całkiem nowe znaczenie",
        ["<b>(a) do końca, całkowicie:</b> <i>drink up</i> (dopić), <i>use up</i> (zużyć do zera), <i>eat up</i>, <i>clear up</i> (posprzątać do czysta).",
         "<b>(b) razem, w całość:</b> <i>add up</i> (zsumować).",
         "<b>(c) głośniej, mocniej:</b> <i>speak up</i> (mówić głośniej), <i>turn the music up</i>.",
         "<b>Nowe znaczenie, którego nie zgadniesz z części:</b> <i>look sth up</i> (sprawdzić), <i>bring sth up</i> (poruszyć temat), <i>pick sth up</i> (podłapać), <i>turn up</i> (pojawić się), <i>put up with</i> (znosić), <i>keep up with</i> (nadążać), <i>look up to</i> (podziwiać).",
         "<b>Szyk:</b> <i>use, look, bring, clear, add, pick + up</i> są rozdzielne (Type 2), więc zaimek idzie do środka: <i>look <b>it</b> up</i>. Czasowniki z dwiema cząstkami (<i>put up with, keep up with, look up to</i>) są nierozdzielne: <i>put up with <b>it</b></i>."],
        "drink up · use up · add up · speak up · look up · bring up · turn up · put up with · keep up with",
        "W Part 1 i Part 2 luka to często sama cząstka. Najpierw ustal znaczenie całego czasownika, dopiero potem wybieraj cząstkę.",
        [("<b>Drink up</b>. We need to go.", "Dopij. Musimy iść."),
         ("I've <b>used up</b> the shampoo. Is there any more?", "Zużyłem cały szampon. Jest jeszcze jakiś?"),
         ("Could you <b>speak up</b>? We can't hear you.", "Czy możesz mówić głośniej? Nie słyszymy cię."),
         ("I don't know. I'll have to <b>look it up</b>.", "Nie wiem. Będę musiał to sprawdzić.")],
        [("I don't know this word. I'll look up it.", "I don't know this word. I'll look it up.",
          "Type 2: zaimek zawsze między czasownikiem a cząstką."),
         ("I can't put up it with any longer.", "I can't put up with it any longer.",
          "Dwie cząstki = nierozdzielny; dopełnienie stoi na samym końcu.")],
        "wordpower-up multi-word-verbs"),
]


# ---------------------------------------------------------------- Multi-word verbs z up (Wordpower)
PHRASAL = [
    pv("drink up / drink (sth) up",
       [("dopić, wypić do końca", "to finish all of a drink")],
       "Type 1 i 2. <b>up</b> = „do końca”. Jako polecenie zwykle bez dopełnienia: <i>Drink up!</i> Z zaimkiem: <i>drink <b>it</b> up</i>. Tak samo działa <b>eat up</b>.",
       [("<b>Drink up</b>. We need to go.", "Dopij. Musimy iść."),
        ("<b>Drink</b> your coffee <b>up</b> before it gets cold.", "Dopij kawę, zanim wystygnie.")],
       "finish your drink", "drink", "type-1 type-2"),
    pv("speak up",
       [("mówić głośniej", "to speak more loudly"),
        ("zabrać głos, powiedzieć otwarcie, co się myśli", "to say what you think clearly and publicly")],
       "Type 1 (bez dopełnienia). <b>up</b> = „głośniej”. W drugim znaczeniu często <b>speak up for sb</b> = stanąć w czyjejś obronie.",
       [("Could you <b>speak up</b>? We can't hear you at the back.", "Czy możesz mówić głośniej? Z tyłu cię nie słychać."),
        ("If you disagree, you should <b>speak up</b>.", "Jeśli się nie zgadzasz, powinieneś zabrać głos.")],
       "talk louder; raise your voice", "speak", "type-1"),
    pv("use (sth) up",
       [("zużyć do końca, wyczerpać", "to use all of something so that nothing is left")],
       "Type 2 (rozdzielny): <i>use <b>it</b> up</i>. <b>up</b> = „do końca”. Różnica: <i>I've <b>used up</b> the milk</i> (ja zużyłem) vs <i>We've <b>run out of</b> milk</i> (skończyło się nam).",
       [("I've <b>used up</b> the shampoo. Is there any more?", "Zużyłem cały szampon. Jest jeszcze jakiś?"),
        ("Don't <b>use</b> all the hot water <b>up</b>.", "Nie zużyj całej ciepłej wody.")],
       "finish (a supply); exhaust", "use", "type-2"),
    pv("add (sth) up",
       [("zsumować, podliczyć", "to calculate the total of several numbers"),
        ("trzymać się kupy, zgadzać się (zwykle w przeczeniu)", "to seem reasonable or make sense")],
       "Znaczenie 1: Type 2 (<i>add <b>it</b> up</i>), <b>up</b> = „razem”. Znaczenie 2: Type 1, bez dopełnienia: <i>His story doesn't add up.</i>",
       [("Let me see the bill. I think they've <b>added</b> it <b>up</b> incorrectly.",
         "Pokaż rachunek. Chyba źle go podliczyli."),
        ("He says he was at home, but it just doesn't <b>add up</b>.", "Mówi, że był w domu, ale to się nie trzyma kupy.")],
       "calculate the total; make sense", "add", "type-1 type-2"),
    pv("clear (sth) up",
       [("posprzątać, uprzątnąć", "to make a place tidy by removing things from it"),
        ("wyjaśnić (nieporozumienie, sprawę)", "to solve or explain a problem or misunderstanding")],
       "Type 2 (rozdzielny): <i>clear <b>it</b> up</i>. Bez dopełnienia o pogodzie: <i>It's clearing up</i> = przejaśnia się.",
       [("You dropped it, so I think you should <b>clear</b> it <b>up</b>.", "Ty to upuściłeś, więc chyba ty powinieneś to posprzątać."),
        ("I'd like to <b>clear up</b> this misunderstanding.", "Chciałbym wyjaśnić to nieporozumienie.")],
       "tidy up; clean up; sort out", "clear", "type-2"),
    pv("look (sth) up",
       [("sprawdzić, wyszukać (w słowniku, w internecie)", "to find a piece of information in a book or on a computer")],
       "Type 2 (rozdzielny): <i>look <b>it</b> up</i>, nie <i>look up it</i>. Nie myl z <b>look up to sb</b> (podziwiać) – tam są dwie cząstki i nic nie wchodzi do środka.",
       [("I don't know. I'll have to <b>look</b> it <b>up</b>.", "Nie wiem. Będę musiał to sprawdzić."),
        ("She <b>looked up</b> the opening hours on the website.", "Sprawdziła godziny otwarcia na stronie.")],
       "check; search for (information)", "look", "type-2"),
    pv("bring (sth) up",
       [("poruszyć (temat), wspomnieć o czymś", "to start to talk about a particular subject"),
        ("wychować (dziecko)", "to look after a child until he or she is an adult")],
       "Type 2 (rozdzielny): <i>bring <b>it</b> up</i>. W drugim znaczeniu często w stronie biernej: <i>I was brought up in Kraków.</i>",
       [("Why don't you <b>bring</b> it <b>up</b> at the meeting?", "Może poruszysz to na zebraniu?"),
        ("Nobody wanted to <b>bring up</b> the subject of money.", "Nikt nie chciał poruszać tematu pieniędzy.")],
       "mention; raise (a subject)", "bring", "type-2"),
    pv("turn up",
       [("pojawić się, przyjść, zjawić się", "to arrive or appear somewhere, often unexpectedly or late"),
        ("podgłośnić, podkręcić (turn sth up)", "to increase the sound, heat or power of something")],
       "Znaczenie 1: Type 1, bez dopełnienia. Znaczenie 2: Type 2 (<i>turn <b>it</b> up</i>), <b>up</b> = „głośniej, mocniej”; przeciwieństwo: <i>turn down</i>.",
       [("We invited 50 people, but only a few <b>turned up</b>.", "Zaprosiliśmy 50 osób, ale przyszło tylko kilka."),
        ("I love this song. <b>Turn</b> it <b>up</b>!", "Uwielbiam tę piosenkę. Podgłośnij!")],
       "appear; arrive; show up", "turn", "type-1 type-2"),
    pv("put up with (sb / sth)",
       [("znosić, tolerować", "to accept an unpleasant person or situation without complaining")],
       "Type 4 (dwie cząstki, nierozdzielny): <i>put up with <b>him</b></i>. Bardzo częste z <i>can't</i>: <i>I can't put up with it any longer.</i> Nie myl z <i>put sb up</i> (przenocować kogoś).",
       [("He's so rude. I don't know why people <b>put up with</b> him.", "Jest taki niegrzeczny. Nie wiem, czemu ludzie go znoszą."),
        ("I can't <b>put up with</b> this noise any longer.", "Nie mogę dłużej znosić tego hałasu.")],
       "tolerate; stand; bear", "put", "type-4"),
    pv("keep up with (sb / sth)",
       [("nadążać za kimś, dotrzymywać kroku", "to move or progress at the same speed as somebody or something"),
        ("być na bieżąco z czymś", "to continue to learn about something that is changing")],
       "Type 4 (dwie cząstki, nierozdzielny): <i>keep up with <b>you</b></i>. Bez dopełnienia samo <b>keep up</b>: <i>Slow down, I can't keep up!</i>",
       [("Walk more slowly! I can't <b>keep up with</b> you.", "Idź wolniej! Nie nadążam za tobą."),
        ("It's hard to <b>keep up with</b> all the changes in technology.", "Trudno być na bieżąco ze wszystkimi zmianami w technologii.")],
       "go at the same speed as; stay up to date with", "keep", "type-4"),
]


# ---------------------------------------------------------------- Frazy z tekstu (zaznaczenia i dopiski)
COLLOC = [
    colloc("a gradual / slight decrease in sth",
           "stopniowy / nieznaczny spadek czegoś",
           "a slow (gradual) or small (slight) fall in the amount or number of something",
           [("After the first two years, there was <b>a gradual decrease in</b> the number of members using the pool.",
             "Po pierwszych dwóch latach nastąpił stopniowy spadek liczby członków korzystających z basenu."),
            ("There was <b>a slight decrease</b> after the first year.", "Po pierwszym roku nastąpił nieznaczny spadek.")],
           "adj+noun",
           "Spadek <b>in</b> czegoś. To samo czasownikiem: <i>the number <b>decreased gradually / slightly</b></i>. Rzeczownik ma akcent na pierwszej sylabie (<b>DE</b>crease), czasownik na drugiej (de<b>CREASE</b>).",
           "describing-data"),
    colloc("a noticeable increase in sth",
           "zauważalny wzrost czegoś",
           "a rise that is big enough to be seen clearly",
           [("There was a slight decrease after the first year and then <b>a noticeable increase</b> in our third year.",
             "Po pierwszym roku nastąpił nieznaczny spadek, a potem, w trzecim roku, zauważalny wzrost."),
            ("There has been <b>a noticeable increase in</b> prices this year.", "W tym roku nastąpił zauważalny wzrost cen.")],
           "adj+noun",
           "<b>noticeable</b> /ˈnəʊtɪsəbl/ od <i>notice</i> (zauważyć); <i>e</i> zostaje przed <i>-able</i>. Przysłówek: <b>noticeably</b>. Wzrost <b>in</b> czegoś.",
           "describing-data"),
    colloc("an obvious boost in sth",
           "wyraźny wzrost, skok czegoś (na plus)",
           "a clear increase or improvement in something",
           [("There has been <b>an obvious boost in</b> participation in group fitness over the four-year period.",
             "W ciągu czterech lat nastąpił wyraźny wzrost uczestnictwa w zajęciach grupowych."),
            ("The good reviews gave the restaurant <b>a boost</b>.", "Dobre recenzje dały restauracji zastrzyk energii.")],
           "adj+noun",
           "<b>a boost</b> to zawsze zmiana na lepsze, dlatego nie ma „boost” przy spadkach. Też czasownik: <i>boost sales / confidence</i>. W tabeli z podręcznika: <i>an obvious / significant boost</i>.",
           "describing-data"),
    colloc("remain steady",
           "utrzymywać się na stałym poziomie, nie zmieniać się",
           "to stay at the same level, without going up or down",
           [("Participation in members' individual gym programmes <b>has remained steady</b> over the four-year period.",
             "Uczestnictwo w indywidualnych programach utrzymuje się na stałym poziomie przez całe cztery lata."),
            ("Prices <b>remained steady</b> throughout the summer.", "Ceny przez całe lato utrzymywały się na stałym poziomie.")],
           "verb+adj",
           "Po <i>remain</i> przymiotnik <b>steady</b>, nie <i>steadily</i>. Okres z <b>over</b>: <i>over the four-year period</i>. Podobnie: <i>stay the same</i>, <i>remain stable</i>.",
           "describing-data"),
    colloc("increase / decrease dramatically",
           "gwałtownie wzrosnąć / spaść",
           "to go up or down suddenly and by a large amount",
           [("Last year, participation <b>decreased dramatically</b>.", "W zeszłym roku uczestnictwo gwałtownie spadło."),
            ("The price of flats has <b>increased dramatically</b> since 2020.", "Ceny mieszkań gwałtownie wzrosły od 2020 roku.")],
           "verb+adverb",
           "Pisownia: dramatic → dramatic<b>ally</b> (nie <i>dramaticly</i>). Słabsze stopnie: <i>slightly</i> (nieznacznie) → <i>noticeably</i> → <i>significantly</i> → <i>dramatically</i>.",
           "describing-data"),
    colloc("word is getting out (that …)",
           "wieść się rozchodzi (że …), ludzie zaczynają o tym mówić",
           "more and more people are hearing about it and telling others",
           [("<b>Word is getting out that</b> this is a great way to get fit – and have fun.",
             "Rozchodzi się wieść, że to świetny sposób na poprawę kondycji i dobrą zabawę."),
            ("<b>Word got out</b> about the concert and the tickets sold out in an hour.",
             "Wieść o koncercie się rozeszła i bilety wyprzedały się w godzinę.")],
           "idiom",
           "<b>word</b> bez przedimka = wieść, wiadomość. Twoja notatka: <i>more and more people are telling others about it</i>. Podobnie: <b>the word is spreading</b>, <b>by word of mouth</b> (pocztą pantoflową).",
           "idiom"),
    colloc("chase a ball",
           "ganiać za piłką",
           "to run after a ball in order to get it",
           [("They need activities that don't involve watching other people <b>chasing a ball</b> around a pitch or court.",
             "Potrzebują zajęć, które nie polegają na oglądaniu, jak inni ganiają za piłką po boisku."),
            ("The dog spent the whole afternoon <b>chasing a ball</b> in the park.", "Pies przez całe popołudnie ganiał za piłką w parku.")],
           "verb+noun",
           "<b>chase</b> /tʃeɪs/ = gonić, ścigać. Też z <i>after</i>: <i>chase after sb</i>. <b>pitch</b> = boisko (piłka nożna), <b>court</b> = kort, boisko do koszykówki."),
]

VOCAB = [
    vocab("misconception", "noun (C)", "/ˌmɪskənˈsepʃn/", "błędne przekonanie, mylne wyobrażenie",
          "a wrong idea about something, often one that many people share",
          [("It's a common <b>misconception</b> that group workouts are just dance classes.",
            "To częste błędne przekonanie, że treningi grupowe to tylko zajęcia taneczne."),
           ("There is a popular <b>misconception</b> about how much water we need to drink.",
            "Istnieje popularne błędne przekonanie co do tego, ile wody trzeba pić.")],
          "Twoja notatka: <i>the wrong idea</i>. Przedrostek <b>mis-</b> = źle (<i>misunderstand, mislead</i>). Kolokacje: <b>a common / popular misconception</b> <b>about</b> sth albo <b>that</b> + zdanie."),
    vocab("aquatic centre", "noun (C)", "/əˈkwætɪk ˈsentə(r)/", "centrum sportów wodnych, kompleks basenowy",
          "a building with swimming pools where people can swim and do water sports",
          [("Our <b>aquatic centre</b> offers a range of swimming lessons.", "Nasze centrum sportów wodnych oferuje różne lekcje pływania."),
           ("The city is building a new <b>aquatic centre</b> with an Olympic-sized pool.",
            "Miasto buduje nowy kompleks basenowy z basenem olimpijskim.")],
          "<b>aquatic</b> = wodny (<i>aquatic plants, aquatic sports</i>). Na co dzień częściej <b>swimming pool</b> albo <b>leisure centre</b>."),
]


# ---------------------------------------------------------------- Typing 1: opis danych (3D)
D = "describing-data"
DATA = [
    gap(f"There was a {GAP} decrease in sales last month.", "slight", "🇵🇱 mały, nieznaczny · zaczyna się na s",
        "W zeszłym miesiącu nastąpił nieznaczny spadek sprzedaży.", "Mała zmiana = <b>slight</b>.", "adj", D),
    gap(f"There has been a {GAP} increase in prices over the last ten years.", "gradual", "🇵🇱 powolny, stopniowy",
        "W ciągu ostatnich dziesięciu lat nastąpił stopniowy wzrost cen.", "Powolna zmiana = <b>gradual</b>.", "adj", D),
    gap(f"There was a {GAP} drop in temperature overnight.", "dramatic", "🇵🇱 duży i nagły, gwałtowny",
        "W nocy nastąpił gwałtowny spadek temperatury.", "Duża i nagła zmiana = <b>dramatic</b>.", "adj", D),
    gap(f"There is a {GAP} difference between the two groups.", "significant", "🇵🇱 znaczący, istotny · zaczyna się na si",
        "Między obiema grupami jest znacząca różnica.", "Duża, ważna zmiana lub różnica = <b>significant</b>.", "adj", D),
    gap(f"There has been a {GAP} improvement in her English.", "noticeable", "🇵🇱 zauważalny",
        "Nastąpiła zauważalna poprawa jej angielskiego.", "Zmiana, którą wyraźnie widać = <b>noticeable</b> (od <i>notice</i>).", "adj", D),
    gap(f"There has been an {GAP} boost in participation in group fitness.", "obvious", "🇵🇱 oczywisty, wyraźny",
        "Nastąpił wyraźny wzrost uczestnictwa w zajęciach grupowych.", "Zmiana, którą widzi każdy = <b>obvious</b>. Przedimek <i>an</i> zdradza samogłoskę.", "adj", D),
    gap(f"Sales have increased {GAP} this year, by only one per cent.", "slightly", "🇵🇱 nieznacznie",
        "Sprzedaż wzrosła w tym roku nieznacznie, tylko o jeden procent.", "slight → <b>slightly</b>.", "adv", D),
    gap(f"Last year, participation decreased {GAP}.", "dramatically", "🇵🇱 gwałtownie, drastycznie",
        "W zeszłym roku uczestnictwo gwałtownie spadło.", "dramatic → dramatic<b>ally</b>: po <i>-ic</i> końcówka <i>-ally</i>.", "adv", D),
    gap(f"Numbers in those classes have increased {GAP}.", "noticeably", "🇵🇱 zauważalnie",
        "Liczba osób na tych zajęciach zauważalnie wzrosła.", "noticeabl<b>e</b> → noticeabl<b>y</b>: <i>e</i> zamienia się w <i>y</i>.", "adv", D),
    gap(f"The town has changed {GAP} over the years.", "gradually", "🇵🇱 stopniowo",
        "Miasto stopniowo zmieniało się przez lata.", "gradual → <b>gradually</b> (podwójne <i>l</i>).", "adv", D),
    gap(f"Costs have risen {GAP} since 2020.", "significantly", "🇵🇱 znacząco",
        "Koszty znacząco wzrosły od 2020 roku.", "significant → <b>significantly</b>.", "adv", D),
    gap(f"Participation in individual gym programmes has remained {GAP}.", "steady", "🇵🇱 na stałym poziomie",
        "Uczestnictwo w indywidualnych programach utrzymuje się na stałym poziomie.",
        "To odpowiedź na pytanie d1 z podręcznika: <i>has remained steady</i> = brak zmiany.", "steady", D),
    gap(f"There was a gradual decrease {GAP} the number of members using the pool.", "in", "przyimek",
        "Nastąpił stopniowy spadek liczby członków korzystających z basenu.", "Spadek <b>in</b> czegoś.", "in", D),
    gap(f"Word is {GAP} that this is a great way to get fit.", "getting out", "🇵🇱 wieść się rozchodzi",
        "Rozchodzi się wieść, że to świetny sposób na poprawę kondycji.",
        "<i>Word is getting out</i> = coraz więcej osób mówi o tym innym.", "word", D),
    rewrite("There was a slight increase in sales.", "slightly", "Sales", "Sales increased slightly.",
            "Sprzedaż nieznacznie wzrosła.", "Rzeczownik <i>increase</i> → czasownik <i>increased</i>; <i>slight</i> → <i>slightly</i>.", "swap", D),
    rewrite("There was a dramatic decrease in participation.", "dramatically", "Participation",
            "Participation decreased dramatically.", "Uczestnictwo gwałtownie spadło.",
            "Przysłówek stoi po czasowniku.", "swap", D),
    rewrite("There has been a gradual increase in prices.", "gradually", "Prices", "Prices have increased gradually.",
            "Ceny stopniowo wzrosły.", "Czas zostaje ten sam: <i>has been</i> → <i>have increased</i> (<i>prices</i> to liczba mnoga).", "swap", D),
    rewrite("There has been a noticeable increase in the number of members.", "noticeably", "The number of members",
            "The number of members has increased noticeably.", "Liczba członków zauważalnie wzrosła.",
            "<i>the number</i> jest w liczbie pojedynczej, więc <b>has</b>.", "swap", D),
    rewrite("Attendance decreased gradually.", "gradual", "There was", "There was a gradual decrease in attendance.",
            "Nastąpił stopniowy spadek frekwencji.", "W drugą stronę: przysłówek → przymiotnik, czasownik → rzeczownik + <i>in</i>.", "swap", D),
    rewrite("Membership has increased significantly.", "significant", "There has been",
            "There has been a significant increase in membership.", "Nastąpił znaczący wzrost liczby członków.",
            "<i>has increased</i> → <i>there has been … increase in</i>.", "swap", D),
    rewrite("There has been no change in participation.", "steady", "Participation", "Participation has remained steady.",
            "Uczestnictwo utrzymuje się na stałym poziomie.", "Brak zmiany = <i>remain steady</i>.", "steady", D),
    fix("There was a slightly decrease in membership.", "There was a slight decrease in membership.",
        "Nastąpił nieznaczny spadek liczby członków.", "Przed rzeczownikiem przymiotnik: <b>slight</b>.", "adj", D),
    fix("Numbers have increased noticeable.", "Numbers have increased noticeably.",
        "Liczby zauważalnie wzrosły.", "Po czasowniku przysłówek: <b>noticeably</b>.", "adv", D),
    fix("Participation has remained steadily over the four-year period.", "Participation has remained steady over the four-year period.",
        "Uczestnictwo utrzymuje się na stałym poziomie przez cały czteroletni okres.", "<i>steadily</i> → <b>steady</b>.", "steady", D),
    fix("There was a noticeable increase of the number of members.", "There was a noticeable increase in the number of members.",
        "Nastąpił zauważalny wzrost liczby członków.", "<i>increase of</i> → <b>increase in</b>.", "in", D),
    tr("Nastąpił nieznaczny spadek liczby członków.", "a slight decrease in",
       "There was a slight decrease in the number of members.", "Rama: <i>there was</i> + przymiotnik + rzeczownik + <i>in</i>.", "adj", D),
    tr("W zeszłym roku frekwencja gwałtownie spadła.", "decrease dramatically",
       "Last year, attendance decreased dramatically.", "Rama: podmiot + czasownik + przysłówek.", "adv", D,
       alt="Attendance decreased dramatically last year."),
    tr("Uczestnictwo utrzymuje się na stałym poziomie.", "remain steady", "Participation has remained steady.",
       "Stan trwający do teraz: Present Perfect.", "steady", D),
    tr("Rozchodzi się wieść, że to świetny sposób na poprawę kondycji.", "Word is getting out that …",
       "Word is getting out that this is a great way to get fit.", "<i>get fit</i> = poprawić kondycję.", "word", D),
]


# ---------------------------------------------------------------- Typing 2: Present Perfect Simple vs Continuous (Review 1b)
P = "present-perfect"
PERFECT = [
    gap(f"You look exhausted. What have you {GAP}? (do)", "been doing", "czasownik w dobrej formie",
        "Wyglądasz na wykończonego. Co ty robiłeś?", "Widać ślady czynności (zmęczenie), pytasz o samo działanie.", "ppc", P),
    gap(f"I've {GAP} the kitchen all morning, and there's still a lot to do. (clean)", "been cleaning", "czasownik w dobrej formie",
        "Sprzątam kuchnię cały ranek i wciąż jest dużo do zrobienia.", "<i>all morning</i> + czynność niedokończona.", "ppc", P),
    gap(f"I've {GAP} the kitchen. Look how tidy it is! (clean)", "cleaned", "czasownik w dobrej formie",
        "Posprzątałem kuchnię. Zobacz, jak jest czysto!", "Pokazujesz gotowy rezultat.", "pps", P),
    gap(f"She's {GAP} three emails this morning. (write)", "written", "czasownik w dobrej formie",
        "Napisała dziś rano trzy maile.", "Podana liczba (<i>three</i>) = rezultat.", "pps", P),
    gap(f"She's {GAP} emails since nine o'clock. (write)", "been writing", "czasownik w dobrej formie",
        "Pisze maile od dziewiątej.", "<i>since nine o'clock</i>, bez liczby: liczy się czas trwania.", "ppc", P),
    gap(f"I haven't {GAP} you for ages. How are you? (see)", "seen", "czasownik w dobrej formie",
        "Nie widziałem cię od wieków. Co słychać?", "<i>see</i> = widzieć to czasownik stanu.", "stative", P),
    gap(f"We've {GAP} each other since primary school. (know)", "known", "czasownik w dobrej formie",
        "Znamy się od podstawówki.", "<i>know</i> nigdy nie ma formy ciągłej.", "stative", P),
    gap(f"Sorry I'm late. Have you {GAP} long? (wait)", "been waiting", "czasownik w dobrej formie",
        "Przepraszam za spóźnienie. Długo czekasz?", "Pytanie o to, jak długo trwa czynność.", "ppc", P),
    gap(f"I haven't quite {GAP} the report yet. (finish)", "finished", "czasownik w dobrej formie",
        "Jeszcze nie całkiem skończyłem raport.", "<i>yet</i> + pytanie o rezultat (skończone czy nie).", "pps", P),
    gap(f"I've got exams next month, so I've {GAP} most of the time. (revise)", "been revising", "czasownik w dobrej formie",
        "W przyszłym miesiącu mam egzaminy, więc przez większość czasu się uczę.", "Powtarzająca się czynność z ostatniego okresu.", "ppc", P),
    gap(f"How many matches have they {GAP} this season? (win)", "won", "czasownik w dobrej formie",
        "Ile meczów wygrali w tym sezonie?", "<i>How many</i> = liczba, więc Simple.", "pps", P),
    gap(f"He's {GAP} that car for ten years. (have)", "had", "czasownik w dobrej formie",
        "Ma ten samochód od dziesięciu lat.", "<i>have</i> = posiadać to czasownik stanu.", "stative", P),
    fix("I am learning English for three years.", "I have been learning English for three years.",
        "Uczę się angielskiego od trzech lat.", "Po polsku czas teraźniejszy, po angielsku Present Perfect Continuous.", "ppc", P,
        alt="I've been learning English for three years."),
    fix("I've been knowing her since 2015.", "I've known her since 2015.",
        "Znam ją od 2015 roku.", "<i>been knowing</i> → <b>known</b>.", "stative", P),
    tr("Co ostatnio porabiasz?", "these days", "What have you been doing these days?",
       "Pytanie o czynności z ostatniego okresu, trwającego do teraz.", "ppc", P),
    tr("Od lat śpiewam w chórze.", "for years", "I've been singing in a choir for years.",
       "Czynność zaczęta w przeszłości i trwająca do teraz.", "ppc", P, alt="I have been singing in a choir for years."),
    tr("Jeszcze nie skończyliśmy tego raportu.", "yet", "We haven't finished this report yet.",
       "Rezultat (skończone / nieskończone) + <i>yet</i> na końcu.", "pps", P, alt="We have not finished this report yet."),
]


# ---------------------------------------------------------------- Typing 3: szyk multi-word verbs (Review 1a)
M = "multi-word-verbs"
ORDER = [
    order(f"I never studied Italian at school. I just {GAP} while I was working in Rome.", "up / picked / it", "picked it up",
          "Nigdy nie uczyłem się włoskiego w szkole. Po prostu podłapałem go, pracując w Rzymie.",
          "<i>pick sth up</i> jest rozdzielny.", "type2", M),
    order(f"He shouldn't {GAP} just because we earn less than he does.", "us / down / look / on", "look down on us",
          "Nie powinien patrzeć na nas z góry tylko dlatego, że zarabiamy mniej od niego.",
          "<i>look down on sb</i>: dwie cząstki, zaimek na końcu.", "type34", M),
    order(f"I hate this dark, cold weather. It really {GAP}.", "me / gets / down", "gets me down",
          "Nie znoszę tej ciemnej, zimnej pogody. Naprawdę mnie dołuje.",
          "<i>get sb down</i>: osoba zawsze w środku.", "type2", M),
    order(f"That story isn't true. I'm sure he {GAP}.", "it / up / made", "made it up",
          "Ta historia nie jest prawdziwa. Jestem pewien, że ją zmyślił.",
          "<i>make sth up</i> = zmyślić; rozdzielny.", "type2", M),
    order(f"We need a new plan. Has anyone {GAP} a better idea?", "with / come / up", "come up with",
          "Potrzebujemy nowego planu. Czy ktoś wpadł na lepszy pomysł?",
          "<i>come up with sth</i>: trzy słowa stoją razem, dopełnienie po nich.", "type34", M),
    order(f"This puzzle is too hard. I just can't {GAP}.", "out / it / figure", "figure it out",
          "Ta łamigłówka jest za trudna. Po prostu nie mogę jej rozgryźć.",
          "<i>figure sth out</i> jest rozdzielny.", "type2", M),
    order(f"I don't know this word. I'll {GAP} in a dictionary.", "it / up / look", "look it up",
          "Nie znam tego słowa. Sprawdzę je w słowniku.", "<i>look sth up</i> jest rozdzielny.", "type2", M),
    order(f"There's no shampoo left. Somebody has {GAP}.", "up / it / used", "used it up",
          "Nie ma już szamponu. Ktoś go zużył.", "<i>use sth up</i> jest rozdzielny.", "type2", M),
    order(f"His behaviour is terrible. I can't {GAP} any longer.", "with / it / up / put", "put up with it",
          "Jego zachowanie jest okropne. Nie mogę go dłużej znosić.",
          "<i>put up with sth</i>: dwie cząstki, zaimek na końcu.", "type34", M),
    order(f"You walk too fast. I can't {GAP}.", "up / you / keep / with", "keep up with you",
          "Idziesz za szybko. Nie nadążam za tobą.", "<i>keep up with sb</i>: dwie cząstki, zaimek na końcu.", "type34", M),
    order(f"It's a good suggestion. Why don't you {GAP} at the next meeting?", "up / it / bring", "bring it up",
          "To dobra propozycja. Może poruszysz ją na następnym zebraniu?", "<i>bring sth up</i> jest rozdzielny.", "type2", M),
    order(f"She's a great coach. All the players {GAP}.", "to / look / her / up", "look up to her",
          "Jest świetną trenerką. Wszyscy zawodnicy ją podziwiają.",
          "<i>look up to sb</i>: dwie cząstki, zaimek na końcu. Porównaj z <i>look it up</i>.", "type34", M),
]


# ---------------------------------------------------------------- Typing 4: Wordpower up (Review 3)
W = "wordpower-up"
WORDPOWER = [
    gap(f"{GAP}! The taxi is waiting outside.", "Drink up", "🇵🇱 dopij",
        "Dopij! Taksówka czeka na zewnątrz.", "Polecenie bez dopełnienia.", "up-end", W),
    gap(f"We can't hear you at the back. Could you {GAP}, please?", "speak up", "🇵🇱 mówić głośniej",
        "Nie słyszymy cię z tyłu. Czy możesz mówić głośniej?", "Mówisz to komuś, kogo słabo słychać.", "up-more", W),
    gap(f"Who has {GAP} all the hot water?", "used up", "🇵🇱 zużył do końca",
        "Kto zużył całą ciepłą wodę?", "<i>use up</i> = zużyć do zera.", "up-end", W),
    gap(f"The waiter has {GAP} the numbers wrongly, so the bill is too high.", "added up", "🇵🇱 zsumował",
        "Kelner źle zsumował liczby, więc rachunek jest za wysoki.", "Liczby dodajesz „do kupy”.", "up-more", W),
    gap(f"You broke the plate, so you should {GAP} the mess.", "clear up", "🇵🇱 posprzątać",
        "Ty stłukłeś talerz, więc ty powinieneś posprzątać bałagan.", "<i>clear up</i> = uprzątnąć do czysta.", "up-end", W),
    gap(f"I'll {GAP} the opening hours on their website.", "look up", "🇵🇱 sprawdzę, wyszukam",
        "Sprawdzę godziny otwarcia na ich stronie.", "<i>look sth up</i> = wyszukać informację.", "up-idiom", W),
    gap(f"Nobody wanted to {GAP} the subject of money.", "bring up", "🇵🇱 poruszyć (temat)",
        "Nikt nie chciał poruszać tematu pieniędzy.", "<i>bring sth up</i> = zacząć o czymś mówić.", "up-idiom", W),
    gap(f"He promised to come at eight, but he didn't {GAP} until ten.", "turn up", "🇵🇱 pojawić się",
        "Obiecał przyjść o ósmej, ale pojawił się dopiero o dziesiątej.", "<i>turn up</i> = przyjść, zjawić się.", "up-idiom", W),
    gap(f"I can't {GAP} this noise any longer.", "put up with", "🇵🇱 znosić",
        "Nie mogę dłużej znosić tego hałasu.", "<i>put up with</i> = tolerować.", "up-idiom", W),
    gap(f"Technology changes so fast that it's hard to {GAP} it.", "keep up with", "🇵🇱 nadążać za",
        "Technologia zmienia się tak szybko, że trudno za nią nadążyć.", "<i>keep up with</i> = iść tym samym tempem.", "up-idiom", W),
    gap(f"She's a brilliant musician. Younger players really {GAP} her.", "look up to", "🇵🇱 podziwiają",
        "Jest znakomitą muzyczką. Młodsi muzycy naprawdę ją podziwiają.", "<i>look up to sb</i> = podziwiać, szanować.", "up-idiom", W),
    gap(f"She {GAP} Spanish just by living in Madrid for a year.", "picked up", "🇵🇱 podłapała, nauczyła się przy okazji",
        "Podłapała hiszpański, po prostu mieszkając przez rok w Madrycie.", "<i>pick sth up</i> = nauczyć się bez formalnej nauki.", "up-idiom", W),
    tr("Jak ty z nim wytrzymujesz?", "put up with", "How do you put up with him?",
       "Zaimek po obu cząstkach.", "type34", W),
    tr("Zużyliśmy cały papier.", "use up", "We've used up all the paper.",
       "Skutek widoczny teraz (nie ma papieru): Present Perfect.", "up-end", W, alt="We have used up all the paper."),
    tr("Sprawdzę to w słowniku.", "look up", "I'll look it up in a dictionary.",
       "Zaimek <i>it</i> w środku.", "type2", W, alt="I'll look it up in the dictionary."),
    tr("Nie poruszaj tego przy kolacji.", "bring up", "Don't bring it up at dinner.",
       "Zaimek <i>it</i> w środku.", "type2", W),
]


# ---------------------------------------------------------------- Typing 5: ability (Review 2a)
A = "ability"
ABILITY = [
    rewrite("She can solve problems very quickly.", "ability", "She has",
            "She has the ability to solve problems very quickly.", "Ma zdolność bardzo szybkiego rozwiązywania problemów.",
            "<i>can</i> → <i>has the ability to</i> + bezokolicznik.", "ability", A),
    rewrite("He can repair cars very well.", "skilled", "He is", "He is skilled at repairing cars.",
            "Jest wprawny w naprawianiu samochodów.", "<i>skilled <b>at</b></i> + <i>-ing</i>. <i>very well</i> znika, bo siedzi już w <i>skilled</i>.",
            "ability", A, alt="He's skilled at repairing cars."),
    rewrite("The students in this class all paint extremely well.", "outstanding", "The students in this class are",
            "The students in this class are all outstanding painters.", "Wszyscy uczniowie w tej klasie są wybitnymi malarzami.",
            "Czasownik <i>paint</i> → rzeczownik <i>painters</i>; <i>all</i> stoi po <i>are</i>.", "adj-noun", A),
    rewrite("She could become a great singer.", "potential", "She has",
            "She has the potential to become a great singer.", "Ma potencjał, żeby zostać świetną piosenkarką.",
            "<i>could</i> → <i>has the potential to</i> + bezokolicznik.", "ability", A),
    rewrite("He's better than most drivers.", "exceptional", "He's", "He's an exceptional driver.",
            "Jest wyjątkowym kierowcą.", "<i>exceptional</i> = lepszy niż prawie wszyscy. Przedimek <b>an</b>.", "adj-noun", A,
            alt="He is an exceptional driver."),
    rewrite("My brother can dance very well.", "extraordinary", "My brother is", "My brother is an extraordinary dancer.",
            "Mój brat jest niezwykłym tancerzem.", "<i>dance</i> → <i>dancer</i>; przedimek <b>an</b> przed samogłoską.", "adj-noun", A),
    rewrite("She is very good at languages.", "talent", "She has", "She has a talent for languages.",
            "Ma talent do języków.", "<i>a talent <b>for</b></i> sth.", "ability", A),
    gap(f"She's very skilled {GAP} designing websites.", "at", "przyimek",
        "Jest bardzo wprawna w projektowaniu stron.", "<i>skilled at</i>, tak jak <i>good at</i>.", "ability", A),
    gap(f"He has a real talent {GAP} music.", "for", "przyimek",
        "Ma prawdziwy talent do muzyki.", "<i>a talent for</i> sth.", "ability", A),
]


# ---------------------------------------------------------------- Typing 6: word formation (Review 2b)
F = "word-formation"
FORMATION = [
    gap(f"Our team has a new {GAP} who makes us run every morning. (TRAIN)", "trainer", "utwórz słowo od wyrazu w nawiasie",
        "Nasza drużyna ma nowego trenera, który każe nam biegać co rano.", "Osoba: train + <b>-er</b>.", "wf", F),
    gap(f"There were over two hundred {GAP} in the race. (COMPETE)", "competitors", "utwórz słowo od wyrazu w nawiasie",
        "W wyścigu wzięło udział ponad dwustu zawodników.", "Osoba: compet<b>itor</b>; tu liczba mnoga po <i>two hundred</i>.", "wf", F),
    gap(f"You don't have to be very {GAP} to enjoy cycling. (ATHLETE)", "athletic", "utwórz słowo od wyrazu w nawiasie",
        "Nie trzeba być bardzo wysportowanym, żeby lubić jazdę na rowerze.", "Przymiotnik: athlet<b>ic</b>.", "wf", F),
    gap(f"She turned {GAP} at the age of sixteen. (PROFESSION)", "professional", "utwórz słowo od wyrazu w nawiasie",
        "Przeszła na zawodowstwo w wieku szesnastu lat.", "Przymiotnik: profession<b>al</b>; <i>turn professional</i>.", "wf", F),
    gap(f"It was the best {GAP} of his career. (PERFORM)", "performance", "utwórz słowo od wyrazu w nawiasie",
        "To był najlepszy występ w jego karierze.", "Rzeczownik: perform<b>ance</b>.", "wf", F),
    gap(f"The {GAP} team lifted the trophy in front of the fans. (VICTORY)", "victorious", "utwórz słowo od wyrazu w nawiasie",
        "Zwycięska drużyna uniosła trofeum przed kibicami.", "Przymiotnik: victor<b>ious</b> (<i>y</i> → <i>i</i>).", "wf", F),
]


OUTPUTS = {
    "fce-grammar-unit-3-review-3d.tsv": GRAMMAR,
    "fce-collocations-unit-3-review-3d.tsv": COLLOC,
    "fce-vocabulary-unit-3-review-3d.tsv": VOCAB,
    "fce-phrasal-verbs-unit-3-review-3d.tsv": PHRASAL,
    "fce-typing-unit-3-review-3d.tsv": DATA + PERFECT + ORDER + WORDPOWER + ABILITY + FORMATION,
}

if __name__ == "__main__":
    for name, rows in OUTPUTS.items():
        write_tsv(name, rows)
