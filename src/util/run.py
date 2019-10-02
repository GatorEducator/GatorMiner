"""Entry point"""
import sys
from analyzer import read_file
from analyzer import word_freq

if __name__ == '__main__':
    FREQ = word_freq(read_file(sys.argv[1]))
    print(FREQ)
