import os
import json

from . import markdown as md
from . import constants as cts


def get_json_files(dir_path):
    """Get JSON files in a directory"""
    json_files = [
        os.path.join(dir_path, js)
        for js in os.listdir(dir_path)
        if js.endswith(cts.JSON_EXT)
    ]
    json_lst = []
    for file in json_files:
        with open(file) as file:
            json_lst.append(json.load(file))
    return json_lst


def clean_report(raw_json_lst):
    """Filter out unwanted key items in the report"""
    clean_json = []
    for js in raw_json_lst:
        clean_json.append(
            {k: v for k, v in js.items() if k in cts.REPORT_KEYS})
    return clean_json


def parse_md(json_lst):
    for js in json_lst:
        js.update(md.md_parser(js[cts.REPORT_REFLECTION]))
    return json_lst


if __name__ == "__main__":
    print(
        parse_md(clean_report(get_json_files("../resources/sample_report")))[0]
    )
    # print(jsonfiles)
