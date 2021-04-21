<<<<<<< HEAD
import src.grammar_analyzer as ga


def test_grammar_analyzer():
    input_text = "This are a pen.\
                  It is beautifuly."
    output = ga.grammar_analyzer(input_text)
    expected = [(2, 28)]
    assert output == expected


def test_grammar_analyzer2():
    input_text = "Python can only interpret names that you have\
spelled correctly. This is because when you declare a variable or a function,\
Python store the value with the exact, name you have declared."
    output = ga.grammar_analyzer(input_text)
    expected = [(4, 12)]
=======
import pytest
import src.grammar_analyzer as ga

def test_grammar_analyzer():
    "Test grammar errors and grade it"
    input_text = "This are a pen. \n It is beatifuly"
    output = ga.grammar_analyzer(input_text)
    expected = [{2,28}]
>>>>>>> 17ddf3e451761911416636b9b3c74006202d8b2f
    assert output == expected
