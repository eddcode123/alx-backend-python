#!/usr/bin/env python3
"""Test access_nested_map"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Raise keyerror exception in the parameterized case"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, expected, mock_get):
        """Test that get_json retrieves and returns JSON data correctly"""
        # Configure the mock
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected

        # call the the function get_json
        result = get_json(test_url)

        self.assertEqual(result, expected)
        mock_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
