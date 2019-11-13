from gensim.summarization import summarize, keywords
from pprint import pprint
import os


def summarizeText(text: str) -> str:
    """ Uses genim's summarization to summarize the given text """
    pass


def getText(fileName: str) -> str:
    """ Returns selected passages from the file after given a file name """
    pass


def getFileNames() -> [str]:
    """ Uses os library to find all markdown files in given directory """

    directory = "cs100f2019_lab05_reflections"
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".md"):
            print(os.path.join(directory, filename))
        else:
            continue


if __name__ == '__main__':
    """fileNames = getFileNames()  # The directory is currently hardcoded
    for file in fileNames:
        text = summarizeText(getText(file))
        pprint(f"{file}:\t{text}", end="\n-----------------\n")"""
    print(getFileNames())
