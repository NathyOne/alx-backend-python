# #!/usr/bin/env python3
# from utils import get_json
# from unittest.mock import patch, Mock
# import unittest
# from parameterized import parameterized
# from utils import memoize
# from utils import access_nested_map


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


# class TestMemoize(unittest.TestCase):
#     def test_memoize(self):
#         class TestClass:
#             call_count = 0

#             def a_method(self):
#                 TestClass.call_count += 1
#                 return 42

#             @memoize
#             def a_property(self):
#                 return self.a_method()

#         obj = TestClass()

#         result1 = obj.a_property
#         result2 = obj.a_property 

#         # Assertions
#         self.assertEqual(result1, 42)
#         self.assertEqual(result2, 42)
#         # a_method should be called only once
#         self.assertEqual(TestClass.call_count, 1)


# if __name__ == '__main__':
#     unittest.main()
