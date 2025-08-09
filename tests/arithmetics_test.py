import pytest
from src.arithmetics import add, subtract

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(2,4) == -2
