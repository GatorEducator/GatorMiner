"""Text summary"""
import os
import logging
from typing import Dict, List
import commonmark


logging.basicConfig(
    format="[%(asctime)s]{%(pathname)s:%(lineno)d}\n\
%(levelname)s: %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.WARNING,
)


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
    """Merge two dictionaries and store values of common keys in list"""
    if dict_1 is None:
        dict_1 = {k: [] for k in dict_2.keys()}
    elif isinstance(list(dict_1.values())[0], list) is False:
        dict_1 = {k: [v] for k, v in dict_1.items()}
    for key, value in dict_2.items():
        try:
            dict_1[key].append(value)
        except KeyError as err:
            logging.warning(f"Key does not exist: {err}")

    return dict_1


def merge_data(directory: str) -> Dict[str, List[str]]:
    """A pipeline to collect all the md files in a directory to a dict"""
    file_names = get_file_names(directory)
    main_md_dict = None
    for file in file_names:
        individual_dict = md_parser(read_file(file))
        main_md_dict = merge_dict(main_md_dict, individual_dict)
    return main_md_dict


def md_parser(input_md: str) -> Dict[str, str]:
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
