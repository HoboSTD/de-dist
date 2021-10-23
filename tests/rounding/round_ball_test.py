"""
Tests for src/distributions/round_ball.py
"""

import pytest

from src.rounding.round_ball import RoundBall

@pytest.mark.parametrize("x,dec,explow,exphigh", [
    (0.15, 1, 0.1, 0.2),
    (-1.52, 1, -1.6, -1.5),
    (1.526, 2, 1.52, 1.53),
    (-0.726, 2, -0.73, -0.72),
    (1.5, 3, 1.500, 1.501),
    (0.21, 1, 0.2, 0.3)
])
def test_should_return_expected_limits(x,dec,explow,exphigh):
    
    r = RoundBall(dec)

    assert r.limits(x) == (explow, exphigh)
