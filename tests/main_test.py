"""
Tests for src/main.py
"""

import pytest
from src.distributions.cauchy import Cauchy
from src.distributions.norm import Norm
from src.main import get_likelihood

def test_should_return_empty_list_with_no_distributions():
    
    sample = [1, 5, 2, 3, 5, 6, 7]

    dists = []

    assert get_likelihood(sample, dists) == []


@pytest.mark.parametrize("sample,dists,likelihoods", [
    ([0.22204242, 1.84922605,-1.28702148, -0.0123778 , 0.07474418,
       -1.13721395, 0.69838433, 0.33901584, 0.0064624 , -2.24975486,
        0.62372228, 0.61522663, 1.20961844, 0.43562501, -0.74016835,
       -0.34255835, 1.66108685, -0.59715636, 1.40097694, -0.63342791],
       [Norm(0, 0.1), Norm(0, 1), Norm(0, 1.5), Norm(0, 2), Cauchy(0, 1)],
       [0, 0.89, 0.09, 0, 0]),
])
def test_should_return_expected_likelihoods(sample, dists, likelihoods):
    
    res = get_likelihood(sample, dists)

    print(res)

    for i in range(0, len(likelihoods)):
        assert abs(res[i][1] - likelihoods[i]) <= 0.1
