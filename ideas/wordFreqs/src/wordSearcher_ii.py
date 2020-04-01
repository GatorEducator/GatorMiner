#!/usr/bin/env python3

# program to find word freqs in a text.


DATE = "20 March 2020"
VERSION = "i"
AUTHOR = " myName"
AUTHORMAIL = "@allegheny.edu"

# directories: if necessary
#OUTPUT_DIR = "/tmp/0out/" # all results are saved in this local directory
#OUTPUT_DIR = "0out/" # all results are saved in this local directory
#INPUT_DIR = "data/"


def help():
		h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
		print("  "+len(h_str) * "-")
		print(h_str)
		print("  "+len(h_str) * "-")

		print("\n\t [+] Program to load a text file of text and to")
		print("\t return a frequency plot of the word freqs.")
		platform_str = get_platformType()
		print("\t+ OS type: ",platform_str) # determine what the os is.
		#print("""\n\tLibrary installation notes:""")
		command_str = "USAGE: programName <wordFile.txt>"
		if platform_str.lower() == "linux" or platform_str.lower() == "osx":
			print("\n\t [+] \U0001f600 ", command_str)
		else:
			print("\n\t+ :-) ", command_str)
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



def openAndCleanData(inFile):
    """ loads a text file and returns a string of contents"""
    data_str = open(inFile,"r").read().lower() #return a string in lowercase
    #print("type :",type(data_str))
    punct_str = "!.,'\""
    for i in punct_str:
        data_str = data_str.replace(i,"") #remove the punctuation
    return data_str
#end of openFile()


def collectFreqs(data_str):
    """collect the numbers of words and return a dictionary of freqs"""
    #print("  collectFreqs()")
    data_list = sorted(data_str.split()) # return an abc-sorted list
    freq_list = [] # we will store the freqs in a list
    count_dic = {} # store words and counts
    for i in data_list:
        if i not in count_dic: count_dic[i] = 1
        else: count_dic[i] = count_dic[i] + 1
    #print("  Count_dic :",count_dic)

    # place freqs in the list
    for i in count_dic:
        freq_list.append(count_dic[i]/len(data_list))
    #print("  freq_list :",freq_list)

    return freq_list
#end of collectFreqs()


def plotter(in_list, inFile_str):
    """ plots the freq data"""
    try:
        from pylab import plot, show, title, savefig, xlabel, ylabel, legend

    except:
        print("\n\t [+] One or more of your libraries is not loading! :-( ")
        exit()
    y = in_list
    x = [i for i in range(len(in_list))]
    plot(x,y, linestyle="", marker = 'v')
    title("Frequency of words used")
    xlabel("Words")
    ylabel("Magnitude of Frequency")

    fname_str = inFile_str.replace(".txt","_out.png")

    print("\t [+] Saving new filename:", fname_str)
    savefig(fname_str) #save in root directory
    show()

#end of plotter()

def checkDataDir(dir_str):
#function to determine whether a data output directory exists.
#if the directory doesnt exist, then it is created

    try:
        os.makedirs(dir_str)
        #print("  PROBLEM: output_dir doesn't exist")
        print("\t [+] Creating :",dir_str)
        return 1

    except OSError:
        return 0
#end of checkDataDir()



def begin(inFile):
    """ Driver function """
    print("\t [+] Loading file :", inFile)
    data = openAndCleanData(inFile)
    #print("  Contents :",data)
    collectedFreqs_list = collectFreqs(data)
    #print(" collectedFreqs_list :",collectedFreqs_list)
    plotter(collectedFreqs_list,inFile)
    print("\t [+] Program finished")
#end of begin()


# command line paramters code
###################################
import itertools, sys
#from pylab import plot, show, title, savefig, xlabel, ylabel, legend
if __name__ == '__main__':

    if len(sys.argv) == 2: #one option added to command line
       begin(sys.argv[1])
    else:
       help()
       sys.exit(0)
