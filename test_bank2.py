from bank import value

def test_for_0():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_for_20():
    assert value("harry") == 20
    assert value("hermione") == 20
    assert value("hexagon") == 20

def test_for_100():
    assert value("nyan") == 100
    assert value("cat") == 100
    assert value("rocks") == 100
