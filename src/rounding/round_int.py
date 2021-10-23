"""
"""

from math import floor, ceil
from typing import Tuple
from src.rounding.round import Round

class RoundInt(Round):
    def limits(self, x: float) -> Tuple[int, int]:
        
        return floor(x), ceil(x)
