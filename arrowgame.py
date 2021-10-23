"""
Add samples as you go on and then prints out the likelihood of that distribution generating it (when
compare to the other distributions).
"""

from typing import List
from src.distributions.cauchy import Cauchy
from src.distributions.dist import DiscreteDist
from src.distributions.norm import Norm
from src.helpers import is_float
from src.main import get_likelihood

SAMPLE: List[float] = []
DISTS: List[DiscreteDist] = [Norm(0, 0.1), Norm(0, 1), Norm(0, 1.5), Norm(0, 2), Cauchy(0, 1)]

def process_input():
    
    inp = input()

    num = is_float(inp)

    if num is not None:
        SAMPLE.append(float(inp))
    elif inp == "d":
        SAMPLE.pop()

def print_likelihood():

    print(get_likelihood(SAMPLE, DISTS))

while True:
    process_input()

    print_likelihood()
