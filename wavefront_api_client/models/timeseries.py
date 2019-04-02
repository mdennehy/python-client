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


class Timeseries(object):
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
        'data': 'list[list[float]]',
        'host': 'str',
        'label': 'str',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'data': 'data',
        'host': 'host',
        'label': 'label',
        'tags': 'tags'
    }

    def __init__(self, data=None, host=None, label=None, tags=None):  # noqa: E501
        """Timeseries - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._host = None
        self._label = None
        self._tags = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if host is not None:
            self.host = host
        if label is not None:
            self.label = label
        if tags is not None:
            self.tags = tags

    @property
    def data(self):
        """Gets the data of this Timeseries.  # noqa: E501

        Data returned by this time series.  This is returned as a list of points, where each point is represented as a two-element list with 1st element being the timestamp in epoch SECONDS and the 2nd element being the numeric value of the series at the timestamp  # noqa: E501

        :return: The data of this Timeseries.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Timeseries.

        Data returned by this time series.  This is returned as a list of points, where each point is represented as a two-element list with 1st element being the timestamp in epoch SECONDS and the 2nd element being the numeric value of the series at the timestamp  # noqa: E501

        :param data: The data of this Timeseries.  # noqa: E501
        :type: list[list[float]]
        """

        self._data = data

    @property
    def host(self):
        """Gets the host of this Timeseries.  # noqa: E501

        Source/Host of this timeseries  # noqa: E501

        :return: The host of this Timeseries.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Timeseries.

        Source/Host of this timeseries  # noqa: E501

        :param host: The host of this Timeseries.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def label(self):
        """Gets the label of this Timeseries.  # noqa: E501

        Label of this timeseries  # noqa: E501

        :return: The label of this Timeseries.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Timeseries.

        Label of this timeseries  # noqa: E501

        :param label: The label of this Timeseries.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def tags(self):
        """Gets the tags of this Timeseries.  # noqa: E501

        Tags (key-value annotations) of this timeseries  # noqa: E501

        :return: The tags of this Timeseries.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Timeseries.

        Tags (key-value annotations) of this timeseries  # noqa: E501

        :param tags: The tags of this Timeseries.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

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
        if issubclass(Timeseries, dict):
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
        if not isinstance(other, Timeseries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
