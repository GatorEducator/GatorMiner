"""Where NLP modules should be in"""
import re
from typing import List, Tuple
import nltk
# import matplotlib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = PorterStemmer()
token_dict = {}


def read_file(path: str):
    """ read file from path """
    with open(path) as input_file:
        data = input_file.read().lower()
        return data


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return tokens


def normalize(data):
    data = re.sub(r"\b[a-zA-Z]\b", " ", data)
    data = re.sub(r"\b[0-9]+\b", " ", data)
    data = re.sub(r"[\W_]", " ", data)
    stop_words = set(stopwords.words('english'))
    # filtered_sentence = [w for w in data if w not in stop_words]
    filtered_str = [w for w in tokenize(data) if w not in stop_words]
    result = [' '.join(filtered_str)]
    # token_dict['file'] = data
    return result


def word_freq(input_raw: str) -> List[Tuple[str, int]]:
    """Take raw input text and return top 50 most frequent in list of tuple"""
    # regex remove numbers, single characters, and non-alphanumeric
    input_raw = re.sub(r"\b[a-zA-Z]\b", " ", input_raw)
    input_raw = re.sub(r"\b[0-9]+\b", " ", input_raw)
    input_raw = re.sub(r"[\W_]", " ", input_raw)
    # set stop words from the nltk library
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(input_raw)  # breakdown text into a list of tokens
    # remove stopwords
    filtered_sentence = [w for w in tokens if w not in stop_words]
    # words = [w.lower() for w in filtered_sentence]
    # vocab = sorted(set(words)) # return all the vocabs used in the text
    freqdict = nltk.FreqDist(words)
    # freqdict.plot()  # plot frequency
    return freqdict.most_common(50)


if __name__ == '__main__':
    # text_stems = tokenize(read_file("samples/sample_reflection.txt"))
    result = normalize(read_file("samples/sample_reflection.txt"))
    # tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfidf = TfidfVectorizer()
    # print(result)
    # tfs = tfidf.fit_transform(token_dict.values())
    tfs = tfidf.fit_transform(result)
    feature_names = tfidf.get_feature_names()
    for col in tfs.nonzero()[1]:
        print(feature_names[col], ' - ', tfs[0, col])
    # print(tfs)
