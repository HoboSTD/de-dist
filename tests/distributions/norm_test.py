"""
Tests for src/distributions/norm.py
"""

import pytest
from src.distributions.dist import DiscreteDist
from src.distributions.norm import Norm


@pytest.mark.parametrize("loc,scale,x,exp", [
    (0, 1, 0, 0.03),
    (7, 2, 5, 0.01)
])
def test_should_have_expected_probability_for_x(loc,scale,x, exp):
    
    c: DiscreteDist = Norm(loc, scale)

    assert abs(c.get_probability(x) - exp) <= 0.1

