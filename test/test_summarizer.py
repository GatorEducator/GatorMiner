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


def test_merge_dict():
    """Test that merge_dict returns a dict of key and value lists"""
    test_dict_1 = {"key1": "value1"}
    test_dict_2 = {"key1": "value2"}
    output = summarizer.merge_dict(test_dict_1, test_dict_2)
    expected = {"key1": ["value1", "value2"]}
    assert expected == output


def test_get_file_names(tmp_path):
    """Test that get file names return a list of paths"""
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "hello.md"
    p2 = d / "world.md"
    p1.write_text("text")
    p2.write_text("text")
    output = summarizer.get_file_names(d)
    expected = [f"{d}/hello.md", f"{d}/world.md"]
    assert expected == output


def test_md_parser():
    """Test that md parser produce the key value pair of heading and paragraphs
    """
    text = "Some solutions that can be developed to \
avoid harm or fix the harm are conducting more research and not offering it \
to a selective group of people. More research needs to be done especially in \
terms of embryos. In addition, if germline editing is only offered to a \
select group of people, the wealthy, it will be problematic for the class \
system."
    input_md = f"## header1\n{text}\n## header2\n{text}"
    output = summarizer.md_parser(input_md)
    text = text + " "
    expected = {"header1": text, "header2": text}
    assert expected == output


def test_summarizer(tmp_path):
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
