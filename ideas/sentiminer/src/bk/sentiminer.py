#!/usr/bin/env python3

__author__ = "Oliver Bonham-Carter"
__date__ = "29 November 2018"

# program to determine a sentiment score from a user entered sentence or a file.


def help():
    """ Help function to show how to use the program"""
    print("  ", __author__, "::", __date__)
    print(
        "\n   Program to read in a sentence, load a sentiment file and then analyse and plt the text's sentiment content"
    )
    print(
        "\n   Program takes parameters 'S' for 'sentence' otherwise a filename will be prompted "
    )
    print("   Run: ./sentimate.py s ")
    print("   Run: ./sentimate.py f <file>")


# end of help()


def getSentiments(csvfile):
    """opens the file csv file containing finn sentiment words"""
    word_dict = {}
    with open(csvfile, newline="") as csvfile:
        datareader = csv.reader(csvfile, delimiter=",")
        for row in datareader:
            word_dict[row[0]] = row[1]
    return word_dict


# end of getSentiments()


def getSentence():
    """ask the user to enter something to evaluate"""
    data_str = input("Enter a sentence to scan for sentiment : ")
    print(" Your input is: ", data_str, type(data_str))

    return data_str.split()  # return a list


# end of getSentence()


def getFile(fname):
    """open textfile name to load and extract text"""
    # fname = input("  Enter the name of the file :")
    data_str = ""
    try:
        with open(fname) as file:
            for line in file:
                data_str = data_str + line
                data_str = data_str.replace("\n", " ")
        # print("contents: ",data_str, type(data_str))
    except FileNotFoundError:
        print("Error with finding the file... exiting")
        exit()
    data_str = data_str.lower()
    # remove basic punctuation
    punctuation = "!`':,?.()/\\"
    for p in punctuation:
        data_str = data_str.replace(p, " ")
    return data_str.split()  # return a list


# end of getFile()


def studySentiment(text_list, sentiments_dict):
    """function to to determine the sentiment score from the text."""
    score = 0  # current score of the sentimental words
    hits = 0  # the number of words which have a sentiment value
    for i in text_list:
        # print("   Current word: ",i)
        try:
            wordScore_int = int(sentiments_dict[i])
            print("  ", i, "    score: ", wordScore_int)
            score = score + wordScore_int
            hits = hits + 1
        except KeyError:
            # print("  <<",i,">> Word not found in sentiments_dict...")
            pass
    print("  score :", score)
    print("  score/hits:", score / hits)


# end of studySentiment()


def begin(in_str, inFile=""):
    """begin the program."""
    text_list = ""
    if in_str.lower() == "f":
        text_list = getFile(inFile)

    else:
        text_list = getSentence()

    print("  Contents : ", text_list, type(text_list))
    csvfile = "finn.csv"
    sentiments_dict = getSentiments(csvfile)
    print("  Analyzing the sentiment score of text... ")
    studySentiment(text_list, sentiments_dict)


# end of begin()

# command line paramters code
###################################
# import itertools, sys
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator
# from collections import namedtuple
import csv, sys, re


if __name__ == "__main__":

    if len(sys.argv) == 2:  # user enters a sentence
        begin(sys.argv[1])
        exit()

    if len(sys.argv) == 3:  # two options ["f", "filename"] added to command line
        begin(sys.argv[1], sys.argv[2])
    else:
        # if len(sys.argv) == 2: #one option added to command line
        #   begin(sys.argv[1])
        # else:
        help()
        sys.exit(0)


# plotting notes...

# n_groups = 5

# means_men = (20, 35, 30, 35, 27)
# std_men = (2, 3, 4, 1, 2)

# means_women = (25, 32, 34, 20, 25)
# std_women = (3, 5, 2, 3, 3)

# fig, ax = plt.subplots()

# index = np.arange(n_groups)
# bar_width = 0.35

# opacity = 0.4
# error_config = {'ecolor': '0.3'}

# rects1 = ax.bar(index, means_men, bar_width,
#                alpha=opacity, color='b',
#                yerr=std_men, error_kw=error_config,
#                label='Men')

# rects2 = ax.bar(index + bar_width, means_women, bar_width,
#                alpha=opacity, color='r',
#                yerr=std_women, error_kw=error_config,
#                label='Women')

# ax.set_xlabel('Group')
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(index + bar_width / 2)
# ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
# ax.legend()

# fig.tight_layout()
# plt.show()
