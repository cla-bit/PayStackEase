""" Tests for the AsyncBaseClientAPI and AsyncPayStackClientAPI methods """

import pytest
from aioresponses import aioresponses
from datetime import datetime, date

from paystackease._abase import AsyncBaseClientAPI
from paystackease.errors import SecretKeyError
from tests.conftest import async_base_client, async_paystack_base_client


@pytest.mark.asyncio
async def test_base_url(async_base_client):
    """ Test base url"""
    base_url = async_base_client._PAYSTACK_API_URL
    assert base_url == "https://api.paystack.co/"


@pytest.mark.asyncio
async def test_secret_key():
    """ Test for secret key"""
    secret_key = "sk_secret_key"
    client = AsyncBaseClientAPI(secret_key)
    assert client._secret_key == secret_key


@pytest.mark.asyncio
async def test_no_secret_key():
    """ Test for no secret key"""
    with pytest.raises(SecretKeyError):
        AsyncBaseClientAPI()


@pytest.mark.asyncio
async def test_convert_to_string(async_base_client):
    """Tests for convert to string"""
    assert async_base_client._convert_to_string(True) == "true"
    assert async_base_client._convert_to_string(False) == "false"
    assert async_base_client._convert_to_string(date.today()) == date.today().strftime("%Y-%m-%d")
    assert async_base_client._convert_to_string(datetime.today()) == datetime.today().strftime("%Y-%m-%d %H:%M:%S")


@pytest.mark.asyncio
async def test_make_paystack_http_headers(async_base_client):
    """Tests for make paystack http headers"""
    secret_key = "sk_secret_key"
    headers = async_base_client._make_paystack_http_headers()
    assert headers["Authorization"] == f"Bearer {secret_key}"
    assert headers["content-type"] == "application/json"


@pytest.mark.asyncio
async def test_request_url(async_base_client):
    """Tests for request url"""
    with aioresponses() as mock_client:
        mock_response = {"status": "success"}
        mock_client.get(
            "https://api.paystack.co/test",
            payload=mock_response,
            status=200,
        )
        response = await async_base_client._request_url("GET", "/test")
        assert response == mock_response
        mock_client.assert_called()


@pytest.mark.asyncio
async def test_get_request(async_paystack_base_client):
    """ Test the get request method"""
    with aioresponses() as mock_client:
        mock_response = {"status": "success"}
        mock_client.get(
            "https://api.paystack.co/test",
            payload=mock_response,
            status=200,
        )
        response = await async_paystack_base_client._get_request("test")
        assert response == mock_response


@pytest.mark.asyncio
async def test_post_request(async_paystack_base_client):
    """ Test the get request method"""
    with aioresponses() as mock_client:
        mock_response = {"status": "success"}
        mock_data = {"key": "value"}
        mock_client.post(
            "https://api.paystack.co/test",
            payload=mock_response,
            status=200,
        )
        response = await async_paystack_base_client._post_request("test", data=mock_data)
        assert response == mock_response


@pytest.mark.asyncio
async def test_put_request(async_paystack_base_client):
    """ Test the get request method"""
    with aioresponses() as mock_client:
        mock_response = {"status": "success"}
        mock_data = {"key": "value"}
        mock_client.put(
            "https://api.paystack.co/test",
            payload=mock_response,
            status=200,
        )
        response = await async_paystack_base_client._put_request("test", data=mock_data)
        assert response == mock_response


@pytest.mark.asyncio
async def test_delete_request(async_paystack_base_client):
    """ Test the get request method"""
    with aioresponses() as mock_client:
        mock_response = {"status": "success"}
        mock_data = {"key": "value"}
        mock_client.delete(
            "https://api.paystack.co/test",
            payload=mock_response,
            status=200,
        )
        response = await async_paystack_base_client._delete_request("test", data=mock_data)
        assert response == mock_response
