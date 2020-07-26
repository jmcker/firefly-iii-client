# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RuleTrigger(object):
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
        'active': 'bool',
        'created_at': 'datetime',
        'id': 'int',
        'order': 'int',
        'stop_processing': 'bool',
        'type': 'str',
        'updated_at': 'datetime',
        'value': 'str'
    }

    attribute_map = {
        'active': 'active',
        'created_at': 'created_at',
        'id': 'id',
        'order': 'order',
        'stop_processing': 'stop_processing',
        'type': 'type',
        'updated_at': 'updated_at',
        'value': 'value'
    }

    def __init__(self, active=None, created_at=None, id=None, order=None, stop_processing=None, type=None, updated_at=None, value=None):  # noqa: E501
        """RuleTrigger - a model defined in OpenAPI"""  # noqa: E501

        self._active = None
        self._created_at = None
        self._id = None
        self._order = None
        self._stop_processing = None
        self._type = None
        self._updated_at = None
        self._value = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if order is not None:
            self.order = order
        if stop_processing is not None:
            self.stop_processing = stop_processing
        self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        self.value = value

    @property
    def active(self):
        """Gets the active of this RuleTrigger.  # noqa: E501

        If the trigger is active.  # noqa: E501

        :return: The active of this RuleTrigger.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this RuleTrigger.

        If the trigger is active.  # noqa: E501

        :param active: The active of this RuleTrigger.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created_at(self):
        """Gets the created_at of this RuleTrigger.  # noqa: E501


        :return: The created_at of this RuleTrigger.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RuleTrigger.


        :param created_at: The created_at of this RuleTrigger.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this RuleTrigger.  # noqa: E501


        :return: The id of this RuleTrigger.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RuleTrigger.


        :param id: The id of this RuleTrigger.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def order(self):
        """Gets the order of this RuleTrigger.  # noqa: E501

        Order of the trigger  # noqa: E501

        :return: The order of this RuleTrigger.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this RuleTrigger.

        Order of the trigger  # noqa: E501

        :param order: The order of this RuleTrigger.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def stop_processing(self):
        """Gets the stop_processing of this RuleTrigger.  # noqa: E501

        When true, other triggers will not be checked if this trigger was triggered.  # noqa: E501

        :return: The stop_processing of this RuleTrigger.  # noqa: E501
        :rtype: bool
        """
        return self._stop_processing

    @stop_processing.setter
    def stop_processing(self, stop_processing):
        """Sets the stop_processing of this RuleTrigger.

        When true, other triggers will not be checked if this trigger was triggered.  # noqa: E501

        :param stop_processing: The stop_processing of this RuleTrigger.  # noqa: E501
        :type: bool
        """

        self._stop_processing = stop_processing

    @property
    def type(self):
        """Gets the type of this RuleTrigger.  # noqa: E501

        The type of thing this trigger responds to. A limited set is possible  # noqa: E501

        :return: The type of this RuleTrigger.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleTrigger.

        The type of thing this trigger responds to. A limited set is possible  # noqa: E501

        :param type: The type of this RuleTrigger.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["from_account_starts", "from_account_ends", "from_account_is", "from_account_contains", "to_account_starts", "to_account_ends", "to_account_is", "to_account_contains", "amount_less", "amount_exactly", "amount_more", "description_starts", "description_ends", "description_contains", "description_is", "transaction_type", "category_is", "budget_is", "tag_is", "currency_is", "has_attachments", "has_no_category", "has_any_category", "has_no_budget", "has_any_budget", "has_no_tag", "has_any_tag", "notes_contain", "notes_start", "notes_end", "notes_are", "no_notes", "any_notes"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this RuleTrigger.  # noqa: E501


        :return: The updated_at of this RuleTrigger.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RuleTrigger.


        :param updated_at: The updated_at of this RuleTrigger.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def value(self):
        """Gets the value of this RuleTrigger.  # noqa: E501

        The accompanying value the trigger responds to. This value is often mandatory, but this depends on the trigger.  # noqa: E501

        :return: The value of this RuleTrigger.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RuleTrigger.

        The accompanying value the trigger responds to. This value is often mandatory, but this depends on the trigger.  # noqa: E501

        :param value: The value of this RuleTrigger.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, RuleTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
