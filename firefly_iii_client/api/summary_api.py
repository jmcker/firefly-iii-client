# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from firefly_iii_client.api_client import ApiClient
from firefly_iii_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SummaryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_basic_summary(self, start, end, **kwargs):  # noqa: E501
        """Returns basic sums of the users data.  # noqa: E501

        Returns basic sums of the users data, like the net worth, spent and earned amounts. It is multi-currency, and is in Firefly III to populate the dashboard.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_basic_summary(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param str currency_code: A currency code like EUR or USD, to filter the result. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BasicSummaryEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_basic_summary_with_http_info(start, end, **kwargs)  # noqa: E501

    def get_basic_summary_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Returns basic sums of the users data.  # noqa: E501

        Returns basic sums of the users data, like the net worth, spent and earned amounts. It is multi-currency, and is in Firefly III to populate the dashboard.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_basic_summary_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param date start: A date formatted YYYY-MM-DD.  (required)
        :param date end: A date formatted YYYY-MM-DD.  (required)
        :param str currency_code: A currency code like EUR or USD, to filter the result. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[BasicSummaryEntry], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'start',
            'end',
            'currency_code'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_basic_summary" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'start' is set
        if self.api_client.client_side_validation and ('start' not in local_var_params or  # noqa: E501
                                                        local_var_params['start'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start` when calling `get_basic_summary`")  # noqa: E501
        # verify the required parameter 'end' is set
        if self.api_client.client_side_validation and ('end' not in local_var_params or  # noqa: E501
                                                        local_var_params['end'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end` when calling `get_basic_summary`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params and local_var_params['start'] is not None:  # noqa: E501
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params and local_var_params['end'] is not None:  # noqa: E501
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'currency_code' in local_var_params and local_var_params['currency_code'] is not None:  # noqa: E501
            query_params.append(('currency_code', local_var_params['currency_code']))  # noqa: E501

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
            '/api/v1/summary/basic', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BasicSummaryEntry]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
