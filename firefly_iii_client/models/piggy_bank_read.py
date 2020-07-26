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


class PiggyBankRead(object):
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
        'attributes': 'PiggyBank',
        'id': 'str',
        'links': 'ObjectLink',
        'type': 'str'
    }

    attribute_map = {
        'attributes': 'attributes',
        'id': 'id',
        'links': 'links',
        'type': 'type'
    }

    def __init__(self, attributes=None, id=None, links=None, type=None):  # noqa: E501
        """PiggyBankRead - a model defined in OpenAPI"""  # noqa: E501

        self._attributes = None
        self._id = None
        self._links = None
        self._type = None
        self.discriminator = None

        self.attributes = attributes
        self.id = id
        self.links = links
        self.type = type

    @property
    def attributes(self):
        """Gets the attributes of this PiggyBankRead.  # noqa: E501


        :return: The attributes of this PiggyBankRead.  # noqa: E501
        :rtype: PiggyBank
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this PiggyBankRead.


        :param attributes: The attributes of this PiggyBankRead.  # noqa: E501
        :type: PiggyBank
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this PiggyBankRead.  # noqa: E501


        :return: The id of this PiggyBankRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PiggyBankRead.


        :param id: The id of this PiggyBankRead.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def links(self):
        """Gets the links of this PiggyBankRead.  # noqa: E501


        :return: The links of this PiggyBankRead.  # noqa: E501
        :rtype: ObjectLink
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PiggyBankRead.


        :param links: The links of this PiggyBankRead.  # noqa: E501
        :type: ObjectLink
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def type(self):
        """Gets the type of this PiggyBankRead.  # noqa: E501

        Immutable value  # noqa: E501

        :return: The type of this PiggyBankRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PiggyBankRead.

        Immutable value  # noqa: E501

        :param type: The type of this PiggyBankRead.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, PiggyBankRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
