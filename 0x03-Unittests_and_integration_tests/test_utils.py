#!/usr/bin/env python3
from utils import get_json
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized
from utils import memoize
from utils import access_nested_map


# class TestAccessNestedMap(unittest.TestCase):

#     @parameterized.expand([      # ← FIRST DECORATOR
#         ({"a": 1}, ("a",), 1),
#         ({"a": {"b": 2}}, ("a",), {"b": 2}),
#         ({"a": {"b": 2}}, ("a", "b"), 2),
#     ])
#     def test_access_nested_map(self, nested_map, path, expected):
#         """Test that access_nested_map returns the expected result"""
#         self.assertEqual(access_nested_map(nested_map, path), expected)

#     @parameterized.expand([      # ← SECOND DECORATOR
#         ({}, ("a",), "'a'"),
#         ({"a": 1}, ("a", "b"), "'b'"),
#     ])
#     def test_access_nested_map_exception(self, nested_map, path, expected_message):
#         """Test that access_nested_map raises KeyError with expected message"""
#         with self.assertRaises(KeyError) as context:
#             access_nested_map(nested_map, path)

#         self.assertEqual(str(context.exception), expected_message)


# class TestGetJson(unittest.TestCase):

#     def test_get_json(self):
#         """Test get_json with multiple test cases"""
#         test_cases = [
#             ("http://example.com", {"payload": True}),
#             ("http://holberton.io", {"payload": False})
#         ]

#         for test_url, test_payload in test_cases:
#             with self.subTest(url=test_url, payload=test_payload):
#                 with patch('utils.requests.get') as mock_get:
#                     mock_response = Mock()
#                     mock_response.json.return_value = test_payload
#                     mock_get.return_value = mock_response

#                     result = get_json(test_url)

#                     mock_get.assert_called_once_with(test_url)
#                     self.assertEqual(result, test_payload)

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator functionality"""

    def test_memoize(self):
        """Test that memoize caches the result and calls the method only once"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Use patch to mock a_method and track its calls
        with patch.object(test_instance, 'a_method') as mock_method:
            # Configure the mock to return a specific value
            mock_method.return_value = 42

            # Call a_property twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            # Assert that the correct result is returned both times
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert that a_method was called only once due to memoization
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
