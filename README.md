# podstawy_jezyka_python

Moje rozwiązania zadań z podstaw Pythona. Są tu trzy osobne części:

- `zad1` - 20 krótkich ćwiczeń z konsoli (zmienne, napisy, liczby, logika),
- `zad2` - 11 małych programów z konsoli (temperatura, hasło, kalkulator i kilka innych),
- `zad_gui` - 13 zadań z tkintera, zebranych w jednym oknie, z którego się je odpala.

## Co jest potrzebne

Python 3.12 i uv. Do zadań z okienkami Python musi mieć tkintera.

```sh
uv sync
```

## Jak uruchamiać

Wszystko odpala się z katalogu `source/`:

```sh
cd source
uv run python -m zad1.main      # menu ćwiczeń 1-20
uv run python -m zad2.main      # menu ćwiczeń 1-11
uv run python -m zad_gui.main   # okno z listą zadań gui
```

W menu konsolowym wpisuje się numer ćwiczenia i Enter, a pusty Enter kończy program.
Pojedyncze zadanie z okienkiem można odpalić też bez menu, np. `uv run python -m zad_gui.tasks.converter`.

## Co gdzie leży

```
source/
  console_io.py    wczytywanie liczb od użytkownika
  zad1/
    main.py        menu
    basics.py      import this, zasady Zen, tekst powitalny
    variables.py   zmienne, typy, konwersje, input
    strings.py     napisy: indeksy, łączenie, wielkie litery, odwracanie
    integers.py    działania, parzystość, lista 1-10, podzielność przez 3
    floats.py      pole koła, zaokrąglanie, średnia
    booleans.py    czy liczba jest większa niż 10
  zad2/
    main.py        menu
    numbers.py     ćwiczenia na liczbach (temperatura, wiek, średnia, porównanie, kalkulator)
    text.py        ćwiczenia na tekście (powitanie, liczenie znaków, hasło, powielanie, quiz)
  zad_gui/
    main.py        okno startowe z listą zadań
    tasks/         po jednym pliku na każde okno tkinter
```

W obu menu ćwiczenie to zwykła funkcja w jednym z modułów. Tam, gdzie dało się to łatwo oddzielić,
samo liczenie jest osobną funkcją (np. `compare`, `is_password_valid`), a wczytywanie i wypisywanie
robi funkcja obok, dzięki temu liczenie można sprawdzić bez klikania.

## Zadania tkinter

Wyniki (np. dane z logowania, zapisana notatka) pokazują się w oknach messagebox.

1. logowanie, 2. zgody - `login.py`, `consents.py`
3. wybór języka, 4. lista zakupów - `language.py`, `shopping_list.py`
5. notatnik, 6. ankieta - `notepad.py`, `survey.py`
7. notatnik z menu i plikami, 8. konwerter, 9. lista studentów, 10. ustawienia -
   `notepad_files.py`, `converter.py`, `students.py`, `settings.py`
11. minutnik, 12. paint, 13. edytor tekstu z szukaniem i licznikiem słów -
    `timer.py`, `paint.py`, `text_editor.py`

## Do zapamiętania

- `import this` pokazuje tekst tylko za pierwszym razem, drugi wybór w menu nic nie wypisze.
