# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class MetaPagination(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'count': 'int',
        'current_page': 'int',
        'per_page': 'int',
        'total': 'int',
        'total_pages': 'int'
    }

    attribute_map = {
        'count': 'count',
        'current_page': 'current_page',
        'per_page': 'per_page',
        'total': 'total',
        'total_pages': 'total_pages'
    }

    def __init__(self, count=None, current_page=None, per_page=None, total=None, total_pages=None):  # noqa: E501
        """MetaPagination - a model defined in OpenAPI"""  # noqa: E501

        self._count = None
        self._current_page = None
        self._per_page = None
        self._total = None
        self._total_pages = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if current_page is not None:
            self.current_page = current_page
        if per_page is not None:
            self.per_page = per_page
        if total is not None:
            self.total = total
        if total_pages is not None:
            self.total_pages = total_pages

    @property
    def count(self):
        """Gets the count of this MetaPagination.  # noqa: E501


        :return: The count of this MetaPagination.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MetaPagination.


        :param count: The count of this MetaPagination.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def current_page(self):
        """Gets the current_page of this MetaPagination.  # noqa: E501


        :return: The current_page of this MetaPagination.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this MetaPagination.


        :param current_page: The current_page of this MetaPagination.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def per_page(self):
        """Gets the per_page of this MetaPagination.  # noqa: E501


        :return: The per_page of this MetaPagination.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this MetaPagination.


        :param per_page: The per_page of this MetaPagination.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def total(self):
        """Gets the total of this MetaPagination.  # noqa: E501


        :return: The total of this MetaPagination.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this MetaPagination.


        :param total: The total of this MetaPagination.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def total_pages(self):
        """Gets the total_pages of this MetaPagination.  # noqa: E501


        :return: The total_pages of this MetaPagination.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this MetaPagination.


        :param total_pages: The total_pages of this MetaPagination.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetaPagination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
