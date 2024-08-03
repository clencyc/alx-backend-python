#!/usr/bin/env python3
"""Annotated function safely_get_value that takes a dictionary dct
    a key key and an optional default value default and returns the value
    with key key in dct if it exists, or default otherwise."""

from typing import Dict, Any, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Dict[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    if key in dct:
        return dct[key]
    else:
        return default