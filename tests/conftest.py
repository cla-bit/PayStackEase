""" Fixtures for testing purposes """

import pytest
import pytest_asyncio

from paystackease._abase import AsyncBaseClientAPI, AsyncPayStackBaseClientAPI
from paystackease._base import BaseClientAPI, PayStackBaseClientAPI
from paystackease.apis.apple_pay import ApplePayClientAPI
from paystackease.async_apis import AsyncApplePayClientAPI


@pytest_asyncio.fixture
async def async_base_client():
    """ Async base client fixture"""
    async with AsyncBaseClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_paystack_base_client():
    """ Paystack async request client fixture"""
    async with AsyncPayStackBaseClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_apple_pay_client():
    """ Apple pay client fixture"""
    async with AsyncApplePayClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest.fixture
def base_client():
    """ Base client fixture"""
    return BaseClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def paystack_request_client():
    """ Paystack request client fixture"""
    return PayStackBaseClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def apple_pay_client():
    """ Apple pay client fixture"""
    return ApplePayClientAPI(secret_key="sk_secret_key")
