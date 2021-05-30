"""Test module for markdown.py."""
import pytest
import src.markdown as md
import io
import os


def test_merge_dict():
    """Test that merge_dict returns a dict of key and value lists."""
    test_dict_1 = {"key1": "value1"}
    test_dict_2 = {"key1": "value2"}
    output_preserved = md.merge_dict(test_dict_1, test_dict_2, True)
    output_not_preserved = md.merge_dict(test_dict_1, test_dict_2, False)
    expected = {"key1": ["value1", "value2"]}
    assert expected == output_preserved
    assert expected == output_not_preserved


def test_merge_dict_keys():
    """Test that merge_dict adds empty string for unique keys."""
    test_dict_1 = {"key1": "value1"}
    test_dict_2 = {"key1": "value2", "key2": "value3"}
    output_preserved = md.merge_dict(test_dict_1, test_dict_2, True)
    output_not_preserved = md.merge_dict(test_dict_1, test_dict_2, False)
    expected_preserved = {"key1": ["value1", "value2"], "key2": ["", "value3"]}
    expected_not_preserved = {"key1": ["value1", "value2"]}
    assert expected_preserved == output_preserved
    assert expected_not_preserved == output_not_preserved


def test_get_file_names(tmp_path):
    """Test that get file names return a list of paths."""
    directory = tmp_path / "sub"
    directory.mkdir()
    para_1 = directory / "hello.md"
    para_2 = directory / "world.md"
    para_1.write_text("text")
    para_2.write_text("text")
    output = md.get_file_names(directory)
    expected = [f"{directory}{os.path.sep}hello.md",
                f"{directory}{os.path.sep}world.md"]
    assert expected[0] in output
    assert expected[1] in output


def test_md_parser():
    """Md parser produce the key value pair of heading and paragraphs."""
    text = "Some solutions that can be developed to \
avoid harm or fix the harm are conducting more research and not offering it \
to a selective group of people. More research needs to be done especially in \
terms of embryos. In addition, if germline editing is only offered to a \
select group of people, the wealthy, it will be problematic for the class \
system."
    input_md = f"## header1\n{text}\n## header2\n{text}"
    output = md.md_parser(input_md, is_clean=False)
    text = text + " "
    expected = {"header1": text, "header2": text}
    assert expected == output


def test_collect_md_with_two_inputs(tmp_path):
    """Test that md pipeline works."""
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
    expected = {
        "reflection by": ["", ""],
        "header1": [txt + " ", txt + " "],
        "header2": [txt + " ", txt + " "],
    }
    output = md.collect_md(directory, is_clean=False)
    assert expected == output


def test_collect_md_with_three_inputs(tmp_path):
    """Test that md pipeline works."""
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
    expected = {
        "reflection by": ["", "", ""],
        "header1": [txt + " ", txt + " ", txt + " "],
        "header2": [txt + " ", txt + " ", txt + " "],
    }
    output = md.collect_md(directory, is_clean=False)
    assert expected == output


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("# heading\n```\nregular code block\n```", {"heading": ""},),
        ("# heading\n```\ntype\nnew line\n```", {"heading": ""},),
        (
            "# heading\n```\ntype\nblock one\n```\n```\ntype\nblock 2\n```",
            {"heading": ""},
        ),
        (
            "# heading\n```\ntype\nblock1\n```\ntext\n```\ntype\nblock2\n```",
            {"heading": "text "},
        ),
        ("# heading\ntext with\n```fenced code block\n```",
         {"heading": "text with "},),
        (
            "# heading\ntext with\n```multiple line\nfenced code block\n```",
            {"heading": "text with "},
        ),
        ("# heading\n[linkname](url)![]()", {"heading": "linkname "},),
        ("# heading\n![imgname](path)", {"heading": "imgname "},),
    ],
)
def test_md_parser_clean(input_text, expected):
    """Test if md parser cleans the markdown documents."""
    output = md.md_parser(input_text)
    assert output == expected


def test_import_uploaded_files():
    """Test if the uploaded files are actually imported."""
    uploaded_files = []
    uploaded_files.append(io.BytesIO(
        open("resources/sample_md_reflections/lab1/reflection1.md", "rb")
        .read()))
    uploaded_files.append(io.BytesIO(
        open("resources/sample_md_reflections/lab1/reflection2.md", "rb")
        .read()))
    json_lst = []
    json_lst.append(md.import_uploaded_files(uploaded_files))
    assert json_lst is not []
