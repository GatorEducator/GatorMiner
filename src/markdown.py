"""Markdown parser"""
import os
import logging
from io import StringIO
from typing import Dict, List
import commonmark
import pandas as pd
from . import constants as cts


# pylint: disable=logging-fstring-interpolation
logging.basicConfig(
    format="[%(asctime)s]{%(pathname)s:%(lineno)d}\n%(levelname)s:\
         %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.ERROR,
)


def read_file(path: str) -> str:
    """ read file from path """
    with open(path, encoding="utf8") as input_file:
        data = input_file.read()
        return data


def get_file_names(directory_name: str) -> List[str]:
    """ Uses os library to find all markdown files in given directory """
    file_list = []
    for file in os.listdir(directory_name):
        filename = os.fsdecode(file)
        if filename.endswith(cts.MD_EXT) or filename.endswith(cts.TXT_EXT):
            file_list.append(os.path.join(directory_name, filename))
        else:
            continue

    return file_list


def merge_dict(dict_1, dict_2: Dict[str, str], preserve: bool) -> \
        Dict[str, List[str]]:
    """Merge two dictionaries and store values of common keys in list"""
    if dict_1 is None:
        dict_1 = {k: [] for k in dict_2.keys()}
    elif isinstance(list(dict_1.values())[0], list) is False:
        dict_1 = {k: [v] for k, v in dict_1.items()}
    if(preserve):
        for key in dict_2.keys():
            if key not in dict_1:
                dict_1[key] = []
                for f in range(0, len(list(dict_1.values())[0])):
                    dict_1[key].append("")
    for key in dict_1.keys():
        try:
            dict_1[key].append(dict_2[key])
        except KeyError as err:
            dict_1[key].append("")
            logging.warning(f"Key does not exist: {err}")
    return dict_1


def collect_md(directory: str, is_clean=True) -> Dict[str, List[str]]:
    """A pipeline to collect all the md files in a directory to a dict"""
    file_names = get_file_names(directory)
    main_md_dict = None
    for file in file_names:
        individual_dict = md_parser(read_file(file), is_clean)
        main_md_dict = merge_dict(main_md_dict, individual_dict, False)
    return main_md_dict


def collect_md_text(directory: str, is_clean=True) -> List[str]:
    """A pipeline to collect all md files in a directory to a list of text"""
    file_names = get_file_names(directory)
    main_md_list = []
    for file in file_names:
        individual_dict = md_parser(read_file(file), is_clean)
        md_text = " ".join(individual_dict.values())
        main_md_list.append(md_text)
    return main_md_list


def md_parser(input_md: str, is_clean=True) -> Dict[str, str]:
    """Parse a markdown file and return as dict of headers and paragraphs"""
    ast = commonmark.Parser().parse(input_md)
    types = {}
    if is_clean:
        types = {"code_block", "link", "image", "code", "block_quote"}
    global md_dict
    md_dict = {}
    cur_heading = ""
    for subnode, enter in ast.walker():
        if subnode.t == "heading" and enter:
            # set header as key name
            md_dict[subnode.first_child.literal.lower()] = ""
            cur_heading = subnode.first_child.literal.lower()
        elif (
            subnode.literal is not None
            and subnode.literal.lower() != cur_heading
            and subnode.t not in types
        ):
            # add related text to the header
            md_dict[cur_heading] += subnode.literal + " "
        else:
            continue
    return md_dict


def import_uploaded_files(paths: List) -> Dict[str, List[str]]:
    """Importing the individual files"""
    main_md_dict = None
    for path in paths:
        stringio = StringIO(path.getvalue().decode("utf-8"))
        individual_dict = md_parser(stringio.read(), True)
        main_md_dict = merge_dict(main_md_dict, individual_dict, True)
    return main_md_dict


def build_pd(md_dict):
    """build dictionary into dataframe"""
    md_df = pd.DataFrame(md_dict)
    return md_df


if __name__ == "__main__":
    build_pd(collect_md("resources/test"))
