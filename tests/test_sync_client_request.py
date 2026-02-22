""" Tests for the sync requests API"""

import responses

from tests.conftest import sync_base_client_request


@responses.activate
def test_get_request(sync_base_client_request):
    """Test the get request method"""
    response_data = {"status": "success"}
    responses.add(
        responses.GET, "https://api.paystack.co/test", status=200, json=response_data
    )
    response = sync_base_client_request._get_request("test", params=response_data)
    assert response.status == "success"


@responses.activate
def test_post_request(sync_base_client_request):
    """Test post request method"""
    response_data = {"status": "success"}
    responses.add(
        responses.POST, "https://api.paystack.co/test", status=200, json=response_data
    )
    response = sync_base_client_request._post_request("test", data=response_data)
    assert response.status == "success"


@responses.activate
def test_put_request(sync_base_client_request):
    """Test put request method"""
    response_data = {"status": "success"}
    responses.add(
        responses.PUT, "https://api.paystack.co/test", status=200, json=response_data
    )
    response = sync_base_client_request._put_request("test", data=response_data)
    assert response.status == "success"


@responses.activate
def test_delete_request(sync_base_client_request):
    """Test delete request method"""
    response_data = {"status": "success"}
    responses.add(
        responses.DELETE, "https://api.paystack.co/test", status=200, json=response_data
    )
    response = sync_base_client_request._delete_request("test", data=response_data)
    assert response.status == "success"
