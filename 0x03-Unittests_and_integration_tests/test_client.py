#!/usr/bin/env python3

from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import GithubOrgClient
import unittest


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("https://google.org", {"payload": True}),
        ("https://abc.org", {"payload": True})
    ])
    def test_org(self, url, payload):
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            print(mock_response)
            mock_response.json.return_value = payload
            mock_get.return_value = mock_response

            client = GithubOrgClient(url)
            result = client.org()

            self.assertEqual(result, payload)
            mock_get.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
