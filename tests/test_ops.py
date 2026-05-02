"""Tests for code module."""
import pytest

from code import add, greet, multiply


def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0


def test_greet():
    """Test greet function."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("World") == "Hello, World!"


def test_add_with_negative():
    """Test addition with negative numbers."""
    assert add(-5, -3) == -8 