import pytest
import src.grammar_analyzer as ga

def test_grammar_analyzer():
    "Test grammar errors and grade it"
    input_text = "This are a pen. \n It is beatifuly"
    output = ga.grammar_analyzer(input_text)
    expected = [{2,28}]
    assert output == expected
