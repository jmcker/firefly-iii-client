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
from firefly_iii_client.api.charts_api import ChartsApi  # noqa: E501
from firefly_iii_client.rest import ApiException


class TestChartsApi(unittest.TestCase):
    """ChartsApi unit test stubs"""

    def setUp(self):
        self.api = firefly_iii_client.api.charts_api.ChartsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_chart_ab_overview(self):
        """Test case for get_chart_ab_overview

        Dashboard chart with an overview of the available budget.  # noqa: E501
        """
        pass

    def test_get_chart_account_expense(self):
        """Test case for get_chart_account_expense

        Dashboard chart with expense account balance information.  # noqa: E501
        """
        pass

    def test_get_chart_account_overview(self):
        """Test case for get_chart_account_overview

        Dashboard chart with asset account balance information.  # noqa: E501
        """
        pass

    def test_get_chart_account_revenue(self):
        """Test case for get_chart_account_revenue

        Dashboard chart with revenue account balance information.  # noqa: E501
        """
        pass

    def test_get_chart_category_overview(self):
        """Test case for get_chart_category_overview

        Dashboard chart with an overview of the users categories.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
