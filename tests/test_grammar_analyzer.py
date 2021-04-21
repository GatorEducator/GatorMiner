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
    assert output == expected
