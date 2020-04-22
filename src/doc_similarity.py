from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np


def create_pair(key_lst):
    pairs = []
    # create a list of tuples
    for i, v in enumerate((key_lst)):
        for key in key_lst[i + 1 :]:
            pairs.append((v, key))

    return pairs


def tfidf_cosine_similarity(pair):

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


text_lst = ["normalized text1", "normalized text2"]

key_lst = ["author 1", "author 2", "author 3", "author 4", "author 5"]


print(create_pair(key_lst))
