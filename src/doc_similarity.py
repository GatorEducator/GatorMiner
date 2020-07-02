import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer


def create_pair(key_lst):
    """Create non-repetitive pairs from two lists"""
    pairs = []
    # create a list of tuples
    for i, v in enumerate((key_lst)):
        for key in key_lst[i + 1:]:
            pairs.append((v, key))

    return pairs


def tfidf_cosine_similarity(pair):
    """Use tfidf vector to calucate similarity of two documents"""
    doc_1, doc_2 = pair

    # text to vector
    vectorizer = TfidfVectorizer(min_df=0.0, max_df=1.0, ngram_range=(1, 1))
    # calculate the feature matrix
    feature_matrix = vectorizer.fit_transform([doc_1, doc_2]).astype(float)
    doc_v1 = feature_matrix.toarray()[0].tolist()
    doc_v2 = feature_matrix.toarray()[1].tolist()

    # compute cosine similarity manually
    cosine_similarity = np.dot(doc_v1, doc_v2)

    return cosine_similarity


def spacy_doc_similarity(pair):
    PARSER = spacy.load("en_core_web_sm")
    doc_1, doc_2 = pair
    doc_1 = PARSER(doc_1)
    doc_2 = PARSER(doc_2)
    similarity = doc_1.similarity(doc_2)
    return similarity
