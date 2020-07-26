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


class PiggyBankEvent(object):
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
        'amount': 'str',
        'created_at': 'datetime',
        'currency_code': 'str',
        'currency_decimal_places': 'int',
        'currency_id': 'int',
        'currency_symbol': 'str',
        'journal_id': 'int',
        'transaction_id': 'int',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'amount': 'amount',
        'created_at': 'created_at',
        'currency_code': 'currency_code',
        'currency_decimal_places': 'currency_decimal_places',
        'currency_id': 'currency_id',
        'currency_symbol': 'currency_symbol',
        'journal_id': 'journal_id',
        'transaction_id': 'transaction_id',
        'updated_at': 'updated_at'
    }

    def __init__(self, amount=None, created_at=None, currency_code=None, currency_decimal_places=None, currency_id=None, currency_symbol=None, journal_id=None, transaction_id=None, updated_at=None):  # noqa: E501
        """PiggyBankEvent - a model defined in OpenAPI"""  # noqa: E501

        self._amount = None
        self._created_at = None
        self._currency_code = None
        self._currency_decimal_places = None
        self._currency_id = None
        self._currency_symbol = None
        self._journal_id = None
        self._transaction_id = None
        self._updated_at = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if created_at is not None:
            self.created_at = created_at
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_decimal_places is not None:
            self.currency_decimal_places = currency_decimal_places
        if currency_id is not None:
            self.currency_id = currency_id
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        if journal_id is not None:
            self.journal_id = journal_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def amount(self):
        """Gets the amount of this PiggyBankEvent.  # noqa: E501


        :return: The amount of this PiggyBankEvent.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PiggyBankEvent.


        :param amount: The amount of this PiggyBankEvent.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def created_at(self):
        """Gets the created_at of this PiggyBankEvent.  # noqa: E501


        :return: The created_at of this PiggyBankEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PiggyBankEvent.


        :param created_at: The created_at of this PiggyBankEvent.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def currency_code(self):
        """Gets the currency_code of this PiggyBankEvent.  # noqa: E501


        :return: The currency_code of this PiggyBankEvent.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this PiggyBankEvent.


        :param currency_code: The currency_code of this PiggyBankEvent.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_decimal_places(self):
        """Gets the currency_decimal_places of this PiggyBankEvent.  # noqa: E501


        :return: The currency_decimal_places of this PiggyBankEvent.  # noqa: E501
        :rtype: int
        """
        return self._currency_decimal_places

    @currency_decimal_places.setter
    def currency_decimal_places(self, currency_decimal_places):
        """Sets the currency_decimal_places of this PiggyBankEvent.


        :param currency_decimal_places: The currency_decimal_places of this PiggyBankEvent.  # noqa: E501
        :type: int
        """

        self._currency_decimal_places = currency_decimal_places

    @property
    def currency_id(self):
        """Gets the currency_id of this PiggyBankEvent.  # noqa: E501


        :return: The currency_id of this PiggyBankEvent.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this PiggyBankEvent.


        :param currency_id: The currency_id of this PiggyBankEvent.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this PiggyBankEvent.  # noqa: E501


        :return: The currency_symbol of this PiggyBankEvent.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this PiggyBankEvent.


        :param currency_symbol: The currency_symbol of this PiggyBankEvent.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def journal_id(self):
        """Gets the journal_id of this PiggyBankEvent.  # noqa: E501

        The journal associated with the event.  # noqa: E501

        :return: The journal_id of this PiggyBankEvent.  # noqa: E501
        :rtype: int
        """
        return self._journal_id

    @journal_id.setter
    def journal_id(self, journal_id):
        """Sets the journal_id of this PiggyBankEvent.

        The journal associated with the event.  # noqa: E501

        :param journal_id: The journal_id of this PiggyBankEvent.  # noqa: E501
        :type: int
        """

        self._journal_id = journal_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this PiggyBankEvent.  # noqa: E501


        :return: The transaction_id of this PiggyBankEvent.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this PiggyBankEvent.


        :param transaction_id: The transaction_id of this PiggyBankEvent.  # noqa: E501
        :type: int
        """

        self._transaction_id = transaction_id

    @property
    def updated_at(self):
        """Gets the updated_at of this PiggyBankEvent.  # noqa: E501


        :return: The updated_at of this PiggyBankEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PiggyBankEvent.


        :param updated_at: The updated_at of this PiggyBankEvent.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, PiggyBankEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
