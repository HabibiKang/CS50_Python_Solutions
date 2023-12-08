from numb3rs import validate

def test_validate1():
    assert validate("127.0.0.1")
    assert validate("255.255.255.255")
    assert validate("200.150.1.1")
    assert validate("0.0.0.0")
    assert validate("1.1.1.1")

def test_validate2():
    assert not validate("512.512.512.512")
    assert not validate("233.233.233.233.233")
    assert not validate("1.256.256.256")
    assert not validate("256.1.1.1")
    assert not validate("1.2.3.1000")
    assert not validate("cat")


test_validate1()
test_validate2()
