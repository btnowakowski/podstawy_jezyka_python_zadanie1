import sys

import matplotlib.pyplot as plt
import requests

from web_scraper import analysis, scraper

TOP_N = 10
OUTPUT_FILE = "najczestsze_slowa.txt"


def show_chart(top_words):
    words = [word for word, _ in top_words]
    counts = [count for _, count in top_words]
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts)
    plt.title("Najczęstsze słowa w komentarzach")
    plt.xlabel("Słowo (lemat)")
    plt.ylabel("Liczba wystąpień")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def save_top_words(top_words, path=OUTPUT_FILE):
    with open(path, "w", encoding="utf-8") as f:
        for word, count in top_words:
            f.write(f"{word}: {count}\n")


def main():
    print("Interpreter:", sys.executable)

    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    url = args[0] if args else input("Adres strony z komentarzami: ").strip()

    try:
        html = scraper.download_page(url)
    except (requests.RequestException, RuntimeError) as exc:
        print(f"Błąd: {exc}")
        return
    print("Strona pobrana poprawnie.")

    soup = scraper.parse_html(html)
    authors, comments = scraper.extract_comments(soup)
    if not comments:
        print("Nie znaleziono komentarzy na tej stronie.")
        return
    for author, comment in zip(authors, comments):
        print(f"{author}: {comment}")

    text = " ".join(comments)
    tokens = analysis.tokenize(text)
    filtered = analysis.remove_stop_words(tokens)
    print("\nPrzykładowe tokeny:", tokens[:10])
    print("Bez stopwords:", filtered[:10])
    print(f"Słowa: {len(filtered)}, unikalne: {len(set(filtered))}")

    lemmas = analysis.lemmatize(comments)
    counts = analysis.count_words(lemmas)
    print("\nPrzykładowe lematy:", lemmas[:10])

    print(f"\nLiczba komentarzy: {len(comments)}")
    print(f"Liczba znaków: {len(text)}")
    print(f"Słowa po lematyzacji: {len(lemmas)}, unikalne lematy: {len(counts)}")

    if not counts:
        print("\nBrak słów do analizy (same stopwords, cyfry lub znaki).")
        return

    top_words = counts.most_common(TOP_N)
    print(f"\n{TOP_N} najczęstszych lematów:")
    for word, count in top_words:
        print(f"{word}: {count}")

    if "--save" in sys.argv:
        save_top_words(top_words)
        print(f"Zapisano do {OUTPUT_FILE}")

    show_chart(top_words)


if __name__ == "__main__":
    main()
