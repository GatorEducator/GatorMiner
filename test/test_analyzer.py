"""Test module for analyzer.py"""
import pytest
import src.util.analyzer as analyzer


def test_tokenize():
    """Test tokenize break down str into list of str correctly with the porter
    method from nltk package"""
    input_text = "Test tokenize break down str into list of str correctly"
    output = analyzer.tokenize(input_text)
    expected = ["test", "tokenize", "break", "str", "list", "str", "correctly"]
    assert output == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (
            "The programer programs many functional programs.",
            ["programer", "program", "functional", "program"],
        ),
        (
            "It is likely that many like words have liked liking other likes",
            ["likely", "like", "word", "like", "like", "like"],
        ),
        (
            "If you can't avoid it. We'll all use punctuation.",
            ['avoid', 'use', 'punctuation'],
        ),
    ],
)
def test_tokenize_parametrize(input_text, expected):
    """parametrize test tokenize"""
    output = analyzer.tokenize(input_text)
    assert output == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (
            "A list of words with stopwords should drop some",
            " list of words with stopwords should drop some",
        ),
        (
            "A second sentence was more of a test because we need more tests",
            " second sentence was more of  test because we need more tests",
        ),
    ],
)
# pylint: disable=W0613
def test_normalize(input_text, expected):
    """parametrize test normalize"""
    output = analyzer.normalize(input_text)
    assert output == expected
