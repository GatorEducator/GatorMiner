"""CLI Entry point"""
import sys
import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
from nltk.probability import FreqDist


from src import analyzer as az
from src import summarizer as sz
from src import arguments

if __name__ == "__main__":
    tm_arguments = arguments.parse(sys.argv[1:])
    directory = tm_arguments.directory
    function = tm_arguments.function
    if function == "frequency":
        print(az.dir_frequency(directory))
    elif function == "summary":
        print(sz.summarizer(directory))

text = "directory"
# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize
# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(text)
token

fdist = FreqDist(token)
fdist

fdist1 = fdist.most_common(10)
fdist1
