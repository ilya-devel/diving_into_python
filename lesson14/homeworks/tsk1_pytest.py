from lesson12.tsk3 import FactorialGenerate
import pytest


def test_without_arguments():
    with pytest.raises(Exception):
        assert FactorialGenerate()


def test_with_one_argument():
    assert [i for i in FactorialGenerate(5)] == [1, 2, 6, 24, 120]


def test_with_two_argument():
    assert [i for i in FactorialGenerate(1, 5)] == [1, 2, 6, 24, 120]


def test_with_three_argument():
    assert [i for i in FactorialGenerate(1, 5, 1)] == [1, 2, 6, 24, 120]


def test_with_four_argument():
    assert [i for i in FactorialGenerate(1, 5, 1, 5)] == [1, 2, 6, 24, 120]


if __name__ == '__main__':
    pytest.main(['-v'])
