#!/usr/bin/env python3
"""Talia 3A Reading – Famous athletes (unit 3, ćwiczenie 5): frazy zaznaczone w tekstach
o Mike'u Weirze, Chrisie Froomie i Marii Szarapowej, plus *a packed schedule* z notatki.

Uruchom z katalogu repo: python decks/athletes_3a.py
Nadpisuje pliki TSV w output/. Nie zmieniaj pierwszych pól istniejących wierszy –
od nich zależy GUID notatki w Anki (zmiana = nowa karta i utrata historii powtórek).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cardlib import (colloc_translation, examples_block, grammar_explanation,  # noqa: E402
                     meaning_fields, mistakes_block, open_cloze_fields, translation_fields,
                     write_tsv)

T = "athletes-reading unit-3a"
DP = "dependent-prepositions"


def colloc(item, pl, en, examples, ctype, note="", extra=""):
    return [item, colloc_translation(pl, en, note), examples_block(examples, "example"), ctype,
            f"fce collocations {ctype.replace('+', '-')} {T} {extra}".strip()]


def grammar(rule, formula, usage, signal, tip, examples, mistakes, extra=""):
    return [rule, grammar_explanation(formula, usage, tip, signal=signal), examples_block(examples),
            mistakes_block(mistakes), f"fce grammar {T} {extra}".strip()]


def pv(verb, meanings, note, examples, synonyms, base, extra=""):
    return [verb, meaning_fields(meanings, note), examples_block(examples), synonyms,
            f"fce phrasal-verbs {base} {T} {extra}".strip()]


def oc(sentence, answer, why, rule, tip, extra=""):
    return [*open_cloze_fields(sentence, answer, why, rule, tip), "open-cloze",
            f"fce use-of-english open-cloze {T} {extra}".strip()]


def tr(pl, hint, answer, alt, expl, wrong, extra=""):
    return [*translation_fields(pl, hint, answer, alt, expl, wrong), "translation",
            f"fce use-of-english translation {T} {extra}".strip()]


# ---------------------------------------------------------------- Collocations
COLLOC = [
    colloc("give sb a (huge) competitive advantage over sb",
           "dawać komuś (ogromną) przewagę nad kimś",
           "to put somebody in a better position than the people they compete against",
           [("'Super-vision' <b>gives them a huge competitive advantage over</b> players with normal eyesight.",
             "„Superwzrok” daje im ogromną przewagę nad zawodnikami z normalnym wzrokiem."),
            ("Speaking three languages <b>gave her a real advantage over</b> the other candidates.",
             "Znajomość trzech języków dała jej realną przewagę nad innymi kandydatami.")],
           "verb+noun",
           "Przewaga <b>over</b> kimś, nigdy <i>above</i> ani <i>than</i>. Inne czasowniki w tym samym schemacie: <b>have / gain / get an advantage over sb</b>. Odwrotnie: <b>be at a disadvantage</b> (być w gorszej sytuacji).",
           DP),
    colloc("be well known for sth",
           "być dobrze znanym z czegoś, słynąć z czegoś",
           "to be famous because of a particular quality, skill or achievement",
           [("Chris Froome <b>is well known for</b> his outstanding performance in international races.",
             "Chris Froome jest dobrze znany ze świetnych występów w wyścigach międzynarodowych."),
            ("This region <b>is well known for</b> its wine.", "Ten region słynie ze swoich win.")],
           "adj+preposition",
           "<b>known for</b> + to, z czego słyniesz; <b>known as</b> + kim albo czym ktoś jest (<i>He is known as 'Froomey'</i>). Kalka <i>known from</i> jest błędem. Mocniejsze warianty: <b>widely known</b>, <b>world-famous</b>.",
           DP),
    colloc("be awarded sth",
           "otrzymać coś (medal, nagrodę, stypendium)",
           "to be given a prize or an official payment, usually after a decision by a jury or a committee",
           [("At the 2016 Olympics <b>he was awarded</b> a bronze medal.", "Na igrzyskach w 2016 roku otrzymał brązowy medal."),
            ("She <b>was awarded</b> a scholarship to study in Canada.", "Przyznano jej stypendium na studia w Kanadzie.")],
           "verb+noun",
           "<i>award sb sth</i> → w stronie biernej osoba jest podmiotem: <b>He was awarded a medal</b>, NIE <i>he was awarded with a medal</i>. Z <i>with</i> łączy się inny czasownik: <b>present sb with sth</b>. Rzeczownik <b>an award</b> = nagroda.",
           "passive"),
    colloc("suffer from sth",
           "cierpieć na coś, zmagać się z czymś",
           "to be badly affected by an illness or a problem, usually over a long period",
           [("Froome <b>suffers from</b> asthma, which is a common problem among racing cyclists.",
             "Froome cierpi na astmę, która jest częstym problemem wśród kolarzy wyścigowych."),
            ("Many students <b>suffer from</b> stress before exams.", "Wielu uczniów zmaga się ze stresem przed egzaminami.")],
           "verb+preposition",
           "Z <b>from</b> przy stanie przewlekłym: <i>suffer from asthma / depression / back pain</i>. Jednorazowe zdarzenie bez przyimka: <i>suffer a broken leg</i>, <i>suffer a defeat</i>. Po polsku „cierpieć NA”, po angielsku zawsze <b>from</b>.",
           DP),
    colloc("on the advice of sb",
           "za radą kogoś, zgodnie z czyjąś radą",
           "because somebody with knowledge or authority told you to do it",
           [("Froome claimed he took the medication <b>on the advice of</b> his doctor.",
             "Froome twierdził, że wziął lek za radą swojego lekarza."),
            ("<b>On the advice of</b> her coach, she pulled out of the race.", "Za radą trenerki wycofała się z wyścigu.")],
           "preposition+noun",
           "Równie dobrze: <b>on sb's advice</b> (<i>on his doctor's advice</i>). Przyimek <b>on</b>, nie <i>after</i> ani <i>by</i>. <b>advice</b> jest niepoliczalne: <i>a piece of advice</i>, <i>some advice</i> – NIE <i>an advice</i>, <i>advices</i>. Czasownik przez <b>s</b>: <b>advise</b> /ədˈvaɪz/.",
           DP),
    colloc("drop the case against sb",
           "wycofać / umorzyć sprawę przeciwko komuś",
           "to decide to stop a legal or official investigation against somebody",
           [("After an investigation, <b>the case against him was dropped</b>.", "Po dochodzeniu sprawę przeciwko niemu umorzono."),
            ("The police <b>dropped the case against</b> the two men for lack of evidence.",
             "Policja umorzyła sprawę przeciwko obu mężczyznom z braku dowodów.")],
           "verb+noun",
           "Najczęściej w stronie biernej: <b>the case was dropped</b>. Ten sam schemat: <b>drop the charges</b> (wycofać zarzuty). Sprawa <b>against</b> kimś. Nie myl z <i>the case</i> = walizka, przypadek.",
           DP),
    colloc("become a household name",
           "stać się powszechnie znanym, zyskać sławę w każdym domu",
           "to become so famous that almost everybody knows the name",
           [("Maria Sharapova <b>has become a household name</b>, known even to people who don't follow tennis.",
             "Maria Szarapowa stała się powszechnie znana – kojarzą ją nawet ludzie, którzy nie śledzą tenisa."),
            ("The app <b>became a household name</b> in less than a year.", "Aplikacja stała się powszechnie znana w niecały rok.")],
           "verb+noun",
           "Dosłownie „nazwisko domowe”, czyli znane w każdym domu – o ludziach i o markach. NIE <i>a home name</i>. Bliskie znaczeniowo: <b>be a big name</b>, <b>make a name for yourself</b> (wyrobić sobie nazwisko).",
           "idiom"),
    colloc("be free of / from sth",
           "być wolnym od czegoś, obyć się bez czegoś",
           "to not have or not be affected by something unpleasant",
           [("Her professional career <b>has not been free of</b> controversy.", "Jej kariera zawodowa nie obyła się bez kontrowersji."),
            ("For the first time in months he was completely <b>free from</b> pain.", "Po raz pierwszy od miesięcy był zupełnie wolny od bólu.")],
           "adj+preposition",
           "<b>free of</b> i <b>free from</b> są tu wymienne. W tekście zdanie jest przeczące i to celowa litota: <i>has not been free of controversy</i> = „bywało kontrowersyjnie”. Taki ostrożny ton jest bardzo przydatny w essayu. <b>controversy</b> /ˈkɒntrəvɜːsi/ jest w tym znaczeniu niepoliczalne.",
           DP),
    colloc("be banned from doing sth",
           "mieć zakaz robienia czegoś, zostać zawieszonym",
           "to be officially stopped from doing something",
           [("Sharapova <b>was banned from playing</b> for two years after a drug test found meldonium.",
             "Szarapowa dostała dwuletni zakaz gry po tym, jak test antydopingowy wykrył meldonium."),
            ("He <b>was banned from driving</b> for six months.", "Dostał półroczny zakaz prowadzenia pojazdów.")],
           "verb+preposition",
           "<i>ban sb from doing sth</i> → strona bierna <b>be banned from doing sth</b>. Po <b>from</b> zawsze <b>-ing</b>, NIGDY bezokolicznik (<i>banned to play</i> ❌). Rzeczownik: <b>a two-year ban</b>; przymiotnik: <b>a banned substance</b> (środek zabroniony).",
           DP),
    colloc("cause a widespread public outcry",
           "wywołać powszechne oburzenie opinii publicznej",
           "to make a lot of people publicly express anger about a decision or event",
           [("The ruling <b>caused a widespread public outcry</b> and her ban was later reduced.",
             "Decyzja wywołała powszechne oburzenie opinii publicznej i zakaz później skrócono."),
            ("The plan to close the hospital <b>caused a public outcry</b>.", "Plan zamknięcia szpitala wywołał publiczne oburzenie.")],
           "verb+noun",
           "<b>an outcry</b> /ˈaʊtkraɪ/ = głośny protest, krzyk oburzenia. Zamiennie: <b>spark / provoke / lead to an outcry</b>. <b>widespread</b> = szeroko rozpowszechniony; jedno słowo, nie zamienia się na <i>wide</i>."),
    colloc("a packed schedule",
           "napięty, wypełniony po brzegi grafik",
           "a timetable with very little free time in it",
           [("I can't take on anything else this month – I've got <b>a packed schedule</b>.",
             "Nie wezmę w tym miesiącu nic więcej – mam napięty grafik."),
            ("Her day was <b>packed with</b> meetings and training sessions.", "Jej dzień był wypełniony spotkaniami i treningami.")],
           "adj+noun",
           "Od <i>pack</i> = pakować: grafik „zapakowany” po brzegi. Pełna wersja: <b>packed with activities / meetings</b>. Podobne: <b>a busy / tight schedule</b>. Wymowa <b>schedule</b>: BrE /ˈʃedjuːl/, AmE /ˈskedʒuːl/. Przydatne też: <b>behind schedule</b> (z opóźnieniem), <b>ahead of schedule</b> (przed czasem)."),
]


# ---------------------------------------------------------------- Phrasal verbs
PHRASAL = [
    pv("go on to do sth",
       [("następnie coś zrobić, przejść do kolejnego osiągnięcia",
         "to do something after finishing something else, often something bigger or more important")],
       "Type 1 (nierozdzielny) + bezokolicznik z <b>to</b>. Uwaga na parę: <b>go on to do sth</b> = skończyć jedno i zrobić coś nowego; <b>go on doing sth</b> = robić dalej to samo, nie przerywać. <i>After the operation he went on to win</i> (wygrał potem) ≠ <i>he went on winning</i> (wygrywał dalej).",
       [("After the operation, he <b>went on to win</b> a series of top golfing championships.",
         "Po operacji wygrał następnie serię najważniejszych turniejów golfowych."),
        ("She studied medicine and <b>went on to become</b> a surgeon.", "Studiowała medycynę, a potem została chirurgiem."),
        ("He ignored the pain and <b>went on playing</b> until the end of the match.",
         "Zignorował ból i grał dalej do końca meczu.")],
       "later + verb; proceed to do sth; (≠ go on doing sth = continue)",
       "go", "type-1"),
]


# ---------------------------------------------------------------- Grammar
GRAMMAR = [
    grammar(
        "the only / the first / the last + noun + (ever) to + infinitive",
        "<code>the only / first / last / best + rzeczownik + (ever) + to + bezokolicznik</code>",
        ["Po <b>only</b>, <b>first</b>, <b>last</b>, <b>next</b> i po stopniu najwyższym bezokolicznik z <b>to</b> zastępuje całe zdanie względne.",
         "<i>He is the only Canadian player <b>who has ever won</b> a major championship.</i> = <i>He is the only Canadian player <b>ever to win</b> a major championship.</i>",
         "<b>ever</b> stoi przed <i>to</i> i wzmacnia „w ogóle, kiedykolwiek”.",
         "Podmiotem bezokolicznika jest osoba z rzeczownika – konstrukcja działa tylko wtedy, gdy to ona wykonuje czynność."],
        "only · first · last · next · the best · the youngest",
        "Krótsza i bardziej formalna niż zdanie względne, więc podnosi ocenę za Language w Writing. W Part 4 bywa parafrazą zdania z <i>who was the first person that…</i>",
        [("Mike Weir is <b>the only</b> Canadian player <b>ever to win</b> a major world championship.",
          "Mike Weir jest jedynym Kanadyjczykiem, który kiedykolwiek wygrał wielkie mistrzostwa świata."),
         ("She was <b>the first woman to run</b> the marathon in under two and a half hours.",
          "Była pierwszą kobietą, która przebiegła maraton poniżej dwóch i pół godziny."),
         ("He was <b>the youngest player ever to score</b> for the club.", "Był najmłodszym zawodnikiem, który kiedykolwiek strzelił gola dla klubu.")],
        [("He is the only Canadian player ever winning a major championship.",
          "He is the only Canadian player ever to win a major championship.",
          "Po <i>only / first / last</i> idzie bezokolicznik z <b>to</b>, nie forma <i>-ing</i>."),
         ("She was the first woman who run the marathon in under two hours.",
          "She was the first woman to run the marathon in under two hours.",
          "Albo pełne zdanie względne z poprawnym czasem (<i>who ran</i>), albo – krócej i lepiej – bezokolicznik.")],
        "infinitive"),
    grammar(
        "Passive with two objects: he was awarded a medal",
        "<code>award / give / offer / send / tell / show + sb + sth</code> → <code>sb + be + imiesłów bierny + sth</code>",
        ["Czasowniki z dwoma dopełnieniami tworzą stronę bierną najczęściej od <b>osoby</b>: <i>They awarded him a medal</i> → <b>He was awarded a medal</b>.",
         "Rzecz zostaje po czasowniku i nie bierze żadnego przyimka: <b>was awarded a medal</b>, NIE <i>was awarded with a medal</i>.",
         "Druga, rzadsza możliwość to strona bierna od rzeczy – wtedy osoba potrzebuje <b>to</b>: <i>A medal was awarded <b>to</b> him</i>.",
         "W tekście o Froomie są obie konstrukcje: <i>he was awarded a bronze medal</i> i <i>he was given a blood test</i>."],
        "award · give · offer · send · tell · show · pay · promise",
        "To jeden z najczęstszych schematów w Part 4. Typowa parafraza: <i>The club gave him a contract.</i> → <i>He <b>was given</b> a contract by the club.</i>",
        [("At the 2016 Olympics, <b>he was awarded</b> a bronze medal.", "Na igrzyskach w 2016 roku otrzymał brązowy medal."),
         ("This caused problems when <b>he was given</b> a blood test after a win.",
          "To wywołało problemy, kiedy po zwycięstwie zrobiono mu badanie krwi."),
         ("We <b>were offered</b> a discount because the order was late.", "Zaproponowano nam zniżkę, bo zamówienie się opóźniło.")],
        [("He was awarded with a bronze medal.", "He was awarded a bronze medal.",
          "Po <i>be awarded</i> rzecz idzie wprost, bez przyimka. Z <i>with</i> łączy się <b>present sb with sth</b>."),
         ("A bronze medal was awarded him.", "A bronze medal was awarded to him.",
          "Jeśli podmiotem jest rzecz, osoba musi mieć <b>to</b>.")],
        "passive"),
]


# ---------------------------------------------------------------- Open cloze
OPEN_CLOZE = [
    oc("Chris Froome is well known <b>______</b> his outstanding performance in international races.", "for",
       "<b>be well known for sth</b> = słynąć z czegoś.",
       "known <b>for</b> + to, z czego słyniesz; known <b>as</b> + kim ktoś jest.",
       "Kalka z polskiego „znany Z” podpowiada <i>from</i> – to zawsze błąd.", DP),
    oc("Froome suffers <b>______</b> asthma, which is a common problem among racing cyclists.", "from",
       "<b>suffer from sth</b> = cierpieć na coś (stan przewlekły).",
       "suffer <b>from</b> + choroba; bez przyimka przy jednorazowym zdarzeniu: <i>suffer a defeat</i>.",
       "Po polsku „cierpieć NA astmę”, po angielsku <b>from</b>.", DP),
    oc("He claimed he took the medication on the advice <b>______</b> his doctor.", "of",
       "<b>on the advice of sb</b> = za czyjąś radą.",
       "on the advice <b>of</b> sb = on sb's advice.",
       "Cała fraza jest stała: zaczyna się od <b>on</b>, kończy na <b>of</b>.", DP),
    oc("After an investigation, the case <b>______</b> him was dropped.", "against",
       "<b>the case against sb</b> = sprawa przeciwko komuś.",
       "case / charges / evidence <b>against</b> sb.",
       "<i>Drop</i> znaczy tu „umorzyć”, nie „upuścić”.", DP),
    oc("Sharapova was banned <b>______</b> playing for two years after a failed drug test.", "from",
       "<b>be banned from doing sth</b> = mieć zakaz robienia czegoś.",
       "ban sb <b>from</b> doing sth → be banned <b>from</b> doing sth.",
       "Po <i>from</i> zawsze <b>-ing</b>, nigdy bezokolicznik.", DP),
    oc("Her professional career has not been free <b>______</b> controversy.", "of",
       "<b>be free of / from sth</b> = być wolnym od czegoś.",
       "free <b>of</b> = free <b>from</b> – oba poprawne.",
       "Przeczenie <i>has not been free of…</i> to grzeczny sposób powiedzenia „bywało burzliwie”.", DP),
    oc("'Super-vision' gives them a huge competitive advantage <b>______</b> players with normal eyesight.", "over",
       "<b>an advantage over sb</b> = przewaga nad kimś.",
       "have / gain / give sb an advantage <b>over</b> sb.",
       "Nigdy <i>above</i> ani <i>than</i> – <i>than</i> idzie tylko po stopniu wyższym.", DP),
    oc("After the operation, he went <b>______</b> to win a series of top golfing championships.", "on",
       "<b>go on to do sth</b> = następnie coś zrobić.",
       "go <b>on</b> + <b>to</b> + bezokolicznik = kolejne osiągnięcie; go <b>on</b> + <b>-ing</b> = robić dalej to samo.",
       "Luka sprawdza partykułę czasownika wielowyrazowego – najpierw rozpoznaj cały czasownik, potem wstaw brakujący element."),
]


# ---------------------------------------------------------------- Translations
TR = [
    tr("Jest jedynym Kanadyjczykiem, który kiedykolwiek wygrał wielkie mistrzostwa świata.",
       "the only … ever to",
       "He is the only Canadian ever to win a major world championship.",
       "He is the only Canadian player who has ever won a major world championship.",
       ("the only + rzeczownik + ever to + bezokolicznik.",
        "Bezokolicznik zastępuje zdanie względne; <i>ever</i> stoi przed <b>to</b>."),
       "He is the only Canadian ever winning a major world championship.", "infinitive"),
    tr("Po operacji wygrał następnie serię najważniejszych turniejów golfowych.", "go on to",
       "After the operation, he went on to win a series of top golfing championships.",
       "After the operation, he went on to win a number of major golf championships.",
       ("go on <b>to</b> + bezokolicznik.",
        "<i>went on winning</i> znaczyłoby „wygrywał dalej”, a nie „potem wygrał”."),
       "After the operation, he went on winning a series of top golfing championships."),
    tr("To daje im ogromną przewagę nad zawodnikami z normalnym wzrokiem.", "advantage over",
       "That gives them a huge competitive advantage over players with normal eyesight.",
       "It gives them a huge advantage over players who have normal eyesight.",
       ("an advantage <b>over</b> sb.", "Przewaga jest <i>over</i>, nigdy <i>above</i>."),
       "That gives them a huge competitive advantage above players with normal eyesight.", DP),
    tr("Jest dobrze znany ze swoich występów w wyścigach międzynarodowych.", "well known for",
       "He is well known for his performances in international races.",
       "He is well known for the way he performs in international races.",
       ("known <b>for</b> sth.", "<i>known from</i> to kalka z polskiego „znany z”."),
       "He is well known from his performances in international races.", DP),
    tr("Na igrzyskach w 2016 roku otrzymał brązowy medal.", "be awarded",
       "At the 2016 Olympics, he was awarded a bronze medal.",
       "He was awarded a bronze medal at the 2016 Olympic Games.",
       ("be awarded + rzecz, bez przyimka.", "Nazwy igrzysk z przedimkiem: <b>the</b> Olympics, <b>the</b> Olympic Games."),
       "On the 2016 Olympics he was awarded with a bronze medal.", "passive"),
    tr("Froome cierpi na astmę, która jest częstym problemem wśród kolarzy.", "suffer from",
       "Froome suffers from asthma, which is a common problem among cyclists.",
       "Froome has asthma, a common problem among cyclists.",
       ("suffer <b>from</b> + choroba · among + grupa.", "„Wśród” przy grupie to <b>among</b>, nie <i>between</i> (to dla dwóch)."),
       "Froome suffers on asthma, what is a common problem between cyclists.", DP),
    tr("Wziął lek za radą swojego lekarza.", "on the advice of",
       "He took the medication on the advice of his doctor.",
       "He took the medication on his doctor's advice.",
       ("on the advice <b>of</b> sb.", "<i>advice</i> jest niepoliczalne – nigdy <i>an advice</i>."),
       "He took the medication after the advice of his doctor.", DP),
    tr("Po dochodzeniu sprawę przeciwko niemu umorzono.", "the case … was dropped",
       "After an investigation, the case against him was dropped.",
       "The case against him was dropped after an investigation.",
       ("the case <b>against</b> sb + strona bierna.", "Po polsku bezosobowo („umorzono”), po angielsku strona bierna."),
       "After an investigation, they dropped the case for him.", DP),
    tr("Stała się osobą znaną dosłownie w każdym domu.", "a household name",
       "She has become a household name.", "She is a household name now.",
       ("become + a household name.", "Idiom jest stały – żadnego słowa nie można wymienić."),
       "She has become a home name."),
    tr("Jej kariera zawodowa nie obyła się bez kontrowersji.", "free of controversy",
       "Her professional career has not been free of controversy.",
       "Her professional career has not been free from controversy.",
       ("be free <b>of</b> / <b>from</b> sth.", "<i>controversy</i> w tym znaczeniu bez <i>-s</i> i bez przedimka."),
       "Her professional career has not been free of controversies.", DP),
    tr("Szarapowa dostała dwuletni zakaz gry.", "be banned from",
       "Sharapova was banned from playing for two years.",
       "Sharapova received a two-year ban from playing.",
       ("be banned <b>from</b> + <b>-ing</b>.", "Po <i>from</i> nigdy nie ma bezokolicznika."),
       "Sharapova was banned to play for two years.", DP),
    tr("Decyzja wywołała powszechne oburzenie opinii publicznej.", "a public outcry",
       "The ruling caused a widespread public outcry.",
       "The decision sparked a widespread public outcry.",
       ("cause / spark + a widespread public outcry.", "<b>widespread</b> to jedno słowo i nie zamienia się na <i>wide</i>."),
       "The ruling caused a wide public outcry."),
    tr("W tym tygodniu mam napięty grafik.", "a packed schedule",
       "I've got a packed schedule this week.", "My schedule is packed this week.",
       ("a packed schedule · have got + rzeczownik.", "Pełna wersja: <i>packed <b>with</b> meetings / activities</i>."),
       "I have a full of activities schedule this week."),
]


OUTPUTS = {
    "fce-collocations-athletes-3a.tsv": COLLOC,
    "fce-phrasal-verbs-athletes-3a.tsv": PHRASAL,
    "fce-grammar-athletes-3a.tsv": GRAMMAR,
    "fce-use-of-english-athletes-3a.tsv": OPEN_CLOZE,
    "fce-use-of-english-athletes-3a-translation.tsv": TR,
}

if __name__ == "__main__":
    for name, rows in OUTPUTS.items():
        write_tsv(name, rows)
