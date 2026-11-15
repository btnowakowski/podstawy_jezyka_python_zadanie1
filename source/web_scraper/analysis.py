import re
from collections import Counter

import spacy
from spacy.lang.pl import STOP_WORDS

MODEL_NAME = "pl_core_news_sm"


def tokenize(text):
    # letters only, so digits and punctuation never become tokens
    return re.findall(r"[^\W\d_]+", text.lower())


def remove_stop_words(tokens, stop_words=STOP_WORDS):
    return [token for token in tokens if token not in stop_words]


def lemmatize(comments, stop_words=STOP_WORDS):
    nlp = spacy.load(MODEL_NAME)
    lemmas = []
    for doc in nlp.pipe(comments):
        for token in doc:
            lemma = token.lemma_.lower()
            if lemma.isalpha() and lemma not in stop_words:
                lemmas.append(lemma)
    return lemmas


def count_words(words):
    return Counter(words)
