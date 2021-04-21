# pylint: disable=missing-docstring
import language_tool_python
import re
from typing import List, Tuple

# Mention the language keyword


def grammar_analyzer(text: str) -> List[Tuple[int, int]]:
    '''A tool to check grammar error and grade it in the reflection'''
    tool = language_tool_python.LanguageTool('en-US')

    # Variable represent number of grammar errors in the text
    err_num = 0

    # count for grammar errors
    for line in text:
        matches = tool.check(line)
        err_num = err_num + len(matches)

    # Store all alphanumeric characters in the reflection in a list
    words = re.sub('[^0-9a-zA-Z]+', ' ', str(text)).lower().split()

    # Calculate the error percentage of grammar error per number of words
    err_percentage = 0
    if len(words) != 0:
        err_percentage = int(100*err_num/(len(words)))
    else:
        pass

    # Store number of errors and grade in a list
    grammar_err = []
    grammar_err.append((err_num, err_percentage))
    return grammar_err
