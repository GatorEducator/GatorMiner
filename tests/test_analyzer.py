"""Test module for analyzer.py"""
import pytest
import src.analyzer as analyzer


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
            ["avoid", "use", "punctuation"],
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
        ("... ! @ # $ *** ##", "      ",),
    ],
)
# pylint: disable=W0613
def test_normalize(input_text, expected):
    """parametrize test normalize"""
    output = analyzer.normalize(input_text)
    assert output == expected


def test_compute_frequency():
    """Test if it return correct frequency result"""
    token_lst = ["hello", "hello", "hello"]
    output = analyzer.compute_frequency(token_lst)
    assert output == [("hello", 3)]


def test_word_frequency():
    """Test if it return correct frequency result from a file"""
    text = "hello world hello world hello world"
    output = analyzer.word_frequency(text)
    expected = [("hello", 3), ("world", 3)]
    assert expected == output


def test_dir_frequency(tmp_path):
    """Test if it return correct frequency result from a directory"""
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "hello.md"
    p2 = d / "world.md"
    text = "hello world hello world hello world"
    p1.write_text(text)
    p2.write_text(text)
    output = analyzer.dir_frequency(d)
    expected = [("hello", 6), ("world", 6)]
    assert expected == output


def test_part_of_speech():
    """Test if it return correct part of speech information"""
    text = "The greatest technical challenge that I faced \
was getting the program to run"
    output = analyzer.part_of_speech(text)
    assert output == [
        ("The", "DET"),
        ("greatest", "ADJ"),
        ("technical", "ADJ"),
        ("challenge", "NOUN"),
        ("that", "DET"),
        ("I", "PRON"),
        ("faced", "VERB"),
        ("was", "AUX"),
        ("getting", "VERB"),
        ("the", "DET"),
        ("program", "NOUN"),
        ("to", "PART"),
        ("run", "VERB"),
    ]


def test_named_entity_recognization():
    """Test if it return correct noun phrases"""
    text = "Apple is looking at buying U.K. startup for $1 billion"
    output = analyzer.named_entity_recognization(text)
    assert output == [
        ("Apple", "ORG"),
        ("U.K.", "GPE"),
        ("$1 billion", "MONEY"),
    ]


def test_noun_phrase():
    text = "Apple is looking at buying U.K. startup for $1 billion"
    output = analyzer.noun_phrase(text)
    assert output == ["Apple", "U.K. startup"]
