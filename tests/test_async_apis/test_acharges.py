""" Test for asynchornous Charges """

import pytest
from datetime import date

from tests.conftest import async_charges_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("email", "amount", "pin", "authorization_code", "reference",
     "device_id", "bank", "bank_transfer", "qr", "ussd", "mobile_money", "metadata"
     ),
    [
        ("test-email@gmail.com", 10000, 1234, "AUTH_test1234", "test-ref1234",
         "test-device-id", None,
         {"account_expires_at": "2023-09-12T13:10:00Z"}, {"provider": "visa"},
         None, None, {"nickname": "tester"}
         ),
        ("test-email@gmail.com", 10000, 1234, None, "test-ref1234",
         "test-device-id", {"code": "123", "account_number": "0000000000"},
         {"account_expires_at": "2023-09-12T13:10:00Z"}, {"provider": "visa"},
         None, None, {"nickname": "tester"}
         )
    ],

)
async def test_create_charge(async_charges_client, mocked_responses, email,
                             amount, pin, authorization_code, reference,
                             device_id, bank, bank_transfer, qr, ussd,
                             mobile_money, metadata):
    url = "https://api.paystack.co/charge"
    expected_data = {"email": email, "amount": amount, "pin": pin,
                     "authorization_code": authorization_code, "reference": reference,
                     "device_id": device_id, "bank": bank, "bank_transfer": bank_transfer,
                     "qr": qr, "ussd": ussd, "mobile_money": mobile_money, "metadata": metadata}

    mocked_responses.post(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_charges_client.create_charge(
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
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_submit_pin(async_charges_client, mocked_responses):
    url = "https://api.paystack.co/charge/submit_pin"
    pin = 1234
    reference = "test-reference1234"
    expected_data = {"pin": pin, "reference": reference}
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_charges_client.submit_pin(pin=pin, reference=reference)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_submit_otp(async_charges_client, mocked_responses):
    url = "https://api.paystack.co/charge/submit_otp"
    otp = 1234
    reference = "test-reference1234"
    expected_data = {"otp": otp, "reference": reference}
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_charges_client.submit_otp(otp=otp, reference=reference)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_submit_phone(async_charges_client, mocked_responses):
    url = "https://api.paystack.co/charge/submit_phone"
    phone = "08012345678"
    reference = "test-reference1234"
    expected_data = {"phone": phone, "reference": reference}
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_charges_client.submit_phone(phone=phone, reference=reference)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_submit_birthday(async_charges_client, mocked_responses):
    url = "https://api.paystack.co/charge/submit_birthday"
    birthday = date(2013, 12, 12)
    reference = "test-reference1234"
    expected_data = {"birthday": birthday.strftime("%Y-%m-%d"), "reference": reference}
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_charges_client.submit_birthday(birthday=birthday, reference=reference)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_submit_address(async_charges_client, mocked_responses):
    url = "https://api.paystack.co/charge/submit_address"
    address = "Oakland Zone"
    city = "NY"
    state = "NY"
    zipcode = "10001"
    reference = "test-reference1234"
    expected_data = {
        "reference": reference,
        "address": address, "city": city, "state": state,
        "zip_code": zipcode
    }
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_charges_client.submit_address(
        reference=reference, address=address,
        city=city, state=state, zipcode=zipcode
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_check_pending_charge(async_charges_client, mocked_responses):
    response_data = {"status": "success"}
    reference = "test-reference1234"
    url = f"https://api.paystack.co/charge/{reference}"
    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_charges_client.check_pending_charge(reference=reference)
    mocked_responses.assert_called()
    assert response is not None
