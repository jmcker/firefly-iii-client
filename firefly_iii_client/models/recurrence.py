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


class Recurrence(object):
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
        'apply_rules': 'bool',
        'created_at': 'datetime',
        'description': 'str',
        'first_date': 'date',
        'latest_date': 'date',
        'notes': 'str',
        'nr_of_repetitions': 'int',
        'repeat_until': 'date',
        'repetitions': 'list[RecurrenceRepetition]',
        'title': 'str',
        'transactions': 'list[RecurrenceTransaction]',
        'type': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'apply_rules': 'apply_rules',
        'created_at': 'created_at',
        'description': 'description',
        'first_date': 'first_date',
        'latest_date': 'latest_date',
        'notes': 'notes',
        'nr_of_repetitions': 'nr_of_repetitions',
        'repeat_until': 'repeat_until',
        'repetitions': 'repetitions',
        'title': 'title',
        'transactions': 'transactions',
        'type': 'type',
        'updated_at': 'updated_at'
    }

    def __init__(self, active=None, apply_rules=None, created_at=None, description=None, first_date=None, latest_date=None, notes=None, nr_of_repetitions=None, repeat_until=None, repetitions=None, title=None, transactions=None, type=None, updated_at=None):  # noqa: E501
        """Recurrence - a model defined in OpenAPI"""  # noqa: E501

        self._active = None
        self._apply_rules = None
        self._created_at = None
        self._description = None
        self._first_date = None
        self._latest_date = None
        self._notes = None
        self._nr_of_repetitions = None
        self._repeat_until = None
        self._repetitions = None
        self._title = None
        self._transactions = None
        self._type = None
        self._updated_at = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if apply_rules is not None:
            self.apply_rules = apply_rules
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        self.first_date = first_date
        if latest_date is not None:
            self.latest_date = latest_date
        if notes is not None:
            self.notes = notes
        if nr_of_repetitions is not None:
            self.nr_of_repetitions = nr_of_repetitions
        if repeat_until is not None:
            self.repeat_until = repeat_until
        if repetitions is not None:
            self.repetitions = repetitions
        self.title = title
        if transactions is not None:
            self.transactions = transactions
        self.type = type
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def active(self):
        """Gets the active of this Recurrence.  # noqa: E501

        If the recurrence is even active.  # noqa: E501

        :return: The active of this Recurrence.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Recurrence.

        If the recurrence is even active.  # noqa: E501

        :param active: The active of this Recurrence.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def apply_rules(self):
        """Gets the apply_rules of this Recurrence.  # noqa: E501

        Whether or not to fire the rules after the creation of a transaction.  # noqa: E501

        :return: The apply_rules of this Recurrence.  # noqa: E501
        :rtype: bool
        """
        return self._apply_rules

    @apply_rules.setter
    def apply_rules(self, apply_rules):
        """Sets the apply_rules of this Recurrence.

        Whether or not to fire the rules after the creation of a transaction.  # noqa: E501

        :param apply_rules: The apply_rules of this Recurrence.  # noqa: E501
        :type: bool
        """

        self._apply_rules = apply_rules

    @property
    def created_at(self):
        """Gets the created_at of this Recurrence.  # noqa: E501


        :return: The created_at of this Recurrence.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Recurrence.


        :param created_at: The created_at of this Recurrence.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this Recurrence.  # noqa: E501

        Not to be confused with the description of the actual transaction(s) being created.  # noqa: E501

        :return: The description of this Recurrence.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Recurrence.

        Not to be confused with the description of the actual transaction(s) being created.  # noqa: E501

        :param description: The description of this Recurrence.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def first_date(self):
        """Gets the first_date of this Recurrence.  # noqa: E501

        First time the recurring transaction will fire. Must be after today.  # noqa: E501

        :return: The first_date of this Recurrence.  # noqa: E501
        :rtype: date
        """
        return self._first_date

    @first_date.setter
    def first_date(self, first_date):
        """Sets the first_date of this Recurrence.

        First time the recurring transaction will fire. Must be after today.  # noqa: E501

        :param first_date: The first_date of this Recurrence.  # noqa: E501
        :type: date
        """
        if first_date is None:
            raise ValueError("Invalid value for `first_date`, must not be `None`")  # noqa: E501

        self._first_date = first_date

    @property
    def latest_date(self):
        """Gets the latest_date of this Recurrence.  # noqa: E501

        First time the recurring transaction will fire. Must be after today.  # noqa: E501

        :return: The latest_date of this Recurrence.  # noqa: E501
        :rtype: date
        """
        return self._latest_date

    @latest_date.setter
    def latest_date(self, latest_date):
        """Sets the latest_date of this Recurrence.

        First time the recurring transaction will fire. Must be after today.  # noqa: E501

        :param latest_date: The latest_date of this Recurrence.  # noqa: E501
        :type: date
        """

        self._latest_date = latest_date

    @property
    def notes(self):
        """Gets the notes of this Recurrence.  # noqa: E501


        :return: The notes of this Recurrence.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Recurrence.


        :param notes: The notes of this Recurrence.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def nr_of_repetitions(self):
        """Gets the nr_of_repetitions of this Recurrence.  # noqa: E501

        Max number of created transactions. Use either this field or repeat_until.  # noqa: E501

        :return: The nr_of_repetitions of this Recurrence.  # noqa: E501
        :rtype: int
        """
        return self._nr_of_repetitions

    @nr_of_repetitions.setter
    def nr_of_repetitions(self, nr_of_repetitions):
        """Sets the nr_of_repetitions of this Recurrence.

        Max number of created transactions. Use either this field or repeat_until.  # noqa: E501

        :param nr_of_repetitions: The nr_of_repetitions of this Recurrence.  # noqa: E501
        :type: int
        """

        self._nr_of_repetitions = nr_of_repetitions

    @property
    def repeat_until(self):
        """Gets the repeat_until of this Recurrence.  # noqa: E501

        Date until the recurring transaction can fire. Use either this field or repetitions.  # noqa: E501

        :return: The repeat_until of this Recurrence.  # noqa: E501
        :rtype: date
        """
        return self._repeat_until

    @repeat_until.setter
    def repeat_until(self, repeat_until):
        """Sets the repeat_until of this Recurrence.

        Date until the recurring transaction can fire. Use either this field or repetitions.  # noqa: E501

        :param repeat_until: The repeat_until of this Recurrence.  # noqa: E501
        :type: date
        """

        self._repeat_until = repeat_until

    @property
    def repetitions(self):
        """Gets the repetitions of this Recurrence.  # noqa: E501


        :return: The repetitions of this Recurrence.  # noqa: E501
        :rtype: list[RecurrenceRepetition]
        """
        return self._repetitions

    @repetitions.setter
    def repetitions(self, repetitions):
        """Sets the repetitions of this Recurrence.


        :param repetitions: The repetitions of this Recurrence.  # noqa: E501
        :type: list[RecurrenceRepetition]
        """

        self._repetitions = repetitions

    @property
    def title(self):
        """Gets the title of this Recurrence.  # noqa: E501


        :return: The title of this Recurrence.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Recurrence.


        :param title: The title of this Recurrence.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def transactions(self):
        """Gets the transactions of this Recurrence.  # noqa: E501


        :return: The transactions of this Recurrence.  # noqa: E501
        :rtype: list[RecurrenceTransaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this Recurrence.


        :param transactions: The transactions of this Recurrence.  # noqa: E501
        :type: list[RecurrenceTransaction]
        """

        self._transactions = transactions

    @property
    def type(self):
        """Gets the type of this Recurrence.  # noqa: E501


        :return: The type of this Recurrence.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Recurrence.


        :param type: The type of this Recurrence.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["withdrawal", "transfer", "deposit", "opening-balance", "reconciliation"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this Recurrence.  # noqa: E501


        :return: The updated_at of this Recurrence.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Recurrence.


        :param updated_at: The updated_at of this Recurrence.  # noqa: E501
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
        if not isinstance(other, Recurrence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
