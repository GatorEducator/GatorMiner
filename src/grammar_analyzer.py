import language_check
from . import markdown as md
from typing import Dict, List

# Mention the language keyword
# pylint: disable=missing-docstring

def grammar_analyzer(directory: str) -> Dict[str, List[int][str]]:
    '''A tool to check grammar error in reflection'''
    tool = language_check.LanguageTool('en-US')
    i = 0
    # Parse the file which needs to be checked
    main_md_dict = md.collect_md(directory, is_clean=False)
    # initialize summarized dict with keys in sources
    grammar_checker = {k: [] for k in main_md_dict.keys()}
    for key, values in main_md_dict.items():
        for item in values:
            for line in item:
                matches = tool.check(line)
                i = i + len(matches)
                grammar_checker[key].append(i)
                for mistake in matches:
                    grammar_checker[key][i].append(mistake)
    return grammar_checker
