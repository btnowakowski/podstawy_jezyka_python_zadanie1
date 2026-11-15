import requests
from bs4 import BeautifulSoup, UnicodeDammit


def download_page(url, timeout=15):
    response = requests.get(url, timeout=timeout)
    if response.status_code != 200:
        raise RuntimeError(f"Nie udało się pobrać strony, status: {response.status_code}")
    # when the header names a charset requests decodes correctly, otherwise it would guess latin-1
    if "charset" in response.headers.get("Content-Type", "").lower():
        return response.text
    return UnicodeDammit(response.content, is_html=True).unicode_markup or response.text


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup


def extract_comments(soup):
    authors = []
    comments = []
    for block in soup.select("div.comment.clearfix"):
        author = block.select_one('strong[itemprop="author"]')
        text = block.select_one('p[itemprop="description"]')
        if author is None or text is None:
            continue
        text = text.get_text(" ", strip=True)
        if text:
            authors.append(author.get_text(" ", strip=True))
            comments.append(text)
    return authors, comments
