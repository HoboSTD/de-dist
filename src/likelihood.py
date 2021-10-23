"""

"""

from typing import List
from src.distributions.dist import DiscreteDist

class Likelihood():
    
    
    def calc(self, sample: List[float], dist: DiscreteDist) -> float:
        """Returns the likelihood that a given distribution could produce the given sample."""

        if not (self.__is_valid_sample__(sample) and self.__is_valid_dist__(dist)):
            return 0

        prod = 1
        for x in sample:
            prod *= dist.get_probability(x)

        return prod

    def __is_valid_sample__(self, sample: List[float]) -> bool:
        return not (sample is None or len(sample) == 0)

    def __is_valid_dist__(self, dist: DiscreteDist) -> bool:
        return not (dist is None)
