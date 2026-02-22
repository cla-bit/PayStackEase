""" Tests for the sync base client API"""

import responses
from datetime import date, datetime

from tests.conftest import sync_base_client, env_var


def test_base_url(sync_base_client):
    """Test base url"""
    assert sync_base_client._PAYSTACK_API_URL == "https://api.paystack.co/"


def test_convert_to_string(sync_base_client):
    """Tests for convert to string"""
    assert sync_base_client._convert_to_string(True) == "true"
    assert sync_base_client._convert_to_string(False) == "false"
    assert sync_base_client._convert_to_string(date.today()) == date.today().strftime(
        "%Y-%m-%d"
    )
    assert sync_base_client._convert_to_string(
        datetime.today()
    ) == datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def test_make_paystack_http_headers(sync_base_client, env_var):
    """Tests for make paystack http headers"""
    sync_base_client._secret_key = env_var
    headers = sync_base_client._make_paystack_http_headers()
    assert headers["Authorization"] == f"Bearer test_secret_key"
    assert headers["content-type"] == "application/json"


@responses.activate
def test_request_url(sync_base_client):
    """Tests for request url"""
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/test",
        json=response_data,
        status=200,
    )
    # asserting that the request url is correct
    response = sync_base_client._request_url("GET", "test")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == "https://api.paystack.co/test"
    assert response.status == "success"
