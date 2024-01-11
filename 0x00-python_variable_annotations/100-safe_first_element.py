#!/usr/bin/env python3
"""a variable annotations module"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of the input list
    or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
