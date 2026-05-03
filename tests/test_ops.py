"""Simple tests for code.py"""
from code import add, multiply


def test_add():
    """Test: 2 + 3 = 5"""
    assert add(2, 3) == 5


def test_add_negative():
    """Test: -5 + -3 = -8"""
    assert add(-5, -3) == -8


def test_multiply():
    """Test: 3 * 4 = 12"""
    assert multiply(3, 4) == 12 
