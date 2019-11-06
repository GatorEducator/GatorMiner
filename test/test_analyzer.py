"""Test module for analyzer.py"""
import src.util.analyzer as analyzer


def test_tokenize():
    """Test tokenize break down str into list of str correctly with the porter
    method from nltk package"""
    test_input = "Test tokenize break down str into list of str correctly"
    output = analyzer.tokenize(test_input)
    expected = [
        "test",
        "token",
        "break",
        "down",
        "str",
        "into",
        "list",
        "of",
        "str",
        "correctli",
    ]
    assert output == expected
