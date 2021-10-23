"""

"""


from decimal import Decimal, ROUND_HALF_UP
from typing import Tuple
from src.rounding.round import Round

class RoundUp(Round):
    def limits(self, x: float) -> Tuple[int, int]:
        
        num = int(Decimal(x).quantize(0, ROUND_HALF_UP))

        return num - 0.5, num + 0.5
