"""Test cases for json util."""

import src.json_util as js


def test_get_json_files(tmp_path):
    """Test that get json files return correct json files."""
    directory = tmp_path / "sub"
    directory.mkdir()
    para_1 = directory / "hello.json"
    para_2 = directory / "world.json"
    para_1.write_text("{\"assignment\": \"java-assignment\"}")
    para_2.write_text("{\"assignment\": \"java-assignment\"}")
    output = js.get_json_files(directory)
    expect = [
        {'assignment': 'java-assignment'},
        {'assignment': 'java-assignment'}
    ]
    assert expect == output


def test_clean_report():
    """Test clean report filters out unwanted keys and contain correct keys."""
    raw_json_lst = [
        {
            "assignment": "java-assignment",
            "reflection": """# Reflection by\nuser one\n## Header1\n\
Hello World.""",
            "report": "A report",
            "time": "2020-01-15T18:01:55.416Z",
            "userId": "computer-science-101-fall-2018-practical-9-user1",
            "uuidID": "069004d0-2a9a-4030-822c-b99560e89b30",
        },
        {
            "assignment": "java-assignment",
            "reflection": """# Reflection by\n user two \n\n## Header1\ntext.\
\n## Header2\nWorld.""",
            "report": "A report",
            "time": "2020-01-15T18:01:55.416Z",
            "userId": "computer-science-101-fall-2018-practical-9-user2",
            "uuidID": "069004d0-2a9a-4030-822c-b99560e89b30",
        }
    ]
    clean_json_lst = js.clean_report(raw_json_lst)
    assert clean_json_lst is not None
    assert "report" not in clean_json_lst[0].keys()
    assert "time" not in clean_json_lst[0].keys()
    assert "uuidid" not in clean_json_lst[0].keys()
    assert "header1" in clean_json_lst[0].keys()
    assert "reflection by" in clean_json_lst[0].keys()
