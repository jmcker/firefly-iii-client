# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import firefly_iii_client
from firefly_iii_client.api.search_api import SearchApi  # noqa: E501
from firefly_iii_client.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = firefly_iii_client.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_accounts(self):
        """Test case for search_accounts

        Search for accounts  # noqa: E501
        """
        pass

    def test_search_transactions(self):
        """Test case for search_transactions

        Search for transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
