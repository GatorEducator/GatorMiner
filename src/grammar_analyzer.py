# pylint: disable=missing-docstring
import language_tool_python
from typing import Dict, List

# Mention the language keyword


def grammar_analyzer(text: str) -> List[str]:
    '''A tool to check grammar error in reflection'''
    tool = language_tool_python.LanguageTool('en-US')
    i = 0
    # store the number of errors as keys and errors as items of a dictionary
    grammar_err = []
    # initialize key and item into grammar_err dictionary
    for line in text:
        matches = tool.check(line)
        i = i + len(matches)
        pass

    for mistake in matches:
        grammar_err.append([i, mistake])
    return grammar_err
