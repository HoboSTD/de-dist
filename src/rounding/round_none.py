"""
"""

from typing import Tuple
from src.rounding.round import Round

class RoundNone(Round):
    def limits(self, x: float) -> Tuple[int, int]:
        return (x, x)