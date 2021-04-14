# pylint: disable=missing-docstring
import language_tool_python
from . import markdown as md
from typing import Dict, List

# Mention the language keyword


def grammar_analyzer(text: str) -> Dict[int, List[str]]:
    '''A tool to check grammar error in reflection'''
    tool = language_tool_python.LanguageTool('en-US')
    i = 0
    # Parse the file which needs to be checked
    grammar_err = {}
    # initialize summarized dict with keys in sources
    for line in text:
        matches = tool.check(line)
        i = i + len(matches)
        grammar_err.append(i)
        for mistake in matches:
            grammar_err[i].append(mistake)
    return grammar_err
