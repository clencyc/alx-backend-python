#!/usr/bin/env python3
"""Annotated function to_kv that takes a string
 k and an int OR float v as arguments and
   returns a tuple containing k and the square of v."""


def to_kv(k: str, v: int) -> tuple:
    """Return a tuple of k and the square of v."""
    return (k, v * v)