# podstawy_jezyka_python

Moje rozwiązania zadań z podstaw Pythona. Każda część ma swój folder w `source/` i własne README
z opisem zadań i uwagami.

| Część | Co to jest | Opis |
|-------|-----------|------|
| `zad1` | 20 ćwiczeń z konsoli: Zen of Python, zmienne, napisy, liczby, logika | [source/zad1](source/zad1/README.md) |
| `zad2` | 11 małych programów z konsoli: temperatura, hasło, kalkulator i inne | [source/zad2](source/zad2/README.md) |
| `zad3` | 5 zadań z warunkami: trójkąt, silnia, film, wypłata | [source/zad3](source/zad3/README.md) |
| `zad4` | 11 zadań z warunkami i pętlami: liczby pierwsze, zgadywanie, sumowanie | [source/zad4](source/zad4/README.md) |
| `web_scraper` | pobieranie komentarzy ze strony i analiza słów (spaCy, wykres) | [source/web_scraper](source/web_scraper/README.md) |
| `zad_gui` | 13 zadań z tkintera w jednym oknie z listą | [source/zad_gui](source/zad_gui/README.md) |

## Wymagania

- Python 3.12 (wersja przypięta w `.python-version`) i [uv](https://docs.astral.sh/uv/)
- tkinter, ale tylko do `zad_gui`. 


Zadania `zad1`-`zad4` i `zad_gui` używają tylko biblioteki standardowej. Pakiety zewnętrzne
(`requests`, `beautifulsoup4`, `spacy`, `matplotlib`, model `pl_core_news_sm`) są potrzebne tylko do scrapera.

## Instalacja

```sh
uv sync
```

Tworzy `.venv` i instaluje wszystko z `pyproject.toml`.

## Uruchamianie

Wszystko odpala się z katalogu `source/`:

```sh
cd source
uv run python -m zad1.main
uv run python -m zad2.main
uv run python -m zad3.main
uv run python -m zad4.main
uv run python -m zad_gui.main
uv run python -m web_scraper.main https://adres-strony
```

W menu konsolowym (`zad1`-`zad4`) wpisuje się numer ćwiczenia i Enter, a pusty Enter kończy program.

## Co gdzie leży

```
source/
  console_io.py    wspólne: wczytywanie liczb od użytkownika i pętla menu
  zad1/ ... zad4/  ćwiczenia konsolowe (main.py = menu, reszta = ćwiczenia pogrupowane tematycznie)
  web_scraper/     scraper.py (pobieranie), analysis.py (analiza), main.py (cały przebieg)
  zad_gui/         main.py (okno startowe) i tasks/ (jedno okno tkinter na plik)
```

W ćwiczeniach konsolowych każde ćwiczenie to osobna funkcja. Tam, gdzie dało się to łatwo oddzielić,
samo liczenie siedzi w osobnej funkcji (np. `compare`, `is_prime`), a wczytywanie i wypisywanie robi
funkcja obok, dzięki temu liczenie można sprawdzić bez klikania.
