# zad_gui - tkinter

13 zadań z gui zebranych w jednym oknie startowym. Kliknięcie w zadanie otwiera je w osobnym oknie,
na środku ekranu i na pierwszym planie.

```sh
cd source
uv run python -m zad_gui.main
```

Pojedyncze zadanie bez okna startowego, np. konwerter:

```sh
uv run python -m zad_gui.tasks.converter
```

## Zadania

| # | Zadanie | Plik w `tasks/` |
|---|---------|-----------------|
| 1 | Formularz logowania | `login.py` |
| 2 | Zgody użytkownika | `consents.py` |
| 3 | Wybór języka programowania | `language.py` |
| 4 | Lista zakupów | `shopping_list.py` |
| 5 | Notatnik z polem Text | `notepad.py` |
| 6 | Formularz ankiety | `survey.py` |
| 7 | Menu i pliki | `notepad_files.py` |
| 8 | Konwerter jednostek | `converter.py` |
| 9 | Lista studentów | `students.py` |
| 10 | Ustawienia w zakładkach | `settings.py` |
| 11 | Minutnik | `timer.py` |
| 12 | Paint | `paint.py` |
| 13 | Projekt własny - edytor tekstu | `text_editor.py` |

## Pliki

- `main.py` - okno startowe z listą zadań
- `tasks/__init__.py` - wspólne: ustawianie rozmiaru i środkowanie okna (`show_centered`), uruchamianie jednego okna (`run_standalone`)
- `tasks/*.py` - jedno okno tkinter na plik, każde ma swój rozmiar w `SIZE`

## Uwagi

- Wyniki (dane z logowania, zapisana notatka, zgody, ustawienia) pokazują się w oknach messagebox.
- Zadania 7 i 13 mają menu Plik i dodatkowo przyciski Nowy / Otwórz / Zapisz w oknie. Skróty: Ctrl+N, Ctrl+O, Ctrl+S.
- Zadanie 10: rozmiar czcionki i kolor zmieniają tylko podgląd w zakładce Wygląd, nie całą aplikację.
- Zadanie 12: menu z gumką otwiera się prawym przyciskiem myszy, na Macu to Ctrl+klik albo klik dwoma palcami.
- Zadanie 13: Ctrl+F otwiera okno szukania z podświetlaniem, na pasku stanu jest licznik słów.
  Słowem jest fragment między spacjami, w którym jest litera lub cyfra.
