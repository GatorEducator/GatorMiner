"""Entry point"""
import sys
from analyzer import normalize, read_file, word_freq, computeTfIDF

if __name__ == '__main__':
    TFIDF = normalize(read_file(sys.argv[1]))
    FREQ = word_freq(read_file(sys.argv[1]))
    # print(FREQ)
    computeTfIDF(TFIDF)
