from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/3") == 33
    assert convert("3/4") == 75
    assert convert("1/4") == 25

    with pytest.raises(ValueError):
        convert("hot/dog")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
