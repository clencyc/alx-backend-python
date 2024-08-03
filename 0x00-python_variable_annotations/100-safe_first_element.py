#!/usr/bin/env python3
# The types of the elements of the input are not know

from typing import Any, Optional, Sequence, Union


def safe_first_element(lst: Sequence) -> Union[object, None]:
    """Return the first element of a list if it exists."""
    if lst:
        return lst[0]
    else:
        return None