#!/usr/bin/env python3


DATE = "31 July 2019"
VERSION = "i"
AUTHOR = " myName"
AUTHORMAIL = "@allegheny.edu"

# directories, if necessary ...
#OUTPUT_DIR = "/tmp/0out/" # all results are saved in this local directory
#OUTPUT_DIR = "0out/" # all results are saved in this local directory
#INPUT_DIR = "data/"


def help():
	h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
	print("  "+len(h_str) * "-")
	print(h_str)
	print("  "+len(h_str) * "-")

	print("\n\t A program to determine a sentiment score")

	print("\t from a user entered sentence or a file.")
	platform_str = get_platformType()

	print("\n\t [+] Program takes parameters 'S' for 'sentence'\n\t otherwise a filename will be prompted ")
	command_str               = "\n\t   - Enter a sentence: ./sentimate.py s"
	command_str = command_str + "\n\t   - Enter a textfile: ./sentimate.py f <file>"

	print("\n\t [+] OS type: ",platform_str) # determine what the os is.
	#print("""\n\tLibrary installation notes:""")
	command_str = "USAGE:" + command_str
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		print("\t [+] \U0001f600 ", command_str)
	else:
		print("\t+ :-) ", command_str)
	#print("\t [+] INPUT directory (your data files are here)     : ",INPUT_DIR)
	#print("\t [+] OUTPUT directory (your output is placed here)  : ",OUTPUT_DIR)
#end of help()

def get_platformType():
    """Function to dermine the OS type."""
    platforms = {
        'darwin' : 'OSX',
        'win32'  : 'Windows',
        'linux1' : 'Linux',
        'linux2' : 'Linux'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]
#end of get_platformType()



def old_help():
        """ Help function to show how to use the program"""
        print("  ",__author__,"::",__date__)
        print("\n   Program to read in a sentence, load a sentiment file and then analyse and plt the text's sentiment content")
        print("\n   Program takes parameters 'S' for 'sentence' otherwise a filename will be prompted ")
        print("   Run: ./sentimate.py s ")
        print("   Run: ./sentimate.py f <file>")
#end of help()



def getSentiments(csvfile):
    """opens the file csv file containing finn sentiment words"""
    word_dict = {}
    with open(csvfile, newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        for row in datareader:
            word_dict[row[0]] = row[1]
    return word_dict
#end of getSentiments()



def getSentence():
    """ask the user to enter something to evaluate"""
    data_str = input("Enter a sentence to scan for sentiment : ")
    print("\t [+] Your input is: ",data_str, type(data_str))

    return data_str.split() #return a list
#end of getSentence()



def getFile(fname):
    """open textfile name to load and extract text"""
    #fname = input("  Enter the name of the file :")
    data_str = ""
    try:
        with open(fname) as file:
            for line in file:
                data_str = data_str + line
                data_str = data_str.replace("\n"," ")
        #print("contents: ",data_str, type(data_str))
    except FileNotFoundError:
        print("\t [+] Error with finding the file... exiting")
        exit()
    data_str = data_str.lower()
    #remove basic punctuation
    punctuation = "!`':,?.()/\\"
    for p in punctuation:
        data_str = data_str.replace(p," ")
    return data_str.split() # return a list
#end of getFile()



def studySentiment(text_list, sentiments_dict):
    """function to to determine the sentiment score from the text."""
    score = 0 # current score of the sentimental words
    hits = 0 # the number of words which have a sentiment value
    for i in text_list:
        #print("   Current word: ",i)
        try:
            wordScore_int = int(sentiments_dict[i])
            print("\t ~ ", i,"    score: ",wordScore_int)
            score =  score + wordScore_int
            hits = hits + 1
        except KeyError:
            #print("  <<",i,">> Word not found in sentiments_dict...")
            pass
    print("\t\t" + "- -" * 10)
    try:
        print("\n\t [+] hits (number of sentiment words) :",hits)
        print("\t [+] score :",score)
        print("\t [+] score/hits:",score/hits)
    except ZeroDivisionError:
        print("\t [+] Not enough input to function ... :-(")
        exit()
#end of studySentiment()



def begin(in_str, inFile = ""):
    """Begin the program."""
    text_list = ""
    if in_str.lower() == "f":
        text_list = getFile(inFile)

    else:
        text_list = getSentence()


    print( "\t [+] Contents : ", text_list, type(text_list))
    csvfile = "finn.csv"
    sentiments_dict = getSentiments(csvfile)
    print("\t [+] Analyzing the sentiment score of text... ")
    studySentiment(text_list, sentiments_dict)


#end of begin()

# command line paramters code
###################################
#import itertools, sys
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.ticker import MaxNLocator
#from collections import namedtuple
import csv,sys, re



if __name__ == '__main__':

    if len(sys.argv)  == 2: #user enters a sentence
        begin(sys.argv[1])
        exit()

    if len(sys.argv) == 3: #two options ["f", "filename"] added to command line
       begin(sys.argv[1],sys.argv[2])
    else:
    #if len(sys.argv) == 2: #one option added to command line
    #   begin(sys.argv[1])
    #else:
       help()
       sys.exit(0)







# plotting notes...

#n_groups = 5

#means_men = (20, 35, 30, 35, 27)
#std_men = (2, 3, 4, 1, 2)

#means_women = (25, 32, 34, 20, 25)
#std_women = (3, 5, 2, 3, 3)

#fig, ax = plt.subplots()

#index = np.arange(n_groups)
#bar_width = 0.35

#opacity = 0.4
#error_config = {'ecolor': '0.3'}

#rects1 = ax.bar(index, means_men, bar_width,
#                alpha=opacity, color='b',
#                yerr=std_men, error_kw=error_config,
#                label='Men')

#rects2 = ax.bar(index + bar_width, means_women, bar_width,
#                alpha=opacity, color='r',
#                yerr=std_women, error_kw=error_config,
#                label='Women')

#ax.set_xlabel('Group')
#ax.set_ylabel('Scores')
#ax.set_title('Scores by group and gender')
#ax.set_xticks(index + bar_width / 2)
#ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
#ax.legend()

#fig.tight_layout()
#plt.show()
