# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.alert_api import AlertApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestAlertApi(unittest.TestCase):
    """AlertApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.alert_api.AlertApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_alert_tag(self):
        """Test case for add_alert_tag

        Add a tag to a specific alert  # noqa: E501
        """
        pass

    def test_create_alert(self):
        """Test case for create_alert

        Create a specific alert  # noqa: E501
        """
        pass

    def test_delete_alert(self):
        """Test case for delete_alert

        Delete a specific alert  # noqa: E501
        """
        pass

    def test_get_alert(self):
        """Test case for get_alert

        Get a specific alert  # noqa: E501
        """
        pass

    def test_get_alert_history(self):
        """Test case for get_alert_history

        Get the version history of a specific alert  # noqa: E501
        """
        pass

    def test_get_alert_tags(self):
        """Test case for get_alert_tags

        Get all tags associated with a specific alert  # noqa: E501
        """
        pass

    def test_get_alert_version(self):
        """Test case for get_alert_version

        Get a specific historical version of a specific alert  # noqa: E501
        """
        pass

    def test_get_alerts_summary(self):
        """Test case for get_alerts_summary

        Count alerts of various statuses for a customer  # noqa: E501
        """
        pass

    def test_get_all_alert(self):
        """Test case for get_all_alert

        Get all alerts for a customer  # noqa: E501
        """
        pass

    def test_hide_alert(self):
        """Test case for hide_alert

        Hide a specific integration alert   # noqa: E501
        """
        pass

    def test_remove_alert_tag(self):
        """Test case for remove_alert_tag

        Remove a tag from a specific alert  # noqa: E501
        """
        pass

    def test_set_alert_tags(self):
        """Test case for set_alert_tags

        Set all tags associated with a specific alert  # noqa: E501
        """
        pass

    def test_snooze_alert(self):
        """Test case for snooze_alert

        Snooze a specific alert for some number of seconds  # noqa: E501
        """
        pass

    def test_undelete_alert(self):
        """Test case for undelete_alert

        Undelete a specific alert  # noqa: E501
        """
        pass

    def test_unhide_alert(self):
        """Test case for unhide_alert

        Unhide a specific integration alert  # noqa: E501
        """
        pass

    def test_unsnooze_alert(self):
        """Test case for unsnooze_alert

        Unsnooze a specific alert  # noqa: E501
        """
        pass

    def test_update_alert(self):
        """Test case for update_alert

        Update a specific alert  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()