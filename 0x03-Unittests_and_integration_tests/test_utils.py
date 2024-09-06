#!/usr/bin/env python3
"""
parameterize a unit test
write the first unit test for utils.access_nested_map.
"""

from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
class TestAccessNestedMap(TestCase):
    """
    Test access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
         ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """"Test method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
