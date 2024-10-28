"""Test the functionality of naive prime algorithm."""

from main import find_all_primes


def test_find_all_primes_class1():
    result = find_all_primes(10)
    assert result == [2, 3, 5, 7]


def test_find_all_primes_class2():
    result = find_all_primes(1)
    assert result == []


def test_find_all_primes_class3():
    result = find_all_primes(-1)
    assert result == []


def test_find_all_primes_class4():
    result = find_all_primes(50)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


if __name__ == "__main__":
    test_find_all_primes_class1()
    test_find_all_primes_class2()
    test_find_all_primes_class3()
    test_find_all_primes_class4()
