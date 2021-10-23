"""
The main file.
"""

from typing import List, Tuple

from src.distributions.dist import DiscreteDist
from src.rounding.round_ball import RoundBall
from src.likelihood import Likelihood

def get_likelihood(sample: List[float], dists: List[DiscreteDist]) -> List[Tuple[DiscreteDist,
        float]]:

    if len(dists) == 0:
        return []

    l = Likelihood()
    r = RoundBall(2)

    res: List[Tuple[DiscreteDist, float]] = []
    sum = 0
    for dist in dists:
        p = l.calc(sample, dist)
        res.append(list([dist, p]))
        sum += p

    for i in range(0, len(res)):
        if sum != 0:
            res[i][1] = r.limits(res[i][1] / sum)[0]

    return res
