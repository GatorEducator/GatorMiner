"""Test module for analyzer.py"""
import src.util.summarizer as summarizer


def test_summarize_text():
    """Test that summarize text works"""
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
    """Test that summarizer pipeline works"""
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "hello.md"
    p2 = d / "world.md"
    text = "Some solutions that can be developed to \
avoid harm or fix the harm are conducting more research and not offering it \
to a selective group of people. More research needs to be done especially in \
terms of embryos. In addition, if germline editing is only offered to a \
select group of people, the wealthy, it will be problematic for the class \
system."
    p1.write_text(f"# Reflection by\n\n## header1\n{text}\n## header2\n{text}")
    p2.write_text(f"# Reflection by\n\n## header1\n{text}\n## header2\n{text}")
    output = summarizer.summarizer(d)
    summrized_text = "Some solutions that can be developed to avoid harm or \
fix the harm are conducting more research and not offering \
it to a selective group of people."
    expected = {
        "header1": [summrized_text, summrized_text],
        "header2": [summrized_text, summrized_text],
    }
    assert expected == output


def test_summarizer_with_three_inputs(tmp_path):
    """Test that summarizer pipeline works"""
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "hello.md"
    p2 = d / "world.md"
    p3 = d / "python.md"
    text = "Some solutions that can be developed to \
avoid harm or fix the harm are conducting more research and not offering it \
to a selective group of people. More research needs to be done especially in \
terms of embryos. In addition, if germline editing is only offered to a \
select group of people, the wealthy, it will be problematic for the class \
system."
    p1.write_text(f"# Reflection by\n\n## header1\n{text}\n## header2\n{text}")
    p2.write_text(f"# Reflection by\n\n## header1\n{text}\n## header2\n{text}")
    p3.write_text(f"# Reflection by\n\n## header1\n{text}\n## header2\n{text}")
    output = summarizer.summarizer(d)
    summrized_text = "Some solutions that can be developed to avoid harm or \
fix the harm are conducting more research and not offering \
it to a selective group of people."
    expected = {
        "header1": [summrized_text, summrized_text, summrized_text],
        "header2": [summrized_text, summrized_text, summrized_text],
    }
    assert expected == output
