# #!/usr/bin/env python3
from utils import get_json
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([      # ← FIRST DECORATOR
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([      # ← SECOND DECORATOR
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """Test that access_nested_map raises KeyError with expected message"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    @patch('requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),    # ← Tuple 1
        ("http://holberton.io", {"payload": False})   # ← Tuple 2
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        response = Mock()
        response.json.return_value = test_payload
        mock_get.return_value = response

        getJson = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(getJson, test_payload)

        if __name__ == '__main__':
            unittest.main()
