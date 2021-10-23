"""
Tests for src/distributions/cauchy.py
"""

import pytest
from src.distributions.cauchy import Cauchy
from src.distributions.dist import DiscreteDist

def test_should_have_cdf_at_mean_equal_to_half():
    
    c = Cauchy()

    assert c.cdf(0) == 0.5

def test_should_be_able_to_have_different_means():

    c = Cauchy(7, 2)

    assert c.cdf(7) == 0.5

@pytest.mark.parametrize("loc,scale,x,exp", [
    (0, 1, 0, 0.03),
    (7, 2, 5, 0.08)
])
def test_should_have_expected_probability_for_x(loc,scale,x, exp):
    
    c: DiscreteDist = Cauchy(loc, scale)

    assert abs(c.get_probability(x) - exp) <= 0.1

