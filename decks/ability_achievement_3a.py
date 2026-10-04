#!/usr/bin/env python3
"""Talia 3A Ability and achievement: słownictwo z tekstów, kolokacje, multi-word verbs,
reguła enough, open cloze, word formation, KWT i tłumaczenia PL → EN.

Uruchom z katalogu repo: python decks/ability_achievement_3a.py
Nadpisuje pliki TSV w output/. Nie zmieniaj pierwszych pól istniejących wierszy –
od nich zależy GUID notatki w Anki (zmiana = nowa karta i utrata historii powtórek).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cardlib import (GAP as G, KWT_GAP as GAP, colloc_translation, examples_block,  # noqa: E402
                     kwt_fields, meaning_fields, mistakes_block, open_cloze_fields,
                     translation_fields, vocab_back, word_formation_fields, write_tsv)

T = "ability-achievement unit-3a"
DP = "dependent-prepositions"


def vocab(front, pos, ipa, pl, en, examples, note="", extra=""):
    return [front, vocab_back(pos, ipa, pl, en, note), examples_block(examples, "example"),
            f"fce vocabulary {T} {extra}".strip()]


def colloc(item, pl, en, examples, ctype, note=""):
    return [item, colloc_translation(pl, en, note), examples_block(examples, "example"), ctype,
            f"fce collocations {ctype.replace('+', '-')} {T}"]


def pv(verb, meanings, note, examples, synonyms, base, types, extra=""):
    return [verb, meaning_fields(meanings, note), examples_block(examples), synonyms,
            f"fce phrasal-verbs {base} {T} multi-word-verbs {types} {extra}".strip()]


def oc(sentence, answer, why, rule, tip, extra=""):
    return [*open_cloze_fields(sentence, answer, why, rule, tip), "open-cloze",
            f"fce use-of-english open-cloze {T} {extra}".strip()]


def wf(sentence, base, answer, formation, expl):
    return [*word_formation_fields(sentence, base, answer, formation, expl), "word-formation",
            f"fce use-of-english word-formation {T}"]


def kwt(original, keyword, gap, answer, full, why, rule, tip):
    return [*kwt_fields(original, keyword, gap, answer, full, why, rule, tip), "key-word-transformation",
            f"fce use-of-english key-word-transformation {T}"]


def tr(pl, hint, answer, alt, expl, wrong, extra=""):
    return [*translation_fields(pl, hint, answer, alt, expl, wrong), "translation",
            f"fce use-of-english translation {T} {extra}".strip()]


# ---------------------------------------------------------------- Vocabulary
VOCAB = [
    vocab("competitor", "noun", "/kəmˈpetɪtə(r)/", "zawodnik, rywal; konkurent (firma)",
          "a person or team taking part in a competition; a company that sells similar products",
          [("She finished two seconds ahead of her closest <b>competitor</b>.", "Skończyła dwie sekundy przed swoją najgroźniejszą rywalką."),
           ("Our main <b>competitor</b> has just lowered its prices.", "Nasz główny konkurent właśnie obniżył ceny.")],
          "Rodzina wyrazów (Part 3): <i>compete</i> → <i>competition</i> → <i>competitive</i> → <i>competitor</i>."),
    vocab("in spite of (sth / doing sth)", "preposition", "/ɪn ˈspaɪt əv/", "pomimo, mimo",
          "without being prevented by something",
          [("He stays on his feet <b>in spite of</b> being pushed by other players.", "Utrzymuje się na nogach, mimo że inni zawodnicy go popychają."),
           ("We went for a walk <b>in spite of</b> the rain.", "Poszliśmy na spacer pomimo deszczu.")],
          "Po <i>in spite of</i> stoi rzeczownik albo <b>-ing</b>, nigdy całe zdanie. Synonim bez <i>of</i>: <i>despite</i>. Z całym zdaniem → <i>even though / although</i>.",
          "linking-words"),
    vocab("even though", "conjunction", "/ˈiːvn ðəʊ/", "mimo że, chociaż",
          "despite the fact that",
          [("<b>Even though</b> all the musicians had talent, only some of them became famous.", "Mimo że wszyscy muzycy mieli talent, tylko niektórzy stali się sławni."),
           ("I failed the test <b>even though</b> I'd studied a lot.", "Oblałem test, mimo że dużo się uczyłem.")],
          "Po <i>even though</i> stoi całe zdanie (podmiot + czasownik). Mocniejsze niż <i>although</i>. Samo <i>even</i> nie wystarczy: NIE <i>Even he studied…</i>",
          "linking-words"),
    vocab("be no exception", "phrase", "/bi nəʊ ɪkˈsepʃn/", "nie być wyjątkiem",
          "to be the same as all the others in a group",
          [("Nearly all top players have long arms, and he's <b>no exception</b>.", "Prawie wszyscy najlepsi zawodnicy mają długie ręce i on nie jest wyjątkiem."),
           ("Everyone in my family loves music, and I'm <b>no exception</b>.", "Wszyscy w mojej rodzinie kochają muzykę i ja nie jestem wyjątkiem.")],
          "Rodzina: <i>exception</i> → <i>exceptional</i> (wyjątkowy) → <i>exceptionally</i>."),
    vocab("only to (do sth)", "phrase", "/ˈəʊnli tə/", "…a potem okazało się, że…; tylko po to, żeby…",
          "used before a disappointing or surprising result of an action",
          [("I ran to the station, <b>only to find</b> that the train had already left.", "Pobiegłem na dworzec, a tam okazało się, że pociąg już odjechał."),
           ("She studied all weekend, <b>only to discover</b> that the exam had been cancelled.", "Uczyła się cały weekend, a potem okazało się, że egzamin odwołano.")],
          "Zwykle po przecinku, z bezokolicznikiem: <i>only to find / discover / realise</i>. W tekście: <i>only to find out that we're not very good at it</i>."),
    vocab("come naturally to sb", "phrase", "/kʌm ˈnætʃrəli tə/", "przychodzić komuś łatwo, naturalnie",
          "to be easy for someone to do without having to learn or try hard",
          [("Languages seem to <b>come naturally to</b> her.", "Wydaje się, że języki przychodzą jej naturalnie."),
           ("Public speaking doesn't <b>come naturally to</b> me, so I practise a lot.", "Wystąpienia publiczne nie przychodzą mi łatwo, więc dużo ćwiczę.")],
          "Podmiotem jest <b>czynność</b>, a osoba stoi po <b>to</b>: <i>Singing comes naturally to him</i> (NIE <i>He comes naturally to singing</i>).",
          "dependent-prepositions"),
    vocab("be born that way", "phrase", "/bi bɔːn ðæt weɪ/", "urodzić się takim, mieć to od urodzenia",
          "to have a quality from birth, not because you learned it",
          [("Talented people must <b>be born that way</b>.", "Utalentowani ludzie muszą się tacy rodzić."),
           ("I'm not naturally organised – I wasn't <b>born that way</b>, I had to learn it.", "Nie jestem z natury zorganizowany – nie urodziłem się taki, musiałem się tego nauczyć.")],
          "Strona bierna: <i>I was born</i> (NIE <i>I born</i>). Podobnie: <i>be born lucky</i>, <i>be born a leader</i>."),
    vocab("without a doubt", "phrase (adverb)", "/wɪˈðaʊt ə daʊt/", "bez wątpienia",
          "used to say that you are completely certain",
          [("<b>Without a doubt</b>, some people are brilliant at certain things.", "Bez wątpienia niektórzy ludzie są wybitni w pewnych dziedzinach."),
           ("It was <b>without a doubt</b> the best concert I've ever been to.", "To był bez wątpienia najlepszy koncert, na jakim byłem.")],
          "Przydatne w Speaking Part 3–4 i w eseju. Podobnie: <i>no doubt</i>, <i>undoubtedly</i>."),
    vocab("there's a lot to be said for (sth / doing sth)", "phrase", "/ðeəz ə lɒt tə bi sed fə/", "wiele przemawia za czymś, coś ma wiele zalet",
          "used to say that something has many advantages",
          [("<b>There's a lot to be said for</b> practice.", "Wiele przemawia za ćwiczeniem."),
           ("<b>There's a lot to be said for</b> learning a little every day.", "Wiele przemawia za tym, żeby uczyć się po trochu codziennie.")],
          "Po <b>for</b>: rzeczownik albo <b>-ing</b>. Świetne w eseju (Writing Part 1) do wprowadzenia argumentu.",
          "dependent-prepositions"),
    vocab("what it takes (to do sth)", "phrase", "/wɒt ɪt teɪks/", "to, czego potrzeba (żeby coś osiągnąć)",
          "the qualities or effort that you need to succeed at something",
          [("According to Ericsson, that's <b>what it takes</b> to become really skilled.", "Według Ericssona właśnie tego potrzeba, żeby stać się naprawdę wprawnym."),
           ("Do you think you have <b>what it takes</b> to be a professional musician?", "Myślisz, że masz to, czego potrzeba, żeby być zawodowym muzykiem?")],
          "<i>have what it takes</i> = mieć predyspozycje, „mieć to coś”."),
    vocab("be meaningful to sb", "adjective + preposition", "/ˈmiːnɪŋfl tə/", "mieć znaczenie dla kogoś, być dla kogoś istotnym",
          "important, serious or useful to someone",
          [("If new information is interesting, it'll probably be more <b>meaningful to</b> us.", "Jeśli nowa informacja jest ciekawa, prawdopodobnie będzie miała dla nas większe znaczenie."),
           ("The gift was small, but it was very <b>meaningful to</b> her.", "Prezent był mały, ale wiele dla niej znaczył.")],
          "Przyimek <b>to</b>. Rodzina: <i>mean</i> → <i>meaning</i> → <i>meaningful</i> / <i>meaningless</i>.",
          "dependent-prepositions"),
    vocab("associate sth with sth", "verb", "/əˈsəʊʃieɪt/", "kojarzyć coś z czymś, łączyć",
          "to connect someone or something in your mind with someone or something else",
          [("It helps if we <b>associate</b> new information <b>with</b> something we already know.", "Pomaga, jeśli kojarzymy nowe informacje z czymś, co już znamy."),
           ("I always <b>associate</b> the smell of coffee <b>with</b> my grandmother's kitchen.", "Zapach kawy zawsze kojarzy mi się z kuchnią babci.")],
          "<b>associate A with B</b> (NIE <i>to</i>). Strona bierna: <i>be associated with</i>. Rzeczownik: <i>association</i>.",
          "dependent-prepositions"),
    vocab("be at your best", "phrase", "/bi æt jə best/", "być w najlepszej formie",
          "to be as good, effective or energetic as you can be",
          [("Between ten and midday, most people <b>are at their best</b>.", "Między dziesiątą a południem większość ludzi jest w najlepszej formie."),
           ("I'm not <b>at my best</b> first thing in the morning.", "Z samego rana nie jestem w najlepszej formie.")],
          "<i>your</i> zmieniamy: <i>at my / his / their best</i>. NIE kalka <i>in my best form</i>."),
    vocab("it pays to (do sth)", "phrase", "/ɪt peɪz tə/", "opłaca się (coś zrobić)",
          "used to say that doing something brings an advantage",
          [("If you want to learn something physical, <b>it pays to wait</b> until the afternoon.", "Jeśli chcesz nauczyć się czegoś fizycznego, opłaca się poczekać do popołudnia."),
           ("<b>It pays to</b> check your answers before you hand in the test.", "Opłaca się sprawdzić odpowiedzi przed oddaniem testu.")],
          "Podmiot zawsze <b>it</b> + bezokolicznik z <i>to</i>. Podobnie: <i>hard work pays off</i> = ciężka praca się opłaca."),
    vocab("be at its peak", "phrase", "/bi æt ɪts piːk/", "być u szczytu, osiągać maksimum",
          "to be at the highest or strongest level",
          [("Between 2 pm and 6 pm, our muscle strength <b>is at its peak</b>.", "Między 14 a 18 nasza siła mięśni jest największa."),
           ("Traffic <b>is at its peak</b> between 8 and 9 a.m.", "Ruch jest największy między 8 a 9 rano.")],
          "<i>its</i> zmieniamy: <i>athletes are at their peak in their twenties</i>. Porównaj: <i>be at your best</i>."),
    # ---- z tekstów i strony 3A (bez zaznaczenia)
    vocab("early bird / night owl", "noun", "/ˌɜːli ˈbɜːd/ · /ˈnaɪt aʊl/", "ranny ptaszek / nocny marek",
          "a person who likes getting up early / a person who likes staying up late",
          [("Are you an <b>early bird</b> or a <b>night owl</b>?", "Jesteś rannym ptaszkiem czy nocnym markiem?"),
           ("I'm a real <b>night owl</b> – I do my best work after 10 p.m.", "Jestem prawdziwym nocnym markiem – najlepiej pracuje mi się po 22.")],
          "", "extra"),
    vocab("first thing (in the morning)", "phrase (adverb)", "/ˌfɜːst ˈθɪŋ/", "z samego rana, zaraz na początku dnia",
          "very early in the morning, before doing anything else",
          [("I'll call you <b>first thing</b> tomorrow.", "Zadzwonię do ciebie jutro z samego rana."),
           ("Learning is harder <b>first thing</b>, because the brain needs time to warm up.", "Z samego rana uczy się trudniej, bo mózg potrzebuje czasu na rozgrzewkę.")],
          "Bez przyimka: <i>first thing tomorrow</i> (NIE <i>in first thing</i>).", "extra"),
    vocab("have a talent for (sth / doing sth)", "phrase", "/hæv ə ˈtælənt fə/", "mieć talent do czegoś",
          "to have a natural ability to do something well",
          [("Some people <b>have a talent for</b> kicking a ball around a field.", "Niektórzy mają talent do kopania piłki na boisku."),
           ("She <b>has a real talent for</b> languages.", "Ma prawdziwy talent do języków.")],
          "Przyimek <b>for</b> (NIE <i>to</i> / <i>in</i>). Przymiotnik: <i>talented</i>.", "extra dependent-prepositions"),
    vocab("consistency", "noun", "/kənˈsɪstənsi/", "systematyczność, regularność, konsekwencja",
          "the quality of always behaving or performing in a similar way",
          [("In learning, <b>consistency</b> matters more than talent.", "W nauce systematyczność liczy się bardziej niż talent."),
           ("The team's success comes from <b>consistency</b>, not luck.", "Sukces drużyny bierze się z regularności, a nie ze szczęścia.")],
          "Przymiotnik: <i>consistent</i> (<i>consistent practice</i>). Z Twojej notatki przy zdaniu <i>Children learn faster than adults</i>.",
          "extra"),
    vocab("make sense (to sb)", "phrase", "/meɪk sens/", "mieć sens, być zrozumiałym (dla kogoś)",
          "to be easy to understand or to be a sensible thing to do",
          [("His explanation didn't <b>make sense</b> to me.", "Jego wyjaśnienie nie miało dla mnie sensu."),
           ("It <b>makes sense</b> to study difficult subjects in the morning.", "Sensownie jest uczyć się trudnych przedmiotów rano.")],
          "NIE kalka <i>It has sense</i>. <i>make sense of sth</i> = zrozumieć coś (<i>I couldn't make sense of the instructions</i>).",
          "extra"),
]


# ---------------------------------------------------------------- Collocations
COLLOC = [
    colloc("cover long distances", "pokonywać długie dystanse", "to travel a long way",
           [("Cross-country skiers <b>cover long distances</b>.", "Narciarze biegowi pokonują długie dystanse."),
            ("Some birds <b>cover</b> thousands of kilometres every year.", "Niektóre ptaki pokonują co roku tysiące kilometrów.")],
           "verb+noun", "Też: <i>cover a distance of 10 km</i>; <i>cover a topic</i> = omówić temat."),
    colloc("beat sb (by sth)", "pokonać kogoś (różnicą…)", "to defeat someone in a competition",
           [("In 1964, he <b>beat</b> his closest competitor <b>by</b> 40 seconds.", "W 1964 roku pokonał najgroźniejszego rywala o 40 sekund."),
            ("We <b>beat</b> the other team 3–1 and won the cup.", "Pokonaliśmy drugą drużynę 3:1 i zdobyliśmy puchar.")],
           "verb+object", "<b>beat</b> + osoba / drużyna, <b>win</b> + zawody / nagroda: <i>win a race, win a medal</i>. NIE <i>win a competitor</i>."),
    colloc("score points / score a goal", "zdobywać punkty / strzelić gola", "to get points or a goal in a game",
           [("Long arms make it easier to catch the ball and <b>score points</b>.", "Długie ręce ułatwiają łapanie piłki i zdobywanie punktów."),
            ("He <b>scored</b> two <b>goals</b> in the final.", "Strzelił dwa gole w finale.")],
           "verb+noun", "Też: <i>score high marks</i> = dostać wysokie oceny."),
    colloc("catch sb's attention / catch the attention of sb", "przykuć czyjąś uwagę", "to make someone notice something",
           [("This problem <b>caught the attention of</b> a German psychologist.", "Ten problem przykuł uwagę niemieckiego psychologa."),
            ("A bright headline will <b>catch the reader's attention</b>.", "Wyrazisty nagłówek przyciągnie uwagę czytelnika.")],
           "verb+noun", "Podobnie: <i>attract attention</i>. Nie myl z <i>pay attention to</i> = zwracać uwagę na."),
    colloc("make progress", "robić postępy", "to improve or develop over time",
           [("I must practise every day in order to <b>make progress</b>.", "Muszę ćwiczyć codziennie, żeby robić postępy."),
            ("She's <b>made a lot of progress</b> with her English this year.", "W tym roku zrobiła duże postępy w angielskim.")],
           "verb+noun", "<i>progress</i> jest niepoliczalny: <i>make progress / make a lot of progress</i> (NIE <i>a progress</i>, NIE <i>do progress</i>)."),
]


# ---------------------------------------------------------------- Phrasal verbs
PV = [
    pv("account for (sth)",
       [("wyjaśniać, być przyczyną czegoś", "to be the explanation or reason for something"),
        ("stanowić (część całości)", "to form a particular amount or part of something")],
       "<b>Type 3</b> – nierozdzielny: account for his success / account for it (NIE account it for).",
       [("His low centre of gravity <b>accounts for</b> his ability to stay on his feet.", "Nisko położony środek ciężkości wyjaśnia, dlaczego utrzymuje się na nogach."),
        ("Bad weather <b>accounted for</b> the delay.", "Opóźnienie było spowodowane złą pogodą."),
        ("Students <b>account for</b> about 30% of the city's population.", "Studenci stanowią około 30% mieszkańców miasta.")],
       "explain, be the reason for, make up", "account", "type-3"),
    pv("think of (sth / sb)",
       [("pomyśleć o, wyobrazić sobie; <i>make sb think of</i> = kojarzyć się", "to have an image or an idea come into your mind"),
        ("przypomnieć sobie, wpaść na (pomysł)", "to remember something; to produce an idea")],
       "<b>Type 3</b> – nierozdzielny: think of a picture / think of it. Porównaj: <i>think about</i> = rozmyślać, zastanawiać się nad czymś dłużej.",
       [("A new word might make us <b>think of</b> a picture.", "Nowe słowo może skojarzyć nam się z obrazem."),
        ("I can't <b>think of</b> his name right now.", "Nie mogę sobie teraz przypomnieć jego imienia."),
        ("Can you <b>think of</b> a better solution?", "Przychodzi ci do głowy lepsze rozwiązanie?")],
       "imagine, remember, come up with", "think", "type-3"),
    pv("turn out",
       [("okazać się (że…)", "to happen in a particular way, or to be discovered to be true")],
       "<b>Type 1</b> – bez dopełnienia: <i>It turns out that…</i> / <i>turn out to be + noun/adj</i> / <i>turn out well</i>. Uwaga: <i>turn sth out</i> (zgasić światło) to inny czasownik (Type 2).",
       [("<b>It turns out that</b> practice really does make perfect.", "Okazuje się, że praktyka naprawdę czyni mistrza."),
        ("The test <b>turned out to be</b> easier than I expected.", "Test okazał się łatwiejszy, niż się spodziewałem."),
        ("Don't worry – everything will <b>turn out</b> fine.", "Nie martw się – wszystko dobrze się skończy.")],
       "prove (to be), emerge, end up", "turn", "type-1"),
    pv("find (sth) out",
       [("dowiedzieć się, odkryć", "to get information about something or learn a fact")],
       "<b>Type 2</b> – rozdzielny, ale najczęściej z <i>that / about / what / if</i> po partykule: <i>find out that…</i>, <i>find out about sth</i>. Z zaimkiem: <i>find it out</i> (rzadkie).",
       [("We try to learn something new, only to <b>find out</b> that we're not very good at it.", "Próbujemy nauczyć się czegoś nowego, a potem się okazuje, że nie idzie nam to najlepiej."),
        ("I have to <b>find out about</b> the way car engines work.", "Muszę się dowiedzieć, jak działają silniki samochodowe."),
        ("Did you <b>find out</b> what time the course starts?", "Dowiedziałeś się, o której zaczyna się kurs?")],
       "discover, learn, realise", "find", "type-2"),
    pv("stick with (sth)",
       [("wytrwać przy czymś, nie rezygnować z czegoś", "to continue doing or using something, even when it is difficult")],
       "<b>Type 3</b> – nierozdzielny: stick with the course / stick with it (NIE stick it with). Przeciwieństwo: <i>give up</i> (3A).",
       [("The book is really boring. Should I just <b>stick with it</b>?", "Ta książka jest naprawdę nudna. Mam się jej trzymać?"),
        ("Learning an instrument is hard at first, but if you <b>stick with it</b>, you'll improve.", "Nauka gry na instrumencie jest na początku trudna, ale jeśli wytrwasz, zrobisz postępy.")],
       "persevere, persist, keep going", "stick", "type-3", "extra"),
    pv("warm up / warm (sth / sb) up",
       [("rozgrzać się (przed wysiłkiem)", "to prepare your body for exercise"),
        ("rozgrzać coś / kogoś", "to make something or someone warmer or ready")],
       "<b>Type 1</b> (Always warm up before a run) i <b>Type 2</b> (warm up your muscles / warm them up). Rzeczownik: <i>a warm-up</i>.",
       [("Our bodies and brains need time to <b>warm up</b>.", "Nasze ciała i mózgi potrzebują czasu na rozgrzewkę."),
        ("Always <b>warm up</b> before you go for a run.", "Zawsze się rozgrzej, zanim pójdziesz pobiegać."),
        ("The choir <b>warms up</b> their voices before every concert.", "Chór rozgrzewa głosy przed każdym koncertem.")],
       "prepare, loosen up, heat up", "warm", "type-1 type-2", "extra"),
]


# ---------------------------------------------------------------- Grammar: enough
GRAMMAR = [[
    "enough – word order: adjective + enough / enough + noun",
    '<div class="formula"><b>📐 Struktura:</b><br><code>adjective / adverb + enough</code> → good enough, fast enough<br>'
    '<code>enough + noun</code> → enough eggs, enough time<br>'
    '<code>… enough + to-infinitive / for sb</code> → old enough to drive, enough chairs for everyone</div>'
    '<div class="usage"><b>📖 Użycie:</b><ul>'
    '<li><b>enough</b> stoi <b>po</b> przymiotniku i przysłówku.</li>'
    '<li><b>enough</b> stoi <b>przed</b> rzeczownikiem.</li>'
    '<li>Z czasownikiem: po czasowniku (lub dopełnieniu): <i>I didn\'t sleep enough</i>.</li></ul></div>'
    '<div class="signal-words"><b>🔑 Z Twojej notatki:</b> adjective + enough (good enough) · enough + nouns (enough eggs)</div>'
    '<div class="tip"><b>💡 Wskazówka FCE:</b> Klasyczna transformacja w Part 4: <i>She\'s too young to vote.</i> → <i>She isn\'t <b>old enough to</b> vote.</i></div>',
    examples_block([("Is my English <b>good enough</b> for the exam?", "Czy mój angielski jest wystarczająco dobry na egzamin?"),
              ("We don't have <b>enough eggs</b> to make a cake.", "Nie mamy dość jajek, żeby upiec ciasto."),
              ("She's <b>old enough</b> to travel on her own.", "Jest wystarczająco dorosła, żeby podróżować sama."),
              ("He didn't practise <b>enough</b>, so he didn't make much progress.", "Nie ćwiczył wystarczająco dużo, więc nie zrobił dużych postępów.")]),
    mistakes_block([("It's enough good.", "It's good enough.", "Z przymiotnikiem <i>enough</i> stoi <b>po</b> nim."),
              ("We have eggs enough.", "We have enough eggs.", "Z rzeczownikiem <i>enough</i> stoi <b>przed</b> nim."),
              ("He isn't enough old to drive.", "He isn't old enough to drive.", "Kolejność: przymiotnik + <i>enough</i> + <i>to</i>-bezokolicznik.")]),
    f"fce grammar enough word-order {T}",
]]


# ---------------------------------------------------------------- Use of English: open cloze, word formation, KWT
OC = [
    oc(f"A lack of sleep accounts {G} many of the mistakes students make.", "for",
       "<b>account for</b> = wyjaśniać, być przyczyną.", "verb + preposition: account for",
       "Gdy zdanie mówi o przyczynie albo o części całości (30% of…), sprawdź <i>account for</i>.", DP),
    oc(f"Languages seem to come naturally {G} some children.", "to",
       "Stałe wyrażenie <b>come naturally to sb</b>.", "fixed phrase: come naturally to sb",
       "Osoba, dla której coś jest łatwe, stoi po <i>to</i>.", DP),
    oc(f"She finished the race in spite {G} a painful injury.", "of",
       "<b>in spite of</b> + rzeczownik. Bez <i>of</i> → <i>despite</i>.", "fixed phrase: in spite of",
       "Jeśli po luce stoi rzeczownik albo <i>-ing</i>, a przed nią <i>in spite</i> – brakuje <i>of</i>.", DP),
    oc(f"We often associate the smell of coffee {G} Monday mornings.", "with",
       "<b>associate A with B</b> = kojarzyć coś z czymś.", "verb + object + preposition: associate … with",
       "Polskie „kojarzyć <b>z</b>” pasuje tu do <i>with</i> – ale przy innych czasownikach nie ufaj kalce.", DP),
    oc(f"Stories from your own life are more meaningful {G} you than random examples.", "to",
       "<b>meaningful to sb</b> = mający znaczenie dla kogoś.", "adjective + preposition: meaningful to",
       "Przymiotniki oceny dla kogoś (meaningful, important, useful) często łączą się z <i>to</i>.", DP),
    oc(f"Most people are {G} their best between ten and midday.", "at",
       "Stałe wyrażenie <b>be at your best</b>.", "fixed phrase: be at sb's best",
       "<i>their best</i> bez przyimka to sygnał: brakuje <i>at</i>."),
    oc(f"Traffic in the city is at {G} peak around 8 a.m.", "its",
       "Stałe wyrażenie <b>be at its peak</b>; zaimek dzierżawczy zgadza się z podmiotem (traffic → its).", "fixed phrase: be at its / their peak",
       "Po <i>at</i> i przed <i>peak / best</i> zwykle brakuje zaimka dzierżawczego."),
    oc(f"I studied all night, only {G} discover that the exam had been cancelled.", "to",
       "<b>only to do sth</b> – zaskakujący, rozczarowujący skutek.", "only + to-infinitive",
       "Po przecinku i <i>only</i>, przed czasownikiem w formie podstawowej – wpisz <i>to</i>."),
    oc(f"There's a lot to be said {G} learning a little every day.", "for",
       "Stałe wyrażenie <b>there's a lot to be said for sth</b>.", "fixed phrase: a lot to be said for",
       "Po <i>said</i> w tym wyrażeniu zawsze <i>for</i>.", DP),
    oc(f"Only a few players have what it {G} to reach the top.", "takes",
       "<b>have what it takes</b> = mieć to, czego potrzeba.", "fixed phrase: what it takes (to do sth)",
       "Po <i>what it</i> i przed <i>to</i> + czasownik – wpisz <i>takes</i>."),
    oc(f"{G} though he trained every day, he didn't make the team.", "Even",
       "<b>even though</b> + zdanie = mimo że.", "linking word: even though",
       "Przed <i>though</i> w jednowyrazowej luce pasuje tylko <i>Even</i> (<i>even though</i> = mimo że)."),
    oc(f"The weather turned {G} to be perfect for the race.", "out",
       "<b>turn out to be</b> = okazać się.", "phrasal verb: turn out to be",
       "<i>turned ___ to be</i> – prawie zawsze <i>out</i>."),
    oc(f"The bright poster caught the attention {G} everyone in the room.", "of",
       "<b>catch the attention of sb</b>.", "noun + preposition: attention of",
       "Wersja z dopełniaczem: <i>the attention of everyone</i> = <i>everyone's attention</i>."),
    oc(f"He beat his opponent {G} ten points.", "by",
       "Różnicę wyniku wprowadza <b>by</b>: beat sb by 10 points / 40 seconds.", "beat sb by + amount",
       "Liczba punktów, sekund, metrów po <i>beat / win / lose</i> → <i>by</i>."),
    oc(f"Everyone in my family can sing, and I'm {G} exception.", "no",
       "<b>be no exception</b> = nie być wyjątkiem.", "fixed phrase: be no exception",
       "Przed <i>exception</i> w tym znaczeniu stoi <i>no</i>, nie <i>not</i> ani <i>an</i>."),
    oc(f"{G} a doubt, practice is the key to success.", "Without",
       "<b>without a doubt</b> = bez wątpienia.", "fixed phrase: without a doubt",
       "Na początku zdania przed <i>a doubt</i> – <i>Without</i>."),
    oc(f"My brother has a talent {G} making people laugh.", "for",
       "<b>have a talent for sth / doing sth</b>.", "noun + preposition: talent for",
       "Po <i>talent</i> zawsze <i>for</i>.", DP),
    oc(f"She's made a lot {G} progress with her English this year.", "of",
       "<b>make a lot of progress</b> – <i>progress</i> jest niepoliczalny.", "quantifier: a lot of + uncountable noun",
       "Między <i>a lot</i> a rzeczownikiem prawie zawsze brakuje <i>of</i>."),
    oc(f"I can't think {G} his name right now.", "of",
       "<b>think of</b> = przypomnieć sobie.", "phrasal verb: think of",
       "<i>can't think ___</i> + imię / pomysł → <i>of</i>."),
]

WF = [
    wf(f"Ten {G} took part in the final of the 15-kilometre race.", "COMPETE", "competitors",
       "COMPETE → -e + -itor → COMPETITOR(S)", "Rzeczownik w liczbie mnogiej (po <i>Ten</i>). Uwaga na <b>-s</b>!"),
    wf(f"The students who became famous were more {G} than the others.", "COMPETE", "competitive",
       "COMPETE → -e + -itive → COMPETITIVE", "Przymiotnik (po <i>more</i>). Rodzina: compete, competition, competitive, competitor."),
    wf(f"Information that is {G} to us is easier to remember.", "MEAN", "meaningful",
       "MEAN → meaning + -ful → MEANINGFUL", "Przymiotnik (po <i>is</i>, przed <i>to us</i>). Dwa kroki: <i>mean → meaning → meaningful</i>."),
    wf(f"She's an {G} pianist – one of the best in the country.", "EXCEPTION", "exceptional",
       "EXCEPTION → + -al → EXCEPTIONAL", "Przymiotnik przed rzeczownikiem. Podpowiedź: <i>an</i> przed luką = słowo zaczyna się od samogłoski."),
    wf(f"Mnemonics work by {G} – linking new facts to pictures.", "ASSOCIATE", "association",
       "ASSOCIATE → -e + -ion → ASSOCIATION", "Rzeczownik (po przyimku <i>by</i>)."),
    wf(f"He's very {G}, but he still has to practise every day.", "TALENT", "talented",
       "TALENT → + -ed → TALENTED", "Przymiotnik (po <i>very</i>)."),
    wf(f"Some people seem to be {G} good at sport.", "NATURE", "naturally",
       "NATURE → natural + -ly → NATURALLY", "Przysłówek przed przymiotnikiem <i>good</i>. Dwa kroki: <i>nature → natural → naturally</i>."),
]

KWT = [
    kwt("Although he was tired, he finished the race.", "SPITE", f"He finished the race {GAP} tired.",
        "in spite of being", "He finished the race in spite of being tired.",
        "Zdanie z <i>although</i> zamieniamy na <b>in spite of + -ing</b>.", "although + clause → in spite of + -ing",
        "Po <i>in spite of</i> nie może stać <i>he was</i> – potrzebne <i>being</i>."),
    kwt("His success can be explained by his height.", "ACCOUNTS", f"His height {GAP} success.",
        "accounts for his", "His height accounts for his success.",
        "<b>account for</b> = wyjaśniać. Podmiotem staje się przyczyna (his height).", "be explained by → account for",
        "Nie zapomnij o zaimku <i>his</i> przed <i>success</i>."),
    kwt("Maths is very easy for her.", "NATURALLY", f"Maths {GAP} her.",
        "comes naturally to", "Maths comes naturally to her.",
        "<b>come naturally to sb</b> = przychodzić komuś łatwo.", "be easy for sb → come naturally to sb",
        "Podmiot (Maths) zostaje, osoba po <i>to</i>; czasownik w 3. osobie: <i>comes</i>."),
    kwt("Later we discovered that the shop was closed.", "TURNED", f"It {GAP} the shop was closed.",
        "turned out that", "It turned out that the shop was closed.",
        "<b>It turned out that…</b> = okazało się, że…", "discover that → it turns out that",
        "Czas przeszły zostaje: <i>turned</i>."),
    kwt("Everyone noticed the advert immediately.", "ATTENTION", f"The advert immediately {GAP} everyone.",
        "caught the attention of", "The advert immediately caught the attention of everyone.",
        "<b>catch the attention of sb</b> = przykuć czyjąś uwagę.", "notice sth → sth catches sb's attention",
        "Zmienia się podmiot: teraz to reklama przykuwa uwagę."),
    kwt("It's worth waiting until the afternoon to learn a new sport.", "PAYS", f"It {GAP} until the afternoon to learn a new sport.",
        "pays to wait", "It pays to wait until the afternoon to learn a new sport.",
        "<b>it pays to do sth</b> = opłaca się coś zrobić.", "it's worth + -ing → it pays + to-infinitive",
        "Po <i>worth</i> jest <i>-ing</i>, po <i>pays</i> – <i>to</i> + bezokolicznik."),
    kwt("Like all the other players, he has very long arms.", "EXCEPTION", f"All the other players have very long arms, and he {GAP}.",
        "is no exception", "All the other players have very long arms, and he is no exception.",
        "<b>be no exception</b> = nie być wyjątkiem.", "like all the others → be no exception",
        "<i>no</i>, nie <i>not an</i>."),
    kwt("This song reminds me of my holidays.", "ASSOCIATE", f"I {GAP} my holidays.",
        "associate this song with", "I associate this song with my holidays.",
        "<b>associate A with B</b>. Podmiotem staje się osoba.", "sth reminds me of sth → I associate sth with sth",
        "Przyimek <b>with</b>, nie <i>of</i> ani <i>to</i>."),
    kwt("She's too young to drive.", "OLD", f"She isn't {GAP} drive.",
        "old enough to", "She isn't old enough to drive.",
        "<b>too + adj</b> ↔ <b>not + przeciwny adj + enough</b>.", "too young → not old enough",
        "<i>enough</i> stoi po przymiotniku – jak w Twojej notatce (<i>good enough</i>)."),
]


# ---------------------------------------------------------------- Translation
TR = [
    tr("Mimo że miał talent, nigdy nie ćwiczył.", "even though",
       "Even though he had talent, he never practised.", "Even though he was talented, he never practised.",
       ("even though + zdanie.", "Po <i>even though</i> podmiot i czasownik."), "In spite of he had talent, he never practised."),
    tr("Pomimo deszczu poszliśmy na spacer.", "in spite of",
       "In spite of the rain, we went for a walk.", "Despite the rain, we went for a walk.",
       ("in spite of + rzeczownik.", "Nie zdanie – sam rzeczownik albo <i>-ing</i>."), "In spite of it was raining, we went for a walk."),
    tr("Okazało się, że test był łatwiejszy, niż się spodziewaliśmy.", "turn out",
       "It turned out that the test was easier than we had expected.", "The test turned out to be easier than we expected.",
       ("turn out.", "Dwie konstrukcje: <i>It turned out that…</i> albo <i>X turned out to be…</i>"), ""),
    tr("Matematyka zawsze przychodziła mi łatwo.", "come naturally to",
       "Maths has always come naturally to me.", "Maths always came naturally to me (at school).",
       ("come naturally to sb.", "Podmiotem jest matematyka, a nie ja. Jeśli nadal tak jest – Present Perfect z <i>always</i>."),
       "I have always come naturally to maths."),
    tr("Zapach kawy zawsze kojarzy mi się z kuchnią babci.", "associate … with",
       "I always associate the smell of coffee with my grandmother's kitchen.", "I always associate the smell of coffee with my grandma's kitchen.",
       ("associate A with B.", "Podmiotem jest osoba (I), a nie zapach – inaczej niż po polsku."),
       "The smell of coffee always associates me with my grandmother's kitchen."),
    tr("Z samego rana nie jestem w najlepszej formie.", "be at your best · first thing",
       "I'm not at my best first thing in the morning.", "",
       ("be at my best.", "Nie kalka „w formie”; <i>first thing</i> bez przyimka."), "I'm not in my best form first thing in the morning."),
    tr("Opłaca się wcześnie kupować bilety.", "it pays to",
       "It pays to buy tickets early.", "It pays to book tickets early.",
       ("it pays + to-infinitive.", "Podmiot zawsze <i>it</i>."), "It pays buying tickets early."),
    tr("Czy masz to, czego potrzeba, żeby zostać zawodowym muzykiem?", "what it takes",
       "Do you have what it takes to become a professional musician?", "Have you got what it takes to be a professional musician?",
       ("have what it takes.", "Stałe wyrażenie – nie tłumacz słowo w słowo „czego potrzeba”."), ""),
    tr("Wiele przemawia za nauką z samego rana.", "there's a lot to be said for · first thing",
       "There's a lot to be said for studying first thing in the morning.", "",
       ("a lot to be said for + -ing.", "Po <i>for</i> forma <i>-ing</i>."), "There's a lot to be said for to study first thing in the morning."),
    tr("Nasza drużyna pokonała ich różnicą dziesięciu punktów.", "beat",
       "Our team beat them by ten points.", "We beat them by ten points.",
       ("beat sb by + wynik.", "<b>beat</b> + przeciwnik; <b>win</b> tylko z zawodami lub nagrodą."), "Our team won them by ten points."),
    tr("Muszę ćwiczyć codziennie, żeby robić postępy.", "make progress",
       "I have to practise every day to make progress.", "I need to practise every day in order to make progress.",
       ("make progress.", "<i>progress</i> jest niepoliczalny – bez <i>a</i>."), "I have to practise every day to make a progress."),
    tr("Ta książka jest nudna, ale wytrwam przy niej.", "stick with",
       "This book is boring, but I'll stick with it.", "",
       ("Type 3.", "Zaimek (<b>it</b>) po partykule."), "This book is boring, but I'll stick it with."),
    tr("Z biegiem lat widziałem, jak to się rozwija.", "see · develop",
       "Over the years, I've seen how it has developed.", "",
       ("Present Perfect.", "Twoje zdanie z notatek – poprawne. <i>Over the years</i> → Present Perfect (ten sam wzorzec co w zdaniu o chórze)."),
       "Over the years, I saw how it develops.", "my-sentences"),
    tr("Czy mój angielski jest wystarczająco dobry na egzamin?", "enough",
       "Is my English good enough for the exam?", "",
       ("adjective + enough.", "<i>enough</i> po przymiotniku."), "Is my English enough good for the exam?"),
    tr("Nie mamy dość jajek, żeby upiec ciasto.", "enough",
       "We don't have enough eggs to make a cake.", "We haven't got enough eggs to bake a cake.",
       ("enough + noun.", "<i>enough</i> przed rzeczownikiem."), "We don't have eggs enough to make a cake."),
    tr("Opóźnienie było spowodowane złą pogodą.", "account for",
       "Bad weather accounted for the delay.", "",
       ("Type 3.", "Podmiotem jest przyczyna (bad weather)."), ""),
    tr("Nie przychodzi mi do głowy lepszy pomysł.", "think of",
       "I can't think of a better idea.", "",
       ("Type 3.", "„Przychodzi mi do głowy” = <i>I can think of</i>."), "I can't think about a better idea."),
    tr("Najpierw się rozgrzej, a potem biegnij.", "warm up",
       "Warm up first, and then go for a run.", "First warm up, then start running.",
       ("Type 1.", "Bez dopełnienia – rozgrzewasz się przed biegiem."), ""),
    tr("To był bez wątpienia najlepszy koncert, na jakim byłem.", "without a doubt",
       "It was without a doubt the best concert I've ever been to.", "Without a doubt, it was the best concert I've ever been to.",
       ("Present Perfect.", "Po stopniu najwyższym (<i>the best … I've ever…</i>) – Present Perfect."),
       "It was without a doubt the best concert I was ever."),
    tr("Pobiegłem na dworzec, a tam okazało się, że pociąg już odjechał.", "only to",
       "I ran to the station, only to find that the train had already left.", "I ran to the station, only to find out that the train had already gone.",
       ("only to + bezokolicznik.", "Wcześniejsza czynność → Past Perfect (<i>had already left</i>)."), ""),
    tr("Ten problem przykuł uwagę całego zespołu.", "catch the attention of",
       "This problem caught the attention of the whole team.", "This problem caught the whole team's attention.",
       ("catch – nieregularny.", "catch – <b>caught</b> – caught."), "This problem catched the attention of the whole team."),
]


OUTPUTS = {
    "fce-vocabulary-ability-achievement-3a.tsv": VOCAB,
    "fce-collocations-ability-achievement-3a.tsv": COLLOC,
    "fce-phrasal-verbs-ability-achievement-3a.tsv": PV,
    "fce-grammar-enough-3a.tsv": GRAMMAR,
    "fce-use-of-english-ability-achievement-3a.tsv": OC + WF + KWT,
    "fce-use-of-english-ability-achievement-3a-translation.tsv": TR,
}

if __name__ == "__main__":
    for name, rows in OUTPUTS.items():
        write_tsv(name, rows)
