"""Test module for summarizer.py"""
import src.summarizer as summarizer


def test_summarize_text():
    """Test that summarize text works."""
    input_text = "Some solutions that can be developed to avoid harm or fix \
the harm are conducting more research and not offering it \
to a selective group of people. More research needs to be \
done especially in terms of embryos. In addition, if germline \
editing is only offered to a select group of people, \
the wealthy, it will be problematic for the class system."
    expected = "Some solutions that can be developed to avoid harm or \
fix the harm are conducting more research and not offering \
it to a selective group of people."
    output = summarizer.summarize_text(input_text)
    assert output == expected


def test_summarizer_with_two_inputs(tmp_path):
    """Test that summarizer pipeline works."""
    directory = tmp_path / "sub"
    directory.mkdir()
    p_1 = directory / "hello.md"
    p_2 = directory / "world.md"
    txt = "Some solutions that can be developed to \
avoid harm or fix the harm are conducting more research and not offering it \
to a selective group of people. More research needs to be done especially in \
terms of embryos. In addition, if germline editing is only offered to a \
select group of people, the wealthy, it will be problematic for the class \
system."
    p_1.write_text(f"# Reflection by\n\n## header1\n{txt}\n## header2\n{txt}")
    p_2.write_text(f"# Reflection by\n\n## header1\n{txt}\n## header2\n{txt}")
    output = summarizer.summarizer(directory)
    summrized_text = "Some solutions that can be developed to avoid harm or \
fix the harm are conducting more research and not offering \
it to a selective group of people."
    expected = {
        "header1": [summrized_text, summrized_text],
        "header2": [summrized_text, summrized_text],
    }
    assert expected == output


def test_summarizer_with_three_inputs(tmp_path):
    """Test that summarizer pipeline works."""
    directory = tmp_path / "sub"
    directory.mkdir()
    p_1 = directory / "hello.md"
    p_2 = directory / "world.md"
    p_3 = directory / "python.md"
    txt = "Some solutions that can be developed to \
avoid harm or fix the harm are conducting more research and not offering it \
to a selective group of people. More research needs to be done especially in \
terms of embryos. In addition, if germline editing is only offered to a \
select group of people, the wealthy, it will be problematic for the class \
system."
    p_1.write_text(f"# Reflection by\n\n## header1\n{txt}\n## header2\n{txt}")
    p_2.write_text(f"# Reflection by\n\n## header1\n{txt}\n## header2\n{txt}")
    p_3.write_text(f"# Reflection by\n\n## header1\n{txt}\n## header2\n{txt}")
    output = summarizer.summarizer(directory)
    summrized_text = "Some solutions that can be developed to avoid harm or \
fix the harm are conducting more research and not offering \
it to a selective group of people."
    expected = {
        "header1": [summrized_text, summrized_text, summrized_text],
        "header2": [summrized_text, summrized_text, summrized_text],
    }
    assert expected == output
