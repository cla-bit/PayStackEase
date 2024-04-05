""" Test for synchronous Customers """

import json
from datetime import date
import pytest

from tests.conftest import async_refund_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("transaction_ref_id", "amount", "currency", "customer_note", "merchant_note"),
    [
        (
            "TRANS_testing",
            100000,
            "NGN",
            "Testing Customer Note",
            "Testing Merchant Note",
        ),
        ("TRANS_testing", None, None, None, None),
    ],
)
async def test_create_refund(
    async_refund_client,
    mocked_responses,
    transaction_ref_id,
    amount,
    currency,
    customer_note,
    merchant_note,
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/refund"
    response_data = {"status": "success"}
    expected_data = {
        "transaction": transaction_ref_id,
        "amount": amount,
        "currency": currency,
        "customer_note": customer_note,
        "merchant_note": merchant_note,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_refund_client.create_refund(
        transaction_ref_or_id=transaction_ref_id,
        amount=amount,
        currency=currency,
        customer_note=customer_note,
        merchant_note=merchant_note,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("reference", "currency", "from_date", "to_date", "per_page", "page"),
    [
        ("REF_testing1234", "NGN", date(2012, 12, 12), date(2012, 12, 12), 1, 10),
        (None, None, None, None, None, None),
    ],
)
async def test_list_refunds(
    async_refund_client,
    mocked_responses,
    reference,
    currency,
    from_date,
    to_date,
    per_page,
    page,
):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/refund"
    response_data = {"status": "success"}
    url_params = {
        "reference": reference,
        "currency": currency,
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

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_refund_client.list_refunds(
        reference=reference,
        currency=currency,
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_refund(async_refund_client, mocked_responses):
    """Test for synchronous Customers"""
    ref_id = "test-ref-id"
    url = f"https://api.paystack.co/refund/{ref_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_refund_client.fetch_refund(reference=ref_id)
    mocked_responses.assert_called()
    assert response is not None
