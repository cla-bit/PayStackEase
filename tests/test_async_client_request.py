""" Tests for the async requests API"""

import pytest
from aioresponses import aioresponses

from tests.conftest import async_base_client_request


@pytest.mark.asyncio
async def test_get_request(async_base_client_request):
    """ Test the get request method"""
    with aioresponses() as mock_client:
        mock_response = {"status": "success"}
        mock_client.get(
            "https://api.paystack.co/test",
            payload=mock_response,
            status=200,
        )
        response = await async_base_client_request._get_request("test")
        assert response.status == "success"


@pytest.mark.asyncio
async def test_post_request(async_base_client_request):
    """ Test the get request method"""
    with aioresponses() as mock_client:
        mock_response = {"status": "success"}
        mock_data = {"key": "value"}
        mock_client.post(
            "https://api.paystack.co/test",
            payload=mock_response,
            status=200,
        )
        response = await async_base_client_request._post_request("test", data=mock_data)
        assert response.status == "success"


@pytest.mark.asyncio
async def test_put_request(async_base_client_request):
    """ Test the get request method"""
    with aioresponses() as mock_client:
        mock_response = {"status": "success"}
        mock_data = {"key": "value"}
        mock_client.put(
            "https://api.paystack.co/test",
            payload=mock_response,
            status=200,
        )
        response = await async_base_client_request._put_request("test", data=mock_data)
        assert response.status == "success"


@pytest.mark.asyncio
async def test_delete_request(async_base_client_request):
    """ Test the get request method"""
    with aioresponses() as mock_client:
        mock_response = {"status": "success"}
        mock_data = {"key": "value"}
        mock_client.delete(
            "https://api.paystack.co/test",
            payload=mock_response,
            status=200,
        )
        response = await async_base_client_request._delete_request("test", data=mock_data)
        assert response.status == "success"
