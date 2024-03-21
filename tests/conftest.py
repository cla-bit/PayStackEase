""" Fixtures for testing purposes """

import pytest
from paystackease._abase import AsyncBaseClientAPI, AsyncPayStackBaseClientAPI
from paystackease._base import BaseClientAPI, PayStackBaseClientAPI
from paystackease.apis.apple_pay import ApplePayClientAPI


@pytest.fixture
async def async_base_client():
    """ Async base client fixture"""
    return AsyncBaseClientAPI(secret_key="sk_secret_key")


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
