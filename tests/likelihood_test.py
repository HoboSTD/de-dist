"""
Tests for src/likelihood.py
"""

import pytest
from src.distributions.norm import Norm
from src.distributions.cauchy import Cauchy
from src.likelihood import Likelihood

def test_should_return_zero_when_dist_is_None():
    
    l = Likelihood()

    assert l.calc([1, 2, 3, 4], None) == 0

def test_should_return_zero_when_sample_is_empty():

    l = Likelihood()

    assert l.calc(None, Norm()) == 0
    assert l.calc([], Norm()) == 0

@pytest.mark.parametrize("sample,dist,baddist", [
    ([0.71155342, -0.99608666,  0.35718583,  0.60964406, -1.63703384,
       -0.05079048, -1.07931541,  1.52235017], Norm(0, 1), Norm(15, 1)),
    ([0.71155342, -0.99608666,  0.35718583,  0.60964406, -1.63703384,
       -0.05079048, -1.07931541,  1.52235017], Norm(0, 1), Cauchy(0, 1)),
    ([0.58755082, -1.95900827, 0.89697574, 0.32320017,
        -0.2096736 , 6.45967173, -0.08329996, 33.10104183,
         0.30464658, 0.04313449, -0.85626042, 1.43348461,
        -1.72846515, -38.49404961, 0.8837066 ], Cauchy(0, 1.5), Norm(0, 1))
])
def test_should_have_most_likely_distribution_be_likely(sample, dist, baddist):

    l = Likelihood()

    assert l.calc(sample, dist) > l.calc(sample, baddist)
