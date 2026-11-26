# Grammar Focus 4A i 4B (notatka źródłowa)

Źródło: Empower Upper-Intermediate, Grammar Focus s. 140 (4A *used to and would*, 4B *Obligation and permission*) i strony ćwiczeń 4A a–b oraz 4B a–b (zrzuty ekranu z 2026-11-26).

## Co jest nowe względem talii 4A z 2026-11-18

Talia `decks/used_to_would_4a.py` ma już reguły *used to*, *would*, *no longer / any more*, *used to / would* vs Past Simple, *than I used to be* i *be / get used to*. Tu dochodzą tylko:

- schemat opowiadania *used to → would → Past Simple* i *never used to* (bez *did*),
- *wouldn't* jako powtarzana odmowa (*He wouldn't allow us to speak*),
- ćwiczenia a (która forma pasuje, czasem obie) i b (wybór poprawnej formy) jako 12 kart `multiple-choice`.

Wskazówki z s. 140 o *didn't use to* i *usually* + Present Simple są już w istniejących regułach, więc ich nie powtarzam.

## 4B Obligation and permission

Tabela z s. 140 rozbita na 7 reguł: *must* vs *have to / need to*, *mustn't* vs *don't have to / needn't*, *can / be allowed to*, *should / ought to*, *be supposed to*, *make / let* + bezokolicznik bez *to*, strona bierna *be forced / made / allowed to*.

Ćwiczenie a to 8 KWT (dodane 7 własnych w tym samym stylu). Ćwiczenie b (zasady kursu komputerowego) to 8 luk z regułą w nawiasie (dodane 4 własne). W zdaniu a5 przyjąłem odpowiedź *You can go (leave) if you like*, bo oryginał *You don't have to stay here* znaczy, że można wyjść.

## Paczka

`output/fce-grammar-focus-4a-4b.apkg` (64 notatki, 73 karty):

| Podtalia | Plik | Zawartość |
|----------|------|-----------|
| `4A I'm more cautious::7 Grammar focus` | `fce-grammar-used-to-would-4a-focus.tsv`, `fce-use-of-english-used-to-would-4a-focus.tsv` | 2 reguły, 12 kart wyboru |
| `4B Obligation and permission::1 Grammar` | `fce-grammar-obligation-permission-4b.tsv` | 7 reguł |
| `4B Obligation and permission::2 Gap fill & KWT` | `fce-use-of-english-obligation-permission-4b.tsv` | 15 KWT, 12 open cloze |
| `4B Obligation and permission::3 Translation` | `fce-use-of-english-obligation-permission-4b-translation.tsv` | 16 zdań PL → EN |

Odtworzenie: `python decks/grammar_focus_4a_4b.py`, potem `build_apkg.py` z podtaliami jak wyżej i `--deck "FCE Preparation"`.
