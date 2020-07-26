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


class ObjectLink(object):
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
        '_0': 'ObjectLink0',
        '_self': 'str'
    }

    attribute_map = {
        '_0': '0',
        '_self': 'self'
    }

    def __init__(self, _0=None, _self=None):  # noqa: E501
        """ObjectLink - a model defined in OpenAPI"""  # noqa: E501

        self.__0 = None
        self.__self = None
        self.discriminator = None

        if _0 is not None:
            self._0 = _0
        if _self is not None:
            self._self = _self

    @property
    def _0(self):
        """Gets the _0 of this ObjectLink.  # noqa: E501


        :return: The _0 of this ObjectLink.  # noqa: E501
        :rtype: ObjectLink0
        """
        return self.__0

    @_0.setter
    def _0(self, _0):
        """Sets the _0 of this ObjectLink.


        :param _0: The _0 of this ObjectLink.  # noqa: E501
        :type: ObjectLink0
        """

        self.__0 = _0

    @property
    def _self(self):
        """Gets the _self of this ObjectLink.  # noqa: E501


        :return: The _self of this ObjectLink.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this ObjectLink.


        :param _self: The _self of this ObjectLink.  # noqa: E501
        :type: str
        """

        self.__self = _self

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
        if not isinstance(other, ObjectLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
