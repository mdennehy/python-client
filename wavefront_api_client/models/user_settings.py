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


class UserSettings(object):
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
        'always_hide_querybuilder': 'bool',
        'chart_title_scalar': 'int',
        'hide_ts_when_querybuilder_shown': 'bool',
        'landing_dashboard_slug': 'str',
        'preferred_time_zone': 'str',
        'show_onboarding': 'bool',
        'show_querybuilder_by_default': 'bool',
        'use24_hour_time': 'bool',
        'use_dark_theme': 'bool'
    }

    attribute_map = {
        'always_hide_querybuilder': 'alwaysHideQuerybuilder',
        'chart_title_scalar': 'chartTitleScalar',
        'hide_ts_when_querybuilder_shown': 'hideTSWhenQuerybuilderShown',
        'landing_dashboard_slug': 'landingDashboardSlug',
        'preferred_time_zone': 'preferredTimeZone',
        'show_onboarding': 'showOnboarding',
        'show_querybuilder_by_default': 'showQuerybuilderByDefault',
        'use24_hour_time': 'use24HourTime',
        'use_dark_theme': 'useDarkTheme'
    }

    def __init__(self, always_hide_querybuilder=None, chart_title_scalar=None, hide_ts_when_querybuilder_shown=None, landing_dashboard_slug=None, preferred_time_zone=None, show_onboarding=None, show_querybuilder_by_default=None, use24_hour_time=None, use_dark_theme=None):  # noqa: E501
        """UserSettings - a model defined in Swagger"""  # noqa: E501

        self._always_hide_querybuilder = None
        self._chart_title_scalar = None
        self._hide_ts_when_querybuilder_shown = None
        self._landing_dashboard_slug = None
        self._preferred_time_zone = None
        self._show_onboarding = None
        self._show_querybuilder_by_default = None
        self._use24_hour_time = None
        self._use_dark_theme = None
        self.discriminator = None

        if always_hide_querybuilder is not None:
            self.always_hide_querybuilder = always_hide_querybuilder
        if chart_title_scalar is not None:
            self.chart_title_scalar = chart_title_scalar
        if hide_ts_when_querybuilder_shown is not None:
            self.hide_ts_when_querybuilder_shown = hide_ts_when_querybuilder_shown
        if landing_dashboard_slug is not None:
            self.landing_dashboard_slug = landing_dashboard_slug
        if preferred_time_zone is not None:
            self.preferred_time_zone = preferred_time_zone
        if show_onboarding is not None:
            self.show_onboarding = show_onboarding
        if show_querybuilder_by_default is not None:
            self.show_querybuilder_by_default = show_querybuilder_by_default
        if use24_hour_time is not None:
            self.use24_hour_time = use24_hour_time
        if use_dark_theme is not None:
            self.use_dark_theme = use_dark_theme

    @property
    def always_hide_querybuilder(self):
        """Gets the always_hide_querybuilder of this UserSettings.  # noqa: E501


        :return: The always_hide_querybuilder of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._always_hide_querybuilder

    @always_hide_querybuilder.setter
    def always_hide_querybuilder(self, always_hide_querybuilder):
        """Sets the always_hide_querybuilder of this UserSettings.


        :param always_hide_querybuilder: The always_hide_querybuilder of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._always_hide_querybuilder = always_hide_querybuilder

    @property
    def chart_title_scalar(self):
        """Gets the chart_title_scalar of this UserSettings.  # noqa: E501


        :return: The chart_title_scalar of this UserSettings.  # noqa: E501
        :rtype: int
        """
        return self._chart_title_scalar

    @chart_title_scalar.setter
    def chart_title_scalar(self, chart_title_scalar):
        """Sets the chart_title_scalar of this UserSettings.


        :param chart_title_scalar: The chart_title_scalar of this UserSettings.  # noqa: E501
        :type: int
        """

        self._chart_title_scalar = chart_title_scalar

    @property
    def hide_ts_when_querybuilder_shown(self):
        """Gets the hide_ts_when_querybuilder_shown of this UserSettings.  # noqa: E501


        :return: The hide_ts_when_querybuilder_shown of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._hide_ts_when_querybuilder_shown

    @hide_ts_when_querybuilder_shown.setter
    def hide_ts_when_querybuilder_shown(self, hide_ts_when_querybuilder_shown):
        """Sets the hide_ts_when_querybuilder_shown of this UserSettings.


        :param hide_ts_when_querybuilder_shown: The hide_ts_when_querybuilder_shown of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._hide_ts_when_querybuilder_shown = hide_ts_when_querybuilder_shown

    @property
    def landing_dashboard_slug(self):
        """Gets the landing_dashboard_slug of this UserSettings.  # noqa: E501


        :return: The landing_dashboard_slug of this UserSettings.  # noqa: E501
        :rtype: str
        """
        return self._landing_dashboard_slug

    @landing_dashboard_slug.setter
    def landing_dashboard_slug(self, landing_dashboard_slug):
        """Sets the landing_dashboard_slug of this UserSettings.


        :param landing_dashboard_slug: The landing_dashboard_slug of this UserSettings.  # noqa: E501
        :type: str
        """

        self._landing_dashboard_slug = landing_dashboard_slug

    @property
    def preferred_time_zone(self):
        """Gets the preferred_time_zone of this UserSettings.  # noqa: E501


        :return: The preferred_time_zone of this UserSettings.  # noqa: E501
        :rtype: str
        """
        return self._preferred_time_zone

    @preferred_time_zone.setter
    def preferred_time_zone(self, preferred_time_zone):
        """Sets the preferred_time_zone of this UserSettings.


        :param preferred_time_zone: The preferred_time_zone of this UserSettings.  # noqa: E501
        :type: str
        """

        self._preferred_time_zone = preferred_time_zone

    @property
    def show_onboarding(self):
        """Gets the show_onboarding of this UserSettings.  # noqa: E501


        :return: The show_onboarding of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_onboarding

    @show_onboarding.setter
    def show_onboarding(self, show_onboarding):
        """Sets the show_onboarding of this UserSettings.


        :param show_onboarding: The show_onboarding of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._show_onboarding = show_onboarding

    @property
    def show_querybuilder_by_default(self):
        """Gets the show_querybuilder_by_default of this UserSettings.  # noqa: E501


        :return: The show_querybuilder_by_default of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_querybuilder_by_default

    @show_querybuilder_by_default.setter
    def show_querybuilder_by_default(self, show_querybuilder_by_default):
        """Sets the show_querybuilder_by_default of this UserSettings.


        :param show_querybuilder_by_default: The show_querybuilder_by_default of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._show_querybuilder_by_default = show_querybuilder_by_default

    @property
    def use24_hour_time(self):
        """Gets the use24_hour_time of this UserSettings.  # noqa: E501


        :return: The use24_hour_time of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use24_hour_time

    @use24_hour_time.setter
    def use24_hour_time(self, use24_hour_time):
        """Sets the use24_hour_time of this UserSettings.


        :param use24_hour_time: The use24_hour_time of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._use24_hour_time = use24_hour_time

    @property
    def use_dark_theme(self):
        """Gets the use_dark_theme of this UserSettings.  # noqa: E501


        :return: The use_dark_theme of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_dark_theme

    @use_dark_theme.setter
    def use_dark_theme(self, use_dark_theme):
        """Sets the use_dark_theme of this UserSettings.


        :param use_dark_theme: The use_dark_theme of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._use_dark_theme = use_dark_theme

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
        if issubclass(UserSettings, dict):
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
        if not isinstance(other, UserSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
