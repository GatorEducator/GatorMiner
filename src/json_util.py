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
    raw_json_lst = []
    for file in json_files:
        with open(file) as file:
            raw_json_lst.append(json.load(file))
    return raw_json_lst


def clean_report(raw_json_lst):
    """Filter out unwanted key items and updated with md parsing"""
    clean_json = []
    for js in raw_json_lst:
        filtered = {k: v for k, v in js.items() if k in cts.REPORT_KEYS}
        md_dict = md.md_parser(filtered[cts.REPORT_REFLECTION])
        filtered.update({"combined": " ".join(md_dict.values())})
        filtered.update(md_dict)
        clean_json.append(filtered)
    return clean_json
