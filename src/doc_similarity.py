from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def cosine_similarity(pair):

    doc_1, doc_2 = pair

    # text to vector
    vectorizer = CountVectorizer()
    all_sentences_to_vector = vectorizer.fit_transform([doc_1, doc_2])
    text_to_vector_v1 = all_sentences_to_vector.toarray()[0].tolist()
    text_to_vector_v2 = all_sentences_to_vector.toarray()[1].tolist()

    # distance of similarity
    cosine = distance.cosine(text_to_vector_v1, text_to_vector_v2)
    print(
        "Similarity of two sentences are equal to ", round((1 - cosine) * 100, 2), "%"
    )
    return cosine


# text_lst = ["normalized text1", "normalized text2"]
# vectorizer = TfidfVectorizer(min_df=0.0, max_df=1.0, ngram_range=(1,1))
#
# # calculate the feature matrix
# feature_matrix = vectorizer.fit_transform(text_lst).astype(float)


key_lst = ["author 1", "author 2", "author 3", "author 4", "author 5"]


def create_pair(key_lst):
    pairs = []
    # create a list of tuples
    for i, v in enumerate((key_lst)):
        for key in key_lst[i+1:]:
            pairs.append((v, key))

    return pairs


print(create_pair(key_lst))
