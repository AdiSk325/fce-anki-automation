#!/usr/bin/env python3
"""Talia 3A Words connected with sport: słownictwo z ćwiczeń a–b, rodziny wyrazów z tabeli
(word formation i akcent), przyimki, KWT i tłumaczenia PL → EN, w tym poprawione zdania
z ćwiczenia c.

Uruchom z katalogu repo: python decks/sport_3a.py
Nadpisuje pliki TSV w output/. Nie zmieniaj pierwszych pól istniejących wierszy –
od nich zależy GUID notatki w Anki (zmiana = nowa karta i utrata historii powtórek).
Słowo *competitor* ma już kartę w talii 3A Ability and achievement, więc tu go nie ma.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cardlib import (GAP as G, KWT_GAP as GAP, colloc_translation, examples_block,  # noqa: E402
                     kwt_fields, open_cloze_fields, stress_fields, translation_fields, vocab_back,
                     word_formation_fields, write_tsv)

T = "sport unit-3a"
DP = "dependent-prepositions"


def vocab(front, pos, ipa, pl, en, examples, note="", extra=""):
    return [front, vocab_back(pos, ipa, pl, en, note), examples_block(examples, "example"),
            f"fce vocabulary {T} {extra}".strip()]


def colloc(item, pl, en, examples, ctype, note="", extra=""):
    return [item, colloc_translation(pl, en, note), examples_block(examples, "example"), ctype,
            f"fce collocations {ctype.replace('+', '-')} {T} {extra}".strip()]


def oc(sentence, answer, why, rule, tip, extra=""):
    return [*open_cloze_fields(sentence, answer, why, rule, tip), "open-cloze",
            f"fce use-of-english open-cloze {T} {extra}".strip()]


def wf(sentence, base, answer, formation, expl, stress=None):
    return [*word_formation_fields(sentence, base, answer, formation, expl, stress), "word-formation",
            f"fce use-of-english word-formation {T}"]


def kwt(original, keyword, gap, answer, full, why, rule, tip):
    return [*kwt_fields(original, keyword, gap, answer, full, why, rule, tip), "key-word-transformation",
            f"fce use-of-english key-word-transformation {T}"]


def stress(syllables, stressed, ipa, pl, rule):
    return [*stress_fields(syllables, stressed, stressed + 1, ipa, pl, rule), "word-stress",
            f"fce use-of-english word-stress pronunciation {T}"]


def tr(pl, hint, answer, alt, expl, wrong, extra=""):
    return [*translation_fields(pl, hint, answer, alt, expl, wrong), "translation",
            f"fce use-of-english translation {T} {extra}".strip()]


# ---------------------------------------------------------------- Vocabulary
VOCAB = [
    vocab("champion", "noun", "/ˈtʃæmpiən/", "mistrz, mistrzyni (zawodów)",
          "a person or team that has won a competition, especially an important one",
          [("Eero Mäntyranta was a cross-country skiing <b>champion</b>.", "Eero Mäntyranta był mistrzem w biegach narciarskich."),
           ("She became world <b>champion</b> at the age of nineteen.", "Została mistrzynią świata w wieku dziewiętnastu lat.")],
          "„Mistrz świata” = <b>world champion</b>, nie <i>master of the world</i>. Zawody to <b>championship</b> (mistrzostwa). Akcent: <b>CHAM</b>pion, <b>CHAM</b>pionship."),
    vocab("perform (well / badly)", "verb", "/pəˈfɔːm/", "spisywać się, osiągać wyniki; występować (na scenie)",
          "to do something well or badly, e.g. in a competition, a test or a job; to entertain an audience",
          [("He <b>performed</b> so well because he had more red blood cells than most skiers.", "Spisywał się tak dobrze, bo miał więcej czerwonych krwinek niż większość narciarzy."),
           ("Our team <b>performed</b> badly in the second half.", "Nasza drużyna słabo zagrała w drugiej połowie.")],
          "Zwykle z przysłówkiem: <i>perform well / badly / brilliantly</i> = <i>do well / badly</i>. Rodzina: <b>performance</b> (występ, wynik), <b>performer</b> (wykonawca)."),
    vocab("training", "noun (uncountable)", "/ˈtreɪnɪŋ/", "trening, treningi; szkolenie",
          "regular physical exercise and practice to prepare for a sport or a competition",
          [("Pulisic is successful because of regular <b>training</b>.", "Pulisic odnosi sukcesy dzięki regularnym treningom."),
           ("I can't come tonight – I've got football <b>training</b>.", "Nie mogę dziś przyjść – mam trening piłki nożnej.")],
          "Niepoliczalny: <i>a lot of training</i>, <i>a training session</i> (NIE <i>a training</i>, <i>trainings</i>). Czasownik: <b>train</b>, osoba: <b>trainer</b> (np. na siłowni); trener drużyny to zwykle <b>coach</b>."),
    vocab("technique", "noun", "/tekˈniːk/", "technika (sposób wykonania)",
          "a particular way of doing something that needs skill",
          [("He's also successful because of his <b>technique</b> – the special way he plays.", "Odnosi sukcesy także dzięki technice – szczególnemu sposobowi gry."),
           ("Her swimming <b>technique</b> has improved a lot this year.", "Jej technika pływania bardzo się w tym roku poprawiła.")],
          "Pisownia <b>-que</b>, akcent na końcu: tech<b>NIQUE</b>. <i>technology</i> to technologia, nie technika gry."),
    vocab("the opposing team", "adjective + noun", "/əˈpəʊzɪŋ ˈtiːm/", "drużyna przeciwna, przeciwnicy",
          "the team that you are playing against",
          [("The <b>opposing team</b> found it hard to keep him from scoring goals.", "Drużynie przeciwnej trudno było powstrzymać go przed strzelaniem goli."),
           ("Two players from the <b>opposing team</b> were sent off.", "Dwóch zawodników z drużyny przeciwnej wyrzucono z boiska.")],
          "<b>opposing</b> (przeciwny w rywalizacji) ≠ <b>opposite</b> (naprzeciwko, odwrotny). Przeciwnik w grze: <b>opponent</b>."),
    vocab("athlete", "noun", "/ˈæθliːt/", "sportowiec, zawodnik; lekkoatleta",
          "a person who is good at sport and takes part in competitions; (BrE) a person who does athletics",
          [("Most of Kenya's best <b>athletes</b> are from the Kalenjin tribe.", "Większość najlepszych kenijskich sportowców pochodzi z plemienia Kalenjin."),
           ("More than ten thousand <b>athletes</b> took part in the Games.", "W igrzyskach wzięło udział ponad dziesięć tysięcy sportowców.")],
          "Dwie sylaby: <b>ATH</b>lete (NIE <i>ath-e-lete</i>). Rodzina: <b>athletics</b> (lekkoatletyka), <b>athletic</b> (wysportowany) – akcent przesuwa się: ath<b>LET</b>ic."),
    vocab("professional", "adjective, noun", "/prəˈfeʃənl/", "zawodowy; zawodowiec, profesjonalista",
          "doing a sport or an activity as a paid job, not as a hobby",
          [("<b>Professional</b> basketball players often have a long arm span.", "Zawodowi koszykarze często mają dużą rozpiętość ramion."),
           ("It's hard to earn a living as a <b>professional</b> cyclist.", "Trudno zarobić na życie jako zawodowy kolarz.")],
          "Przeciwieństwo: <b>amateur</b>. Rzeczownik: <b>profession</b> (zawód). Akcent: pro<b>FES</b>sional – nie na przedostatniej sylabie, jak w polskim „profesjonalny”."),
    vocab("represent (your country)", "verb", "/ˌreprɪˈzent/", "reprezentować (kraj, miasto, klub)",
          "to play or compete for your country, city or team",
          [("She'll probably <b>represent</b> her country at the next Olympic Games.", "Prawdopodobnie będzie reprezentować swój kraj na następnych igrzyskach olimpijskich."),
           ("He has <b>represented</b> Poland twenty times.", "Reprezentował Polskę dwadzieścia razy.")],
          "Bez przyimka po <i>represent</i>: <i>represent Kenya</i> (NIE <i>represent for Kenya</i>). Zawody: <b>at the</b> Olympic Games / <b>at the</b> World Cup."),
    vocab("spectator", "noun", "/spekˈteɪtə(r)/", "widz (na meczu, zawodach)",
          "a person who watches an event, especially a sports event",
          [("The <b>spectators</b> cheered as the players walked onto the pitch.", "Widzowie wiwatowali, gdy zawodnicy wychodzili na boisko."),
           ("Over 50,000 <b>spectators</b> watched the final.", "Finał oglądało ponad 50 000 widzów.")],
          "Na meczu: <b>spectators</b>, <b>fans</b>, <b>the crowd</b>. W teatrze i na koncercie: <b>audience</b>; przed telewizorem: <b>viewers</b>. NIE <i>the public</i>."),
    vocab("lead (a race / a game)", "verb", "/liːd/ – led – led", "prowadzić (w wyścigu, meczu)",
          "to be ahead of the others during a game, a race or a competition",
          [("Mateo Amador <b>led</b> the race from the beginning.", "Mateo Amador prowadził w wyścigu od samego początku."),
           ("At half-time, Spain were <b>leading</b> 2–0.", "Do przerwy Hiszpania prowadziła 2:0.")],
          "Nieregularny: lead – <b>led</b> – <b>led</b> (/led/, NIE <i>leaded</i>). Rzeczownik: <i>be in the lead</i> (prowadzić), <i>take the lead</i> (objąć prowadzenie), <i>a 2–0 lead</i>."),
    vocab("award (sb sth)", "verb", "/əˈwɔːd/", "przyznać (nagrodę, punkt, rzut karny)",
          "to give a prize, money or a point to someone officially",
          [("He was <b>awarded</b> a gold medal.", "Przyznano mu złoty medal."),
           ("The referee <b>awarded</b> a penalty in the last minute.", "Sędzia podyktował rzut karny w ostatniej minucie.")],
          "Często w stronie biernej, z osobą jako podmiotem: <i>She was awarded a prize</i> (= „przyznano jej”). Rzeczownik: <b>an award</b> (nagroda); <b>reward</b> to nagroda za wysiłek lub pomoc."),
    vocab("cheer (for sb)", "verb", "/tʃɪə(r)/", "wiwatować, dopingować",
          "to shout loudly to show that you like something or to encourage someone",
          [("The spectators <b>cheered</b> as the players walked onto the pitch.", "Widzowie wiwatowali, gdy zawodnicy wychodzili na boisko."),
           ("We <b>cheered for</b> our team until the final whistle.", "Dopingowaliśmy naszą drużynę do ostatniego gwizdka.")],
          "<i>cheer for sb</i> albo <i>cheer sb on</i> (Type 2: <i>cheer them on</i>) = dopingować. Rzeczownik: <i>a cheer</i> (okrzyk). Potocznie <i>Cheers!</i> = dzięki / na zdrowie."),
    vocab("referee", "noun", "/ˌrefəˈriː/", "sędzia (w meczu)",
          "the person who controls a game and makes sure that the players follow the rules",
          [("The <b>referee</b> blew the whistle and the game began.", "Sędzia zagwizdał i mecz się zaczął."),
           ("The players argued with the <b>referee</b> about the penalty.", "Zawodnicy kłócili się z sędzią o rzut karny.")],
          "<b>referee</b> – piłka nożna, koszykówka, rugby, boks; <b>umpire</b> – tenis, krykiet; <b>judge</b> – gimnastyka, łyżwiarstwo (i sąd). Akcent na końcu: refe<b>REE</b>."),
    vocab("pitch", "noun", "/pɪtʃ/", "boisko (piłkarskie, do rugby)",
          "an area of ground where football, rugby or hockey is played",
          [("The players walked onto the <b>pitch</b>.", "Zawodnicy wyszli na boisko."),
           ("The <b>pitch</b> was too wet, so the match was cancelled.", "Boisko było zbyt mokre, więc mecz odwołano.")],
          "<b>on</b> the pitch, <b>onto</b> the pitch. Inne miejsca: <b>court</b> (tenis, koszykówka, siatkówka), <b>track</b> (bieżnia), <b>course</b> (golf), <b>rink</b> (lodowisko), <b>pool</b> (basen)."),
    vocab("victory", "noun", "/ˈvɪktəri/", "zwycięstwo",
          "success in a game, a competition or a war",
          [("It was their first <b>victory</b> over Brazil.", "To było ich pierwsze zwycięstwo nad Brazylią."),
           ("The team celebrated their <b>victory</b> on the pitch.", "Drużyna świętowała zwycięstwo na boisku.")],
          "<i>a victory <b>over</b> sb</i> (nad kimś). Rodzina: <b>victor</b> (zwycięzca, formalnie – zwykle <i>winner</i>), <b>victorious</b> (zwycięski). Akcent: <b>VIC</b>tory → vic<b>TO</b>rious."),
    vocab("compete (in / against / for)", "verb", "/kəmˈpiːt/", "rywalizować, startować (w zawodach)",
          "to take part in a competition or to try to win something",
          [("Twenty teams will <b>compete in</b> the championship.", "W mistrzostwach wystartuje dwadzieścia drużyn."),
           ("They <b>competed against</b> the best teams in Europe <b>for</b> the gold medal.", "Rywalizowali z najlepszymi drużynami w Europie o złoty medal.")],
          "<b>compete in</b> + zawody, <b>against / with</b> + rywal, <b>for</b> + nagroda. Rodzina (Part 3): <i>competition</i>, <i>competitor</i>, <i>competitive</i>.",
          DP),
    vocab("(ten minutes) into the game", "phrase", "/ˈɪntə ðə ɡeɪm/", "(dziesięć minut) po rozpoczęciu meczu",
          "used to say how much time has passed since something started",
          [("<b>Ten minutes into the game</b>, nobody knew who would win.", "Dziesięć minut po rozpoczęciu meczu nikt nie wiedział, kto wygra."),
           ("We were only five minutes <b>into the film</b> when the lights went out.", "Film trwał dopiero pięć minut, kiedy zgasło światło.")],
          "Typowy początek relacji sportowej. Wzór: <b>czas + into + the + wydarzenie</b>: <i>two hours into the journey</i>, <i>a month into the new job</i>."),
]


# ---------------------------------------------------------------- Collocations
COLLOC = [
    colloc("hold / break / set the world record", "mieć / pobić / ustanowić rekord świata",
           "to have / beat / achieve the best result that has ever been achieved",
           [("Even though she <b>holds the world record</b> in the 1500m, she probably won't represent her country.", "Mimo że ma rekord świata na 1500 m, prawdopodobnie nie będzie reprezentować swojego kraju."),
            ("He <b>broke the world record</b> by two seconds.", "Pobił rekord świata o dwie sekundy.")],
           "verb+noun",
           "Przyimki: <i>the record <b>in</b> the 1500m</i>, <i>break it <b>by</b> two seconds</i>. Akcent: <b>REC</b>ord (rzeczownik) vs re<b>CORD</b> (czasownik: nagrywać)."),
    colloc("win a medal / a race / a championship", "zdobyć medal / wygrać wyścig / wygrać mistrzostwa",
           "to be the best in a competition and get the prize",
           [("She <b>won a gold medal</b> at the Olympics.", "Zdobyła złoty medal na olimpiadzie."),
            ("Our team <b>won the national championship</b> last year.", "Nasza drużyna wygrała w zeszłym roku mistrzostwa kraju.")],
           "verb+noun",
           "<b>win</b> + zawody albo nagroda; <b>beat</b> + przeciwnik (karta <i>beat sb (by sth)</i>). Medal można też dostać: <i>be awarded a medal</i>."),
    colloc("a tight / close game", "wyrównany mecz",
           "a game in which both teams play equally well, so it is hard to say who will win",
           [("Nobody knew who would win, because the game was really <b>tight</b>.", "Nikt nie wiedział, kto wygra, bo mecz był bardzo wyrównany."),
            ("It was a <b>close game</b>, but we won 2–1 in the end.", "To był wyrównany mecz, ale ostatecznie wygraliśmy 2:1.")],
           "adjective+noun",
           "Zdanie z Twojego ćwiczenia c – <i>tight</i> to dobry wybór zamiast <i>equal</i>. Przeciwieństwo: <i>a one-sided game</i>.",
           "my-sentences"),
    colloc("turn professional", "przejść na zawodowstwo",
           "to start doing a sport as a paid job",
           [("He <b>turned professional</b> when he was eighteen.", "Przeszedł na zawodowstwo, gdy miał osiemnaście lat."),
            ("Most tennis players <b>turn professional</b> as teenagers.", "Większość tenisistów przechodzi na zawodowstwo jako nastolatkowie.")],
           "verb+adjective",
           "<i>turn</i> + przymiotnik = stać się (zmiana stanu), jak <i>turn red</i>, <i>turn cold</i>."),
]


# ---------------------------------------------------------------- Open cloze (przyimki i słowa funkcyjne)
OC = [
    oc(f"She will probably represent her country {G} the next Olympic Games.", "at",
       "Zawody i wydarzenia: <b>at</b> the Olympic Games / the World Cup / the championships.",
       "at + wydarzenie (at a concert, at the Olympics)",
       "W Twoim zdaniu z ćwiczenia c było <i>in Olympic Games</i> – brakowało też <b>the</b>.", "my-sentences"),
    oc(f"Ten minutes {G} the game, nobody knew who would win.", "into",
       "czas + <b>into</b> + wydarzenie = tyle minęło od początku.",
       "two hours into the journey, a week into the course",
       "Początek relacji sportowej z ćwiczenia c."),
    oc(f"She holds the world record {G} the 1500 metres.", "in",
       "Rekord <b>w</b> konkurencji: <i>the record in the 100m / in the long jump</i>.",
       "record in + konkurencja",
       "Różnica wyniku: <i>break a record <b>by</b> two seconds</i>.", DP),
    oc(f"Twenty teams will compete {G} the championship this year.", "in",
       "<b>compete in</b> + zawody.",
       "compete in (zawody) / against (rywal) / for (nagroda)",
       "Polskie „startować w” = <i>compete in</i> / <i>take part in</i>.", DP),
    oc(f"The two runners competed {G} the gold medal.", "for",
       "<b>compete for</b> + to, co można zdobyć.",
       "compete in (zawody) / against (rywal) / for (nagroda)",
       "Porównaj: <i>fight for</i>, <i>apply for</i> – też cel, o który się staramy.", DP),
    oc(f"Mateo was {G} the lead from the very beginning of the race.", "in",
       "<b>be in the lead</b> = prowadzić.",
       "be in the lead, take the lead, lose the lead",
       "Czasownik: <i>lead – led – led</i>: <i>Mateo led the race</i>."),
    oc(f"The spectators cheered as the players walked {G} the pitch.", "onto",
       "Ruch na powierzchnię: <b>onto</b> (jedno słowo). Bez ruchu: <i>on the pitch</i>.",
       "walk onto the pitch / be on the pitch",
       "Podobnie: <i>jump onto the stage</i>, <i>get onto the bus</i>."),
    oc(f"The fans cheered {G} their team until the final whistle.", "for / on",
       "<b>cheer for sb</b> = dopingować. Możliwe też <i>cheered on their team</i> (phrasal verb <i>cheer sb on</i>).",
       "cheer for sb / cheer sb on",
       "Z zaimkiem: <i>cheer them on</i> (Type 2) albo <i>cheer for them</i>."),
    oc(f"She was awarded a gold medal {G} her performance in the final.", "for",
       "<b>award sb sth for sth</b> – za coś.",
       "be awarded a prize for sth",
       "Bez <i>with</i> po <i>awarded</i>: <i>was awarded a medal</i>.", DP),
    oc(f"Nobody knew who {G} win, because the game was really tight.", "would / might / could",
       "Przyszłość z perspektywy przeszłości: <b>would</b> (albo <i>might</i> / <i>could</i>), nie <i>can</i>.",
       "nobody knew who would win",
       "W ćwiczeniu c poprawka z <i>can</i> na <i>might</i> była dobra.", "my-sentences"),
    oc(f"It was their first victory {G} Brazil in twenty years.", "over",
       "<b>a victory over sb</b> = zwycięstwo nad kimś.",
       "victory over sb, defeat by sb",
       "Polskie „nad” → <i>over</i>, nie <i>above</i>.", DP),
]


# ---------------------------------------------------------------- Word formation (tabela z ćwiczenia a)
WF = [
    wf(f"She won her first international {G} at the age of sixteen.", "COMPETE", "competition",
       "compete → competition (-ition)",
       "Po <i>international</i> potrzebny rzeczownik – zawody. Osoba to <i>competitor</i>, przymiotnik <i>competitive</i>.",
       "compe<b>TI</b>tion"),
    wf(f"He's tall and {G}, so he's good at most sports.", "ATHLETE", "athletic",
       "athlete → athletic (-ic)",
       "Po <i>tall and</i> przymiotnik: wysportowany.",
       "ath<b>LET</b>ic"),
    wf(f"Running, jumping and throwing are all part of {G}.", "ATHLETE", "athletics",
       "athlete → athletics",
       "Nazwa dyscypliny (lekkoatletyka) ma <b>-s</b>, ale łączy się z czasownikiem w liczbie pojedynczej: <i>Athletics is popular in Kenya</i>.",
       "ath<b>LET</b>ics"),
    wf(f"The {G} team celebrated on the pitch for an hour.", "VICTORY", "victorious",
       "victory → victorious (-ious)",
       "Przed rzeczownikiem potrzebny przymiotnik: zwycięski.",
       "vic<b>TO</b>rious"),
    wf(f"After a tight final, the Brazilian runner was declared the {G}.", "VICTORY", "victor",
       "victory → victor",
       "Osoba, która wygrała (formalnie). W codziennym języku: <i>winner</i>.",
       "<b>VIC</b>tor"),
    wf(f"Our team won the national {G} for the third year in a row.", "CHAMPION", "championship",
       "champion → championship (-ship)",
       "Zawody (mistrzostwa), nie osoba. Końcówka <b>-ship</b> nie zmienia akcentu.",
       "<b>CHAM</b>pionship"),
    wf(f"After months of hard {G}, she was ready for the marathon.", "TRAIN", "training",
       "train → training (-ing)",
       "Po <i>hard</i> rzeczownik niepoliczalny: <i>hard training</i> (bez <i>a</i>)."),
    wf(f"My {G} at the gym writes a new programme for me every month.", "TRAIN", "trainer",
       "train → trainer (-er)",
       "Osoba (trener personalny). Trener drużyny to zwykle <i>coach</i>."),
    wf(f"It was the best {G} of his career – he scored three goals.", "PERFORM", "performance",
       "perform → performance (-ance)",
       "Po <i>the best … of</i> rzeczownik: występ, wynik.",
       "per<b>FOR</b>mance"),
    wf(f"She's a brilliant {G} – the audience loved her.", "PERFORM", "performer",
       "perform → performer (-er)",
       "Po <i>a brilliant</i> rzeczownik oznaczający osobę: wykonawca, artysta."),
    wf(f"He wants to become a {G} footballer one day.", "PROFESSION", "professional",
       "profession → professional (-al)",
       "Przed rzeczownikiem przymiotnik: zawodowy.",
       "pro<b>FES</b>sional"),
    wf(f"It was very {G} of the coach to shout at the referee.", "PROFESSION", "unprofessional",
       "profession → professional → <b>un</b>professional",
       "Sens zdania jest negatywny, więc potrzebny przedrostek <b>un-</b>. W Part 3 zawsze sprawdź, czy słowo nie wymaga zaprzeczenia."),
]


# ---------------------------------------------------------------- Key word transformation
KWT = [
    kwt("Mateo was in front for the whole race.", "LED", f"Mateo {GAP} start to finish.",
        "led the race from", "Mateo led the race from start to finish.",
        "<i>be in front</i> = <b>lead</b> (prowadzić).", "lead – led – led",
        "Liczba słów: led / the / race / from = 4."),
    kwt("They gave her a gold medal for her performance.", "AWARDED", f"She {GAP} a gold medal for her performance.",
        "was awarded", "She was awarded a gold medal for her performance.",
        "Strona bierna z osobą jako podmiotem.", "give sb sth → sb was given / awarded sth",
        "Bez <i>with</i>: <i>was awarded a medal</i>."),
    kwt("He played for his country at the World Cup.", "REPRESENTED", f"He {GAP} at the World Cup.",
        "represented his country", "He represented his country at the World Cup.",
        "<i>play for your country</i> = <b>represent your country</b>.", "represent + dopełnienie, bez przyimka",
        "Nie zmieniaj formy słowa: REPRESENTED już jest w czasie przeszłym."),
    kwt("Nobody has ever run the 1500m faster than her.", "RECORD", f"She {GAP} the 1500m.",
        "holds the world record in", "She holds the world record in the 1500m.",
        "Najlepszy wynik w historii = <b>the world record</b>.", "hold the record in + konkurencja",
        "Pięć słów: holds / the / world / record / in – to górna granica."),
    kwt("He plays basketball for a living.", "PROFESSIONAL", f"He {GAP} player.",
        "is a professional basketball", "He is a professional basketball player.",
        "<i>play for a living</i> = być zawodowcem.", "be a professional + dyscyplina + player",
        "is / a / professional / basketball = 4 słowa (<i>'s</i> też liczy się jako słowo)."),
    kwt("The other team found it difficult to stop him scoring.", "OPPOSING", f"The {GAP} difficult to stop him scoring.",
        "opposing team found it", "The opposing team found it difficult to stop him scoring.",
        "<i>the other team</i> (w meczu) = <b>the opposing team</b>.", "find it difficult to do sth",
        "Nie zgub <b>it</b>: <i>find it difficult</i>."),
    kwt("Our team was winning 2–0 at half-time.", "LEAD", f"Our team {GAP} at half-time.",
        "had a 2–0 lead", "Our team had a 2–0 lead at half-time.",
        "<i>be winning</i> = <b>have a lead</b> (rzeczownik).", "have a 2–0 lead / be in the lead",
        "Wynik 2–0 liczy się jako jedno słowo."),
    kwt("It was the first time she had competed in the Olympics.", "NEVER", f"She {GAP} in the Olympics before.",
        "had never competed", "She had never competed in the Olympics before.",
        "<i>It was the first time sb had done</i> = <i>sb had never done before</i>.", "the first time + Past Perfect ↔ never … before",
        "Czas zostaje ten sam: Past Perfect."),
]


# ---------------------------------------------------------------- Word stress (rodziny wyrazów)
PL_STRESS = "Po polsku akcent pada na przedostatnią sylabę, po angielsku nie ma takiej reguły."
STRESS = [
    stress(["ath", "lete"], 0, "/ˈæθliːt/", "sportowiec",
           "Tylko dwie sylaby – nie wstawiaj dodatkowego <i>e</i> (NIE <i>ath-e-lete</i>)."),
    stress(["ath", "let", "ic"], 1, "/æθˈletɪk/", "wysportowany",
           "Końcówka <b>-ic</b> przesuwa akcent na sylabę tuż przed nią: <b>ATH</b>lete → ath<b>LET</b>ic."),
    stress(["vic", "to", "ry"], 0, "/ˈvɪktəri/", "zwycięstwo",
           "Akcent na początku, środkowa sylaba prawie znika: /ˈvɪktri/."),
    stress(["vic", "to", "ri", "ous"], 1, "/vɪkˈtɔːriəs/", "zwycięski",
           "Końcówka <b>-ious</b> przesuwa akcent na sylabę przed nią: <b>VIC</b>tory → vic<b>TO</b>rious (jak am<b>BI</b>tious)."),
    stress(["com", "pe", "ti", "tion"], 2, "/ˌkɒmpəˈtɪʃn/", "zawody, konkurencja",
           "Końcówka <b>-tion</b>: akcent na sylabie tuż przed nią. Porównaj com<b>PETE</b> i com<b>PET</b>itor."),
    stress(["com", "pet", "i", "tive"], 1, "/kəmˈpetətɪv/", "nastawiony na rywalizację; konkurencyjny",
           "Akcent jak w com<b>PET</b>itor, a nie jak w compe<b>TI</b>tion. " + PL_STRESS),
    stress(["tech", "nique"], 1, "/tekˈniːk/", "technika",
           "Słowa z francuskiego na <b>-ique</b> mają akcent na końcu: tech<b>NIQUE</b>, u<b>NIQUE</b>."),
    stress(["ref", "er", "ee"], 2, "/ˌrefəˈriː/", "sędzia",
           "Końcówka <b>-ee</b> jest akcentowana: refe<b>REE</b>, employ<b>EE</b>, guaran<b>TEE</b>."),
    stress(["spec", "ta", "tor"], 1, "/spekˈteɪtə(r)/", "widz",
           "Akcent na <b>-TA-</b>; końcówka <i>-tor</i> jest słaba: /tə/."),
    stress(["pro", "fes", "sion", "al"], 1, "/prəˈfeʃənl/", "zawodowy",
           "Akcent jak w pro<b>FES</b>sion – końcówka <b>-al</b> go nie przesuwa. " + PL_STRESS),
    stress(["cham", "pi", "on", "ship"], 0, "/ˈtʃæmpiənʃɪp/", "mistrzostwa",
           "Końcówka <b>-ship</b> nie zmienia akcentu: <b>CHAM</b>pion → <b>CHAM</b>pionship. " + PL_STRESS),
    stress(["per", "for", "mance"], 1, "/pəˈfɔːməns/", "występ, wynik",
           "Końcówka <b>-ance</b> nie zmienia akcentu czasownika: per<b>FORM</b> → per<b>FOR</b>mance."),
]


# ---------------------------------------------------------------- Translation
TR = [
    tr("Ona reprezentowała Polskę na igrzyskach olimpijskich.", "represent",
       "She represented Poland at the Olympic Games.", "She represented Poland at the Olympics.",
       ("at the Olympic Games.", "Przyimek <b>at</b> i przedimek <b>the</b> – w ćwiczeniu c brakowało obu."),
       "She represented Poland in Olympic Games.", "my-sentences"),
    tr("Kibice wiwatowali, kiedy zawodnicy wybiegli na boisko.", "cheer · pitch",
       "The fans cheered when the players ran onto the pitch.", "The spectators cheered as the players came out onto the pitch.",
       ("spectators / fans, nie audience.", "<b>onto</b> – ruch na powierzchnię boiska."),
       "The audience cheered when the players ran on the pitch."),
    tr("Prowadził w wyścigu od samego początku.", "lead",
       "He led the race from the very beginning.", "He was in the lead from the very beginning of the race.",
       ("lead – led – led.", "„Prowadzić w wyścigu” = <i>lead the race</i>, bez <i>in</i>."),
       "He leaded in the race from the very beginning."),
    tr("Przyznano jej złoty medal.", "award",
       "She was awarded a gold medal.", "They awarded her a gold medal.",
       ("Strona bierna z osobą.", "Polskie „przyznano jej” → podmiotem jest osoba: <i>She was awarded…</i>"),
       "It was awarded her a gold medal."),
    tr("Sędzia podyktował rzut karny w ostatniej minucie.", "referee · award",
       "The referee awarded a penalty in the last minute.", "The referee gave a penalty in the last minute.",
       ("referee, nie judge.", "W piłce nożnej sędzia to <b>referee</b>; <b>judge</b> ocenia np. gimnastykę."),
       "The judge dictated a penalty in the last minute."),
    tr("Trenuje trzy razy w tygodniu, a jej technika jest coraz lepsza.", "train · technique",
       "She trains three times a week, and her technique is getting better and better.", "She trains three times a week, and her technique keeps improving.",
       ("getting better and better.", "„Coraz lepszy” = <i>better and better</i>; <i>three times a week</i> bez <i>in</i>."),
       "She is training three times in a week, and her technic is more and more better."),
    tr("Mecz był bardzo wyrównany i nikt nie wiedział, kto wygra.", "tight · would",
       "The game was really tight, and nobody knew who would win.", "It was a very close game, and no one knew who was going to win.",
       ("the game · would.", "Konkretny mecz → <b>the</b>; przyszłość z perspektywy przeszłości → <b>would</b> (albo <i>might</i>), nie <i>can</i>."),
       "Game was really equal and nobody knew who can win.", "my-sentences"),
    tr("Kenijska biegaczka Pamela Abasi prowadziła w najważniejszym biegu w swoim kraju i będzie reprezentować Kenię na igrzyskach olimpijskich.", "lead · represent",
       "Kenyan runner Pamela Abasi led the most important race in her country, and she'll represent Kenya at the Olympic Games.", "",
       ("lead a race · at the Olympic Games.", "Prowadzić w biegu = <i>lead a race</i> (<i>lead a competition</i> brzmi jak „kierować zawodami”). Igrzyska: <b>at the</b> Olympic Games."),
       "Kenyan runner Pamela Abasi led the most important competition in her country and she'll represent Kenya in Olympic Games.", "my-sentences"),
    tr("Większość widzów wyszła przed końcem meczu.", "spectator",
       "Most of the spectators left before the end of the match.", "Most spectators left before the match ended.",
       ("most of the + spectators.", "<b>Most of the</b> + konkretna grupa (bez <i>the</i> na początku). Widz na meczu: <i>spectator</i>."),
       "The most of the audience left before the end of the match."),
    tr("Ona jest mistrzynią świata w pływaniu.", "champion",
       "She's the world swimming champion.", "She's a world champion in swimming.",
       ("world champion.", "„Mistrz świata” = <i>world champion</i>, nie <i>master</i>."),
       "She is a master of the world in swimming."),
    tr("Pobił rekord świata o dwie sekundy.", "break a record",
       "He broke the world record by two seconds.", "He beat the world record by two seconds.",
       ("break – broke – broken · by.", "Różnica wyniku: <b>by</b> two seconds (jak <i>beat sb by ten points</i>)."),
       "He broke the world record with two seconds."),
    tr("Dziesięć minut po rozpoczęciu meczu padł pierwszy gol.", "into the game",
       "Ten minutes into the game, the first goal was scored.", "Ten minutes into the match, someone scored the first goal.",
       ("czas + into + the game.", "„Padł gol” = <i>a goal was scored</i> albo <i>sb scored a goal</i>."),
       "Ten minutes after the beginning of the game fell the first goal."),
    tr("Nasza drużyna wygrała mistrzostwa kraju.", "championship",
       "Our team won the national championship.", "Our team won the national championships.",
       ("championship, nie champion.", "Zawody: <i>championship</i>; osoba albo drużyna, która wygrała: <i>champion</i>."),
       "Our team won the national champion."),
    tr("Zawodnicy drużyny przeciwnej grali bardzo agresywnie.", "opposing",
       "The players from the opposing team played very aggressively.", "The opposing team played very aggressively.",
       ("opposing, nie opposite · aggressively.", "<i>opposite</i> = naprzeciwko albo odwrotny. Po <i>played</i> przysłówek."),
       "The players of the opposite team played very aggressive."),
    tr("Rywalizowali o złoty medal z najlepszymi zawodnikami na świecie.", "compete",
       "They competed against the best athletes in the world for the gold medal.", "They competed with the world's best athletes for the gold medal.",
       ("compete against + rywal, for + nagroda.", "„Na świecie” po stopniu najwyższym: <b>in</b> the world."),
       "They competed about the gold medal with the best athletes of the world.", DP),
    tr("Przeszedł na zawodowstwo, kiedy miał osiemnaście lat.", "turn professional",
       "He turned professional when he was eighteen.", "He turned professional at the age of eighteen.",
       ("turn + przymiotnik · be + wiek.", "<i>turn professional</i> = przejść na zawodowstwo; wiek z <b>be</b>, nie <i>have</i>."),
       "He turned professional when he had eighteen years."),
]


OUTPUTS = {
    "fce-vocabulary-sport-3a.tsv": VOCAB,
    "fce-collocations-sport-3a.tsv": COLLOC,
    "fce-use-of-english-sport-3a.tsv": OC + WF + KWT,
    "fce-use-of-english-word-stress-sport-3a.tsv": STRESS,
    "fce-use-of-english-sport-3a-translation.tsv": TR,
}

if __name__ == "__main__":
    for name, rows in OUTPUTS.items():
        write_tsv(name, rows)
