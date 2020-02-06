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


def merge_dict(dict_1, dict_2):
    """Merge dictionaries and keep values of common keys in list"""
    new_dict = {**dict_1, **dict_2}
    for key, value in new_dict.items():
        if key in dict_1 and key in dict_2:
            new_dict[key] = [value, dict_1[key]]

    return new_dict


def summarizer(directory):
    file_names = get_file_names(directory)
    main_md_dict = {}
    for file in file_names:
        individual_dict = md_parser(read_file(file))
        main_md_dict = merge_dict(main_md_dict, individual_dict)
    del main_md_dict["Reflection by"]
    # print(
    #     main_md_dict[
    #         "What was the greatest technical challenge that your team faced and how did you overcome it?"
    #     ]
    # )

    summarized = {k: [] for k in main_md_dict.keys()}

    # # for key, values in main_md_dict.items():
    # for values in main_md_dict[
    #     "What was the greatest technical challenge that your team faced and how did you overcome it?"
    # ]:
    #     # for item in values:
    #     # print(summarized)
    #     # print(values)
    #     summarized[
    #         "What was the greatest technical challenge that your team faced and how did you overcome it?"
    #     ].append(summarize_text(values))

    for key, values in main_md_dict.items():
        for item in values:
            print(item)
            summarized[key].append(summarize_text(item))

    print(summarized)
    # return text


def md_parser(path_to_file):
    """Parse a markdown file and return as dict of headers and paragraphs"""
    ast = commonmark.Parser().parse(path_to_file)
    md_dict = {}
    cur_heading = ""
    for subnode, enter in ast.walker():
        if subnode.t == "heading" and enter:
            # set header as key name
            md_dict[subnode.first_child.literal] = ""
            cur_heading = subnode.first_child.literal
        elif subnode.literal is not None and subnode.literal != cur_heading:
            # add related text to the header
            md_dict[cur_heading] += subnode.literal
        else:
            continue

    return md_dict


if __name__ == "__main__":
    # summarizer("test_resource")
    # md_parser()


# TODO Look deeper into the summarize function and try using different argument
