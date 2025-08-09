from src.calculator import add, subtract
import pytest

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 5