from um import count

def test_count1():
    assert count("yummy") == 0
    assert count("ummy") == 0
    assert count("u m") == 0

def test_count2():
    assert count("um") == 1
    assert count("yummy um") == 1
    assert count("yummy um yummy") == 1

def test_count3():
    assert count("um um") == 2
    assert count("um yummy um...") == 2
    assert count("um yummy yummy u m u m um") == 2

def test_count4():
    assert count("UM") == 1
    assert count("Um yummy um...") == 2
    assert count("U M um") == 1
    assert count("U M") == 0
