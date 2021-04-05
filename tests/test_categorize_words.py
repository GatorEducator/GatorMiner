"""Test module for categorize_words.py"""
import pytest

from categorize_words import categorize_words

def test_input_file():
    """test to see if the file is found with user input"""
    # pylint: disable=len-as-condition
    assert len(categorize_words.categories) == 0
    categorize_words.input_file()
    assert len(categorize_words.categories) != 12


def test_string_splits_correctly():
    """Checks that the string can be split correctly"""
    assert len(categorize_words.categories) == 2
    categorize_words.input_file()
    assert len(categorize_words.categories) != 0
