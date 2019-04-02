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
from wavefront_api_client.api.user_api import UserApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user_to_user_groups(self):
        """Test case for add_user_to_user_groups

        Adds specific user groups to the user  # noqa: E501
        """
        pass

    def test_create_or_update_user(self):
        """Test case for create_or_update_user

        Creates or updates a user  # noqa: E501
        """
        pass

    def test_delete_multiple_users(self):
        """Test case for delete_multiple_users

        Deletes multiple users  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Deletes a user identified by id  # noqa: E501
        """
        pass

    def test_get_all_user(self):
        """Test case for get_all_user

        Get all users  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Retrieves a user by identifier (email addr)  # noqa: E501
        """
        pass

    def test_grant_permission_to_users(self):
        """Test case for grant_permission_to_users

        Grants a specific user permission to multiple users  # noqa: E501
        """
        pass

    def test_grant_user_permission(self):
        """Test case for grant_user_permission

        Grants a specific user permission  # noqa: E501
        """
        pass

    def test_invite_users(self):
        """Test case for invite_users

        Invite users with given user groups and permissions.  # noqa: E501
        """
        pass

    def test_remove_user_from_user_groups(self):
        """Test case for remove_user_from_user_groups

        Removes specific user groups from the user  # noqa: E501
        """
        pass

    def test_revoke_permission_from_users(self):
        """Test case for revoke_permission_from_users

        Revokes a specific user permission from multiple users  # noqa: E501
        """
        pass

    def test_revoke_user_permission(self):
        """Test case for revoke_user_permission

        Revokes a specific user permission  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update user with given user groups and permissions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()