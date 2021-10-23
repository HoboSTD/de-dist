"""
Tests for src/distributions/round_int.py
"""

import pytest
from src.rounding.round_int import RoundInt

@pytest.mark.parametrize("x,low,high", [
    (1, 1, 2),
    (-0.5, -1, 0),
    (7.5, 7, 8)
])
def should_return_expected_limits(x, low, high):

    round = RoundInt()

    assert round.limits(x) == (low, high)
