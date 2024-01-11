#!/usr/bin/env python3
"""a variable annotations module"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely gets the value associated with the given key in the dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
