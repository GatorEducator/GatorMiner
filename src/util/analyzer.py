"""Where NLP modules should be in"""
import re
from typing import List, Tuple
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("punkt")

stemmer = PorterStemmer()


def read_file(path: str):
    """ read file from path """
    with open(path) as input_file:
        data = input_file.read().lower()
        return data


def tokenize(text: str) -> List[str]:
    """break down text into a list of tokens and remove
    the commoner morphological and inflexional endings"""
    tokens = word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems


def normalize(data: str) -> List[str]:
    """Remove single characters, numbers, and stop words"""
    # regex remove numbers, single characters, and non-alphanumeric
    data = re.sub(r"\b[a-zA-Z]\b", " ", data)
    data = re.sub(r"\b[0-9]+\b", " ", data)
    data = re.sub(r"[\W_]", " ", data)
    # set stop words from the nltk library
    stop_words = set(stopwords.words("english"))
    # remove stopwords
    filtered_str = [w for w in tokenize(data) if w not in stop_words]
    return filtered_str


def compute_TfIDF(data: List[str]) -> None:
    """Compute the TFIDF"""
    # remove stopwords again from sklearn pacakge
    tfidf = TfidfVectorizer(stop_words="english")
    tfs = tfidf.fit_transform([" ".join(data)])  # make data iterable for TFIDF
    feature_names = tfidf.get_feature_names()
    for col in tfs.nonzero()[1]:
        print(feature_names[col], " - ", tfs[0, col])


def word_freq(input_raw: str) -> List[Tuple[str, int]]:
    """Compute word frequency"""
    words = normalize(input_raw)
    freqdict = nltk.FreqDist(words)
    return freqdict.most_common(50)
