"""Where NLP modules should be in"""
import sys
import nltk
import matplotlib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def read_file(path):
    with open(path) as input_file:
        data = input_file.read()
        return data


if __name__ == '__main__':
    raw_data = read_file("samples/sample_reflection.txt")
    stop_words = set(stopwords.words('english'))  # set stop words
    tokens = word_tokenize(raw_data)

    filtered_sentence = [w for w in tokens if w not in stop_words]

    # print(filtered_sentence)

    text = nltk.Text(tokens)
    words = [w.lower() for w in text]
    vocab = sorted(set(words))
    freqdict = nltk.FreqDist(text)
    # freqdict.plot()  # plot frequency
    # print(freqdict.most_common(50))
    # print(freqdict)
