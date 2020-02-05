from gensim.summarization import summarize, keywords
from pprint import pprint
import os


def summarize_text(text: str) -> str:
    """ Uses genim's summarization to summarize the given text """
    return summarize(text, word_count=30)


def get_text(fileName: str) -> str:
    """ Returns selected passages from the file after given a file name """
    with open(fileName, "r") as file:
        text = file.read()

    text = text.replace(
        "## What was the greatest technical challenge that your team faced \
and how did you overcome it?",
        "## Based on your experiences with simple DNA manipulation in this \
lab and reflecting on the assigned article, answer the following questions:",
    )

    a = text.split(
        "## Based on your experiences with simple DNA manipulation in this \
lab and reflecting on the assigned article, answer the following questions:"
    )
    return a[1]


def get_file_names(directory_name) -> [str]:
    """ Uses os library to find all markdown files in given directory """
    file_list = []
    # "cs100f2019_lab05_reflections"
    for file in os.listdir(directory_name):
        filename = os.fsdecode(file)
        if filename.endswith(".md") or filename.endswith("txt"):
            file_list.append(os.path.join(directory_name, filename))
        else:
            continue

    return file_list


def summarizer():
    file_names = get_file_names(
        "cs100f2019_lab05_reflections"
    )  # The directory is currently hardcoded
    for file in file_names:
        text = summarize_text(get_text(file))
        print(f"{file}:\t{text}", end="\n-----------------\n")

    return text


if __name__ == "__main__":
    summarizer()

# TODO find an easier way to automate collecting the actual text
# this method relied on knowing the format of the file & cheating the text out

# TODO Look deeper into the summarize function and try using different argument
