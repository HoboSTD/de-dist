"""
Tests for src/helpers.py
"""

from src.helpers import is_float

def test_should_return_value_if_integer():
    
    assert is_float("5") == float(5)

def test_should_return_true_if_negative_integer():
    
    assert is_float("-5") == float(-5)

def test_should_return_none_if_not_integer():

    assert is_float("I very much dislike the programming language Python") == None

def test_should_return_true_if_float():

    assert is_float("5.24") == 5.24

def test_should_return_true_if_negative_float():
    
    assert is_float("-5.24") == -5.24
