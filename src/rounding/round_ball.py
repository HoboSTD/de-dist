"""

"""

from math import floor
from typing import Tuple
from src.rounding.round import Round

class RoundBall(Round):

    def __init__(self, round_to: int) -> None:
        super().__init__()
        self._multiplier = 10 ** round_to

    def limits(self, x: float) -> Tuple[float, float]:
        # shift last significant digit to first digit before decimal point, drop anything after the
        # decimal point
        num = floor(x * self._multiplier)

        # move last significant digit back
        return num / self._multiplier, (num + 1) / self._multiplier
