# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from firefly_iii_client.api_client import ApiClient
from firefly_iii_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ChartsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_chart_ab_overview(self, id, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with an overview of the available budget.  # noqa: E501

        This endpoint returns the data required to generate a pie chart for the available budget.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_ab_overview(id, start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The ID of the available budget. (required)
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ChartDataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_chart_ab_overview_with_http_info(id, start, end, **kwargs)  # noqa: E501

    def get_chart_ab_overview_with_http_info(self, id, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with an overview of the available budget.  # noqa: E501

        This endpoint returns the data required to generate a pie chart for the available budget.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_ab_overview_with_http_info(id, start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The ID of the available budget. (required)
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ChartDataSet], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'start', 'end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_ab_overview" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `get_chart_ab_overview`")  # noqa: E501
        # verify the required parameter 'start' is set
        if ('start' not in local_var_params or
                local_var_params['start'] is None):
            raise ApiValueError("Missing the required parameter `start` when calling `get_chart_ab_overview`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in local_var_params or
                local_var_params['end'] is None):
            raise ApiValueError("Missing the required parameter `end` when calling `get_chart_ab_overview`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/chart/ab/overview/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChartDataSet]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chart_account_expense(self, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with expense account balance information.  # noqa: E501

        This endpoint returns the data required to generate a chart that shows the user how much they've spent on their expense accounts.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_account_expense(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ChartDataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_chart_account_expense_with_http_info(start, end, **kwargs)  # noqa: E501

    def get_chart_account_expense_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with expense account balance information.  # noqa: E501

        This endpoint returns the data required to generate a chart that shows the user how much they've spent on their expense accounts.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_account_expense_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ChartDataSet], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['start', 'end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_account_expense" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in local_var_params or
                local_var_params['start'] is None):
            raise ApiValueError("Missing the required parameter `start` when calling `get_chart_account_expense`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in local_var_params or
                local_var_params['end'] is None):
            raise ApiValueError("Missing the required parameter `end` when calling `get_chart_account_expense`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/chart/account/expense', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChartDataSet]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chart_account_overview(self, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with asset account balance information.  # noqa: E501

        This endpoint returns the data required to generate a chart with basic asset account balance information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_account_overview(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ChartDataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_chart_account_overview_with_http_info(start, end, **kwargs)  # noqa: E501

    def get_chart_account_overview_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with asset account balance information.  # noqa: E501

        This endpoint returns the data required to generate a chart with basic asset account balance information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_account_overview_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ChartDataSet], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['start', 'end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_account_overview" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in local_var_params or
                local_var_params['start'] is None):
            raise ApiValueError("Missing the required parameter `start` when calling `get_chart_account_overview`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in local_var_params or
                local_var_params['end'] is None):
            raise ApiValueError("Missing the required parameter `end` when calling `get_chart_account_overview`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/chart/account/overview', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChartDataSet]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chart_account_revenue(self, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with revenue account balance information.  # noqa: E501

        This endpoint returns the data required to generate a chart that shows the user how much they've earned from their revenue accounts.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_account_revenue(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ChartDataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_chart_account_revenue_with_http_info(start, end, **kwargs)  # noqa: E501

    def get_chart_account_revenue_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with revenue account balance information.  # noqa: E501

        This endpoint returns the data required to generate a chart that shows the user how much they've earned from their revenue accounts.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_account_revenue_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ChartDataSet], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['start', 'end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_account_revenue" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in local_var_params or
                local_var_params['start'] is None):
            raise ApiValueError("Missing the required parameter `start` when calling `get_chart_account_revenue`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in local_var_params or
                local_var_params['end'] is None):
            raise ApiValueError("Missing the required parameter `end` when calling `get_chart_account_revenue`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/chart/account/revenue', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChartDataSet]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chart_category_overview(self, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with an overview of the users categories.  # noqa: E501

        This endpoint returns the data required to generate a bar chart for the expenses and incomes on the users categories.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_category_overview(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ChartDataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_chart_category_overview_with_http_info(start, end, **kwargs)  # noqa: E501

    def get_chart_category_overview_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Dashboard chart with an overview of the users categories.  # noqa: E501

        This endpoint returns the data required to generate a bar chart for the expenses and incomes on the users categories.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_category_overview_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ChartDataSet], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['start', 'end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_category_overview" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in local_var_params or
                local_var_params['start'] is None):
            raise ApiValueError("Missing the required parameter `start` when calling `get_chart_category_overview`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in local_var_params or
                local_var_params['end'] is None):
            raise ApiValueError("Missing the required parameter `end` when calling `get_chart_category_overview`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/chart/category/overview', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChartDataSet]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
