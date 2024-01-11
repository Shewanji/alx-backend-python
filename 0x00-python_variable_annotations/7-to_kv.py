#!/usr/bin/env python3
"""a variable annotations module"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the first element as the string k
    and the second element as the square of the int/float v.
    """
    return k, v ** 2.0
