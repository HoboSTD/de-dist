"""

"""

from typing import List
from src.rounding.round import Round
from src.rounding.round_ball import RoundBall
from src.rounding.round_none import RoundNone
from src.rounding.round_up import RoundUp

class DiscreteDist():

    def __init__(self, round_method: Round = RoundBall(1)) -> None:
        self._round_method = round_method

    def get_probability(self, x: float) -> float:
        """Returns the probability that x is retrieved from the distribution. x is treated as the
        closest integer."""

        low, high = self._round_method.limits(x)

        if low == high:
            # i wish i knew statistics
            return self.pdf(low)

        return self.cdf(high) - self.cdf(low)

    def cdf(self, x: float) -> float:
        pass

    def pdf(self, x: float) -> float:
        pass

    def plot(self) -> None:
        pass

    def __str__(self) -> str:
        pass
