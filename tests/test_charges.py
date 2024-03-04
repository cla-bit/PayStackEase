""" Test for ChargesClientAPI """

import datetime
import json

import pytest
import responses

from paystackease import QRCODE, USSD, MobileMoney
from paystackease.apis import ChargesClientAPI


@pytest.fixture(scope="session", name="charge_client")
@responses.activate
def charge_client_test():
    """Fixture for ChargesClientAPI"""
    response_data = {"status": "success"}
    responses.add(
        responses.GET, "https://api.paystack.co/charge", json=response_data, status=200
    )
    client = ChargesClientAPI()
    return client


@responses.activate
def test_create_charge(charge_client):
    """ Test for create_charge """
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/charge",
        json=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected data
    response = charge_client.create_charge(
        email="test@gmail.com",
        amount=10000,
        bank=None,
        bank_transfer=None,
        authorization_code=None,
        pin=None,
        reference=None,
        qr={"provider": QRCODE.VISA.value},
        ussd={"type": USSD.GUARANTY_BANK.value},
        mobile_money={"phone": "2348012345678", "provider": MobileMoney.MTN.value},
        device_id=None,
        metadata=None,
    )
    expected_data = {
        "email": "test@gmail.com",
        "amount": 10000,
        "bank": None,
        "bank_transfer": None,
        "authorization_code": None,
        "pin": None,
        "reference": None,
        "qr": {"provider": QRCODE.VISA.value},
        "ussd": {"type": USSD.GUARANTY_BANK.value},
        "mobile_money": {"phone": "2348012345678", "provider": MobileMoney.MTN.value},
        "device_id": None,
        "metadata": None,
    }
    expected_url = "https://api.paystack.co/charge"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_submit_pin(charge_client):
    """ Test for submit_pin """
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/charge/submit_pin",
        json=response_data,
        status=200,
    )
    response = charge_client.submit_pin(pin=1234, reference="test")
    expected_data = {"pin": 1234, "reference": "test"}
    expected_url = "https://api.paystack.co/charge/submit_pin"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response


@responses.activate
def test_submit_otp(charge_client):
    """ Test for submit_otp """
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/charge/submit_otp",
        json=response_data,
        status=200,
    )
    response = charge_client.submit_otp(otp=1234, reference="test")
    expected_data = {"otp": 1234, "reference": "test"}
    expected_url = "https://api.paystack.co/charge/submit_otp"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response


@responses.activate
def test_submit_phone(charge_client):
    """ Test for submit_phone """
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/charge/submit_phone",
        json=response_data,
        status=200,
    )
    response = charge_client.submit_phone(phone="2348012345678", reference="test")
    expected_data = {"phone": "2348012345678", "reference": "test"}
    expected_url = "https://api.paystack.co/charge/submit_phone"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response


@responses.activate
def test_submit_birthday(charge_client):
    """ Test for submit_birthday """
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/charge/submit_birthday",
        json=response_data,
        status=200,
    )
    response = charge_client.submit_birthday(
        birthday=datetime.date.today().isoformat(), reference="test"
    )
    expected_data = {"birthday": datetime.date.today().isoformat(), "reference": "test"}
    expected_url = "https://api.paystack.co/charge/submit_birthday"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response


@responses.activate
def test_submit_address(charge_client):
    """ Test for submit_address """
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/charge/submit_address",
        json=response_data,
        status=200,
    )
    response = charge_client.submit_address(
        address="test", reference="test", city="test", state="test", zipcode="test"
    )
    expected_data = {
        "address": "test",
        "reference": "test",
        "city": "test",
        "state": "test",
        "zipcode": "test",
    }
    expected_url = "https://api.paystack.co/charge/submit_address"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response


@responses.activate
def test_check_pending_charges(charge_client):
    """ Test for check_pending_charges """
    response_data = {"status": "success"}
    reference = "test"
    responses.add(
        responses.GET,
        f"https://api.paystack.co/charge/{reference}",
        json=response_data,
        status=200,
    )
    response = charge_client.check_pending_charge(reference=reference)
    expected_url = f"https://api.paystack.co/charge/{reference}"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response
