""" Tests for the sync base client API"""

import pytest
import responses
from datetime import date, datetime

from paystackease.core import SyncBaseClientAPI, SecretKeyError
from tests.conftest import sync_base_client


def test_base_url(sync_base_client):
    """ Test base url"""
    assert sync_base_client._PAYSTACK_API_URL == "https://api.paystack.co/"


def test_secret_key():
    """ Test for secret key"""
    secret_key = "sk_secret_key"
    client = SyncBaseClientAPI(secret_key)
    assert client._secret_key == secret_key


def test_no_secret_key():
    """ Test for no secret key"""
    with pytest.raises(SecretKeyError):
        SyncBaseClientAPI()


def test_convert_to_string(sync_base_client):
    """Tests for convert to string"""
    assert sync_base_client._convert_to_string(True) == "True"
    assert sync_base_client._convert_to_string(False) == "False"
    assert sync_base_client._convert_to_string(date.today()) == date.today().strftime("%Y-%m-%d")
    assert sync_base_client._convert_to_string(datetime.today()) == datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def test_make_paystack_http_headers(sync_base_client):
    """Tests for make paystack http headers"""
    secret_key = "sk_secret_key"
    headers = sync_base_client._make_paystack_http_headers()
    assert headers["Authorization"] == f"Bearer {secret_key}"
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
