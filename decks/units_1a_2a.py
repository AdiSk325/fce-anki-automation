#!/usr/bin/env python3
"""Talie 2A Expressions with get i 1A Character adjectives (word formation, akcent, wymowa g).

Uruchom z katalogu repo: python decks/units_1a_2a.py
Nadpisuje pliki TSV w output/. Nie zmieniaj pierwszych pól istniejących wierszy –
od nich zależy GUID notatki w Anki (zmiana = nowa karta i utrata historii powtórek).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cardlib import (GAP, examples_block, meaning_fields, sound_g_fields, stress_fields,  # noqa: E402
                     translation_fields, vocab_back, word_formation_fields, write_tsv)

TAGS_2A = "expressions-with-get unit-2a"
TAGS_1A = "character-adjectives unit-1a"


def pv_row(verb, meanings, note, examples, synonyms, extra_tags=""):
    return [verb, meaning_fields(meanings, note), examples_block(examples), synonyms,
            f"fce phrasal-verbs get {TAGS_2A} {extra_tags}".strip()]


def vocab_row(front, pos, ipa, pl, en, examples, note=""):
    return [front, vocab_back(pos, ipa, pl, en, note), examples_block(examples, "example"),
            f"fce vocabulary {TAGS_2A}"]


def tr_row(pl, hint, answer, alt, expl, wrong, tags):
    return [*translation_fields(pl, hint, answer, alt, expl, wrong), "translation",
            f"fce use-of-english translation {TAGS_2A} {tags}".strip()]


def sound_row(word, hard, ipa, pl, rule):
    return [*sound_g_fields(word, hard, ipa, pl, rule), "sound-spelling",
            f"fce use-of-english sound-spelling pronunciation {TAGS_2A}"]


def wf_row(sentence, base, answer, formation, stress, expl, extra_tags=""):
    return [*word_formation_fields(sentence, base, answer, formation, expl, stress), "word-formation",
            f"fce use-of-english word-formation {TAGS_1A} {extra_tags}".strip()]


def stress_row(syllables, stressed, position, ipa, pl, rule):
    return [*stress_fields(syllables, stressed, position, ipa, pl, rule), "word-stress",
            f"fce use-of-english word-stress pronunciation {TAGS_1A}"]


G = GAP

# ---------------------------------------------------------------- 2A: expressions (FCE Phrasal Verbs)
PV = [
    pv_row("get rid of (sth / sb)",
           [("pozbyć się (czegoś / kogoś)", "to throw away or remove something or someone you do not want")],
           "Dopełnienie zawsze <b>na końcu</b>, jak w Type 4: get rid of it (NIE get it rid of). W tekście: <i>a way to get rid of the man running the club</i>.",
           [("I finally <b>got rid of</b> my old sofa.", "W końcu pozbyłem się starej kanapy."),
            ("It's really hard to <b>get rid of</b> bad habits.", "Naprawdę trudno pozbyć się złych nawyków."),
            ("I <b>got rid of</b> some old building materials from my cellar.", "Pozbyłem się starych materiałów budowlanych z piwnicy.")],
           "dispose of, throw away, eliminate", "type-4"),
    pv_row("get (a bit) carried away",
           [("dać się ponieść (emocjom, entuzjazmowi), przesadzić", "to become so excited or involved that you lose control of what you are doing")],
           "Bez dopełnienia (jak Type 1). Często z <i>a bit</i>: <i>We all got a bit carried away.</i> Z przyczyną: <i>get carried away by / with sth</i>.",
           [("We all <b>got a bit carried away</b> and ordered far too much food.", "Wszyscy daliśmy się trochę ponieść i zamówiliśmy o wiele za dużo jedzenia."),
            ("Don't <b>get carried away</b> – we only need a small cake.", "Nie przesadzaj – potrzebujemy tylko małego tortu."),
            ("When I drive my new car on the motorway, I <b>get a bit carried away</b>.", "Kiedy jadę nowym samochodem autostradą, trochę mnie ponosi.")],
           "overdo it, go too far, lose control", "type-1"),
    pv_row("get straight to the point",
           [("przejść od razu do rzeczy", "to say the most important thing immediately and in a direct way")],
           "Stałe wyrażenie, bez dopełnienia. Krócej: <i>get to the point</i>. Przeciwieństwo: <i>beat about the bush</i> = owijać w bawełnę.",
           [("Look, I'll <b>get straight to the point</b>: we need more money.", "Słuchajcie, przejdę od razu do rzeczy: potrzebujemy więcej pieniędzy."),
            ("I haven't got much time, so let's <b>get straight to the point</b>.", "Nie mam dużo czasu, więc przejdźmy od razu do rzeczy.")],
           "be direct, come to the point, cut to the chase"),
    pv_row("get involved (in sth)",
           [("zaangażować się (w coś), włączyć się", "to take part in an activity or become connected with it")],
           "<b>get + past participle</b> (get = become). Z czym: <i>get involved <b>in</b> sth</i>. Stopniowanie: <i>get more and more involved</i>. Przy zmianie „przez lata” – Present Perfect: <i>I've got more involved over the years.</i>",
           [("Now lots of new people have <b>got involved</b> in the club.", "Teraz w klubie zaangażowało się mnóstwo nowych osób."),
            ("I'd like to <b>get more involved in</b> the local community.", "Chciałbym bardziej zaangażować się w życie lokalnej społeczności."),
            ("Over the years, I've <b>got more and more involved in</b> the choir.", "Z biegiem lat coraz bardziej angażuję się w chór.")],
           "participate, take part, engage"),
    pv_row("get on sb's nerves",
           [("działać komuś na nerwy, denerwować kogoś", "to annoy someone, especially by doing something again and again")],
           "<b>sb's</b> zamieniamy na zaimek dzierżawczy: get on <b>my / his / her</b> nerves. Często w Continuous: <i>is really getting on my nerves</i>. Typowa transformacja: <i>It annoys me when…</i> → <i>It gets on my nerves when…</i>",
           [("My brother's really <b>getting on my nerves</b> at the moment.", "Brat naprawdę działa mi teraz na nerwy."),
            ("It <b>gets on my nerves</b> when people talk during a film.", "Denerwuje mnie, kiedy ludzie rozmawiają w trakcie filmu."),
            ("That noise is really <b>getting on my nerves</b>.", "Ten hałas naprawdę działa mi na nerwy.")],
           "annoy, irritate, bother"),
    pv_row("get (sth) across (to sb)",
           [("przekazać, wytłumaczyć coś (tak, żeby ktoś zrozumiał)", "to make someone understand an idea or a message")],
           "<b>Type 2</b> – rozdzielny: get your ideas across / get it across (NIE get across it). Z <b>długim</b> dopełnieniem partykuła (i <i>to sb</i>) idzie przed nim: <i>get across to students the importance of…</i>",
           [("Sometimes it's hard to <b>get across to students</b> the importance of learning a foreign language.", "Czasem trudno przekazać uczniom, jak ważna jest nauka języka obcego."),
            ("It's hard to <b>get across to new employees</b> the complexity of our data.", "Trudno wytłumaczyć nowym pracownikom, jak złożone są nasze dane."),
            ("She's really good at <b>getting her ideas across</b>.", "Świetnie potrafi przekazać swoje pomysły.")],
           "communicate, convey, explain", "type-2"),
    pv_row("get (sb) down",
           [("przygnębiać, dołować kogoś", "to make someone feel sad or depressed")],
           "<b>Type 2</b> – z zaimkiem w środku: it gets <b>me</b> down (NIE gets down me). Podmiotem jest zwykle sytuacja: <i>He won't listen and it's getting me down.</i>",
           [("He just won't listen, and it's <b>getting me down</b>.", "On po prostu nie chce słuchać i to mnie dołuje."),
            ("This rainy weather really <b>gets me down</b>.", "Ta deszczowa pogoda naprawdę mnie przygnębia."),
            ("Don't let one bad mark <b>get you down</b>.", "Nie pozwól, żeby jedna słaba ocena cię zdołowała.")],
           "depress, discourage, sadden", "type-2"),
    pv_row("get through (sth)",
           [("przebrnąć przez coś, zdać, zaliczyć (egzamin, trudny etap)", "to succeed in an exam or deal with a difficult experience until it ends"),
            ("dodzwonić się (get through to sb)", "to manage to talk to someone on the phone")],
           "<b>Type 3</b> – nierozdzielny: get through the exam / get through it (NIE get it through). Dodzwonić się: <i>get through (to sb)</i>, bez dopełnienia albo z <i>to</i>.",
           [("He <b>got through</b> his exams very easily last year.", "W zeszłym roku bardzo łatwo zdał egzaminy."),
            ("After seven years of studying music, I <b>got through</b> my diploma concert.", "Po siedmiu latach nauki muzyki zaliczyłem koncert dyplomowy."),
            ("I tried to call the bank, but I couldn't <b>get through</b>.", "Próbowałem zadzwonić do banku, ale nie mogłem się dodzwonić.")],
           "pass, survive, complete; (phone) reach", "type-3"),
    pv_row("work (sth) out",
           [("wymyślić, znaleźć (sposób, rozwiązanie) – work out a way to do sth", "to find the answer to a problem or a way to do something"),
            ("obliczyć", "to calculate an amount"),
            ("ćwiczyć, trenować (bez dopełnienia)", "to do physical exercise to stay fit")],
           "<b>Type 2</b> – rozdzielny: work out a way / work it out (NIE work out it). Bez dopełnienia = ćwiczyć (Type 1). Bliski synonim z 3A: <i>figure sth out</i>.",
           [("We tried to <b>work out</b> a way to save money.", "Próbowaliśmy wymyślić, jak zaoszczędzić pieniądze."),
            ("I can't <b>work out</b> how much we owe you.", "Nie potrafię obliczyć, ile jesteśmy ci winni."),
            ("I <b>work out</b> at the gym three times a week.", "Ćwiczę na siłowni trzy razy w tygodniu.")],
           "figure out, solve, calculate", "type-2 type-1"),
]


# ---------------------------------------------------------------- 2A: vocabulary (FCE Vocabulary)
VOCAB = [
    vocab_row("straight away", "adverb", "/ˌstreɪt əˈweɪ/", "od razu, natychmiast",
              "immediately; without any delay",
              [("I'll call you back <b>straight away</b>.", "Oddzwonię od razu."),
               ("When I realised my mistake, I apologised <b>straight away</b>.", "Kiedy zorientowałem się, że popełniłem błąd, od razu przeprosiłem.")],
              "W mowie naturalniejsze niż <i>immediately</i>, zwykle na końcu zdania. Z Twojej notatki: znasz je biernie – czas używać aktywnie."),
    vocab_row("all of a sudden", "phrase (adverb)", "/ˌɔːl əv ə ˈsʌdn/", "nagle, ni stąd, ni zowąd",
              "suddenly and unexpectedly",
              [("At the next meeting, <b>all of a sudden</b> he said, 'I'll get straight to the point.'", "Na następnym spotkaniu nagle powiedział: „Przejdę od razu do rzeczy”."),
               ("We were walking home when <b>all of a sudden</b> it started to rain.", "Szliśmy do domu, kiedy nagle zaczęło padać.")],
              "Dobre w opowiadaniu (Writing Part 2 – story, Speaking) jako urozmaicenie dla <i>suddenly</i>."),
    vocab_row("a direct approach", "noun phrase (collocation)", "/ə daɪˈrekt əˈprəʊtʃ/", "bezpośrednie podejście",
              "a way of dealing with something that is honest and goes straight to the main point",
              [("We decided a <b>direct approach</b> would be best.", "Uznaliśmy, że najlepsze będzie bezpośrednie podejście."),
               ("With difficult clients, <b>a direct approach</b> usually works better.", "W przypadku trudnych klientów bezpośrednie podejście zwykle działa lepiej.")],
              "Kolokacje: <i>take / adopt a direct approach</i>, <i>a different / new approach</i>. Po <i>approach</i> przyimek <b>to</b>: <i>an approach to learning</i>."),
]


# ---------------------------------------------------------------- 2A: translation (Use of English)
MINE = "Twoje zdanie z ćwiczenia d."

TR = [
    tr_row("W końcu pozbyłem się starej kanapy.", "get rid of",
           "I finally got rid of my old sofa.", "",
           ("get rid of + dopełnienie na końcu.", "Nic nie wchodzi między <i>get rid of</i> a dopełnienie."),
           "I finally got my old sofa rid of.", "type-4"),
    tr_row("Naprawdę trudno pozbyć się złych nawyków.", "get rid of",
           "It's really hard to get rid of bad habits.", "Bad habits are really hard to get rid of.",
           ("get rid of.", "W wersji alternatywnej <i>of</i> zostaje na końcu zdania – to normalne."),
           "", "type-4"),
    tr_row("Pozbyłem się starych materiałów budowlanych z piwnicy.", "get rid of",
           "I got rid of some old building materials from my cellar.", "I got rid of the old building materials in my cellar.",
           (MINE, "Było prawie dobrze. Dodaj <i>some</i> (część rzeczy) albo <i>the</i> (konkretne rzeczy z piwnicy)."),
           "", "type-4 my-sentences"),
    tr_row("Wszyscy daliśmy się trochę ponieść i zamówiliśmy o wiele za dużo jedzenia.", "get carried away",
           "We all got a bit carried away and ordered far too much food.", "We all got a little carried away and ordered way too much food.",
           ("get carried away.", "Bez dopełnienia; <i>a bit</i> stoi między <i>got</i> a <i>carried away</i>."),
           "We all got carried a bit away…", "type-1"),
    tr_row("Kiedy jadę nowym samochodem autostradą, trochę mnie ponosi.", "get carried away",
           "When I drive my new car on the motorway, I get a bit carried away.", "When I drive my new car on the highway, I get a bit carried away.",
           (MINE, "„Autostrada” = <b>the motorway</b> (BrE) albo <b>the highway</b> (AmE) – jedno słowo i z <i>the</i>. Po zdaniu z <i>When…</i> na początku stawiamy przecinek."),
           "When I drive my new car on a high way I get a bit carried away.", "type-1 my-sentences"),
    tr_row("Nie przesadzaj – potrzebujemy tylko małego tortu.", "get carried away",
           "Don't get carried away – we only need a small cake.", "",
           ("get carried away.", "„Nie przesadzaj” w sensie „nie daj się ponieść” = <i>Don't get carried away</i>."),
           "", "type-1"),
    tr_row("Nie mam dużo czasu, więc przejdę od razu do rzeczy.", "get straight to the point",
           "I haven't got much time, so I'll get straight to the point.", "I don't have much time, so I'll get straight to the point.",
           ("Stałe wyrażenie.", "Decyzja w chwili mówienia → <i>I'll</i>."),
           "", ""),
    tr_row("Przejdź od razu do rzeczy – co się stało?", "get straight to the point",
           "Get straight to the point – what happened?", "Just get to the point – what's happened?",
           ("Stałe wyrażenie.", "Tryb rozkazujący: <i>Get straight to the point!</i>"),
           "", ""),
    tr_row("Z biegiem lat coraz bardziej angażuję się w chór.", "get involved",
           "Over the years, I've got more and more involved in the choir.", "I've become more and more involved in the choir over the years.",
           (MINE, "„Z biegiem lat” = <b>over the years</b> (nie <i>through the years</i>) → zmiana trwająca do teraz, więc <b>Present Perfect</b>. <i>more and more</i> stoi przed <i>involved</i>; bez dodatkowego <i>me</i>."),
           "I get involved in the choir me more and more through the years.", "my-sentences"),
    tr_row("Chciałbym bardziej zaangażować się w życie lokalnej społeczności.", "get involved",
           "I'd like to get more involved in the local community.", "I would like to get more involved in local community life.",
           ("get involved in.", "<i>more</i> przed <i>involved</i>; przyimek <b>in</b>."),
           "I'd like to get involved more to the local community.", ""),
    tr_row("Ten hałas naprawdę działa mi na nerwy.", "get on sb's nerves",
           "That noise is really getting on my nerves.", "This noise really gets on my nerves.",
           ("get on my nerves.", "Continuous podkreśla, że irytuje teraz i ciągle."),
           "That noise is really getting on the nerves.", ""),
    tr_row("Denerwuje mnie, kiedy ludzie rozmawiają w trakcie filmu.", "get on sb's nerves",
           "It gets on my nerves when people talk during a film.", "It really gets on my nerves when people talk during films.",
           ("get on my nerves.", "Ta sama konstrukcja co <i>It annoys me when…</i> – klasyka Part 4."),
           "", ""),
    tr_row("W pracy, kiedy nie rozumiem kolegów podczas dyskusji, czasami działają mi na nerwy.", "get on sb's nerves",
           "At work, when I can't understand my colleagues in discussions, they sometimes get on my nerves.", "In my job, when I can't understand my co-workers during discussions, they sometimes get on my nerves.",
           (MINE, "Poprawnie użyte wyrażenie. Drobiazgi: <i>in discussions</i> (liczba mnoga) i naturalniejsze <i>At work</i>."),
           "", "my-sentences"),
    tr_row("Czasem trudno przekazać uczniom, jak ważna jest nauka języka obcego.", "get across",
           "Sometimes it's hard to get across to students the importance of learning a foreign language.", "Sometimes it's hard to get the importance of learning a foreign language across to students.",
           ("Type 2 – długie dopełnienie.", "Dopełnienie jest długie (<i>the importance of…</i>), więc partykuła i <i>to students</i> idą przed nim – reguła z 3A."),
           "", "type-2 my-sentences"),
    tr_row("Świetnie potrafi przekazać swoje pomysły.", "get across",
           "She's really good at getting her ideas across.", "He's really good at getting his ideas across.",
           ("Type 2 – krótkie dopełnienie.", "Krótkie <i>her ideas</i> naturalnie w środku; po <i>good at</i> forma <b>-ing</b>."),
           "She's really good at get across her ideas.", "type-2"),
    tr_row("Próbowałem mu to wytłumaczyć, ale nie umiałem tego przekazać.", "get across",
           "I tried to explain it to him, but I couldn't get it across.", "I tried to explain it to him, but I couldn't get it across to him.",
           ("Type 2 – zaimek.", "Zaimek <b>it</b> w środku: <i>get it across</i>."),
           "…but I couldn't get across it.", "type-2"),
    tr_row("Ta deszczowa pogoda naprawdę mnie dołuje.", "get down",
           "This rainy weather really gets me down.", "This rainy weather is really getting me down.",
           ("Type 2 – zaimek.", "Zaimek <b>me</b> w środku; podmiotem jest pogoda."),
           "This rainy weather really gets down me.", "type-2"),
    tr_row("Nie pozwól, żeby jedna słaba ocena cię zdołowała.", "get down",
           "Don't let one bad mark get you down.", "Don't let one bad grade get you down.",
           ("Type 2 – zaimek.", "Po <i>let sb</i> bezokolicznik bez <i>to</i>: <i>let … get you down</i>."),
           "Don't let one bad mark to get you down.", "type-2"),
    tr_row("Nie wiem, jak przebrnąłem przez tę rozmowę kwalifikacyjną!", "get through",
           "I don't know how I got through that job interview!", "I've no idea how I got through that interview!",
           ("Type 3.", "Dopełnienie po partykule: <i>got through the interview</i>."),
           "I don't know how I got that job interview through!", "type-3"),
    tr_row("Po siedmiu latach nauki muzyki zaliczyłem koncert dyplomowy.", "get through",
           "After seven years of studying music, I got through my diploma concert.", "After seven years of music studies, I got through my diploma concert.",
           (MINE, "Dobrze użyte <i>got through</i>. Naturalniej: <i>of studying music</i>, <i>my diploma concert</i> i przecinek po wstępie."),
           "After 7 years of music study I got through the diploma concert.", "type-3 my-sentences"),
    tr_row("Próbowałem zadzwonić do banku, ale nie mogłem się dodzwonić.", "get through",
           "I tried to call the bank, but I couldn't get through.", "I tried to phone the bank, but I couldn't get through to them.",
           ("get through = dodzwonić się.", "Bez dopełnienia albo z <i>to sb</i>."),
           "", "type-3"),
    tr_row("Musimy wymyślić, jak zaoszczędzić pieniądze.", "work out",
           "We need to work out a way to save money.", "We need to work out how to save money.",
           ("Type 2.", "Długie dopełnienie (<i>a way to…</i> / <i>how to…</i>) po partykule."),
           "We need to work a way to save money out.", "type-2"),
    tr_row("Nie potrafię obliczyć, ile jesteśmy ci winni.", "work out",
           "I can't work out how much we owe you.", "",
           ("Type 2.", "Dopełnieniem jest pytanie zależne (<i>how much…</i>) – stoi po partykule, w szyku twierdzącym."),
           "I can't work out how much do we owe you.", "type-2"),
    tr_row("Oddzwonię od razu.", "straight away",
           "I'll call you back straight away.", "I'll ring you back straight away.",
           ("straight away.", "Na końcu zdania. Przy okazji <i>call you back</i> – Type 2 z zaimkiem w środku."),
           "I'll straight away call you back.", ""),
    tr_row("Kiedy wróciłem do domu, od razu poszedłem spać.", "straight away",
           "When I got home, I went to bed straight away.", "When I got home, I went straight to bed.",
           ("straight away.", "„Wrócić do domu” = <b>get home</b> – kolejne wyrażenie z <i>get</i> (bez <i>to</i>)."),
           "When I got to home, I went to bed straight away.", ""),
    tr_row("Szliśmy do domu, kiedy nagle zaczęło padać.", "all of a sudden",
           "We were walking home when all of a sudden it started to rain.", "We were walking home when, all of a sudden, it started raining.",
           ("all of a sudden.", "Past Continuous (tło) + Past Simple (nagłe zdarzenie)."),
           "", ""),
    tr_row("Uznaliśmy, że najlepsze będzie bezpośrednie podejście.", "a direct approach",
           "We decided that a direct approach would be best.", "We decided a direct approach would be the best option.",
           ("a direct approach.", "Po <i>decided</i> w przeszłości: <i>would be</i>."),
           "We decided that direct approach would be the best.", ""),
]


# ---------------------------------------------------------------- 2A: hard / soft g
RULE_HARD = "g + spółgłoska albo <b>a, o, u</b> → zwykle twarde /g/."
RULE_SOFT = "g + <b>e, i, y</b> → zwykle miękkie /dʒ/."
SOUND = [
    sound_row("guard", True, "/ɡɑːd/", "strażnik; pilnować", RULE_HARD + " Tu: g + u (u nieme)."),
    sound_row("gymnastics", False, "/dʒɪmˈnæstɪks/", "gimnastyka", RULE_SOFT + " Tu: g + y."),
    sound_row("guide", True, "/ɡaɪd/", "przewodnik", RULE_HARD + " Tu: g + u (u nieme)."),
    sound_row("generous", False, "/ˈdʒenərəs/", "hojny", RULE_SOFT + " Tu: g + e."),
    sound_row("biology", False, "/baɪˈɒlədʒi/", "biologia", RULE_SOFT + " Tu: g + y (końcówka <i>-gy</i>)."),
    sound_row("together", True, "/təˈɡeðə/", "razem", "<b>Wyjątek:</b> g + e, a mimo to twarde /g/ – tak samo <i>get, forget, give, girl, begin</i>."),
    sound_row("religion", False, "/rɪˈlɪdʒən/", "religia", RULE_SOFT + " Tu: g + i."),
    sound_row("agree", True, "/əˈɡriː/", "zgadzać się", RULE_HARD + " Tu: g + r (spółgłoska)."),
    sound_row("dangerous", False, "/ˈdeɪndʒərəs/", "niebezpieczny", RULE_SOFT + " Tu: g + e (jak w <i>danger</i>)."),
    sound_row("forget", True, "/fəˈɡet/", "zapominać", "<b>Wyjątek:</b> g + e, a mimo to twarde /g/ – bo w środku jest <i>get</i>."),
    sound_row("bridge", False, "/brɪdʒ/", "most", "Końcówka <b>-dge</b> to zawsze /dʒ/ (bridge, judge, knowledge)."),
    sound_row("gardener", True, "/ˈɡɑːdnə/", "ogrodnik", RULE_HARD + " Tu: g + a."),
]


# ---------------------------------------------------------------- 1A: word formation (Part 3)
WF = [
    wf_row(f"She's very {G} and wants to run her own company before she's thirty.", "AMBITION", "ambitious",
           "AMBITION → -ion + -ious → AMBITIOUS", "am·<b>BI</b>·tious",
           "Przymiotnik (po <i>very</i>). <b>ambitious</b> = ambitny. Rzeczowniki na <i>-tion</i> często dają przymiotnik na <i>-tious</i> (caution → cautious)."),
    wf_row(f"My history teacher is {G} about the subject, and it shows in every lesson.", "PASSION", "passionate",
           "PASSION → + -ate → PASSIONATE", "<b>PAS</b>·sion·ate",
           "Przymiotnik (po <i>is</i>, przed <i>about</i>). <b>passionate about sth</b> = pełen pasji do czegoś."),
    wf_row(f"The shop gives special discounts to reward customer {G}.", "LOYAL", "loyalty",
           "LOYAL → + -ty → LOYALTY", "<b>LOY</b>·al·ty",
           "Rzeczownik (po <i>customer</i>). <b>customer loyalty</b> = lojalność klientów."),
    wf_row(f"His {G} made it very difficult for him to work in a team.", "ARROGANT", "arrogance",
           "ARROGANT → -ant → -ance → ARROGANCE", "<b>AR</b>·ro·gance",
           "Rzeczownik (po <i>His</i>). Przymiotniki na <i>-ant</i> dają rzeczowniki na <i>-ance</i> (important → importance)."),
    wf_row(f"Despite all the problems, the manager remained {G} that the project would succeed.", "OPTIMIST", "optimistic",
           "OPTIMIST → + -ic → OPTIMISTIC", "op·ti·<b>MIS</b>·tic",
           "Przymiotnik (po <i>remained</i>). Końcówka <i>-ic</i> przesuwa akcent: <b>OP</b>timist → opti<b>MIS</b>tic."),
    wf_row(f"Don't be so {G} – I'm sure you'll pass the exam.", "PESSIMIST", "pessimistic",
           "PESSIMIST → + -ic → PESSIMISTIC", "pes·si·<b>MIS</b>·tic",
           "Przymiotnik (po <i>be so</i>). <b>pessimistic</b> = pesymistyczny – przeciwieństwo <i>optimistic</i>."),
    wf_row(f"It took great {G} to finish the marathon with an injured knee.", "DETERMINE", "determination",
           "DETERMINE → -e + -ation → DETERMINATION", "de·ter·mi·<b>NA</b>·tion",
           "Rzeczownik (po <i>great</i>). <b>determination</b> = determinacja. Przed <i>-tion</i> akcent zawsze na sylabie tuż przed końcówką."),
    wf_row(f"She was {G} to pass the exam, so she studied every evening.", "DETERMINE", "determined",
           "DETERMINE → + -d → DETERMINED", "de·<b>TER</b>·mined",
           "Przymiotnik: <b>be determined to do sth</b> = być zdeterminowanym, żeby coś zrobić (jak w podręczniku: <i>I'm determined to become a millionaire</i>)."),
    wf_row(f"Speaking in public regularly gave him much more {G}.", "CONFIDENT", "confidence",
           "CONFIDENT → -ent → -ence → CONFIDENCE", "<b>CON</b>·fi·dence",
           "Rzeczownik (po <i>more</i>). Przymiotniki na <i>-ent</i> dają rzeczowniki na <i>-ence</i>. Z przedrostkiem: <i>self-confident → self-confidence</i>."),
    wf_row(f"Be careful what you say – she's very {G} to criticism.", "SENSE", "sensitive",
           "SENSE → -e + -itive → SENSITIVE", "<b>SEN</b>·si·tive",
           "Przymiotnik: <b>sensitive to sth</b> = wrażliwy na coś. Uwaga na pułapkę: <i>sensible</i> znaczy „rozsądny”."),
    wf_row(f"It would be {G} to book the tickets early, as they sell out fast.", "SENSE", "sensible",
           "SENSE → -e + -ible → SENSIBLE", "<b>SEN</b>·si·ble",
           "Przymiotnik: <b>sensible</b> = rozsądny (NIE „sensowny/wrażliwy”). Pułapka Part 3: z SENSE powstają <i>sensitive</i> i <i>sensible</i> – decyduje sens zdania."),
    wf_row(f"It was very {G} of him to laugh at her mistake.", "SENSITIVE", "insensitive",
           "SENSITIVE → in- + SENSITIVE → INSENSITIVE", "in·<b>SEN</b>·si·tive",
           "Sens zdania jest negatywny, więc potrzebny przedrostek przeczący <b>in-</b>. <i>It was insensitive of him</i> = to było z jego strony nietaktowne."),
    wf_row(f"Her grandmother has always been a great source of {G} for her.", "INSPIRE", "inspiration",
           "INSPIRE → -e + -ation → INSPIRATION", "in·spi·<b>RA</b>·tion",
           "Rzeczownik (po <i>source of</i>). Akcent się przesuwa: in<b>SPIRE</b> → inspi<b>RA</b>tion. Przymiotnik: <i>inspiring</i>."),
    wf_row(f"He is one of the most {G} writers of his generation.", "INFLUENCE", "influential",
           "INFLUENCE → -ce + -tial → INFLUENTIAL", "in·flu·<b>EN</b>·tial",
           "Przymiotnik (po <i>the most</i>). <b>influential</b> = wpływowy. Akcent się przesuwa: <b>IN</b>fluence → influ<b>EN</b>tial."),
    wf_row(f"Plastic waste is one of the most serious {G} problems today.", "ENVIRONMENT", "environmental",
           "ENVIRONMENT → + -al → ENVIRONMENTAL", "en·vi·ron·<b>MEN</b>·tal",
           "Przymiotnik przed rzeczownikiem <i>problems</i>. Akcent się przesuwa: en<b>VI</b>ronment → environ<b>MEN</b>tal."),
    wf_row(f"She is a highly {G} scientist, and people listen to her opinion.", "RESPECT", "respected",
           "RESPECT → + -ed → RESPECTED", "re·<b>SPEC</b>·ted",
           "<b>respected</b> = szanowany (przez innych). Nie myl z <i>respectful</i> = pełen szacunku (dla innych)."),
    wf_row(f"He lacks {G} and never finishes what he starts.", "MOTIVATE", "motivation",
           "MOTIVATE → -e + -ion → MOTIVATION", "mo·ti·<b>VA</b>·tion",
           "Rzeczownik (po <i>lacks</i>). Znów <i>-tion</i> → akcent na sylabie przed końcówką."),
]


# ---------------------------------------------------------------- 1A: word stress
SUFFIX = "Przed końcówkami <b>-ic, -tion, -ial, -ious</b> akcent pada na sylabę tuż przed końcówką."
STRESS = [
    stress_row(["op", "ti", "mis", "tic"], 2, 3, "/ˌɒptɪˈmɪstɪk/", "optymistyczny", SUFFIX + " Tu: -ic."),
    stress_row(["in", "spir", "ing"], 1, 2, "/ɪnˈspaɪərɪŋ/", "inspirujący", "Końcówka <b>-ing</b> nie zmienia akcentu czasownika: in<b>SPIRE</b> → in<b>SPIR</b>ing."),
    stress_row(["ar", "ro", "gant"], 0, 1, "/ˈærəɡənt/", "arogancki", "Wiele trzysylabowych przymiotników ma akcent na 1. sylabie (<b>AR</b>rogant, <b>SEN</b>sitive, <b>PAS</b>sionate)."),
    stress_row(["am", "bi", "tious"], 1, 2, "/æmˈbɪʃəs/", "ambitny", SUFFIX + " Tu: -ious."),
    stress_row(["pas", "sion", "ate"], 0, 1, "/ˈpæʃənət/", "pełen pasji", "Akcent jak w rzeczowniku <b>PAS</b>sion – końcówka <i>-ate</i> go nie przesuwa."),
    stress_row(["self", "con", "fi", "dent"], 1, 2, "/ˌselfˈkɒnfɪdənt/", "pewny siebie", "W złożeniach z <i>self-</i> główny akcent pada na drugi człon: self-<b>CON</b>fident."),
    stress_row(["sen", "si", "tive"], 0, 1, "/ˈsensətɪv/", "wrażliwy", "Akcent jak w <b>SENSE</b> – końcówka <i>-itive</i> go nie przesuwa."),
    stress_row(["de", "ter", "mined"], 1, 2, "/dɪˈtɜːmɪnd/", "zdeterminowany", "Akcent jak w czasowniku de<b>TER</b>mine. Uwaga: <i>-mined</i> to jedna sylaba /mɪnd/."),
    stress_row(["de", "ter", "mi", "na", "tion"], 3, 4, "/dɪˌtɜːmɪˈneɪʃn/", "determinacja", SUFFIX + " Tu: -tion – akcent przesuwa się z de<b>TER</b>mine."),
    stress_row(["pes", "si", "mis", "tic"], 2, 3, "/ˌpesɪˈmɪstɪk/", "pesymistyczny", SUFFIX + " Tu: -ic."),
    stress_row(["en", "vi", "ron", "ment"], 1, 2, "/ɪnˈvaɪrənmənt/", "środowisko", "Końcówka <i>-ment</i> nie jest akcentowana; akcent na 2. sylabie: en<b>VI</b>ronment."),
    stress_row(["en", "vi", "ron", "men", "tal"], 3, 4, "/ɪnˌvaɪrənˈmentl/", "środowiskowy, ekologiczny", "Po dodaniu <b>-al</b> akcent przesuwa się na <i>-men-</i>: environ<b>MEN</b>tal."),
    stress_row(["in", "flu", "en", "tial"], 2, 3, "/ˌɪnfluˈenʃl/", "wpływowy", SUFFIX + " Tu: -ial – akcent przesuwa się z <b>IN</b>fluence."),
    stress_row(["te", "le", "vi", "sion"], 0, 1, "/ˈtelɪvɪʒn/", "telewizja", "<b>Wyjątek:</b> mimo końcówki <i>-sion</i> akcent zwykle pada na 1. sylabę: <b>TE</b>levision (por. de<b>CI</b>sion)."),
]


OUTPUTS = {
    "fce-phrasal-verbs-expressions-with-get-2a.tsv": PV,
    "fce-vocabulary-expressions-with-get-2a.tsv": VOCAB,
    "fce-use-of-english-expressions-with-get-2a-translation.tsv": TR,
    "fce-use-of-english-sound-spelling-g-2a.tsv": SOUND,
    "fce-use-of-english-word-formation-character-1a.tsv": WF,
    "fce-use-of-english-word-stress-1a.tsv": STRESS,
}

if __name__ == "__main__":
    for name, rows in OUTPUTS.items():
        write_tsv(name, rows)
