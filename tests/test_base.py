""" Tests for the BaseClientAPI and PayStackClientAPI methods """
from datetime import date, datetime

import pytest
import responses

from paystackease.sync._api_base import BaseClientAPI
from paystackease.errors import SecretKeyError

from tests.conftest import base_client, paystack_request_client


def test_base_url(base_client):
    """ Test base url"""
    assert base_client._PAYSTACK_API_URL == "https://api.paystack.co/"


def test_secret_key():
    """ Test for secret key"""
    secret_key = "sk_secret_key"
    client = BaseClientAPI(secret_key)
    assert client._secret_key == secret_key


def test_no_secret_key():
    """ Test for no secret key"""
    with pytest.raises(SecretKeyError):
        BaseClientAPI()


def test_convert_to_string(base_client):
    """Tests for convert to string"""
    assert base_client._convert_to_string(True) == "True"
    assert base_client._convert_to_string(False) == "False"
    assert base_client._convert_to_string(date.today()) == date.today().strftime("%Y-%m-%d")
    assert base_client._convert_to_string(datetime.today()) == datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def test_make_paystack_http_headers(base_client):
    """Tests for make paystack http headers"""
    secret_key = "sk_secret_key"
    headers = base_client._make_paystack_http_headers()
    assert headers["Authorization"] == f"Bearer {secret_key}"
    assert headers["content-type"] == "application/json"


@responses.activate
def test_request_url(base_client):
    """Tests for request url"""
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/test",
        json=response_data,
        status=200,
    )
    # asserting that the request url is correct
    response = base_client._request_url("GET", "test")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == "https://api.paystack.co/test"
    assert response == response_data


@responses.activate
def test_get_request(paystack_request_client):
    """ Test the get request method"""
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/test",
        status=200,
        json=response_data
    )
    response = paystack_request_client._get_request('test', params=response_data)
    assert response == response_data


@responses.activate
def test_post_request(paystack_request_client):
    """ Test post request method """
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/test",
        status=200,
        json=response_data
    )
    response = paystack_request_client._post_request('test', data=response_data)
    assert response == response_data


@responses.activate
def test_put_request(paystack_request_client):
    """ Test put request method """
    response_data = {"status": "success"}
    responses.add(
        responses.PUT,
        "https://api.paystack.co/test",
        status=200,
        json=response_data
    )
    response = paystack_request_client._put_request('test', data=response_data)
    assert response == response_data


@responses.activate
def test_delete_request(paystack_request_client):
    """ Test delete request method """
    response_data = {"status": "success"}
    responses.add(
        responses.DELETE,
        "https://api.paystack.co/test",
        status=200,
        json=response_data
    )
    response = paystack_request_client._delete_request('test', data=response_data)
    assert response == response_data
