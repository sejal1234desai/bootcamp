from processors.snake import to_snakecase
from processors.line_counter import LineCounter
from processors.splitter import Splitter
from processors.join_pairs import JoinPairs

def test_to_snakecase():
    lines = iter(["Hello World", "Test Case"])
    result = list(to_snakecase(lines))
    assert result == ["hello_world", "test_case"]

def test_line_counter():
    processor = LineCounter()
    lines = iter(["a", "b", "c"])
    result = list(processor(lines))
    assert result == ["1: a", "2: b", "3: c"]

def test_splitter():
    processor = Splitter(delimiter="|")
    lines = iter(["a|b|c"])
    result = list(processor(lines))
    assert result == ["a", "b", "c"]

def test_join_pairs():
    processor = JoinPairs()
    lines = iter(["a", "b", "c"])
    result = list(processor(lines))
    assert result == ["a b", "c"]
