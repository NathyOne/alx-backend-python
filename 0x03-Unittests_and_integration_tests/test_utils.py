#!/usr/bin/env python3

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


# Import the external library

# Assuming utils.py is available or the function is imported correctly


class TestGetJson(unittest.TestCase):
    """Tests for the utils.get_json function using @parameterized."""

    # 1. Define the test data
    # Each tuple in the list represents one call to the test method.
    # The elements in the tuple map to the arguments of the test method.
    DATA = [
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ]

    # 2. Use the decorator to expand the test
    @parameterized.expand(DATA)
    @patch('requests.get')
    def test_get_json(self, mock_requests_get, test_url, test_payload):
        """
        Tests that get_json returns the expected JSON payload 
        and calls requests.get exactly once with the correct URL.
        """
        # The arguments are: self, the patched object, and the data from the list (in order)

        # 3. Configure the Mock object
        # Create a Mock object for the response
        mock_response = Mock()

        # Configure the return value of its '.json()' method
        mock_response.json.return_value = test_payload

        # Configure the return value of the patched function itself
        mock_requests_get.return_value = mock_response

        # 4. Call the function under test
        result = get_json(test_url)

        # 5. Assert the behavior (Verification)

        # Test that the mocked get method was called exactly once
        # with test_url as argument.
        mock_requests_get.assert_called_once_with(test_url)

        # Test that the output of get_json is equal to test_payload.
        self.assertEqual(result, test_payload)

# To run the tests, you would typically use:
# if __name__ == '__main__':
#     unittest.main()
