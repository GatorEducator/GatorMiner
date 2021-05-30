"""Test module for topic_modeling.py."""
import src.topic_modeling as tm


def test_topic_modeling_produce_output():
    """Test that summarize text works."""
    input_text = [["This", "is", "a", "sentence"]]
    output = tm.topic_model(input_text)
    assert output is not None
