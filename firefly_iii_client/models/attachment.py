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


class Attachment(object):
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
        'attachable_id': 'int',
        'attachable_type': 'str',
        'created_at': 'datetime',
        'download_uri': 'str',
        'filename': 'str',
        'md5': 'str',
        'mime': 'str',
        'notes': 'str',
        'size': 'int',
        'title': 'str',
        'updated_at': 'datetime',
        'upload_uri': 'str'
    }

    attribute_map = {
        'attachable_id': 'attachable_id',
        'attachable_type': 'attachable_type',
        'created_at': 'created_at',
        'download_uri': 'download_uri',
        'filename': 'filename',
        'md5': 'md5',
        'mime': 'mime',
        'notes': 'notes',
        'size': 'size',
        'title': 'title',
        'updated_at': 'updated_at',
        'upload_uri': 'upload_uri'
    }

    def __init__(self, attachable_id=None, attachable_type=None, created_at=None, download_uri=None, filename=None, md5=None, mime=None, notes=None, size=None, title=None, updated_at=None, upload_uri=None):  # noqa: E501
        """Attachment - a model defined in OpenAPI"""  # noqa: E501

        self._attachable_id = None
        self._attachable_type = None
        self._created_at = None
        self._download_uri = None
        self._filename = None
        self._md5 = None
        self._mime = None
        self._notes = None
        self._size = None
        self._title = None
        self._updated_at = None
        self._upload_uri = None
        self.discriminator = None

        self.attachable_id = attachable_id
        self.attachable_type = attachable_type
        if created_at is not None:
            self.created_at = created_at
        if download_uri is not None:
            self.download_uri = download_uri
        self.filename = filename
        if md5 is not None:
            self.md5 = md5
        if mime is not None:
            self.mime = mime
        if notes is not None:
            self.notes = notes
        if size is not None:
            self.size = size
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at
        if upload_uri is not None:
            self.upload_uri = upload_uri

    @property
    def attachable_id(self):
        """Gets the attachable_id of this Attachment.  # noqa: E501

        ID of the model this attachment is linked to.  # noqa: E501

        :return: The attachable_id of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._attachable_id

    @attachable_id.setter
    def attachable_id(self, attachable_id):
        """Sets the attachable_id of this Attachment.

        ID of the model this attachment is linked to.  # noqa: E501

        :param attachable_id: The attachable_id of this Attachment.  # noqa: E501
        :type: int
        """
        if attachable_id is None:
            raise ValueError("Invalid value for `attachable_id`, must not be `None`")  # noqa: E501

        self._attachable_id = attachable_id

    @property
    def attachable_type(self):
        """Gets the attachable_type of this Attachment.  # noqa: E501

        The object class to which the attachment must be linked.  # noqa: E501

        :return: The attachable_type of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._attachable_type

    @attachable_type.setter
    def attachable_type(self, attachable_type):
        """Sets the attachable_type of this Attachment.

        The object class to which the attachment must be linked.  # noqa: E501

        :param attachable_type: The attachable_type of this Attachment.  # noqa: E501
        :type: str
        """
        if attachable_type is None:
            raise ValueError("Invalid value for `attachable_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Bill", "TransactionJournal", "ImportJob"]  # noqa: E501
        if attachable_type not in allowed_values:
            raise ValueError(
                "Invalid value for `attachable_type` ({0}), must be one of {1}"  # noqa: E501
                .format(attachable_type, allowed_values)
            )

        self._attachable_type = attachable_type

    @property
    def created_at(self):
        """Gets the created_at of this Attachment.  # noqa: E501


        :return: The created_at of this Attachment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Attachment.


        :param created_at: The created_at of this Attachment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def download_uri(self):
        """Gets the download_uri of this Attachment.  # noqa: E501


        :return: The download_uri of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._download_uri

    @download_uri.setter
    def download_uri(self, download_uri):
        """Sets the download_uri of this Attachment.


        :param download_uri: The download_uri of this Attachment.  # noqa: E501
        :type: str
        """

        self._download_uri = download_uri

    @property
    def filename(self):
        """Gets the filename of this Attachment.  # noqa: E501


        :return: The filename of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Attachment.


        :param filename: The filename of this Attachment.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def md5(self):
        """Gets the md5 of this Attachment.  # noqa: E501

        MD5 hash of the file for basic duplicate detection.  # noqa: E501

        :return: The md5 of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this Attachment.

        MD5 hash of the file for basic duplicate detection.  # noqa: E501

        :param md5: The md5 of this Attachment.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def mime(self):
        """Gets the mime of this Attachment.  # noqa: E501


        :return: The mime of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._mime

    @mime.setter
    def mime(self, mime):
        """Sets the mime of this Attachment.


        :param mime: The mime of this Attachment.  # noqa: E501
        :type: str
        """

        self._mime = mime

    @property
    def notes(self):
        """Gets the notes of this Attachment.  # noqa: E501


        :return: The notes of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Attachment.


        :param notes: The notes of this Attachment.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def size(self):
        """Gets the size of this Attachment.  # noqa: E501


        :return: The size of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Attachment.


        :param size: The size of this Attachment.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def title(self):
        """Gets the title of this Attachment.  # noqa: E501


        :return: The title of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Attachment.


        :param title: The title of this Attachment.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this Attachment.  # noqa: E501


        :return: The updated_at of this Attachment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Attachment.


        :param updated_at: The updated_at of this Attachment.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def upload_uri(self):
        """Gets the upload_uri of this Attachment.  # noqa: E501


        :return: The upload_uri of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._upload_uri

    @upload_uri.setter
    def upload_uri(self, upload_uri):
        """Sets the upload_uri of this Attachment.


        :param upload_uri: The upload_uri of this Attachment.  # noqa: E501
        :type: str
        """

        self._upload_uri = upload_uri

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
        if not isinstance(other, Attachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
