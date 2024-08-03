#!/usr/bin/env python3
"""Annotated function sum_mixed_list that takes a list input_list of floats
    as argument and returns their sum as a float."""

from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return the sum of the list of floats input_list."""
    return sum(mxd_list)
