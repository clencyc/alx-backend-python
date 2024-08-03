#!/usr/bin/env python3
"""Annotated function element_length that takes a list input_list of strings
    as argument and returns a list of integers representing the lengths of the strings."""

from typing import List, Tuple


def element_length(lst: List[str]) -> list[Tuple[str, int]]:
    """Return a list of integers representing the lengths of the strings in input_list."""
    return [(i, len(i)) for i in lst]