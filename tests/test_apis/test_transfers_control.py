""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import transfers_control_client


@responses.activate
def test_check_balance(transfers_control_client):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/balance"
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_control_client.check_balance()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@responses.activate
def test_fetch_balance(transfers_control_client):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/balance/ledger"
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_control_client.fetch_balance_ledger()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    ("transfer_code", "reason"), [("test-transfer-code", "test-reason")]
)
@responses.activate
def test_resend_otp(transfers_control_client, transfer_code, reason):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/resend_otp"
    response_data = {"status": "success"}
    expected_data = {"transfer_code": transfer_code, "reason": reason}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_control_client.resend_otp(
        transfer_code=transfer_code, reason=reason
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_disable_otp(transfers_control_client):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/disable_otp"
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_control_client.disable_otp()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response == response_data
    assert response is not None


@pytest.mark.parametrize(("otp"), [("test-otp-123")])
@responses.activate
def test_finalize_disable_otp(transfers_control_client, otp):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/disable_otp_finalize"
    response_data = {"status": "success"}
    expected_data = {"otp": otp}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_control_client.finalize_disable_otp(otp=otp)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_enable_otp(transfers_control_client):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/enable_otp"
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_control_client.enable_otp()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response == response_data
    assert response is not None
