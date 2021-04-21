"""Compute and return number of grammar error in text"""
import language_tool_python
import re

# Mention the language keyword


def grammar_analyzer(text: str) -> int:
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

    return err_num, err_percentage
