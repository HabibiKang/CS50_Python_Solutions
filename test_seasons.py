from seasons import get_mins

def test_get_mins1():
    assert get_mins(2022, 5, 24) == "Five hundred twenty-five thousand, six hundred minutes"
def test_get_mins2():
    assert get_mins(2021,5,24) == "One million, fifty-one thousand, two hundred minutes"
def test_get_mins3():
    assert get_mins(2001,4,8) == "Eleven million, six hundred thirty-six thousand, six hundred forty minutes"
