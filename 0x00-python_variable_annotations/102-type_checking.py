#!/usr/bin/env python3
"""Annotated function zoom_array that takes a tuple lst of floats
    as argument and returns a tuple of zoomed in floats."""

from typing import Tuple, List, Iterable


def zoom_array(lst: Iterable, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array), 2)

zoom_3x = zoom_array(tuple(array), 3.0)