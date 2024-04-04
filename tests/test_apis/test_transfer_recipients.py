""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import transfer_recipients_client


@pytest.mark.parametrize(
    (
        "recipient_type",
        "recipient_name",
        "account_number",
        "bank_code",
        "description",
        "currency",
        "authorization_code",
        "metadata",
    ),
    [
        (
            "nuban",
            "Testing",
            "0000000000",
            "053",
            "Testing-recipient",
            "NGN",
            "AUTH_test1234",
            {"status": "sucess"},
        ),
        ("nuban", "Testing", "0000000000", "053", None, None, None, None),
    ],
)
@responses.activate
def test_create_recipient(
    transfer_recipients_client,
    recipient_type,
    recipient_name,
    account_number,
    bank_code,
    description,
    currency,
    authorization_code,
    metadata,
):
    """Test for synchronous Customers"""
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
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfer_recipients_client.create_transfer_recipients(
        recipient_type=recipient_type,
        recipient_name=recipient_name,
        account_number=account_number,
        bank_code=bank_code,
        description=description,
        currency=currency,
        authorization_code=authorization_code,
        metadata=metadata,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("batch",),
    [
        ([{"name": "Tester"}]),
        ([{"name": "Tester", "account_number": "0000000000"}]),
    ],
)
@responses.activate
def test_create_bulk_recipient(transfer_recipients_client, batch):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transferrecipient/bulk"
    response_data = {"status": "success"}
    expected_data = {
        "batch": batch,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfer_recipients_client.bulk_create_transfer_recipient(batch=batch)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page"),
    [(date(2012, 12, 12), date(2012, 12, 12), 1, 10), (None, None, None, None)],
)
@responses.activate
def test_list_recipients(
    transfer_recipients_client, from_date, to_date, per_page, page
):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/transferrecipient"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "from": from_date,
        "to": to_date,
    }
    # Construct the expected URL with parameters
    query_string = "&".join(
        f"{key}={value}" for key, value in url_params.items() if value is not None
    )
    expected_url = url + ("?" + query_string if query_string else "")

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = transfer_recipients_client.list_transfer_recipients(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_fetch_recipient(transfer_recipients_client):
    """Test for synchronous Customers"""
    recipient_id = "test-recipient-id"
    url = f"https://api.paystack.co/transferrecipient/{recipient_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = transfer_recipients_client.fetch_transfer_recipient(
        id_or_code=recipient_id
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    ("recipient_name", "recipient_email"),
    [
        ("Test", "test@email.com"),
        ("Test", None),
    ],
)
@responses.activate
def test_update_recipient(transfer_recipients_client, recipient_name, recipient_email):
    """Test for synchronous Customers"""
    recipient_id = "test-recipient-id"
    url = f"https://api.paystack.co/transferrecipient/{recipient_id}"
    response_data = {"status": "success"}
    expected_data = {"name": recipient_name, "email": recipient_email}

    responses.add(
        responses.PUT,
        url,
        status=200,
        json=response_data,
    )
    response = transfer_recipients_client.update_transfer_recipient(
        id_or_code=recipient_id,
        recipient_name=recipient_name,
        recipient_email=recipient_email,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_delete_recipient(transfer_recipients_client):
    """Test for synchronous Customers"""
    recipient_id = "test-recipient-id"
    url = f"https://api.paystack.co/transferrecipient/{recipient_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.DELETE,
        url,
        status=200,
        json=response_data,
    )
    response = transfer_recipients_client.delete_transfer_recipient(
        id_or_code=recipient_id
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None
