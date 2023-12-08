from plates import is_valid



def test_is_valid1():
    assert is_valid("CS50")
    assert not is_valid("F")
    assert not is_valid("PI3.14")
    assert not is_valid("catdogcatdogcatdog")
    assert not is_valid("AAB22C")
    assert not is_valid("CS05")
    assert not is_valid("12ABC")
    assert not is_valid("11")
