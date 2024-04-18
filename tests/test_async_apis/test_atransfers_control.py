""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import async_transfers_control_client, mocked_responses


@pytest.mark.asyncio
async def test_check_balance(async_transfers_control_client, mocked_responses):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/balance"
    response_data = {"status": "success"}
    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_control_client.check_balance()
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_balance(async_transfers_control_client, mocked_responses):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/balance/ledger"
    response_data = {"status": "success"}
    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_control_client.fetch_balance_ledger()
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("transfer_code", "reason"), [("test-transfer-code", "test-reason")]
)
async def test_resend_otp(
    async_transfers_control_client, mocked_responses, transfer_code, reason
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/resend_otp"
    response_data = {"status": "success"}
    expected_data = {"transfer_code": transfer_code, "reason": reason}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_control_client.resend_otp(
        transfer_code=transfer_code, reason=reason
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_disable_otp(async_transfers_control_client, mocked_responses):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/disable_otp"
    response_data = {"status": "success"}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_control_client.disable_otp()
    mocked_responses.assert_called()
    assert response.status == "success"
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(("otp"), [("test-otp-123")])
async def test_finalize_disable_otp(
    async_transfers_control_client, mocked_responses, otp
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/disable_otp_finalize"
    response_data = {"status": "success"}
    expected_data = {"otp": otp}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_control_client.finalize_disable_otp(otp=otp)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_enable_otp(async_transfers_control_client, mocked_responses):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/enable_otp"
    response_data = {"status": "success"}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_control_client.enable_otp()
    mocked_responses.assert_called()
    assert response.status == "success"
    assert response is not None
