""" Fixtures for testing purposes """

import pytest
import pytest_asyncio
from aioresponses import aioresponses
from paystackease._abase import AsyncBaseClientAPI, AsyncPayStackBaseClientAPI
from paystackease._base import BaseClientAPI, PayStackBaseClientAPI
from paystackease.apis import (
    apple_pay,
    bulk_charges
)
from paystackease.async_apis import (
    aapple_pay,
    abulk_charges
)


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
    async with aapple_pay.AsyncApplePayClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_bulk_charges_client():
    """ Bulk Charges client fixture"""
    async with abulk_charges.AsyncBulkChargesClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def mocked_responses():
    """ Mocked responses fixture"""
    with aioresponses() as mocked:
        yield mocked


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
    return apple_pay.ApplePayClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def bulk_charges_client():
    """ Bulk Charges client fixture"""
    return bulk_charges.BulkChargesClientAPI(secret_key="sk_secret_key")
