""" Tests for base url """

import pytest
import responses
from paystackease.base import BaseClientAPI, PayStackBaseClientAPI


@pytest.fixture(scope="session", name="base_client")
@responses.activate
def base_client_test():
    """Fixture for BaseClientAPI"""
    response_data = {"status": "success"}
    # mocking the response for the base url
    responses.add(
        responses.GET, "https://api.paystack.co/", json=response_data, status=200
    )
    client = BaseClientAPI(secret_key="test_secret_key")
    return client


@pytest.fixture(scope="session", name="paystack_base_client")
@responses.activate
def paystack_base_client_test():
    """Fixture for PayStackBaseClientAPI"""
    response_data = {"status": "success"}
    # mocking the response for the paystack base client
    responses.add(
        responses.GET, "https://api.paystack.co/", json=response_data, status=200
    )
    paystack_client = PayStackBaseClientAPI(secret_key="test_secret_key")
    return paystack_client


def test_base_url(base_client):
    """Tests for base url"""
    # asserting that the base url is correct
    assert base_client.PAYSTACK_API_URL == "https://api.paystack.co/"


def test_init_with_secret_key(base_client):
    """Tests for init with secret key"""
    # asserting that the secret key is set correctly
    assert base_client.secret_key == "test_secret_key"


def test_init_without_secret_key():
    """Tests for init without secret key"""
    # creating an instance of BaseClientAPI without a secret key
    if BaseClientAPI(secret_key=None) is None:
        with pytest.raises(ValueError):
            BaseClientAPI()


def test_make_paystack_http_headers(base_client):
    """Tests for make paystack http headers"""
    # asserting that the headers are set correctly
    headers = base_client._make_paystack_http_headers()
    assert headers["Authorization"] == f"Bearer {base_client.secret_key}"
    assert headers["content-type"] == "application/json"


@responses.activate
def test_request_url(base_client):
    """Tests for request url"""
    response_data = {"status": "success"}
    # mocking the response for the request url
    responses.add(
        responses.GET,
        "https://api.paystack.co/test_endpoint",
        json=response_data,
        status=200,
    )
    # asserting that the request url is correct
    response = base_client._request_url("GET", "test_endpoint")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == "https://api.paystack.co/test_endpoint"
    assert response == response_data


@responses.activate
def test_get_request(paystack_base_client):
    """Test the get request"""
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/test_endpoint",
        json=response_data,
        status=200,
    )
    response = paystack_base_client.get_request("test_endpoint")
    assert response == response_data


@responses.activate
def test_post_request(paystack_base_client):
    """Test the post request"""
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/test_endpoint",
        json=response_data,
        status=200,
    )
    response = paystack_base_client.post_request("test_endpoint")
    assert response == response_data


@responses.activate
def test_put_request(paystack_base_client):
    """Test the put request"""
    response_data = {"status": "success"}
    responses.add(
        responses.PUT,
        "https://api.paystack.co/test_endpoint",
        json=response_data,
        status=200,
    )
    response = paystack_base_client.put_request("test_endpoint")
    assert response == response_data


@responses.activate
def test_delete_request(paystack_base_client):
    """Test the delete request"""
    response_data = {"status": "success"}
    responses.add(
        responses.DELETE,
        "https://api.paystack.co/test_endpoint",
        json=response_data,
        status=200,
    )
    response = paystack_base_client.delete_request("test_endpoint")
    assert response == response_data
