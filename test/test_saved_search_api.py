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
from wavefront_api_client.api.saved_search_api import SavedSearchApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestSavedSearchApi(unittest.TestCase):
    """SavedSearchApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.saved_search_api.SavedSearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_saved_search(self):
        """Test case for create_saved_search

        Create a saved search  # noqa: E501
        """
        pass

    def test_delete_saved_search(self):
        """Test case for delete_saved_search

        Delete a specific saved search  # noqa: E501
        """
        pass

    def test_get_all_entity_type_saved_searches(self):
        """Test case for get_all_entity_type_saved_searches

        Get all saved searches for a specific entity type for a user  # noqa: E501
        """
        pass

    def test_get_all_saved_searches(self):
        """Test case for get_all_saved_searches

        Get all saved searches for a user  # noqa: E501
        """
        pass

    def test_get_saved_search(self):
        """Test case for get_saved_search

        Get a specific saved search  # noqa: E501
        """
        pass

    def test_update_saved_search(self):
        """Test case for update_saved_search

        Update a specific saved search  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
