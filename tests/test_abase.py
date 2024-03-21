""" Tests for the AsyncBaseClientAPI and AsyncPayStackClientAPI methods """
import asyncio
import pytest
import aioresponses

from paystackease._abase import AsyncBaseClientAPI
from paystackease.errors import SecretKeyError
from tests.conftest import async_base_client


@pytest.mark.asyncio
async def test_base_url(async_base_client):
    """ Test base url"""
    async_client_instance = await async_base_client
    base_url = async_client_instance._PAYSTACK_API_URL
    assert base_url == "https://api.paystack.co/"
