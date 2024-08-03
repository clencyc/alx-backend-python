#!/usr/bin/env python3
"""Annotated function zoom_array that takes a tuple lst of floats
    as argument and returns a tuple of zoomed in floats."""

from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)