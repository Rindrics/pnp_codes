import pytest
from fizzbuzz import generate_fizzbuzz_msg


@pytest.mark.parametrize('multiple_of_3', [i for i in range(1, 50) if i % 3 == 0 and i % 5 != 0 and i != 12])
def test_return_fizz(multiple_of_3):
    assert generate_fizzbuzz_msg(multiple_of_3) == 'Fizz'


@pytest.mark.parametrize('multiple_of_5', [i for i in range(1, 50) if i % 5 == 0 and i % 3 != 0])
def test_return_buzz(multiple_of_5):
    assert generate_fizzbuzz_msg(multiple_of_5) == 'Buzz'


@pytest.mark.parametrize('multiple_of_15', [i for i in range(1, 100) if i % 3 == 0 and i % 5 == 0])
def test_return_fizzbuzz(multiple_of_15):
    assert generate_fizzbuzz_msg(multiple_of_15) == 'FizzBuzz'


@pytest.mark.parametrize('otherwise', [i for i in range(1, 100) if i % 3 != 0 and i % 5 != 0])
def test_return_fizzbuzz(otherwise):
    assert generate_fizzbuzz_msg(otherwise) == str(otherwise)


@pytest.mark.parametrize('consecutive', [12, 34])
def test_return_fizzbuzz(consecutive):
    assert generate_fizzbuzz_msg(consecutive) == str(consecutive) + '連番!'
