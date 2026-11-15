# web_scraper

Pobiera komentarze ze wskazanej strony, czyści tekst, usuwa stopwords, lematyzuje polskim modelem
spaCy, pokazuje statystyki i rysuje wykres 10 najczęstszych słów.

## Wymagania

Potrzebne są `requests`, `beautifulsoup4`, `spacy`, `matplotlib` i model `pl_core_news_sm`.
Wszystko jest w `pyproject.toml`, wystarczy `uv sync` w katalogu głównym (model ma ok. 20 MB
i pobiera się z oficjalnych wydań spaCy na GitHubie).

## Uruchamianie

Z katalogu `source/`:

```sh
uv run python -m web_scraper.main https://adres-strony
uv run python -m web_scraper.main https://adres-strony --save
```

- bez adresu program zapyta o niego po uruchomieniu,
- `--save` dodatkowo zapisuje 10 najczęstszych słów do pliku `najczestsze_slowa.txt` w bieżącym katalogu.

## Jak to działa

1. Wypisuje ścieżkę używanego interpretera Pythona.
2. Pobiera stronę (`scraper.download_page`), przerywa z komunikatem, gdy status jest inny niż 200.
3. Parsuje HTML i usuwa `<script>` oraz `<style>` (`scraper.parse_html`).
4. Wyciąga komentarze: bloki `div.comment.clearfix`, w nich autor w `strong[itemprop=author]`
   i tekst w `p[itemprop=description]`. Pomija bloki bez autora albo z pustym tekstem
   (`scraper.extract_comments`).
5. Dzieli tekst na słowa (same litery, małymi literami), usuwa stopwords i liczy słowa i unikalne słowa
   (`analysis.tokenize`, `analysis.remove_stop_words`).
6. Lematyzuje każdy komentarz, odrzuca stopwords i słowa z nie-literami (`analysis.lemmatize`).
7. Wypisuje liczbę komentarzy, liczbę znaków, liczbę słów po lematyzacji i unikalnych lematów.
8. Wypisuje 10 najczęstszych lematów i pokazuje wykres słupkowy (`main.show_chart`).

## Pliki

- `main.py` - cały przebieg, wykres i zapis do pliku
- `scraper.py` - pobranie strony i wyciągnięcie komentarzy
- `analysis.py` - tokenizacja, stopwords, lematyzacja, liczenie

## Przypadki brzegowe, które program obsługuje

- strona bez komentarzy, bez autora lub z pustym tekstem komentarza,
- tekst komentarza z tagami w środku (`<a>`, `<em>`, `<br>`): słowa się nie sklejają,
- różne kodowania: UTF-8 bez nagłówka, windows-1250 i ISO-8859-2 (w nagłówku albo w `<meta>`),
- błąd HTTP (403, 404, 500...), pętla przekierowań, timeout (15 s), brak połączenia, adres bez `http://`,
- komentarze z samych stopwords, cyfr i znaków: program mówi, że nie ma czego analizować, i nie rysuje wykresu,
- mniej niż 10 różnych słów: wykres pokazuje tyle, ile jest.

## Uwagi

- Polecenie nie podawało adresu strony, więc trzeba go wskazać samemu. Selektory pasują do stron z układem
  opisanym wyżej, na innych stronach program napisze, że nie znalazł komentarzy.
- Wykres otwiera się w osobnym oknie, program kończy się po jego zamknięciu.
