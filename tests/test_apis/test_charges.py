""" Test for chares """

import json
from datetime import date, datetime
import pytest
import responses

from paystackease.helpers.tool_kit import PWT, QRCODE, USSD, MobileMoney
from tests.conftest import charges_client


@pytest.mark.parametrize(
    (
        "email",
        "amount",
        "pin",
        "authorization_code",
        "reference",
        "device_id",
        "bank",
        "bank_transfer",
        "qr",
        "ussd",
        "mobile_money",
        "metadata",
    ),
    [
        (
            "test-email@gmail.com",
            10000,
            1234,
            "AUTH_test1234",
            "test-ref1234",
            "test-device-id",
            None,
            {PWT.ACCOUNT_EXPIRES_AT.value: date.today().strftime("%Y-%m-%d")},
            {"provider": QRCODE.VISA.value},
            None,
            None,
            {
                "custom_fields": [
                    {
                        "value": "test",
                        "display_name": "test-display",
                        "variable_name": "test-variable",
                    }
                ]
            },
        ),
        (
            "test-email@gmail.com",
            10000,
            1234,
            None,
            "test-ref1234",
            "test-device-id",
            {"code": "123", "account_number": "0000000000"},
            {PWT.ACCOUNT_EXPIRES_AT.value: datetime.today().strftime("%Y-%m-%d")},
            {"provider": QRCODE.SCAN_TO_PAY.value},
            None,
            None,
            {
                "custom_fields": [
                    {
                        "value": "test",
                        "display_name": "test-display",
                        "variable_name": "test-variable",
                    }
                ]
            },
        ),
    ],
)
@responses.activate
def test_create_charge(
    charges_client,
    email,
    amount,
    pin,
    authorization_code,
    reference,
    device_id,
    bank,
    bank_transfer,
    qr,
    ussd,
    mobile_money,
    metadata,
):
    url = "https://api.paystack.co/charge"
    response_data = {"status": "success"}
    expected_data = {
        "email": email,
        "amount": amount,
        "pin": pin,
        "authorization_code": authorization_code,
        "reference": reference,
        "device_id": device_id,
        "bank": bank,
        "bank_transfer": bank_transfer,
        "qr": qr,
        "ussd": ussd,
        "mobile_money": mobile_money,
        "metadata": metadata,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = charges_client.create_charge(
        email=email,
        amount=amount,
        pin=pin,
        authorization_code=authorization_code,
        reference=reference,
        device_id=device_id,
        bank=bank,
        bank_transfer=bank_transfer,
        qr=qr,
        ussd=ussd,
        mobile_money=mobile_money,
        metadata=metadata,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_submit_pin(charges_client):
    url = "https://api.paystack.co/charge/submit_pin"
    response_data = {"status": "success"}
    pin = 1234
    reference = "test-reference1234"
    expected_data = {"pin": pin, "reference": reference}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = charges_client.submit_pin(pin=pin, reference=reference)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_submit_otp(charges_client):
    url = "https://api.paystack.co/charge/submit_otp"
    response_data = {"status": "success"}
    otp = 1234
    reference = "test-reference1234"
    expected_data = {"otp": otp, "reference": reference}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = charges_client.submit_otp(otp=otp, reference=reference)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_submit_phone(charges_client):
    url = "https://api.paystack.co/charge/submit_phone"
    response_data = {"status": "success"}
    phone = "08012345678"
    reference = "test-reference1234"
    expected_data = {"phone": phone, "reference": reference}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = charges_client.submit_phone(phone=phone, reference=reference)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_submit_birthday(charges_client):
    url = "https://api.paystack.co/charge/submit_birthday"
    response_data = {"status": "success"}
    birthday = date(2013, 12, 12)
    reference = "test-reference1234"
    expected_data = {"birthday": birthday.strftime("%Y-%m-%d"), "reference": reference}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = charges_client.submit_birthday(birthday=birthday, reference=reference)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_submit_address(charges_client):
    url = "https://api.paystack.co/charge/submit_address"
    response_data = {"status": "success"}
    address = "Oakland Zone"
    city = "NY"
    state = "NY"
    zipcode = "10001"
    reference = "test-reference1234"
    expected_data = {
        "reference": reference,
        "address": address,
        "city": city,
        "state": state,
        "zip_code": zipcode,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = charges_client.submit_address(
        reference=reference, address=address, city=city, state=state, zipcode=zipcode
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_check_pending_charge(charges_client):
    response_data = {"status": "success"}
    reference = "test-reference1234"
    url = f"https://api.paystack.co/charge/{reference}"
    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = charges_client.check_pending_charge(reference=reference)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response.status == "success"
