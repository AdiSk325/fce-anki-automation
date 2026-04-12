# Skills Guide

## Po co są skills w tym repo

Skills mają uruchamiać powtarzalne, wieloetapowe workflow, które w tym projekcie wracają regularnie. Dzięki temu agent ma jaśniejszy tryb działania, a Ty możesz szybciej wywołać konkretny rodzaj pracy.

Skills zostały zapisane w `.github/skills/` i są projektowe, czyli dotyczą właśnie tego repo jako przestrzeni do przygotowania do FCE.

## Dostępne skills

### `/create-exercise`

Używaj, gdy chcesz dostać nowe ćwiczenie, zestaw zadań, worksheet, mini-test albo homework.

Najlepsze sytuacje:

- chcesz przećwiczyć konkretną gramatykę,
- chcesz zadania pod Writing, Speaking lub Use of English,
- chcesz ćwiczenie celowane w swoje błędy,
- chcesz, żeby materiał został zapisany do repo.

### `/check-exercise`

Używaj, gdy wykonałeś już zadanie i chcesz je sprawdzić, omówić i zapisać wnioski.

Najlepsze sytuacje:

- masz gotowe odpowiedzi do ćwiczenia,
- chcesz poprawę writingu,
- chcesz ocenę mocnych i słabych stron,
- chcesz, żeby błędy trafiły do pamięci użytkownika.

### `/progress-feedback`

Używaj, gdy chcesz syntetycznego obrazu swojej nauki.

Najlepsze sytuacje:

- chcesz wiedzieć, co idzie dobrze,
- chcesz wiedzieć, co blokuje wynik,
- chcesz ustalić priorytety na kolejne dni,
- chcesz raportu na podstawie dotychczasowych materiałów.

### `/memory-checkpoint`

Używaj, gdy repo i pamięć robią się zbyt rozproszone albo gdy kończysz jeden etap nauki i zaczynasz kolejny.

Najlepsze sytuacje:

- pamięć zawiera za dużo szumu,
- cele się zmieniły,
- chcesz uporządkować `User/` i stan postępu,
- chcesz mieć czysty punkt startowy do kolejnych sesji.

### `/gitflow`

Używaj, gdy chcesz zapisać stan nauki i materiałów do git w sensowny sposób.

Najlepsze sytuacje:

- masz większą paczkę zmian,
- chcesz podzielić commity logicznie,
- chcesz, żeby commit odzwierciedlał realny checkpoint nauki,
- chcesz skontrolować, czy `.gitignore` nadal ma sens.

### `/anki-cycle`

Używaj, gdy Anki ma być częścią większego cyklu nauki, a nie tylko generowaniem pliku TSV.

Najlepsze sytuacje:

- chcesz zrobić fiszki z nowych braków,
- chcesz utrwalić materiał z ćwiczeń,
- chcesz połączyć fiszki z aktywnym sprawdzeniem,
- chcesz walidacji i sensownego wpięcia kart w plan nauki.

### `/study-plan`

Używaj, gdy chcesz planu tygodniowego, sprintu, planu powtórkowego albo mini-roadmapy pod mock exam.

Najlepsze sytuacje:

- nie wiesz, na czym się skupić,
- chcesz zbilansować wszystkie papers,
- po słabszym wyniku potrzebujesz planu naprawczego,
- chcesz przejść z chaotycznej nauki do uporządkowanego cyklu.

## Jak wybierać skill

Najprostsza reguła:

- jeśli chcesz nowe zadanie, użyj `/create-exercise`,
- jeśli chcesz sprawdzić gotowe zadanie, użyj `/check-exercise`,
- jeśli chcesz diagnozy i kierunku dalszej pracy, użyj `/progress-feedback`,
- jeśli chcesz uporządkować pamięć i stan repo, użyj `/memory-checkpoint`,
- jeśli chcesz zapisać stan do git, użyj `/gitflow`,
- jeśli pracujesz z fiszkami jako częścią nauki, użyj `/anki-cycle`,
- jeśli chcesz planu, użyj `/study-plan`.

## Dobra praktyka

- Nie musisz zawsze wywoływać skill ręcznie. Dobrze opisane skills mogą być też dobierane automatycznie przez agenta.
- Im bardziej konkretny opis zadania podasz, tym lepiej skill zadziała.
- Najlepszy efekt daje łączenie skills w cyklu, na przykład:
  1. `/create-exercise`
  2. `/check-exercise`
  3. `/progress-feedback`
  4. `/study-plan`

## Przykładowe wywołania

```text
/create-exercise second conditional, 12 zadań, poziom B2, pod moje częste błędy
```

```text
/check-exercise sprawdź mój writing part 2 i zapisz feedback oraz corrected
```

```text
/progress-feedback podsumuj moje ostatnie 2 tygodnie pracy i powiedz, co teraz robić
```

```text
/anki-cycle zrób fiszki z błędów z ostatniego writingu i przygotuj krótkie ćwiczenie kontrolne
```