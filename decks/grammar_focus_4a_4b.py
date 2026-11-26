#!/usr/bin/env python3
"""Grammar Focus 4A i 4B (podręcznik s. 140 i ćwiczenia a–b do obu sekcji).

4A uzupełnia talię decks/used_to_would_4a.py – bez powtórek jej reguł:
opowiadanie z used to / would / Past Simple, wouldn't (odmowa w przeszłości)
oraz karty wyboru z ćwiczeń 4A a i b.

4B Obligation and permission: must / have to / need to, mustn't vs don't have to,
can / be allowed to, should / ought to, be supposed to, make / let,
be forced to / be allowed to; KWT z ćwiczenia 4B a, luki z 4B b, tłumaczenia PL → EN.

Uruchom z katalogu repo: python decks/grammar_focus_4a_4b.py
Nadpisuje pliki TSV w output/. Nie zmieniaj pierwszych pól istniejących wierszy –
od nich zależy GUID notatki w Anki (zmiana = nowa karta i utrata historii powtórek).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cardlib import (GAP as G, KWT_GAP as GAP, answer_block, examples_block,  # noqa: E402
                     grammar_explanation, kwt_fields, mistakes_block, open_cloze_fields,
                     translation_fields, uoe_explanation, write_tsv)

T4A = "unit-4a"
T4B = "unit-4b"
GF = "grammar-focus"
UW = "used-to-would"
OP = "obligation-permission"


def grammar(unit, rule, formula, usage, signal, tip, examples, mistakes, extra=""):
    return [rule, grammar_explanation(formula, usage, tip, signal=signal, signal_label="🔑 Sygnały:"),
            examples_block(examples), mistakes_block(mistakes), f"fce grammar {unit} {GF} {extra}".strip()]


def mc(instruction, sentence, options, answer, why, rule, tip):
    task = f'<div class="mc"><p class="instruction">{instruction}</p><p>{sentence}</p>'
    if options:
        task += f"<p>a) {options[0]} · b) {options[1]}</p>"
    task += "</div>"
    return [task, answer_block(answer), uoe_explanation(why, rule, tip), "multiple-choice",
            f"fce use-of-english multiple-choice {T4A} {GF} {UW}"]


def oc(sentence, answer, why, rule, tip):
    return [*open_cloze_fields(sentence, answer, why, rule, tip), "open-cloze",
            f"fce use-of-english open-cloze {T4B} {GF} {OP}"]


def kwt(original, keyword, gap, answer, full, why, rule, tip):
    return [*kwt_fields(original, keyword, gap, answer, full, why, rule, tip), "key-word-transformation",
            f"fce use-of-english key-word-transformation {T4B} {GF} {OP}"]


def tr(pl, hint, answer, alt, expl, wrong):
    return [*translation_fields(pl, hint, answer, alt, expl, wrong), "translation",
            f"fce use-of-english translation {T4B} {GF} {OP}"]


# ================================================================ 4A
GRAMMAR_4A = [
    grammar(
        T4A,
        "Telling a story about your past: used to, would and Past Simple together",
        "<code>used to</code> (otwiera wspomnienie) → <code>would ('d)</code> (kolejne powtarzane czynności) → <code>Past Simple</code> (uczucia, stany, pojedyncze zdarzenia)",
        ["Typowy schemat: <b>used to</b> ustawia tło, a dalsze nawyki idą przez <b>would</b>, żeby nie powtarzać w kółko <i>used to</i>.",
         "<b>never used to</b> = <i>didn't use to</i>. Po <i>never</i> nie ma <i>did</i>, więc piszemy <b>used</b> z <i>-d</i>: <i>We never used to go on holidays.</i>",
         "Uczucia i stany (<i>love, like, be, miss</i>) → <b>Past Simple</b> albo <i>used to</i>, nigdy <i>would</i>: <i>We loved it.</i>",
         "Past Simple pasuje zawsze, więc jest bezpiecznym wyjściem, gdy nie masz pewności."],
        "When I was young… · Instead, … · every summer · never",
        "W Writing Part 2 (story, article, email o dzieciństwie) dwa–trzy zdania z taką mieszanką pokazują zakres gramatyki w kryterium <i>Language</i>.",
        [("When I was young, we <b>never used to go</b> on holidays. Instead, we<b>'d spend</b> the whole summer in the fields near our house. We <b>loved</b> it.",
          "Kiedy byłem mały, nigdy nie jeździliśmy na wakacje. Zamiast tego całe lato spędzaliśmy na polach koło domu. Uwielbialiśmy to."),
         ("Before I made my fortune, I<b>'d cycle</b> to work every day. I really <b>miss</b> that.",
          "Zanim się dorobiłem, codziennie jeździłem do pracy rowerem. Bardzo mi tego brakuje."),
         ("I <b>used to</b> walk to school with my brother. We<b>'d stop</b> at the bakery and <b>buy</b> fresh rolls.",
          "Chodziłem do szkoły z bratem. Zatrzymywaliśmy się w piekarni i kupowaliśmy świeże bułki.")],
        [("We never didn't use to go on holidays.", "We never used to go on holidays.",
          "<i>never</i> już jest przeczeniem: bez <i>did / didn't</i>, a wtedy <b>used</b> z <i>-d</i>."),
         ("We would love it.", "We loved it. / We used to love it.",
          "<i>love</i> to uczucie (stan). <i>would</i> działa tylko z czynnościami, a <i>would love</i> znaczy „bardzo bym chciał”.")],
        UW),
    grammar(
        T4A,
        "wouldn't + infinitive: refusing again and again in the past",
        "<code>wouldn't + bezokolicznik</code> = nie chciał, odmawiał (raz po raz) · <code>didn't use to + bezokolicznik</code> = kiedyś nie (nawyk)",
        ["<b>wouldn't</b> opisuje upór albo zakaz, który powtarzał się w przeszłości: <i>He wouldn't allow us to speak</i> = nigdy nam nie pozwalał.",
         "Gdy chodzi o nawyk, pasują obie formy: <i>He <b>didn't use to</b> allow us…</i> i <i>He <b>wouldn't</b> allow us…</i>.",
         "O rzeczach, które „nie chciały” działać, <i>wouldn't</i> pasuje też do jednej sytuacji: <i>The car wouldn't start.</i>",
         "Ze stanami nie: <i>I wouldn't like fish</i> znaczy „nie chciałbym ryby”, a nie „kiedyś nie lubiłem”."],
        "strict · refused · never · however hard I tried",
        "Para do Part 4: <i>He <b>refused to</b> lend me money.</i> ↔ <i>He <b>wouldn't</b> lend me money.</i>",
        [("Our teacher was very strict. He <b>wouldn't allow</b> us to speak at all during class.",
          "Nasz nauczyciel był bardzo surowy. W ogóle nie pozwalał nam mówić na lekcji."),
         ("My dad <b>wouldn't let</b> me stay out after ten.", "Tata nie pozwalał mi wracać później niż o dziesiątej."),
         ("I tried three times, but the laptop <b>wouldn't start</b>.", "Próbowałem trzy razy, ale laptop nie chciał się włączyć.")],
        [("He wouldn't to allow us to speak.", "He wouldn't allow us to speak.",
          "Po <i>would / wouldn't</i> bezokolicznik bez <i>to</i>."),
         ("When I was a child, I wouldn't like fish.", "When I was a child, I didn't like fish. / I didn't use to like fish.",
          "<i>like</i> to stan. <i>wouldn't like</i> brzmi jak tryb warunkowy („nie chciałbym”).")],
        UW),
]

TICK = "Które formy pasują? Czasem pasują obie."
CHOOSE = "Wybierz poprawną formę."

CHOICE_4A = [
    # ćwiczenie a
    mc(TICK, f"She {G} good at maths when she was little.", ("used to be", "would be"),
       "a) used to be",
       "<i>be good at</i> to stan, nie czynność.", "stan (be, have, like, know) → tylko <b>used to</b>",
       "<i>would be</i> brzmiałoby jak „byłaby”."),
    mc(TICK, f"Laura was my best friend – we {G} for hours every day.", ("used to talk", "would talk"),
       "a) i b) – obie",
       "<i>talk</i> to czynność, a <i>every day</i> pokazuje, że się powtarzała.", "powtarzana czynność → <b>used to</b> albo <b>would</b>",
       "Kontekst przeszły daje już pierwsze zdanie (<i>Laura was…</i>), więc <i>would</i> nie brzmi jak tryb warunkowy."),
    mc(TICK, f"I {G} five swimming competitions when I was at school.", ("won", "would win"),
       "a) won",
       "Podana liczba razy (<i>five</i>) to zamknięty wynik, a nie nawyk.", "konkretna liczba razy → <b>Past Simple</b>",
       "Tak samo z <i>three times, once, twice</i>: ani <i>would</i>, ani <i>used to</i>."),
    mc(TICK, f"Our teacher, Mr Williams, was very strict. He {G} allow us to speak at all during class.", ("didn't use to", "wouldn't"),
       "a) i b) – obie",
       "Chodzi o zakaz, który powtarzał się na każdej lekcji.", "powtarzana odmowa → <b>didn't use to</b> albo <b>wouldn't</b>",
       "<i>wouldn't</i> dodaje odcień uporu: „nie chciał nam pozwolić”."),
    mc(TICK, f"I'll never forget the time I {G} my leg. I couldn't walk for weeks!", ("used to break", "broke"),
       "b) broke",
       "Złamanie nogi to jedno zdarzenie (<i>the time</i> = ten jeden raz).", "pojedyncze zdarzenie → <b>Past Simple</b>",
       "<i>used to break</i> znaczyłoby, że łamał nogę regularnie."),
    mc(TICK, f"We {G} a dog, but he died about five years ago.", ("used to have", "would have"),
       "a) used to have",
       "<i>have</i> w znaczeniu „mieć, posiadać” to stan.", "stan → tylko <b>used to</b>",
       "<i>would have</i> brzmi jak „mielibyśmy”."),
    # ćwiczenie b
    mc(CHOOSE, "I <i>used to / would</i> be really good at football when I was young, but now I'm terrible at it.", None,
       "used to",
       "<i>be good at</i> to stan.", "stan → <b>used to</b>, nie <i>would</i>",
       "Kontrast z <i>but now</i> to typowy sygnał <i>used to</i>."),
    mc(CHOOSE, "I <i>didn't use to / didn't used to</i> like jazz, but now it's my favourite kind of music.", None,
       "didn't use to",
       "Po <i>didn't</i> czasownik wraca do formy podstawowej.", "did / didn't + <b>use to</b> (bez -d)",
       "Tak jak <i>didn't go</i>, nie <i>didn't went</i>."),
    mc(CHOOSE, "I <i>used to / 'm used to</i> living on my own. It was strange at first, but now it's fine.", None,
       "'m used to",
       "Teraz to dla mnie normalne – przyzwyczaiłem się. Po <i>to</i> stoi <i>living</i>.", "be used to + <b>-ing</b> = być przyzwyczajonym",
       "<i>-ing</i> po luce od razu wyklucza <i>used to</i> (które chce bezokolicznika)."),
    mc(CHOOSE, "I don't think I'll ever <i>get used to / get use to</i> writing on a tablet computer – it's much easier on a laptop.", None,
       "get used to",
       "Proces przyzwyczajania się → <i>get used to</i>; <i>used</i> zawsze z <i>-d</i>.", "get used to + <b>-ing</b> = przyzwyczaić się",
       "<i>use</i> bez <i>-d</i> występuje tylko po <i>did / didn't</i>."),
    mc(CHOOSE, "Where did you <i>use to go / used to go</i> on holiday when you were a child?", None,
       "use to go",
       "Pytanie z <i>did</i> → czasownik w formie podstawowej.", "Did + podmiot + <b>use to</b> + bezokolicznik?",
       "Ta sama zasada co w przeczeniu z <i>didn't</i>."),
    mc(CHOOSE, "How long did it take you to <i>get used to / used to</i> working from home?", None,
       "get used to",
       "Pytamy o proces przyzwyczajania się, a po luce stoi <i>working</i>.", "get used to + <b>-ing</b>",
       "Po <i>take you to</i> potrzebny bezokolicznik czasownika: <b>get</b>."),
]


# ================================================================ 4B
GRAMMAR_4B = [
    grammar(
        T4B,
        "must vs have to / need to: strong obligation",
        "<code>must + bezokolicznik</code> – zasada mówiącego · <code>have to / need to + bezokolicznik</code> – zasada z zewnątrz · przeszłość: <code>had to / needed to</code>",
        ["<b>must</b>: to ty ustalasz zasadę albo mocno nalegasz: <i>You must wear a helmet. I won't let you ride without one.</i>",
         "<b>have to / need to</b>: opisujesz cudzą zasadę, prawo, regulamin: <i>You have to wear a helmet. It's the law.</i>",
         "<i>must</i> nie ma czasu przeszłego, więc w przeszłości jest tylko <b>had to / needed to</b>.",
         "<i>must</i> brzmi bardzo mocno. W większości sytuacji naturalniejsze jest <i>have to</i>, a pytania z <i>must</i> są bardzo rzadkie (<i>Do I have to…?</i>)."],
        "It's the law · the rules say · the instructor says · I won't let you",
        "Part 4: <i>It is compulsory / necessary to…</i> → <b>have to / need to</b>; <i>It was necessary…</i> → <b>had to</b>.",
        [("You <b>must</b> wear a helmet. I won't let you ride without one.", "Musisz założyć kask. Nie pozwolę ci jechać bez niego."),
         ("You <b>have to</b> wear a helmet. It's the law.", "Trzeba jeździć w kasku. Tak mówi prawo."),
         ("We <b>had to</b> change our passwords straight away.", "Musieliśmy od razu zmienić hasła.")],
        [("Yesterday I must stay late at work.", "Yesterday I had to stay late at work.",
          "<i>must</i> nie ma formy przeszłej → <b>had to</b>."),
         ("Do I must bring my ID?", "Do I have to bring my ID? / Do I need to bring my ID?",
          "<i>must</i> nie łączy się z <i>do</i>. W pytaniach używaj <b>have to / need to</b>.")],
        OP),
    grammar(
        T4B,
        "mustn't vs don't have to / needn't: prohibition vs no obligation",
        "<code>mustn't / can't / be not allowed to</code> = nie wolno · <code>don't have to / don't need to / needn't</code> = nie musisz (ale możesz) · przeszłość: <code>weren't allowed to</code> vs <code>didn't have to / didn't need to</code>",
        ["Polskie „nie musisz” to <b>don't have to</b>, a „nie wolno” to <b>mustn't</b>. To zupełnie różne znaczenia.",
         "<i>You <b>mustn't</b> remove your helmet. It's dangerous.</i> (zakaz) ↔ <i>You <b>don't have to</b> buy a ticket.</i> (nie trzeba, bo za darmo)",
         "<b>needn't</b> + bezokolicznik <b>bez</b> <i>to</i>: <i>You needn't buy a ticket.</i> Natomiast <b>don't need to</b> + <i>to</i>.",
         "W przeszłości: brak obowiązku → <b>didn't have to / didn't need to</b>; zakaz → <b>weren't allowed to / couldn't</b>."],
        "free · optional · if you like → don't have to · dangerous · forbidden → mustn't",
        "Najczęstsza pułapka dla Polaków. Part 4: <i>It isn't necessary to…</i> → <b>don't have to / don't need to</b>; <i>You are not permitted to…</i> → <b>aren't allowed to</b>.",
        [("You <b>mustn't</b> remove your helmet. It's dangerous.", "Nie wolno ci zdejmować kasku. To niebezpieczne."),
         ("You <b>don't have to</b> buy a ticket – the concert is free.", "Nie musisz kupować biletu – koncert jest za darmo."),
         ("You <b>don't need to</b> show your passport at the border, but you <b>need to</b> have some kind of ID.",
          "Na granicy nie musisz pokazywać paszportu, ale musisz mieć jakiś dokument tożsamości.")],
        [("You mustn't come tomorrow if you're busy.", "You don't have to come tomorrow if you're busy.",
          "Chodzi o brak obowiązku („nie musisz”), nie o zakaz."),
         ("You needn't to pay.", "You needn't pay. / You don't need to pay.",
          "<i>needn't</i> + bezokolicznik bez <i>to</i>.")],
        OP),
    grammar(
        T4B,
        "Permission: can / be allowed to (present and past)",
        "teraz: <code>can / am allowed to</code> · <code>can't / am not allowed to</code> · przeszłość: <code>could / was allowed to</code> · <code>couldn't / wasn't allowed to</code>",
        ["Udzielasz zgody: <i>Yes, it's OK, you <b>can</b> go home.</i> Odmawiasz: <i>No, I'm sorry. You <b>can't</b> go home yet.</i>",
         "Opisujesz cudze zasady: <i>I <b>can</b> / <b>I'm allowed to</b> go home now.</i> · <i>I <b>can't</b> / <b>I'm not allowed to</b> go home yet.</i>",
         "Przeszłość: <i>I <b>could</b> / <b>was allowed to</b> go home before 5 pm.</i> Przy jednej konkretnej sytuacji naturalniejsze jest <b>was allowed to</b>.",
         "<b>be allowed to</b> działa we wszystkich czasach, w których <i>can</i> nie ma formy: <i>I've never been allowed to…</i>, <i>You'll be allowed to…</i>"],
        "OK · permission · the rules · let",
        "<i>allow sb to do</i> = <i>let sb do</i>. W Part 4 <i>They let us…</i> → <i>We <b>were allowed to</b>…</i>",
        [("Yes, it's OK, you <b>can</b> go home.", "Tak, w porządku, możesz iść do domu."),
         ("I<b>'m not allowed to</b> go home yet.", "Nie wolno mi jeszcze iść do domu."),
         ("When I was at school, we <b>were allowed to</b> go home before 5 pm.", "Kiedy chodziłem do szkoły, mogliśmy wracać do domu przed 17.")],
        [("I'm not allow to use my phone at work.", "I'm not allowed to use my phone at work.",
          "<i>be allowed to</i> to strona bierna: <b>allowed</b> z <i>-ed</i>."),
         ("Yesterday I could leave early because my boss said so.", "Yesterday I was allowed to leave early.",
          "Jedna konkretna sytuacja → lepiej <b>was allowed to</b>; <i>could</i> mówi o ogólnej zgodzie.")],
        OP),
    grammar(
        T4B,
        "should / ought to: mild obligation and advice",
        "<code>should + bezokolicznik</code> · <code>ought to + bezokolicznik</code> · przeczenie: <code>shouldn't</code>",
        ["Rada albo łagodny obowiązek: <i>I think you <b>should</b> / <b>ought to</b> give the money back.</i>",
         "<b>should</b> jest dużo częstsze. Pytania i przeczenia z <i>ought to</i> są bardzo rzadkie → <i>Should I…?</i>, <i>You shouldn't…</i>",
         "<b>ought</b> zawsze z <b>to</b>; <b>should</b> nigdy z <i>to</i>.",
         "Naturalnie brzmi <i>I <b>don't think</b> you should…</i> zamiast <i>I think you shouldn't…</i>."],
        "I think · It's a good idea · I'd advise you",
        "Part 4: <i>It's a good idea to… / I advise you to…</i> → <b>should / ought to</b>. <i>ought to</i> liczy się jako 2 słowa.",
        [("I think you <b>should</b> give the money back.", "Myślę, że powinieneś oddać te pieniądze."),
         ("You <b>ought to</b> write to them.", "Powinieneś do nich napisać."),
         ("I <b>don't think</b> you <b>should</b> sign it yet.", "Nie sądzę, żebyś powinien to już podpisywać.")],
        [("You should to apologise.", "You should apologise. / You ought to apologise.",
          "Po <i>should</i> bezokolicznik bez <i>to</i>; <i>to</i> ma tylko <i>ought</i>."),
         ("You ought apologise.", "You ought to apologise.",
          "<i>ought</i> bez <i>to</i> nie istnieje.")],
        OP),
    grammar(
        T4B,
        "be supposed to: what the rules or other people expect",
        "<code>am / is / are supposed to + bezokolicznik</code> · <code>was / were supposed to + bezokolicznik</code> (często + <i>but…</i>)",
        ["„Mam / powinienem, bo tak ustalono, tak każą”: <i>I'm supposed to give the money back, but I don't want to.</i>",
         "W przeszłości: plan albo obowiązek, którego <b>nie spełniono</b>: <i>I was supposed to give the money back, but I forgot.</i>",
         "Mówi o oczekiwaniach innych (zasady, umowa), a nie o mojej radzie – dlatego <i>should</i> zamienia się na <i>be supposed to</i>, gdy opisujesz cudzą zasadę.",
         "Wymowa: /səˈpəʊst tə/ – <b>d</b> prawie nie słychać, ale w piśmie musi być."],
        "but I forgot · but I don't want to · the rules say · we were told",
        "Part 4: <i>They advised / told us to…</i> → <i>We <b>were supposed to</b>…</i>; <i>The plan was for me to…</i> → <i>I <b>was supposed to</b>…</i>",
        [("I<b>'m supposed to</b> give the money back, but I don't want to.", "Powinienem oddać te pieniądze, ale nie chcę."),
         ("I <b>was supposed to</b> give the money back, but I forgot.", "Miałem oddać te pieniądze, ale zapomniałem."),
         ("We <b>were supposed to</b> bring strong shoes.", "Mieliśmy przynieść mocne buty.")],
        [("I'm suppose to finish it today.", "I'm supposed to finish it today.",
          "Zawsze <b>supposed</b> z <i>-d</i> – to forma bierna."),
         ("I supposed to call her yesterday.", "I was supposed to call her yesterday.",
          "Bez <i>be</i> (<b>was / were</b>) nie ma tej konstrukcji. <i>I supposed</i> znaczy „przypuszczałem”.")],
        OP),
    grammar(
        T4B,
        "make and let + object + infinitive without to",
        "<code>make + osoba + bezokolicznik bez to</code> = zmusić · <code>let + osoba + bezokolicznik bez to</code> = pozwolić",
        ["<i>They <b>made</b> me <b>pay</b> extra.</i> NIE <i>made me to pay</i>.",
         "<i>They <b>let</b> me <b>come</b> in for free.</i> NIE <i>let me to come</i>.",
         "<b>allow</b> i <b>force</b> wymagają <i>to</i>: <i>They allowed me <b>to</b> come in</i>, <i>They forced me <b>to</b> pay</i>.",
         "<i>let</i> ma tę samą formę w Present, Past i Past Participle: <i>let – let – let</i>."],
        "zmusić → make / force · pozwolić → let / allow",
        "W Part 4 przejście <b>let ↔ allow</b> i <b>make ↔ force</b> to wymiana całej struktury: z <i>to</i> albo bez niego.",
        [("They <b>made</b> me <b>pay</b> extra.", "Kazali mi dopłacić."),
         ("They <b>let</b> me <b>come</b> in for free.", "Wpuścili mnie za darmo."),
         ("My boss <b>made</b> me <b>rewrite</b> the whole script.", "Szef kazał mi przepisać cały skrypt.")],
        [("They made me to pay extra.", "They made me pay extra.",
          "Po <i>make + osoba</i> bezokolicznik bez <i>to</i>."),
         ("They allowed me come in.", "They allowed me to come in. / They let me come in.",
          "<i>allow</i> chce <i>to</i>; bez <i>to</i> działa tylko <i>let</i>.")],
        OP),
    grammar(
        T4B,
        "Passive: be forced to / be made to / be allowed to + to-infinitive",
        "<code>be forced to + bezokolicznik</code> · <code>be made to + bezokolicznik</code> (rzadsze) · <code>be allowed to + bezokolicznik</code>",
        ["Strona bierna, gdy ważniejsza jest osoba zmuszana niż ten, kto zmusza: <i>I <b>was forced to</b> pay extra.</i>",
         "W stronie biernej <i>make</i> odzyskuje <i>to</i>: <i>They made me pay</i> → <i>I <b>was made to</b> pay</i>.",
         "<i>let</i> nie ma strony biernej w tym znaczeniu: <i>They let me come in</i> → <i>I <b>was allowed to</b> come in</i>. NIE <i>I was let come in</i>.",
         "Po wszystkich trzech: <b>to</b> + bezokolicznik."],
        "was / were forced to · was / were allowed to · was / were made to",
        "Typowy KWT: <i>They didn't let me use a dictionary.</i> → <i>I <b>wasn't allowed to use</b> a dictionary.</i>",
        [("I <b>was forced to</b> pay extra.", "Zmuszono mnie do dopłaty."),
         ("I <b>was allowed to</b> come in for free.", "Pozwolono mi wejść za darmo."),
         ("We <b>were made to</b> wait for three hours.", "Kazano nam czekać trzy godziny.")],
        [("I was made pay extra.", "I was made to pay extra.",
          "W stronie biernej po <i>made</i> pojawia się <b>to</b>."),
         ("I was let come in for free.", "I was allowed to come in for free.",
          "Zamiast biernego <i>let</i> → <b>be allowed to</b>.")],
        OP),
]

KWT_4B = [
    # ćwiczenie a
    kwt("You can wear whatever you want.", "NEED", f"You {GAP} a uniform.",
        "don't need to wear", "You don't need to wear a uniform.",
        "Możesz nosić, co chcesz = mundurek nie jest obowiązkowy → <b>don't need to</b>.", "no obligation → don't need to / don't have to",
        "<i>don't</i> to 2 słowa – razem dokładnie 5. Nie <i>mustn't</i> (to byłby zakaz)."),
    kwt("I think you should write to them.", "OUGHT", f"I think you {GAP} to them.",
        "ought to write", "I think you ought to write to them.",
        "<b>should</b> = <b>ought to</b> (rada).", "should do → ought to do",
        "<i>ought</i> zawsze z <b>to</b>."),
    kwt("They made me give them my phone.", "FORCED", f"They {GAP} them my phone.",
        "forced me to give", "They forced me to give them my phone.",
        "<b>make sb do</b> → <b>force sb to do</b>.", "make sb do = force sb to do",
        "Przy <i>force</i> pojawia się <b>to</b>, którego nie ma po <i>make</i>."),
    kwt("They won't let you park there.", "ALLOWED", f"You aren't {GAP} there.",
        "allowed to park", "You aren't allowed to park there.",
        "<b>let sb do</b> → <b>sb is allowed to do</b> (strona bierna).", "not let sb do → sb isn't allowed to do",
        "<i>aren't</i> jest już w zdaniu – w luce tylko <i>allowed to park</i>."),
    kwt("You don't have to stay here.", "CAN", f"{GAP} if you like.",
        "You can go", "You can go if you like.",
        "Nie musisz zostać = możesz iść → <b>can</b> (pozwolenie).", "don't have to stay → can go / leave",
        "Też poprawnie: <i>You can leave</i>. Uwaga na sens: <i>You can stay</i> znaczy coś innego."),
    kwt("They advised us to bring strong shoes.", "SUPPOSED", f"We {GAP} strong shoes.",
        "were supposed to bring", "We were supposed to bring strong shoes.",
        "Ktoś oczekiwał, że coś zrobimy → <b>be supposed to</b>.", "they advised us to do → we were supposed to do",
        "Czas przeszły: <b>were</b>. Nie zgub <i>-d</i> w <i>supposed</i>."),
    kwt("I wasn't allowed to use a dictionary.", "LET", f"They {GAP} a dictionary.",
        "didn't let me use", "They didn't let me use a dictionary.",
        "<b>sb wasn't allowed to do</b> → <b>they didn't let sb do</b>.", "wasn't allowed to do → didn't let me do",
        "Po <i>let me</i> bezokolicznik bez <i>to</i>. <i>didn't</i> = 2 słowa, razem 5."),
    kwt("It was raining so we were forced to stop.", "MADE", f"The rain {GAP}.",
        "made us stop", "The rain made us stop.",
        "Przyczyna staje się podmiotem: <b>X made us do sth</b>.", "we were forced to do → X made us do",
        "W stronie czynnej po <i>made us</i> bez <i>to</i>."),
    # dodatkowe
    kwt("It isn't necessary to book a table.", "HAVE", f"You {GAP} a table.",
        "don't have to book", "You don't have to book a table.",
        "<i>It isn't necessary</i> = brak obowiązku → <b>don't have to</b>.", "it isn't necessary to do → don't have to do",
        "Nie <i>mustn't</i> – to zakaz. <i>don't</i> = 2 słowa."),
    kwt("Visitors are not permitted to take photos inside the museum.", "ALLOWED", f"Visitors {GAP} photos inside the museum.",
        "aren't allowed to take", "Visitors aren't allowed to take photos inside the museum.",
        "<b>be permitted to</b> = <b>be allowed to</b>.", "not permitted to do → not allowed to do",
        "Też poprawnie: <i>are not allowed to take</i> (5 słów)."),
    kwt("My parents made me tidy my room every Saturday.", "MADE", f"I {GAP} my room every Saturday.",
        "was made to tidy", "I was made to tidy my room every Saturday.",
        "Strona bierna od <i>make sb do</i>: <b>sb was made to do</b>.", "made me do → I was made to do",
        "W stronie biernej po <i>made</i> pojawia się <b>to</b>."),
    kwt("It was compulsory for us to wear a tie at school.", "HAD", f"We {GAP} a tie at school.",
        "had to wear", "We had to wear a tie at school.",
        "<i>compulsory</i> = obowiązkowy → <b>have to</b>; w przeszłości <b>had to</b>.", "it was compulsory to do → had to do",
        "<i>must</i> nie ma przeszłej formy."),
    kwt("The plan was for me to call her yesterday, but I forgot.", "SUPPOSED", f"I {GAP} her yesterday, but I forgot.",
        "was supposed to call", "I was supposed to call her yesterday, but I forgot.",
        "Plan, którego nie zrealizowałem → <b>was supposed to</b>.", "the plan was for me to do → I was supposed to do",
        "<i>but I forgot</i> to typowy sygnał tej konstrukcji."),
    kwt("They let us leave work early on Friday.", "ALLOWED", f"We {GAP} work early on Friday.",
        "were allowed to leave", "We were allowed to leave work early on Friday.",
        "<b>let sb do</b> → <b>sb was allowed to do</b>.", "they let us do → we were allowed to do",
        "Nie <i>were let leave</i> – <i>let</i> nie ma takiej strony biernej."),
    kwt("It wasn't necessary for me to buy a ticket.", "NEED", f"I {GAP} a ticket.",
        "didn't need to buy", "I didn't need to buy a ticket.",
        "Brak obowiązku w przeszłości → <b>didn't need to</b>.", "it wasn't necessary to do → didn't need to do",
        "Też poprawnie z HAVE: <i>didn't have to buy</i>, ale tu słowo kluczowe to NEED."),
]

RULES = "Zasada"
OPEN_CLOZE_4B = [
    # ćwiczenie b (rozmowa o zasadach kursu)
    oc(f"({RULES}: All users must change their passwords after first logging in.) Andy: “We {G} to change our password straight away.”",
       "had",
       "Opisujesz cudzą zasadę w przeszłości → <b>had to</b>.", "must (zasada) → had to / needed to (relacja w przeszłości)",
       "Też poprawnie: <b>needed</b>."),
    oc(f"({RULES}: You are not allowed to access the computer system without a new password.) Andy: “They said we {G} access the system without a new one.”",
       "couldn't",
       "Zakaz w relacji z przeszłości: <i>They said we couldn't…</i> Po luce stoi bezokolicznik <i>access</i>, więc nie zmieści się <i>weren't allowed to</i>.",
       "not allowed to → couldn't (jedno słowo + bezokolicznik)",
       "Jedno słowo albo skrót – <i>couldn't</i> liczy się tu jako jeden wyraz w luce."),
    oc(f"({RULES}: You can choose your own password.) Andy: “We were {G} to choose our own passwords.”",
       "allowed",
       "Pozwolenie w przeszłości: <b>were allowed to</b>.", "can (zasada) → was / were allowed to",
       "<i>were</i> i <i>to</i> już są w zdaniu – brakuje tylko <i>allowed</i>."),
    oc(f"({RULES}: Your new password must be at least 20 characters long.) Andy: “We could choose our passwords, but it {G} to contain at least 20 characters.”",
       "had",
       "Obowiązek w przeszłości → <b>had to</b>.", "must → had to",
       "<i>needed</i> też pasuje znaczeniowo; książka podaje <i>had</i>."),
    oc(f"({RULES}: Your password should be easy to remember.) Andy: “It was {G} to be something that's easy to remember.”",
       "supposed",
       "Cudza rada lub oczekiwanie → <b>was supposed to</b>.", "should (zasada) → was supposed to",
       "Uważaj na pisownię: <b>supposed</b> z <i>-d</i>."),
    oc(f"({RULES}: Your password shouldn't be easy to guess.) Andy: “No, it was {G} to be something that's not easy to guess.”",
       "supposed",
       "Znów oczekiwanie z regulaminu → <b>was supposed to</b>.", "shouldn't → was supposed to + not / something that's not…",
       "Przeczenie jest w dalszej części zdania (<i>not easy</i>), więc w luce forma twierdząca."),
    oc(f"({RULES}: You must not tell anyone else your password.) Dan: “So what was it?” Andy: “I {G} tell you!”",
       "can't",
       "Zakaz w teraźniejszości (nadal obowiązuje) → <b>can't</b>.", "must not → can't / am not allowed to",
       "Jedno słowo przed bezokolicznikiem <i>tell</i>: <i>can't</i> (albo <i>mustn't</i>)."),
    oc(f"({RULES}: You must not tell anyone else your password.) Andy: “We're not {G} to tell anyone else!”",
       "allowed",
       "<b>be not allowed to</b> = nie wolno (cudza zasada).", "must not → be not allowed to",
       "Też możliwe: <b>supposed</b> (mniej stanowcze)."),
    # dodatkowe
    oc(f"You don't {G} to show your passport at the border, but you need to have some kind of ID.",
       "need",
       "Brak obowiązku → <b>don't need to</b> / <i>don't have to</i>.", "don't need to = don't have to",
       "Też poprawnie: <b>have</b>."),
    oc(f"The instructor wouldn't {G} us take our helmets off – he said it was too dangerous.",
       "let",
       "Po luce stoi <i>us take</i> (bez <i>to</i>), więc tylko <b>let</b>.", "let + osoba + bezokolicznik bez to",
       "<i>allow</i> nie pasuje, bo wymagałoby <i>us <b>to</b> take</i>."),
    oc(f"Passengers were made {G} wait for three hours before the flight was cancelled.",
       "to",
       "W stronie biernej po <i>made</i> pojawia się <b>to</b>.", "be made to + bezokolicznik",
       "W stronie czynnej: <i>They made passengers wait</i> – bez <i>to</i>."),
    oc(f"I was forced {G} pay extra for my luggage.",
       "to",
       "<b>be forced to</b> + bezokolicznik.", "be forced to do",
       "<i>force</i> zawsze z <i>to</i>, w stronie czynnej i biernej."),
]

TR_4B = [
    tr("Nie musisz przychodzić jutro do biura.", "don't have to",
       "You don't have to come to the office tomorrow.", "You don't need to come / You needn't come to the office tomorrow.",
       ("Brak obowiązku.", "„Nie musisz” = <b>don't have to</b>, nie <i>mustn't</i>."),
       "You mustn't come to the office tomorrow."),
    tr("Nie wolno ci tu parkować.", "mustn't / not allowed to",
       "You mustn't park here.", "You aren't allowed to park here. / You can't park here.",
       ("Zakaz.", "„Nie wolno” = <b>mustn't / can't / aren't allowed to</b>."),
       "You don't have to park here."),
    tr("Wczoraj musiałem zostać dłużej w pracy.", "had to",
       "I had to stay late at work yesterday.", "Yesterday I had to stay late at work.",
       ("Obowiązek w przeszłości.", "<i>must</i> nie ma przeszłej formy → <b>had to</b>."),
       "Yesterday I must stay late at work."),
    tr("Miałem oddać raport w piątek, ale zapomniałem.", "be supposed to",
       "I was supposed to hand in the report on Friday, but I forgot.", "",
       ("Niespełniony plan.", "<b>was supposed to</b> + bezokolicznik; często z <i>but…</i>."),
       "I supposed to give the report on Friday."),
    tr("Szef kazał mi przepisać cały kod.", "make",
       "My boss made me rewrite all the code.", "My boss made me rewrite the whole code.",
       ("make + osoba + bezokolicznik bez to.", "„Kazać komuś” = <b>make sb do</b>."),
       "My boss made me to rewrite all the code."),
    tr("Rodzice nie pozwalali mi grać w gry komputerowe.", "let",
       "My parents didn't let me play computer games.", "My parents wouldn't let me play computer games.",
       ("let + osoba + bezokolicznik bez to.", "Powtarzany zakaz w przeszłości: <i>didn't let</i> albo <i>wouldn't let</i>."),
       "My parents didn't let me to play computer games."),
    tr("Pozwolono nam pracować z domu w piątki.", "be allowed to",
       "We were allowed to work from home on Fridays.", "",
       ("Strona bierna pozwolenia.", "<i>let</i> nie ma tu strony biernej → <b>were allowed to</b>."),
       "We were let to work from home on Fridays."),
    tr("Zmuszono nas do dopłaty.", "be forced to",
       "We were forced to pay extra.", "We were made to pay extra.",
       ("Strona bierna przymusu.", "<b>be forced to / be made to</b> + bezokolicznik z <i>to</i>."),
       "We were made pay extra."),
    tr("Myślę, że powinieneś porozmawiać z kierownikiem.", "should / ought to",
       "I think you should talk to your manager.", "I think you ought to talk to your manager.",
       ("Rada.", "<i>should</i> bez <i>to</i>, <i>ought</i> zawsze z <i>to</i>."),
       "I think you should to talk to your manager."),
    tr("Czy musimy nosić identyfikatory?", "have to",
       "Do we have to wear ID badges?", "Do we need to wear ID badges?",
       ("Pytanie o obowiązek.", "Pytania z <i>must</i> są bardzo rzadkie → <b>Do we have to…?</b>"),
       "Do we must wear ID badges?"),
    tr("Na egzaminie nie można używać słownika.", "not allowed to",
       "You aren't allowed to use a dictionary in the exam.", "You can't use a dictionary in the exam.",
       ("Cudza zasada (regulamin).", "<b>aren't allowed to / can't</b>; <i>mustn't</i> brzmi jak zakaz od mówiącego."),
       "You don't have to use a dictionary in the exam."),
    tr("W podstawówce mogliśmy wychodzić ze szkoły przed piętnastą.", "be allowed to",
       "At primary school we were allowed to leave school before 3 pm.", "At primary school we could leave school before 3 pm.",
       ("Pozwolenie w przeszłości.", "<b>were allowed to / could</b> + bezokolicznik."),
       "At primary school we were allow to leave school before 3 pm."),
    tr("Nie musiałem kupować biletu.", "didn't need to",
       "I didn't need to buy a ticket.", "I didn't have to buy a ticket.",
       ("Brak obowiązku w przeszłości.", "<b>didn't need to / didn't have to</b>; <i>mustn't</i> nie ma przeszłej formy."),
       "I mustn't buy a ticket."),
    tr("Podczas spotkań mamy wyłączać telefony.", "be supposed to",
       "We're supposed to switch off our phones during meetings.", "We have to switch off our phones during meetings.",
       ("Zasada ustalona przez innych.", "<b>be supposed to</b> = tak każą zasady (choć nie wszyscy się stosują)."),
       "We suppose to switch off our phones during meetings."),
    tr("Model nie może mieć dostępu do danych klientów bez zgody.", "be not allowed to",
       "The model isn't allowed to access customer data without permission.", "The model can't access customer data without permission.",
       ("Zakaz z regulaminu.", "<b>isn't allowed to</b> + bezokolicznik; <i>access</i> bez przyimka (<i>access to</i> tylko przy rzeczowniku)."),
       "The model isn't allowed to access to customer data without permission."),
    tr("Kazano nam czekać trzy godziny.", "be made to",
       "We were made to wait for three hours.", "We were forced to wait for three hours.",
       ("Strona bierna od make.", "<i>They made us wait</i> → <b>We were made to wait</b> (wraca <i>to</i>)."),
       "We were made wait for three hours."),
]


OUTPUTS = {
    "fce-grammar-used-to-would-4a-focus.tsv": GRAMMAR_4A,
    "fce-use-of-english-used-to-would-4a-focus.tsv": CHOICE_4A,
    "fce-grammar-obligation-permission-4b.tsv": GRAMMAR_4B,
    "fce-use-of-english-obligation-permission-4b.tsv": KWT_4B + OPEN_CLOZE_4B,
    "fce-use-of-english-obligation-permission-4b-translation.tsv": TR_4B,
}

if __name__ == "__main__":
    for name, rows in OUTPUTS.items():
        write_tsv(name, rows)
