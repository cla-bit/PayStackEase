""" Tests for the AsyncBaseClientAPI and AsyncPayStackClientAPI methods """
import asyncio
import pytest
from aioresponses import aioresponses

from paystackease._abase import AsyncBaseClientAPI
from paystackease.errors import SecretKeyError
from tests.conftest import async_base_client


@pytest.mark.asyncio
async def test_base_url(async_base_client):
    """ Test base url"""
    # async_client_instance = await async_base_client
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
    # async_client_instance = await async_base_client
    assert async_base_client._convert_to_string(True) == "true"


@pytest.mark.asyncio
async def test_make_paystack_http_headers(async_base_client):
    """Tests for make paystack http headers"""
    secret_key = "sk_secret_key"
    # async_client_instance = await async_base_client
    headers = async_base_client._make_paystack_http_headers()
    assert headers["Authorization"] == f"Bearer {secret_key}"
    assert headers["content-type"] == "application/json"


@pytest.mark.asyncio
async def test_request_url(async_base_client):
    """Tests for request url"""

    async with aioresponses() as mocked:
        response_data = {"status": "success"}
        mocked.get(
            "https://api.paystack.co/test",
            status=200,
            json=response_data,
        )
        # # asserting that the request url is correct
        # response = await async_base_client._request_url("GET", "test")
        # # assert len(mocked.calls) == 1
        # # assert mocked.calls[0].request.url == "https://api.paystack.co/test"
        # assert response == response_data


# # @responses.activate
# # def test_get_request(paystack_request_client):
# #     """ Test the get request method"""
# #     response_data = {"status": "success"}
# #     responses.add(
# #         responses.GET,
# #         "https://api.paystack.co/test",
# #         status=200,
# #         json=response_data
# #     )
# #     response = paystack_request_client._get_request('test', params=response_data)
# #     assert response == response_data
# #
# #
# # @responses.activate
# # def test_post_request(paystack_request_client):
# #     """ Test post request method """
# #     response_data = {"status": "success"}
# #     responses.add(
# #         responses.POST,
# #         "https://api.paystack.co/test",
# #         status=200,
# #         json=response_data
# #     )
# #     response = paystack_request_client._post_request('test', data=response_data)
# #     assert response == response_data
# #
# #
# # @responses.activate
# # def test_put_request(paystack_request_client):
# #     """ Test put request method """
# #     response_data = {"status": "success"}
# #     responses.add(
# #         responses.PUT,
# #         "https://api.paystack.co/test",
# #         status=200,
# #         json=response_data
# #     )
# #     response = paystack_request_client._put_request('test', data=response_data)
# #     assert response == response_data
# #
# #
# # @responses.activate
# # def test_delete_request(paystack_request_client):
# #     """ Test delete request method """
# #     response_data = {"status": "success"}
# #     responses.add(
# #         responses.DELETE,
# #         "https://api.paystack.co/test",
# #         status=200,
# #         json=response_data
# #     )
# #     response = paystack_request_client._delete_request('test', data=response_data)
# #     assert response == response_data
