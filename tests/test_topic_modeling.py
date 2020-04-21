"""Test module for topic_modeling.py"""
import src.topic_modeling as tm


def test_topic_modeling_produce_output():
    """Test that summarize text works"""
    input_text = "Some solutions that can be developed to avoid harm or fix \
the harm are conducting more research and not offering it \
to a selective group of people. More research needs to be \
done especially in terms of embryos. In addition, if germline \
editing is only offered to a select group of people, \
the wealthy, it will be problematic for the class system."
    output = tm.topic_model(input_text)
    assert output is not None
