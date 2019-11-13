"""Entry point"""
import sys
from analyzer import normalize, read_file, word_freq, compute_TfIDF
from summary import summarizer

if __name__ == '__main__':
    TFIDF = normalize(read_file(sys.argv[1]))
    FREQ = word_freq(read_file(sys.argv[1]))
    # print(FREQ)
    compute_TfIDF(TFIDF)
    print("\n\n")
    print("___________________________________________")
    print("Printing synopsis of student reflections...")
    print("___________________________________________")
    print("\n\n")
    summarizer()
