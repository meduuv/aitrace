from aitrace import summarize


def test_summarize():
    assert summarize([{"type": "prompt"}, {"type": "prompt"}, {"type": "tool"}]) == {"prompt": 2, "tool": 1}
