import pytest

from poetrypackage import simple_math


def test_add_two_numbers():
    result = simple_math.add_two_numbers(1, 2)
    assert result == 3


def test_subtract_two_numbers():
    result = simple_math.subtract_two_numbers(5, 1)
    assert result == 4


def test_subtract_two_numbers_no_negatives():
    with pytest.raises(ValueError):
        simple_math.subtract_two_numbers(1, 2)
