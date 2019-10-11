import pytest
from unittest import mock
from src.util.analyzer import normalize, tokenize


@pytest.mark.parametrize('input_text, answer',
                         [('The programer programs many functional programs.',
                           ['the', 'program', 'program', 'mani', 'function', 'program', '.']),
                          ('It is likely that many like words have liked liking other likes',
                          ['It', 'is', 'like', 'that', 'mani', 'like', 'word',
                           'have', 'like', 'like', 'other', 'like']),
                          ("If you can't avoid it. We'll all use punctuation.",
                           ['If', 'you', 'ca', "n't", 'avoid', 'it', '.', 'We', "'ll", 'all', 'use', 'punctuat', '.'])])
def test_tokenize(input_text, answer):
    # given
    text = input_text

    # when
    result = tokenize(text)

    # then
    expected_result = answer
    assert result == expected_result


@pytest.mark.parametrize('text_input, answer', [('A list of words with stopwords should drop some',
                                                 ['list', 'word', 'stopword', 'should', 'drop', 'some']),
                                                ('A second sentence was only more of a test because we need more tests',
                                                 ['second', 'sentenc', 'wa', 'onli', 'test', 'need', 'test'])])
@mock.patch('src.util.analyzer.stopwords.words', return_value=['a', 'how', 'becaus', 'i', 'was', 'we',
                                                               'him', 'was', 'on', 'me', 'more', 'with', 'of', ])
def test_normalize(stopwords, text_input, answer):
    #given
    text_input = text_input

    #when
    result = normalize(text_input)

    #then
    expected_result = answer
    assert result == expected_result
