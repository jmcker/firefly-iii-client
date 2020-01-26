# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BillPaidDates(object):
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
        'date': 'date',
        'transaction_group_id': 'int',
        'transaction_journal_id': 'int'
    }

    attribute_map = {
        'date': 'date',
        'transaction_group_id': 'transaction_group_id',
        'transaction_journal_id': 'transaction_journal_id'
    }

    def __init__(self, date=None, transaction_group_id=None, transaction_journal_id=None):  # noqa: E501
        """BillPaidDates - a model defined in OpenAPI"""  # noqa: E501

        self._date = None
        self._transaction_group_id = None
        self._transaction_journal_id = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if transaction_group_id is not None:
            self.transaction_group_id = transaction_group_id
        if transaction_journal_id is not None:
            self.transaction_journal_id = transaction_journal_id

    @property
    def date(self):
        """Gets the date of this BillPaidDates.  # noqa: E501

        Date the bill was paid.  # noqa: E501

        :return: The date of this BillPaidDates.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this BillPaidDates.

        Date the bill was paid.  # noqa: E501

        :param date: The date of this BillPaidDates.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def transaction_group_id(self):
        """Gets the transaction_group_id of this BillPaidDates.  # noqa: E501

        Transaction group ID of the paid bill.  # noqa: E501

        :return: The transaction_group_id of this BillPaidDates.  # noqa: E501
        :rtype: int
        """
        return self._transaction_group_id

    @transaction_group_id.setter
    def transaction_group_id(self, transaction_group_id):
        """Sets the transaction_group_id of this BillPaidDates.

        Transaction group ID of the paid bill.  # noqa: E501

        :param transaction_group_id: The transaction_group_id of this BillPaidDates.  # noqa: E501
        :type: int
        """

        self._transaction_group_id = transaction_group_id

    @property
    def transaction_journal_id(self):
        """Gets the transaction_journal_id of this BillPaidDates.  # noqa: E501

        Transaction journal ID of the paid bill.  # noqa: E501

        :return: The transaction_journal_id of this BillPaidDates.  # noqa: E501
        :rtype: int
        """
        return self._transaction_journal_id

    @transaction_journal_id.setter
    def transaction_journal_id(self, transaction_journal_id):
        """Sets the transaction_journal_id of this BillPaidDates.

        Transaction journal ID of the paid bill.  # noqa: E501

        :param transaction_journal_id: The transaction_journal_id of this BillPaidDates.  # noqa: E501
        :type: int
        """

        self._transaction_journal_id = transaction_journal_id

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
        if not isinstance(other, BillPaidDates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
