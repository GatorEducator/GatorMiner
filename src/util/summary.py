from gensim.summarization import summarize, keywords
from pprint import pprint


def summarizeText(text: str) -> str:
    """ Uses genim's summarization to summarize the given text """
    pass


def getText(fileName: str) -> str:
    """ Returns selected passages from the file after given a file name """
    pass


def getFileNames() -> [str]:
    """ Uses os library to find all markdown files in given directory """

    dirName = "../../cs100f2019_lab05_reflections/"


if __name__ == '__main__':
    fileNames = getFileNames()  # The directory is currently hardcoded
    for file in fileNames:
        text = summarizeText(getText(file))
        pprint(f"{file}:\t{text}", end="\n-----------------\n")
