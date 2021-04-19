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
        pass

    # Store all alphanumeric characters in the reflection in a list
    data = text
    pattern = re.compile(r'[\W_]+')
    data = pattern.sub(' ', data).lower()
    words = data.split()

    # Calculate the error percentage of grammar error per number of words
    err_percentage = int(100*err_num/(len(words)))

    # Store number of errors and grade in a dictionary
    grammar_err = []
    grammar_err.append((err_num, err_percentage))
    return grammar_err
