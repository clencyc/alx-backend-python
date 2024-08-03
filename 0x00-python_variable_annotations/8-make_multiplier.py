#!/usr/bin/env python3
"""Annotated function make_multiplier
 that takes a float multiplier as argument
    and returns a function that multiplies 
    a float by multiplier.
    """


def make_multiplier(multiplier: float) -> callable:
    """Return a function that multiplies a float by multiplier."""
    def fun(n: float) -> float:
        return n * multiplier
    return fun