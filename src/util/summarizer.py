"""Text summary"""
import os
import logging
import pprint
from typing import Dict, List
from gensim.summarization import summarize
import commonmark


logging.basicConfig(
    format="[%(asctime)s]{%(pathname)s:%(lineno)d}\n\
%(levelname)s: %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.ERROR,
)


def summarize_text(text: str) -> str:
    """ Uses genim's summarization to summarize the given text """
    return summarize(text, word_count=30)


def read_file(path: str) -> str:
    """ read file from path """
    with open(path) as input_file:
        data = input_file.read()
        return data


def get_file_names(directory_name: str) -> List[str]:
    """ Uses os library to find all markdown files in given directory """
    file_list = []
    for file in os.listdir(directory_name):
        filename = os.fsdecode(file)
        if filename.endswith(".md") or filename.endswith("txt"):
            file_list.append(os.path.join(directory_name, filename))
        else:
            continue

    return file_list


def merge_dict(dict_1, dict_2: Dict[str, str]) -> Dict[str, List[str]]:
    """Merge dictionaries and keep values of common keys in list"""
    if dict_1 is None:
        dict_1 = {k: [] for k in dict_2.keys()}
    elif isinstance(list(dict_1.values())[0], list) is False:
        dict_1 = {k: [v] for k, v in dict_1.items()}
    for key, value in dict_2.items():
        dict_1[key].append(value)

    return dict_1


def merge_data(directory: str) -> Dict[str, List[str]]:
    """A pipeline to collect all the md files in a directory"""
    file_names = get_file_names(directory)
    main_md_dict = None
    for file in file_names:
        individual_dict = md_parser(read_file(file))
        main_md_dict = merge_dict(main_md_dict, individual_dict)
    return main_md_dict


def summarizer(directory: str) -> Dict[str, List[str]]:
    """A summarizing pipeline"""
    main_md_dict = merge_data(directory)
    del main_md_dict["Reflection by"]
    # initialize summarized dict with keys in sources
    summarized = {k: [] for k in main_md_dict.keys()}
    for key, values in main_md_dict.items():
        for item in values:
            try:
                summarized[key].append(summarize_text(item))
            except ValueError as err:
                logging.error(f"Cannot summarize text: {err}")
    return summarized


def md_parser(input_md: str) -> Dict[str, List[str]]:
    """Parse a markdown file and return as dict of headers and paragraphs"""
    ast = commonmark.Parser().parse(input_md)
    md_dict = {}
    cur_heading = ""
    for subnode, enter in ast.walker():
        if subnode.t == "heading" and enter:
            # set header as key name
            md_dict[subnode.first_child.literal] = ""
            cur_heading = subnode.first_child.literal
        elif subnode.literal is not None and subnode.literal != cur_heading:
            # add related text to the header
            md_dict[cur_heading] += subnode.literal + " "
        else:
            continue

    return md_dict
