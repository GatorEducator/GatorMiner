from gensim.summarization import summarize, keywords
from pprint import pprint
import os
import commonmark


def summarize_text(text: str) -> str:
    """ Uses genim's summarization to summarize the given text """
    return summarize(text, word_count=30)


def read_file(path: str):
    """ read file from path """
    with open(path) as input_file:
        data = input_file.read()
        return data


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


def md_parser(file):
    ast = commonmark.Parser().parse(file)
    md_dict = {}
    cur_heading = ""
    for subnode, enter in ast.walker():
        if subnode.t == "heading" and enter:
            md_dict[subnode.first_child.literal] = ""
            cur_heading = subnode.first_child.literal
        elif subnode.literal is not None and subnode.literal != cur_heading:
            md_dict[cur_heading] += subnode.literal
        else:
            continue

    return md_dict


if __name__ == "__main__":
    # summarizer()
    md_parser()

# TODO find an easier way to automate collecting the actual text
# this method relied on knowing the format of the file & cheating the text out

# TODO Look deeper into the summarize function and try using different argument
