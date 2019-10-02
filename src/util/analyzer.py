"""Where NLP modules should be in"""
import sys
import nltk
import string
import matplotlib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def read_file(path):
    with open(path) as input_file:
        data = input_file.read()
        return data


if __name__ == '__main__':
    raw_data = read_file("samples/sample_reflection.txt")
    raw_data = ''.join(c for c in raw_data if not c.isdigit())
    stop_words = set(stopwords.words('english'))  # set stop words
    punc = set(string.punctuation)
    stop_words.update(punc)
    tokens = word_tokenize(raw_data)

    filtered_sentence = [w for w in tokens if w not in stop_words]

    # print(filtered_sentence)

    text = nltk.Text(filtered_sentence)
    words = [w.lower() for w in text]
    # vocab = sorted(set(words)) # all the vocabs used in the text
    freqdict = nltk.FreqDist(words)
    # freqdict.plot()  # plot frequency
    print(freqdict.most_common(50))
    # print(freqdict)
