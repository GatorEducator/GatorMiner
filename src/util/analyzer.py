"""Where NLP modules should be in"""
from collections import Counter
import re
from typing import List, Tuple
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

PARSER = spacy.load("en_core_web_sm")


def read_file(path: str):
    """ read file from path """
    with open(path) as input_file:
        data = input_file.read()
        return data


def normalize(data: str) -> List[str]:
    """Remove numbers, single characters, to lowercase"""
    data = data.lower()
    normalized_data = re.sub(r"\b[a-zA-Z]\b|\b[0-9]+\b", "", data)
    return normalized_data


def sentence_tokenize(input_text):
    """tokenize paragraph to a list of sentences"""
    sent_lst = []
    sent_pipe = PARSER.create_pipe('sentencizer')
    PARSER.add_pipe(sent_pipe)
    doc = PARSER(input_text)
    for sent in doc.sents:
        sent_lst.append(sent.text)
    return sent_lst


def part_of_speech(input_text):
    """part of speech tagging of sentence"""
    doc = PARSER(input_text)
    pos_lst = []
    for word in doc:
        pos_lst.append(word.text, word.pos_)
    return pos_lst


def tokenize(raw_text: str) -> List[str]:
    """break down text into a list of lemmatized tokens"""
    text = normalize(raw_text)
    tokens = PARSER(text)
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
    tfidf_vectorizer = TfidfVectorizer()
    # make data iterable for TFIDF
    tfs = tfidf_vectorizer.fit_transform([" ".join(data)])
    feature_names = tfidf_vectorizer.get_feature_names()
    for col in tfs.nonzero()[1]:
        print(feature_names[col], " - ", tfs[0, col])
    return tfs, tfidf_vectorizer


def compute_count_vectorize(data):
    """Compute the count vectorize matrix"""
    count_vectorizer = CountVectorizer()
    count = count_vectorizer.fit_transform(data)
    return count, count_vectorizer


def compute_frequency(input_raw: str) -> List[Tuple[str, int]]:
    """Compute word frequency"""
    words = tokenize(input_raw)
    word_freq = Counter(words)
    return word_freq.most_common(50)


def named_entity_recognization(input_text):
    """identifies important elements like places, people, organizations, and
    languages within an input string of text"""
    doc = PARSER(input_text)
    for entity in doc.ents:
        print(entity, entity.label_)
    spacy.displacy.serve(doc, style="ent")
    # display in jupyter notebook
    # displacy.render(about_interest_doc, style='dep', jupyter=True)


def noun_phrase(input_text):
    """Extract noun phrases of the document in a list"""
    doc = PARSER(input_text)
    n_phrase_lst = []
    for chunk in doc.noun_chunks:
        n_phrase_lst.append(chunk)
    return n_phrase_lst
