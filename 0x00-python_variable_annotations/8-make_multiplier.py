#!/usr/bin/env python3
"""a variable annotations module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiply the given float by the multiplier.
        """
        return x * multiplier

    return multiplier_function
