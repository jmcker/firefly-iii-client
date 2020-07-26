# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ChartDataPoint(object):
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
        'key': 'str'
    }

    attribute_map = {
        'key': 'key'
    }

    def __init__(self, key=None):  # noqa: E501
        """ChartDataPoint - a model defined in OpenAPI"""  # noqa: E501

        self._key = None
        self.discriminator = None

        if key is not None:
            self.key = key

    @property
    def key(self):
        """Gets the key of this ChartDataPoint.  # noqa: E501

        The key is the label of the value, so for example: '2018-01-01' => 13 or 'Groceries' => -123.  # noqa: E501

        :return: The key of this ChartDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ChartDataPoint.

        The key is the label of the value, so for example: '2018-01-01' => 13 or 'Groceries' => -123.  # noqa: E501

        :param key: The key of this ChartDataPoint.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if not isinstance(other, ChartDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
