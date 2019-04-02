# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: support@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.models.user_group import UserGroup  # noqa: F401,E501


class UserModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'customer': 'str',
        'groups': 'list[str]',
        'identifier': 'str',
        'last_successful_login': 'int',
        'sso_id': 'str',
        'user_groups': 'list[UserGroup]'
    }

    attribute_map = {
        'customer': 'customer',
        'groups': 'groups',
        'identifier': 'identifier',
        'last_successful_login': 'lastSuccessfulLogin',
        'sso_id': 'ssoId',
        'user_groups': 'userGroups'
    }

    def __init__(self, customer=None, groups=None, identifier=None, last_successful_login=None, sso_id=None, user_groups=None):  # noqa: E501
        """UserModel - a model defined in Swagger"""  # noqa: E501

        self._customer = None
        self._groups = None
        self._identifier = None
        self._last_successful_login = None
        self._sso_id = None
        self._user_groups = None
        self.discriminator = None

        self.customer = customer
        self.groups = groups
        self.identifier = identifier
        if last_successful_login is not None:
            self.last_successful_login = last_successful_login
        if sso_id is not None:
            self.sso_id = sso_id
        self.user_groups = user_groups

    @property
    def customer(self):
        """Gets the customer of this UserModel.  # noqa: E501

        The id of the customer to which this user belongs  # noqa: E501

        :return: The customer of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this UserModel.

        The id of the customer to which this user belongs  # noqa: E501

        :param customer: The customer of this UserModel.  # noqa: E501
        :type: str
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def groups(self):
        """Gets the groups of this UserModel.  # noqa: E501

        The permissions granted to this user  # noqa: E501

        :return: The groups of this UserModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserModel.

        The permissions granted to this user  # noqa: E501

        :param groups: The groups of this UserModel.  # noqa: E501
        :type: list[str]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

    @property
    def identifier(self):
        """Gets the identifier of this UserModel.  # noqa: E501

        The unique identifier of this user, which must be their valid email address  # noqa: E501

        :return: The identifier of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this UserModel.

        The unique identifier of this user, which must be their valid email address  # noqa: E501

        :param identifier: The identifier of this UserModel.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def last_successful_login(self):
        """Gets the last_successful_login of this UserModel.  # noqa: E501


        :return: The last_successful_login of this UserModel.  # noqa: E501
        :rtype: int
        """
        return self._last_successful_login

    @last_successful_login.setter
    def last_successful_login(self, last_successful_login):
        """Sets the last_successful_login of this UserModel.


        :param last_successful_login: The last_successful_login of this UserModel.  # noqa: E501
        :type: int
        """

        self._last_successful_login = last_successful_login

    @property
    def sso_id(self):
        """Gets the sso_id of this UserModel.  # noqa: E501


        :return: The sso_id of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._sso_id

    @sso_id.setter
    def sso_id(self, sso_id):
        """Sets the sso_id of this UserModel.


        :param sso_id: The sso_id of this UserModel.  # noqa: E501
        :type: str
        """

        self._sso_id = sso_id

    @property
    def user_groups(self):
        """Gets the user_groups of this UserModel.  # noqa: E501

        The list of user groups the user belongs to  # noqa: E501

        :return: The user_groups of this UserModel.  # noqa: E501
        :rtype: list[UserGroup]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this UserModel.

        The list of user groups the user belongs to  # noqa: E501

        :param user_groups: The user_groups of this UserModel.  # noqa: E501
        :type: list[UserGroup]
        """
        if user_groups is None:
            raise ValueError("Invalid value for `user_groups`, must not be `None`")  # noqa: E501

        self._user_groups = user_groups

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UserModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
