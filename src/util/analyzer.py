"""Where NLP modules should be in"""
import re
from typing import List, Tuple
import nltk
# import matplotlib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer


def read_file(path: str):
    """ read file from path """
    with open(path) as input_file:
        data = input_file.read()
        return data


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
    words = [w.lower() for w in filtered_sentence]
    # vocab = sorted(set(words)) # return all the vocabs used in the text
    freqdict = nltk.FreqDist(words)
    # freqdict.plot()  # plot frequency
    return freqdict.most_common(50)
