"""
Tests for src/distributions/round_up.py
"""

import pytest

from src.rounding.round_up import RoundUp

@pytest.mark.parametrize("x,low,high", [
    (1, 0.5, 1.5),
    (-0.5, -1, 0)
])
def should_return_expected_limits(x, low, high):

    round = RoundUp()

    assert round.limits(x) == (low, high)
