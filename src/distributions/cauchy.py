"""

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import cauchy
from src.distributions.dist import DiscreteDist

class Cauchy(DiscreteDist):

    def __init__(self, mean: float = 0, stddev: float = 1) -> None:
        self._mean = mean
        self._stddev = stddev
        self._dist = cauchy(loc=mean, scale=stddev)
        super().__init__()
    
    def cdf(self, x: float) -> float:
        return self._dist.cdf(x)

    def pdf(self, x: float) -> float:
        return self._dist.pdf(x)

    def plot(self) -> None:
        fig, ax = plt.subplots(1, 1)
        x = np.linspace(self._dist.ppf(0.01), self._dist.ppf(0.99), 100)
        ax.plot(x, self._dist.pdf(x), 'r-', lw=5, alpha=0.6, label='cauchy pdf')
        plt.show()

    def __str__(self) -> str:
        return f"cauchy({self._mean}, {self._stddev})"

    def __repr__(self) -> str:
        return f"cauchy({self._mean}, {self._stddev})"
