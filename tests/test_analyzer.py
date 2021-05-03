"""Test module for analyzer.py"""

import pytest
import src.analyzer as az
import pandas as pd
import src.constants as cts


def test_tokenize():
    """Test tokenize break down str into list of str correctly with the porter
    method from nltk package"""
    input_text = "Test tokenize break down str into list of str correctly"
    output = az.tokenize(input_text)
    expected = ["test", "tokenize", "break", "str", "list", "str", "correctly"]
    assert output == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (
            "The programer is programming many functional programs.",
            ["programer", "program", "functional", "program"],
        ),
        (
            "It is likely that many like words have liked liking other likes",
            ["likely", "like", "word", "like", "like", "like"],
        ),
        (
            "If you can't avoid it. We'll all use punctuation.",
            ["not", "avoid", "use", "punctuation"],
        ),
        ("can't don't won't", ["not", "not", "will", "not"]),
        ("... ! @ # $ *** ##", [],),
    ],
)
def test_tokenize_parametrize(input_text, expected):
    """parametrize test tokenize"""
    output = az.tokenize(input_text)
    assert output == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("numbers 1 2 3 4 55", "numbers ",),
        ("a sentence\nin a new line", "a sentence in a new line",),
    ],
)
# pylint: disable=W0613
def test_normalize(input_text, expected):
    """parametrize test normalize"""
    output = az.normalize(input_text)
    assert output == expected


def test_compute_frequency():
    """Test if it return correct frequency result"""
    token_lst = ["hello", "hello", "hello"]
    output = az.compute_frequency(token_lst)
    assert output == [("hello", 3)]


def test_word_frequency():
    """Test if it return correct frequency result from a file"""
    text = "hello world hello world hello world"
    output = az.word_frequency(text)
    expected = [("hello", 3), ("world", 3)]
    assert expected == output


def test_dir_frequency(tmp_path):
    """Test if it return correct frequency result from a directory"""
    directory = tmp_path / "sub"
    directory.mkdir()
    para_1 = directory / "hello.md"
    para_2 = directory / "world.md"
    text = "# header\n hello world hello world hello world"
    para_1.write_text(text)
    para_2.write_text(text)
    output = az.dir_frequency(directory)
    expected = [("hello", 6), ("world", 6)]
    assert expected == output


def test_part_of_speech():
    """Test if it return correct part of speech information"""
    text = "The greatest technical challenge that I faced \
was getting the program to run"
    output = az.part_of_speech(text)
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
    output = az.named_entity_recognization(text)
    assert output == [
        ("Apple", "ORG"),
        ("U.K.", "GPE"),
        ("$1 billion", "MONEY"),
    ]


def test_noun_phrase():
    """test return correct noun phrase"""
    text = "Apple is looking at buying U.K. startup for $1 billion"
    output = az.noun_phrase(text)
    assert output == ["Apple", "U.K. startup"]


def test_lemmatized_text():
    """Test lemmatized text works"""
    text = "She loves dogs"
    output = az.lemmatized_text(text)
    expect = "love dog"
    print(output)
    assert output == expect


def test_sentence_tokenize():
    """Test sentence tokenizer works"""
    text = "The greatest technical challenge that I faced \
was getting the program to run. I am looking forward to some \
poroblem even involing some challenging math to be more interesting."
    output = az.sentence_tokenize(text)
    assert output == [
        "The greatest technical challenge that I faced was getting the program \
to run.",
        "I am looking forward to some poroblem even involing some challenging \
math to be more interesting.",
    ]


def test_tfidf():
    """test tfidf return result"""
    input_tokens = [
        "test",
        "tokenize",
        "break",
        "str",
        "list",
        "str",
        "correctly",
    ]
    term_frequency, vector = az.compute_tfidf(input_tokens)
    assert term_frequency is not None
    assert vector is not None


def test_concatenate():
    """test for contcatenated string of all words"""
    input_dict = {
        "What was the most important technical skill that you practiced?":
        ["Using pipenv and pytest", "Naming variables in Python"],
        "What was the most important professional skill that you practiced?":
        ["Communicating with a team remotely", "Resolving issues by talking \
        to teammates"]
    }
    input_df = pd.DataFrame(input_dict)
    output = az.concatenate(input_df)
    expected = "using pipenv and pytest communicating with a team remotely \
naming variables in python resolving issues by talking to teammates "
    assert output == expected


def test_top_polarized_word():
    """Tests if the positive/negative words columns are created"""
    df = pd.DataFrame(columns=[cts.TOKEN, cts.POSITIVE, cts.NEGATIVE])
    input_tokens = [
        ["incredible", "horrible", "terrific", "terrible"],
        ["amazing", "devastating", "boring", "cool"],
        ["alarming", "awesome", "beautiful", "ugly"],
    ]
    df[cts.TOKEN] = pd.Series(input_tokens)
    df[cts.POSITIVE], df[cts.NEGATIVE] = \
        az.top_polarized_word(df[cts.TOKEN].values)
    assert df[cts.POSITIVE] is not None
    assert df[cts.NEGATIVE] is not None
    assert df[cts.POSITIVE].size is df[cts.TOKEN].size
    assert df[cts.NEGATIVE].size is df[cts.TOKEN].size
