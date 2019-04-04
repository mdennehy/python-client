# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: support@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.settings_api import SettingsApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.settings_api.SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_permissions(self):
        """Test case for get_all_permissions

        Get all permissions  # noqa: E501
        """
        pass

    def test_get_customer_preferences(self):
        """Test case for get_customer_preferences

        Get customer preferences  # noqa: E501
        """
        pass

    def test_get_default_user_groups(self):
        """Test case for get_default_user_groups

        Get default user groups customer preferences  # noqa: E501
        """
        pass

    def test_post_customer_preferences(self):
        """Test case for post_customer_preferences

        Update selected fields of customer preferences  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
