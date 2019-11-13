from gensim.summarization import summarize, keywords
from pprint import pprint
import os


def summarizeText(text: str) -> str:
    """ Uses genim's summarization to summarize the given text """
    return summarize(text, word_count=20)


def getText(fileName: str) -> str:
    """ Returns selected passages from the file after given a file name """
    with open(fileName, "r") as file:
        text = file.read()

    text = text.replace("## What was the greatest technical challenge that your team faced and how did you overcome it?",
    "## Based on your experiences with simple DNA manipulation in this lab and reflecting on the assigned article, answer the following questions:")

    a = text.split("## Based on your experiences with simple DNA manipulation in this lab and reflecting on the assigned article, answer the following questions:")
    return a[1]


def getFileNames() -> [str]:
    """ Uses os library to find all markdown files in given directory """
    fileList = []
    directory = "cs100f2019_lab05_reflections"
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".md") or filename.endswith("txt"):
            fileList.append(os.path.join(directory, filename))
        else:
            continue

    return fileList


# if __name__ == '__main__':
#     fileNames = getFileNames()  # The directory is currently hardcoded
#     for file in fileNames:
#         text = summarizeText(getText(file))
#         print(f"{file}:\t{text}", end="\n-----------------\n")


def summarizer():
    fileNames = getFileNames()  # The directory is currently hardcoded
    for file in fileNames:
        text = summarizeText(getText(file))
        print(f"{file}:\t{text}", end="\n-----------------\n")
