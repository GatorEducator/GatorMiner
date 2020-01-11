"""Where NLP modules should be in"""
from collections import Counter
import re
from typing import List, Tuple
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer


def read_file(path: str):
    """ read file from path """
    with open(path) as input_file:
        data = input_file.read().lower()
        return data


def normalize(data: str) -> List[str]:
    """Remove numbers, single characters, to lowercase"""
    data = data.lower()
    normalized_data = re.sub(r"\b[a-zA-Z]\b|\b[0-9]+\b", "", data)
    return normalized_data


def tokenize(raw_text: str) -> List[str]:
    """break down text into a list of lemmatized tokens"""
    parser = spacy.load("en_core_web_sm")
    text = normalize(raw_text)
    tokens = parser(text)
    # lemmatize tokens
    tokens = [
        word.lemma_.strip()
        for word in tokens
        if word.lemma_ != "-PRON-" and word.is_stop is False
    ]
    tokens = [word for word in tokens if len(word) > 1]
    return tokens


def compute_tfidf(data: List[str]) -> None:
    """Compute the TFIDF"""
    tfidf = TfidfVectorizer()
    tfs = tfidf.fit_transform([" ".join(data)])  # make data iterable for TFIDF
    feature_names = tfidf.get_feature_names()
    for col in tfs.nonzero()[1]:
        print(feature_names[col], " - ", tfs[0, col])
    return tfs, tfidf


def compute_frequency(input_raw: str) -> List[Tuple[str, int]]:
    """Compute word frequency"""
    words = tokenize(input_raw)
    word_freq = Counter(words)
    return word_freq.most_common(50)


def named_entity_recognization(input_text):
    """identifies important elements like places, people, organizations, and
    languages within an input string of text"""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)
    for entity in doc.ents:
        print(entity, entity.label_)
    spacy.displacy.serve(doc, style="ent")
