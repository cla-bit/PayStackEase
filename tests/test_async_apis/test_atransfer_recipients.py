""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import async_transfer_recipients_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("recipient_type", "recipient_name", "account_number", "bank_code", "description", "currency", "authorization_code", "metadata"),
    [
        ("nuban", "Testing", "0000000000", "053", "Testing-recipient", "NGN", "AUTH_test1234", {"status": "sucess"}),
        ("nuban", "Testing", "0000000000", "053", None, None, None, None),
    ]
)
async def test_create_recipient(async_transfer_recipients_client, mocked_responses, recipient_type, recipient_name, account_number, bank_code, description, currency, authorization_code, metadata):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/transferrecipient"
    response_data = {"status": "success"}
    expected_data = {
        "type": recipient_type,
        "name": recipient_name,
        "account_number": account_number,
        "bank_code": bank_code,
        "description": description,
        "currency": currency,
        "authorization_code": authorization_code,
        "metadata": metadata,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfer_recipients_client.create_transfer_recipients(
        recipient_type=recipient_type,
        recipient_name=recipient_name,
        account_number=account_number,
        bank_code=bank_code,
        description=description,
        currency=currency,
        authorization_code=authorization_code,
        metadata=metadata
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("batch",),
    [
        ([{"name": "Tester"}]),
        ([{"name": "Tester", "account_number": "0000000000"}]),
    ]
)
async def test_create_bulk_recipient(async_transfer_recipients_client, mocked_responses, batch):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/transferrecipient/bulk"
    response_data = {"status": "success"}
    expected_data = {
        "batch": batch,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfer_recipients_client.bulk_create_transfer_recipient(batch=batch)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page"),
    [
        (date(2012, 12, 12), date(2012, 12, 12), 1, 10),
        (None, None, None, None)
    ]
)
async def test_list_recipients(async_transfer_recipients_client, mocked_responses, from_date, to_date, per_page, page):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/transferrecipient"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "from": from_date,
        "to": to_date,
    }
    # Construct the expected URL with parameters
    query_string = '&'.join(f'{key}={value}' for key, value in url_params.items() if value is not None)
    expected_url = url + ('?' + query_string if query_string else '')

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_transfer_recipients_client.list_transfer_recipients(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_recipient(async_transfer_recipients_client, mocked_responses):
    """ Test for synchronous Customers """
    recipient_id = "test-recipient-id"
    url = f"https://api.paystack.co/transferrecipient/{recipient_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfer_recipients_client.fetch_transfer_recipient(id_or_code=recipient_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("recipient_name", "recipient_email"),
    [
        ("Test", "test@email.com"),
        ("Test", None),
    ]
)
async def test_update_recipient(async_transfer_recipients_client, mocked_responses, recipient_name, recipient_email):
    """ Test for synchronous Customers """
    recipient_id = "test-recipient-id"
    url = f"https://api.paystack.co/transferrecipient/{recipient_id}"
    response_data = {"status": "success"}
    expected_data = {"name": recipient_name, "email": recipient_email}

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfer_recipients_client.update_transfer_recipient(id_or_code=recipient_id, recipient_name=recipient_name, recipient_email=recipient_email)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_delete_recipient(async_transfer_recipients_client, mocked_responses):
    """ Test for synchronous Customers """
    recipient_id = "test-recipient-id"
    url = f"https://api.paystack.co/transferrecipient/{recipient_id}"
    response_data = {"status": "success"}

    mocked_responses.delete(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfer_recipients_client.delete_transfer_recipient(id_or_code=recipient_id)
    mocked_responses.assert_called()
    assert response is not None
