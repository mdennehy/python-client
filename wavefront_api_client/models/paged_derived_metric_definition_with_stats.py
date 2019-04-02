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

from wavefront_api_client.models.derived_metric_definition import DerivedMetricDefinition  # noqa: F401,E501
from wavefront_api_client.models.sorting import Sorting  # noqa: F401,E501


class PagedDerivedMetricDefinitionWithStats(object):
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
        'counts': 'dict(str, int)',
        'cursor': 'str',
        'items': 'list[DerivedMetricDefinition]',
        'limit': 'int',
        'more_items': 'bool',
        'offset': 'int',
        'sort': 'Sorting',
        'total_items': 'int'
    }

    attribute_map = {
        'counts': 'counts',
        'cursor': 'cursor',
        'items': 'items',
        'limit': 'limit',
        'more_items': 'moreItems',
        'offset': 'offset',
        'sort': 'sort',
        'total_items': 'totalItems'
    }

    def __init__(self, counts=None, cursor=None, items=None, limit=None, more_items=None, offset=None, sort=None, total_items=None):  # noqa: E501
        """PagedDerivedMetricDefinitionWithStats - a model defined in Swagger"""  # noqa: E501

        self._counts = None
        self._cursor = None
        self._items = None
        self._limit = None
        self._more_items = None
        self._offset = None
        self._sort = None
        self._total_items = None
        self.discriminator = None

        if counts is not None:
            self.counts = counts
        if cursor is not None:
            self.cursor = cursor
        if items is not None:
            self.items = items
        if limit is not None:
            self.limit = limit
        if more_items is not None:
            self.more_items = more_items
        if offset is not None:
            self.offset = offset
        if sort is not None:
            self.sort = sort
        if total_items is not None:
            self.total_items = total_items

    @property
    def counts(self):
        """Gets the counts of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501

        A map from the state of the derived metric definition to the number of entities in that state within the search results  # noqa: E501

        :return: The counts of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this PagedDerivedMetricDefinitionWithStats.

        A map from the state of the derived metric definition to the number of entities in that state within the search results  # noqa: E501

        :param counts: The counts of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :type: dict(str, int)
        """

        self._counts = counts

    @property
    def cursor(self):
        """Gets the cursor of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501

        The id at which the current (limited) search can be continued to obtain more matching items  # noqa: E501

        :return: The cursor of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this PagedDerivedMetricDefinitionWithStats.

        The id at which the current (limited) search can be continued to obtain more matching items  # noqa: E501

        :param cursor: The cursor of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def items(self):
        """Gets the items of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501

        List of requested items  # noqa: E501

        :return: The items of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :rtype: list[DerivedMetricDefinition]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PagedDerivedMetricDefinitionWithStats.

        List of requested items  # noqa: E501

        :param items: The items of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :type: list[DerivedMetricDefinition]
        """

        self._items = items

    @property
    def limit(self):
        """Gets the limit of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501


        :return: The limit of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PagedDerivedMetricDefinitionWithStats.


        :param limit: The limit of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def more_items(self):
        """Gets the more_items of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501

        Whether more items are available for return by increment offset or cursor  # noqa: E501

        :return: The more_items of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :rtype: bool
        """
        return self._more_items

    @more_items.setter
    def more_items(self, more_items):
        """Sets the more_items of this PagedDerivedMetricDefinitionWithStats.

        Whether more items are available for return by increment offset or cursor  # noqa: E501

        :param more_items: The more_items of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :type: bool
        """

        self._more_items = more_items

    @property
    def offset(self):
        """Gets the offset of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501


        :return: The offset of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PagedDerivedMetricDefinitionWithStats.


        :param offset: The offset of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def sort(self):
        """Gets the sort of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501


        :return: The sort of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :rtype: Sorting
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this PagedDerivedMetricDefinitionWithStats.


        :param sort: The sort of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :type: Sorting
        """

        self._sort = sort

    @property
    def total_items(self):
        """Gets the total_items of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501

        An estimate (lower-bound) of the total number of items available for return.  May not be a tight estimate for facet queries  # noqa: E501

        :return: The total_items of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this PagedDerivedMetricDefinitionWithStats.

        An estimate (lower-bound) of the total number of items available for return.  May not be a tight estimate for facet queries  # noqa: E501

        :param total_items: The total_items of this PagedDerivedMetricDefinitionWithStats.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

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
        if issubclass(PagedDerivedMetricDefinitionWithStats, dict):
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
        if not isinstance(other, PagedDerivedMetricDefinitionWithStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
