"""Entry point"""
import sys
from analyzer import normalize, read_file, word_freq, compute_TfIDF


if __name__ == "__main__":
    TFIDF = normalize(read_file(sys.argv[1]))
    FREQ = word_freq(read_file(sys.argv[1]))
    # print(FREQ)
    compute_TfIDF(TFIDF)
