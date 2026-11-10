#!/usr/bin/env python3
"""Talia 3C Everyday English – Making careful suggestions; Keeping to the topic of the conversation.

Źródło: Empower B2, unit 3C (Student's Book, Useful language 5a–d; Workbook 3C, ćwiczenia 1a i 1b
z kluczem). Większość kart to typ FCE Typing – odpowiedź wpisuje się z klawiatury:
brakujący zwrot, zdanie z rozsypanki, poprawione zdanie albo tłumaczenie PL → EN.

Uruchom z katalogu repo: python decks/careful_suggestions_3c.py
Nadpisuje pliki TSV w output/. Nie zmieniaj pierwszych pól istniejących wierszy –
od nich zależy GUID notatki w Anki (zmiana = nowa karta i utrata historii powtórek).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cardlib import (GAP, examples_block, grammar_explanation, mistakes_block,  # noqa: E402
                     typing_fields, uoe_explanation, write_tsv)

T = "careful-suggestions unit-3c"

# Reguły powtarzane w wyjaśnieniach kart – jedna na zwrot.
R = {
    "could": "<b>We could always</b> + bezokolicznik bez <i>to</i>. <i>always</i> znaczy tu „to zawsze jakaś opcja”, nie „zawsze”.",
    "another-idea": "<b>Another idea might be</b> + <b>to</b> + bezokolicznik.",
    "think": "<b>I think maybe we should</b> + bezokolicznik bez <i>to</i>. <i>maybe</i> stoi przed podmiotem (<i>maybe we</i>).",
    "thought": "<b>I thought maybe we could</b> + bezokolicznik bez <i>to</i>. Czas przeszły <i>thought</i> tylko zmiękcza propozycję.",
    "dont-think": "<b>Don't you think it's a good idea</b> + <b>to</b> + bezokolicznik<b>?</b>",
    "how-sound": "<b>How does it sound if we / I</b> + Present Simple<b>?</b>",
    "dont-agree": "<b>(But) don't you agree that it'd be easier / better</b> + (<b>not</b>) <b>to</b> + bezokolicznik<b>?</b> <i>it'd</i> = <i>it would</i>.",
    "as-saying": "<b>Anyway, as I was saying,</b> + zdanie. Powrót do wątku po dygresji.",
    "going-back": "<b>Just going back to what I was saying before</b> (+ przecinek i dalszy ciąg).",
    "get-back": "<b>So, to get back to</b> + rzeczownik / temat.",
    "another-thing": "<b>Another thing to remember is</b> + rzeczownik. Zwrot stoi na początku zdania.",
}


def grammar(rule, formula, usage, signal, tip, examples, mistakes, extra=""):
    return [rule, grammar_explanation(formula, usage, tip, signal=signal, signal_label="🔑 Zmiękczacze i sygnały:"),
            examples_block(examples), mistakes_block(mistakes), f"fce grammar {T} {extra}".strip()]


def typing(task_type, fields, why, rule, extra=""):
    return [*fields, uoe_explanation(why, R[rule]), task_type, f"fce typing {task_type} {T} {extra}".strip()]


def gap(sentence, answer, hint, pl, why, rule, alt=None):
    """Luka na cały zwrot: wpisujesz 2–4 brakujące słowa."""
    n = len(answer.split())
    full = sentence.replace(GAP, f"<b>{answer}</b>")
    return typing("gap-phrase",
                  typing_fields("⌨️ Wpisz brakujące słowa:", sentence, answer, full, pl=pl, alt=alt,
                                hint=f"🇵🇱 {hint} · {n} słowa"),
                  why, rule)


def order(scrambled, answer, pl, why, rule, alt=None, extra=""):
    """Put the words in the correct order: wpisujesz całe zdanie."""
    return typing("word-order",
                  typing_fields("⌨️ Ułóż zdanie z rozsypanki i wpisz je w całości:", scrambled, answer, answer,
                                pl=pl, alt=alt, body_cls="word scrambled"),
                  why, rule, extra)


def fix(wrong, answer, pl, why, rule, alt=None, extra=""):
    """Correct the mistake: wpisujesz całe poprawione zdanie."""
    return typing("error-correction",
                  typing_fields("⌨️ W zdaniu jest jeden błąd. Wpisz całe poprawne zdanie:", wrong, answer, answer,
                                pl=pl, alt=alt, body_cls="wrong-sentence"),
                  why, rule, extra)


def tr(pl, hint, answer, why, rule, alt=None):
    """Tłumaczenie PL → EN z podanym zwrotem: wpisujesz całe zdanie."""
    return typing("translation",
                  typing_fields("🇵🇱 → 🇬🇧 Przetłumacz i wpisz całe zdanie:", pl, answer, answer, alt=alt,
                                hint=f"Użyj: <b>{hint}</b>"),
                  why, rule)


# ---------------------------------------------------------------- Grammar (zrozumienie tematu)
GRAMMAR = [
    grammar(
        "Careful suggestions (1): putting forward an idea carefully",
        "<code>We could always + bezokolicznik</code><br>"
        "<code>Another idea might be + to + bezokolicznik</code><br>"
        "<code>I think maybe we should + bezokolicznik</code><br>"
        "<code>I thought maybe we could + bezokolicznik</code>",
        ["<b>Po co:</b> gdy temat jest drażliwy (lista gości, pieniądze, czyjaś praca), podajesz pomysł tak, żeby rozmówca mógł łatwo powiedzieć „nie” i nikt nie poczuł się urażony. Zwykłe <i>Let's…</i> albo <i>We should…</i> brzmi wtedy zbyt stanowczo.",
         "<b>Jak to działa:</b> każdy zwrot ma zmiękczacz. <b>could / might</b> zamiast <i>can / will</i>; <b>maybe</b>; <b>always</b> („to zawsze jakaś opcja”); czas przeszły <b>I thought</b> („tak mi tylko przyszło do głowy”).",
         "<b>Forma po zwrocie:</b> po czasownikach modalnych <i>could</i> i <i>should</i> goły bezokolicznik (<i>could invite</i>). Tylko po <b>might be</b> jest <b>to</b>: <i>might be <b>to</b> go</i>.",
         "<b>Szyk:</b> <i>always</i> stoi po <i>could</i> (<i>could always go</i>), a <i>maybe</i> przed podmiotem: <i>I think <b>maybe we</b> should</i>, <i>I thought <b>maybe we</b> could</i>."],
        "could · might · maybe · always · I thought",
        "Speaking Part 3 (rozmowa w parze): te zwroty pokazują, że negocjujesz, a nie narzucasz zdanie, co liczy się w kryterium Interactive Communication. Przydają się też w nieformalnym mailu z propozycją.",
        [("We <b>could always</b> invite them to the evening reception.", "Zawsze możemy zaprosić ich na wieczorne przyjęcie."),
         ("<b>Another idea might be to</b> go the day before.", "Innym pomysłem mogłoby być pojechanie dzień wcześniej."),
         ("<b>I think maybe we should</b> stay home.", "Myślę, że może powinniśmy zostać w domu."),
         ("<b>I thought maybe we could</b> invite Simon.", "Pomyślałem, że może moglibyśmy zaprosić Simona.")],
        [("I think we maybe should stay home.", "I think maybe we should stay home.",
          "<i>maybe</i> stoi przed podmiotem, nie między podmiotem a czasownikiem modalnym."),
         ("I thought maybe we could to invite Simon.", "I thought maybe we could invite Simon.",
          "Po <i>could / should</i> nigdy nie ma <i>to</i>."),
         ("Another idea might be for going the day before.", "Another idea might be to go the day before.",
          "Po <i>might be</i> idzie <b>to</b> + bezokolicznik, nie <i>for</i> + <i>-ing</i>.")],
        "functional-language speaking"),
    grammar(
        "Careful suggestions (2): asking the other person to give their point of view",
        "<code>Don't you think it's a good idea + to + bezokolicznik?</code><br>"
        "<code>How does it sound if we / I + Present Simple?</code><br>"
        "<code>(But) don't you agree that it'd be easier / better + (not) to + bezokolicznik?</code>",
        ["<b>Po co:</b> zamiast stwierdzać, pytasz. Decyzja zostaje po stronie rozmówcy, więc propozycja jest grzeczna nawet wtedy, gdy się z nim nie zgadzasz.",
         "<b>Pytanie przeczące</b> (<i>Don't you think…? Don't you agree…?</i>) sugeruje, że liczysz na odpowiedź „tak”: „Nie sądzisz, że…?”. <b>But</b> na początku pokazuje, że masz inne zdanie niż rozmówca.",
         "<b>it'd</b> = <b>it would</b>. Po nim musi stać czasownik <b>be</b>: <i>it'd <b>be</b> easier</i>. Dalej <b>to</b> + bezokolicznik, w przeczeniu <b>not to</b>: <i>it'd be easier <b>not to</b> invite them</i>.",
         "Po <b>How does it sound if</b> jest Present Simple, chociaż mowa o przyszłości: <i>if we <b>watch</b> a film</i>, nie <i>will watch</i>."],
        "Don't you think…? · Don't you agree…? · How does it sound…? · it'd be",
        "W Speaking Part 3 pytanie do partnera to najprostszy sposób na punkty za współpracę. Te trzy zwroty jednocześnie podają twój pomysł i oddają partnerowi głos.",
        [("<b>Don't you think it's a good idea to</b> take some food?", "Nie sądzisz, że dobrze byłoby wziąć trochę jedzenia?"),
         ("<b>How does it sound if we</b> watch a film on Sunday?", "Co ty na to, żebyśmy w niedzielę obejrzeli film?"),
         ("<b>But don't you agree that it'd be</b> easier <b>to</b> eat out?", "Ale nie zgodzisz się, że łatwiej byłoby zjeść na mieście?"),
         ("But don't you agree that <b>it'd be easier not to</b> invite them?", "Ale nie zgodzisz się, że łatwiej byłoby ich nie zapraszać?")],
        [("Don't you agree to eat out but that it'd easier?", "But don't you agree that it'd be easier to eat out?",
          "Stała rama: <i>But don't you agree that it'd be</i> + przymiotnik + <i>to</i> + czasownik. <i>But</i> zaczyna zdanie, a po <i>it'd</i> musi być <b>be</b>."),
         ("Don't you think a good idea to invite more people?", "Don't you think it's a good idea to invite more people?",
          "Zdanie po <i>think</i> potrzebuje podmiotu i czasownika: <b>it's</b>."),
         ("How does it sound we only have a small cake?", "How does it sound if we only have a small cake?",
          "Brakuje <b>if</b>, które łączy pytanie z propozycją.")],
        "functional-language speaking"),
    grammar(
        "Keeping to the topic of the conversation",
        "<code>Anyway, as I was saying, + zdanie</code><br>"
        "<code>Just going back to what I was saying before, …</code><br>"
        "<code>So, to get back to + temat, …</code><br>"
        "<code>Another thing to remember is + rzeczownik</code>",
        ["<b>Po co:</b> rozmowa zeszła na boczny temat albo ktoś ci przerwał, a ty chcesz grzecznie wrócić do głównego wątku.",
         "<b>as I was saying</b> = „jak mówiłem”. Zawsze <i>say</i>, nigdy <i>speak</i> ani <i>tell</i>.",
         "<b>go back to / get back to</b> = wracać do tematu. Przyimek to zawsze <b>to</b>. Uwaga: <i>get back <b>at</b> sb</i> znaczy „odegrać się na kimś”.",
         "<b>Another thing to remember is…</b> dodaje kolejny punkt do tego samego tematu. Zwrot stoi na początku, a nowa informacja na końcu zdania."],
        "Anyway · as I was saying · going back to · to get back to",
        "W Speaking Part 3 i 4 tymi zwrotami wracasz do pytania egzaminatora, kiedy rozmowa odpłynęła. To też naturalne wypełniacze, które dają sekundę na zebranie myśli.",
        [("<b>Anyway, as I was saying,</b> Tessa needs to decide.", "W każdym razie, jak mówiłem, Tessa musi podjąć decyzję."),
         ("<b>Just going back to what I was saying before.</b>", "Wracając tylko do tego, co mówiłem wcześniej."),
         ("<b>So, to get back to</b> Martin and his problems.", "No więc, wracając do Martina i jego problemów."),
         ("<b>Another thing to remember is</b> the price.", "Kolejna rzecz, o której trzeba pamiętać, to cena.")],
        [("Anyway, as I was speaking, Tessa needs to decide.", "Anyway, as I was saying, Tessa needs to decide.",
          "W tym zwrocie zawsze <b>saying</b>."),
         ("So, to get back at Martin and his problems.", "So, to get back to Martin and his problems.",
          "Do tematu wracamy <b>to</b>; <i>get back at</i> to „zemścić się”."),
         ("Price is the another thing to remember.", "Another thing to remember is the price.",
          "Zaczynasz od całego zwrotu <i>Another thing to remember is</i>. Przed <i>another</i> nie ma <i>the</i> (an + other), a <i>the</i> stoi przed <i>price</i>.")],
        "functional-language speaking"),
]


# ---------------------------------------------------------------- 1. Brakujący zwrot
GAPS = [
    gap(f"We {GAP} invite them to the evening reception.", "could always", "„zawsze możemy”",
        "Zawsze możemy zaprosić ich na wieczorne przyjęcie.",
        "Zdanie Becky z nagrania: pomysł podany jako jedna z opcji.", "could"),
    gap(f"But don't you agree that it'd {GAP} not to invite them?", "be easier", "„byłoby łatwiej”",
        "Ale nie zgodzisz się, że łatwiej byłoby ich nie zapraszać?",
        "Zdanie Toma z nagrania. <i>it'd</i> to <i>it would</i>, więc po nim musi być <b>be</b>.", "dont-agree"),
    gap(f"{GAP} it's a good idea to book a table in advance?", "Don't you think", "„Nie sądzisz, że…?”",
        "Nie sądzisz, że dobrze byłoby zarezerwować stolik z wyprzedzeniem?",
        "Pytanie przeczące: liczysz na odpowiedź „tak”.", "dont-think"),
    gap(f"{GAP} if we meet at the station at six?", "How does it sound", "„Co ty na to, żebyśmy…?”",
        "Co ty na to, żebyśmy spotkali się na dworcu o szóstej?",
        "Pytasz, jak pomysł „brzmi” dla rozmówcy. Po <i>if</i> Present Simple: <i>we meet</i>.", "how-sound"),
    gap(f"{GAP} to take the train instead of driving.", "Another idea might be", "„Innym pomysłem mogłoby być…”",
        "Innym pomysłem mogłoby być pojechanie pociągiem zamiast samochodem.",
        "<i>might</i> zmiękcza: to tylko możliwość. Po <i>be</i> jest <b>to</b> + bezokolicznik.", "another-idea"),
    gap(f"I {GAP} leave a bit earlier, just in case.", "think maybe we should", "„myślę, że może powinniśmy”",
        "Myślę, że może powinniśmy wyjść trochę wcześniej, na wszelki wypadek.",
        "Kolejność: <i>think</i> → <i>maybe</i> → <i>we</i> → <i>should</i>.", "think"),
    gap(f"I {GAP} go for a walk after lunch.", "thought maybe we could", "„pomyślałem, że może moglibyśmy”",
        "Pomyślałem, że może moglibyśmy pójść na spacer po obiedzie.",
        "Kolejność: <i>thought</i> → <i>maybe</i> → <i>we</i> → <i>could</i>.", "thought"),
    gap(f"But {GAP} it'd be better to ask her first?", "don't you agree that", "„nie zgodzisz się, że…?”",
        "Ale nie zgodzisz się, że lepiej byłoby najpierw ją zapytać?",
        "<i>agree</i> + <b>that</b> + zdanie. Nie <i>agree to</i>: to znaczyłoby „zgodzić się coś zrobić”.", "dont-agree"),
    gap(f"Anyway, {GAP}, Tessa needs to decide by Friday.", "as I was saying", "„jak mówiłem”",
        "W każdym razie, jak mówiłem, Tessa musi podjąć decyzję do piątku.",
        "Wracasz do wątku po dygresji. Zawsze <i>saying</i>, nie <i>speaking</i>.", "as-saying"),
    gap(f"Just {GAP} what I was saying before, we still need a venue.", "going back to", "„wracając do”",
        "Wracając do tego, co mówiłem wcześniej: wciąż potrzebujemy sali.",
        "<i>go back <b>to</b></i> + temat. Bez <i>back</i> zdanie traci sens „powrotu”.", "going-back"),
    gap(f"So, {GAP} Martin and his problems, what are we going to do?", "to get back to", "„wracając do”",
        "No więc, wracając do Martina i jego problemów: co robimy?",
        "Dwa razy <i>to</i>: bezokolicznik <i>to get</i> i przyimek <i>back to</i>.", "get-back"),
    gap(f"{GAP} is the cost of the tickets.", "Another thing to remember", "„Kolejna rzecz, o której trzeba pamiętać”",
        "Kolejna rzecz, o której trzeba pamiętać, to koszt biletów.",
        "<i>another</i> = <i>an + other</i>, więc bez <i>the</i> przed nim.", "another-thing"),
]


# ---------------------------------------------------------------- 2. Put the words in the correct order
ORDER = [
    order("could / go / swimming / we / day / always / another .", "We could always go swimming another day.",
          "Zawsze możemy pójść popływać innego dnia.",
          "<i>always</i> stoi zaraz po <i>could</i>, przed czasownikiem głównym.", "could"),
    order("thing / price / remember / another / to / is / the .", "Another thing to remember is the price.",
          "Kolejna rzecz, o której trzeba pamiętać, to cena.",
          "Najpierw sklej zwrot <i>Another thing to remember is</i>, dopiero potem dołóż <i>the price</i>. Twoja wersja: <span class=\"wrong\">Price is the another thing to remember.</span>",
          "another-thing", extra="my-mistakes"),
    order("stay / maybe / I / should / home / think / we .", "I think maybe we should stay home.",
          "Myślę, że może powinniśmy zostać w domu.",
          "<i>maybe</i> przed podmiotem <i>we</i>. Twoja wersja: <span class=\"wrong\">I think we maybe should stay home.</span> W brytyjskim angielskim częściej <i>stay <b>at</b> home</i>.",
          "think", extra="my-mistakes"),
    order("idea / ask / think / to / a / don't you / it's / good ?", "Don't you think it's a good idea to ask?",
          "Nie sądzisz, że dobrze byłoby zapytać?",
          "Ta rama wyszła w ćwiczeniu bezbłędnie. Teraz utrwal ją do automatyzmu.", "dont-think"),
    order("how / sound / we watch / does / on Sunday / a / film / if / it ?", "How does it sound if we watch a film on Sunday?",
          "Co ty na to, żebyśmy w niedzielę obejrzeli film?",
          "Pytanie <i>How does it sound</i> + <i>if</i> + zdanie w Present Simple.", "how-sound"),
    order("to / that / but / easier / it'd / eat out / agree / be / don't you ?", "But don't you agree that it'd be easier to eat out?",
          "Ale nie zgodzisz się, że łatwiej byłoby zjeść na mieście?",
          "Kolejność klocków: <i>But</i> → <i>don't you agree</i> → <i>that</i> → <i>it'd be easier</i> → <i>to eat out</i>. Twoja wersja: <span class=\"wrong\">Don't you agree to eat out but that it'd easier?</span>",
          "dont-agree", alt="But don't you agree that it would be easier to eat out?", extra="my-mistakes"),
    order("be / idea / to / another / a / hire / might / car .", "Another idea might be to hire a car.",
          "Innym pomysłem mogłoby być wynajęcie samochodu.",
          "<i>might be</i> + <i>to</i> + bezokolicznik.", "another-idea"),
    order("maybe / thought / could / I / we / a / order / pizza .", "I thought maybe we could order a pizza.",
          "Pomyślałem, że może moglibyśmy zamówić pizzę.",
          "<i>maybe</i> stoi przed <i>we</i>, a po <i>could</i> nie ma <i>to</i>.", "thought"),
    order("saying / was / anyway / I / as / need / to / we / tickets / book / the .",
          "Anyway, as I was saying, we need to book the tickets.",
          "W każdym razie, jak mówiłem, musimy zarezerwować bilety.",
          "Wtrącenie <i>as I was saying</i> oddziel przecinkami z obu stron.", "as-saying"),
    order("back / just / to / going / what / before / saying / I / was .", "Just going back to what I was saying before.",
          "Wracając tylko do tego, co mówiłem wcześniej.",
          "<i>going back to</i> + <i>what I was saying before</i>. Po <i>what</i> szyk zdania twierdzącego.", "going-back"),
    order("get / so / to / to / back / the / plan / weekend / for / the .", "So, to get back to the plan for the weekend.",
          "No więc, wracając do planu na weekend.",
          "Po <i>So</i> przecinek, potem <i>to get back to</i> + temat.", "get-back"),
    order("sound / does / it / how / if / I / everyone / cook / for ?", "How does it sound if I cook for everyone?",
          "Co ty na to, żebym ugotował dla wszystkich?",
          "Po <i>if</i> może być też <i>I</i>: proponujesz, że sam coś zrobisz.", "how-sound"),
]


# ---------------------------------------------------------------- 3. Correct the mistake
FIX = [
    fix("Don't you think it's a good idea take some food?", "Don't you think it's a good idea to take some food?",
        "Nie sądzisz, że dobrze byłoby wziąć trochę jedzenia?",
        "Brakowało <b>to</b> po <i>a good idea</i>.", "dont-think"),
    fix("Anyway, as I was speaking, Tessa needs to decide.", "Anyway, as I was saying, Tessa needs to decide.",
        "W każdym razie, jak mówiłem, Tessa musi podjąć decyzję.",
        "<i>speaking</i> → <b>saying</b>. <i>say</i> odnosi się do treści, <i>speak</i> do samej czynności mówienia.", "as-saying"),
    fix("Another idea might be for going the day before.", "Another idea might be to go the day before.",
        "Innym pomysłem mogłoby być pojechanie dzień wcześniej.",
        "<i>for going</i> → <b>to go</b>.", "another-idea"),
    fix("Just going to what I was saying before.", "Just going back to what I was saying before.",
        "Wracając tylko do tego, co mówiłem wcześniej.",
        "Brakowało <b>back</b>: wracasz, a nie idziesz.", "going-back"),
    fix("I thought maybe we could to invite Simon.", "I thought maybe we could invite Simon.",
        "Pomyślałem, że może moglibyśmy zaprosić Simona.",
        "Po <i>could</i> nie ma <i>to</i>.", "thought"),
    fix("Of course, we could always checking online.", "Of course, we could always check online.",
        "Oczywiście zawsze możemy sprawdzić w internecie.",
        "<i>checking</i> → <b>check</b>: po czasowniku modalnym goły bezokolicznik.", "could"),
    fix("But don't you agree that it's be better to ask first?", "But don't you agree that it'd be better to ask first?",
        "Ale nie zgodzisz się, że lepiej byłoby najpierw zapytać?",
        "<i>it's be</i> → <b>it'd be</b> (= <i>it would be</i>). Po <i>it's</i> nie może stać <i>be</i>.", "dont-agree",
        alt="But don't you agree that it would be better to ask first?"),
    fix("So, to get back at Martin and his problems.", "So, to get back to Martin and his problems.",
        "No więc, wracając do Martina i jego problemów.",
        "<i>at</i> → <b>to</b>. <i>get back at sb</i> znaczy „odegrać się na kimś”.", "get-back"),
    fix("Another idea might to be booking a DJ for the reception.", "Another idea might be to book a DJ for the reception.",
        "Innym pomysłem mogłoby być zamówienie DJ-a na przyjęcie.",
        "<i>might to be booking</i> → <b>might be to book</b>: najpierw <i>be</i>, potem <i>to</i> + bezokolicznik.", "another-idea"),
    fix("Don't you think a good idea to invite more people?", "Don't you think it's a good idea to invite more people?",
        "Nie sądzisz, że dobrze byłoby zaprosić więcej osób?",
        "Brakowało <b>it's</b>: zdanie po <i>think</i> musi mieć podmiot i czasownik.", "dont-think"),
    fix("Maybe I thought we could get married at home.", "I thought maybe we could get married at home.",
        "Pomyślałem, że może moglibyśmy wziąć ślub w domu.",
        "<i>maybe</i> należy do propozycji, nie do <i>thought</i>, więc stoi przed <i>we</i>.", "thought"),
    fix("How does it sound we only have a small cake?", "How does it sound if we only have a small cake?",
        "Co ty na to, żebyśmy mieli tylko mały tort?",
        "Brakowało <b>if</b>.", "how-sound"),
    fix("I think we maybe should stay at home tonight.", "I think maybe we should stay at home tonight.",
        "Myślę, że może powinniśmy dziś wieczorem zostać w domu.",
        "Twój błąd z ćwiczenia 1a: <i>we maybe should</i> → <b>maybe we should</b>.", "think", extra="my-mistakes"),
    fix("But don't you agree that it'd easier to walk?", "But don't you agree that it'd be easier to walk?",
        "Ale nie zgodzisz się, że łatwiej byłoby pójść pieszo?",
        "Twój błąd z ćwiczenia 1a: po <i>it'd</i> zabrakło <b>be</b>.", "dont-agree",
        alt="But don't you agree that it would be easier to walk?", extra="my-mistakes"),
    fix("How does it sound if we will go by train?", "How does it sound if we go by train?",
        "Co ty na to, żebyśmy pojechali pociągiem?",
        "Po <i>if</i> Present Simple, bez <i>will</i>, chociaż mowa o przyszłości.", "how-sound"),
]


# ---------------------------------------------------------------- 4. Tłumaczenia PL → EN
TR = [
    tr("Zawsze możemy zapytać Toma.", "We could always …", "We could always ask Tom.",
       "Ostrożna propozycja: jedna z możliwych opcji.", "could"),
    tr("Nie sądzisz, że dobrze byłoby zarezerwować stolik?", "Don't you think it's a good idea to …?",
       "Don't you think it's a good idea to book a table?",
       "„Dobrze byłoby” oddajesz przez <i>it's a good idea to</i>.", "dont-think"),
    tr("Co ty na to, żebyśmy spotkali się w sobotę?", "How does it sound if …?",
       "How does it sound if we meet on Saturday?",
       "Po <i>if</i> Present Simple. Dni tygodnia z <b>on</b>.", "how-sound"),
    tr("Innym pomysłem mogłoby być pojechanie pociągiem.", "Another idea might be to …",
       "Another idea might be to go by train.",
       "Środek transportu: <b>by</b> train, bez przedimka.", "another-idea"),
    tr("Myślę, że może powinniśmy poczekać do jutra.", "I think maybe we should …",
       "I think maybe we should wait until tomorrow.",
       "<i>maybe</i> przed <i>we</i>.", "think", alt="I think maybe we should wait till tomorrow."),
    tr("Pomyślałem, że może moglibyśmy zjeść na mieście.", "I thought maybe we could …",
       "I thought maybe we could eat out.",
       "<b>eat out</b> = jeść poza domem, w restauracji.", "thought"),
    tr("Ale nie zgodzisz się, że łatwiej byłoby zostać w domu?", "But don't you agree that it'd …?",
       "But don't you agree that it'd be easier to stay at home?",
       "Pełna rama: <i>it'd be</i> + przymiotnik + <i>to</i> + czasownik.", "dont-agree",
       alt="But don't you agree that it would be easier to stay at home?"),
    tr("W każdym razie, jak mówiłem, musimy podjąć decyzję.", "Anyway, as I was saying, …",
       "Anyway, as I was saying, we need to make a decision.",
       "Decyzję się „robi”: <b>make</b> a decision, nie <i>do</i>.", "as-saying",
       alt="Anyway, as I was saying, we have to make a decision."),
    tr("Wracając do tego, co mówiłem wcześniej: kogo powinniśmy zaprosić?", "Just going back to …",
       "Just going back to what I was saying before, who should we invite?",
       "Po zwrocie przecinek i dalszy ciąg wypowiedzi.", "going-back"),
    tr("No więc, wracając do wesela: ile osób zapraszamy?", "So, to get back to …",
       "So, to get back to the wedding, how many people are we inviting?",
       "Ustalony plan na przyszłość: Present Continuous (<i>are we inviting</i>).", "get-back"),
    tr("Kolejna rzecz, o której trzeba pamiętać, to pogoda.", "Another thing to remember is …",
       "Another thing to remember is the weather.",
       "Zwrot na początku, nowa informacja na końcu. <i>the weather</i> zawsze z <i>the</i>.", "another-thing"),
]


OUTPUTS = {
    "fce-grammar-careful-suggestions-3c.tsv": GRAMMAR,
    "fce-typing-careful-suggestions-3c.tsv": GAPS + ORDER + FIX + TR,
}

if __name__ == "__main__":
    for name, rows in OUTPUTS.items():
        write_tsv(name, rows)
