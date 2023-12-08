from jar import Jar
import pytest

def main():
    test_init()
    test_deposit()
    test_withdraw()

def test_init():
    Jar()

def test_str():
    jar = Jar()

    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"

    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

if __name__ == "__main__":
    main()
