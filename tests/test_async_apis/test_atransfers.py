""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import async_transfers_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    (
        "transfer_source",
        "amount",
        "transfer_recipient",
        "reason",
        "currency",
        "reference",
    ),
    [
        (
            "balance",
            10000,
            "TRANSRECIPIENT_test",
            "Testing-transfer",
            "NGN",
            "test-ref1234",
        ),
        ("balance", 10000, "TRANSRECIPIENT_test", None, None, None),
    ],
)
async def test_create_transfer(
    async_transfers_client,
    mocked_responses,
    transfer_source,
    amount,
    transfer_recipient,
    reason,
    currency,
    reference,
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer"
    response_data = {"status": "success"}
    expected_data = {
        "source": transfer_source,
        "amount": amount,
        "recipient": transfer_recipient,
        "reason": reason,
        "currency": currency,
        "reference": reference,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_client.initiate_transfer(
        transfer_source=transfer_source,
        amount=amount,
        transfer_recipient=transfer_recipient,
        reason=reason,
        currency=currency,
        reference=reference,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("transfer_code", "otp"), [("testing-transfer-code", "testing-otp")]
)
async def test_finalize_transfer(
    async_transfers_client, mocked_responses, transfer_code, otp
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/finalize_transfer"
    response_data = {"status": "success"}
    expected_data = {"transfer_code": transfer_code, "otp": otp}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_client.finalize_transfer(
        transfer_code=transfer_code, otp=otp
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("transfer_source", "transfers"),
    [("balance", [{"amount": 1000, "reason": "balance"}])],
)
async def test_bulk_transfer(
    async_transfers_client, mocked_responses, transfer_source, transfers
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/bulk"
    response_data = {"status": "success"}
    expected_data = {"source": transfer_source, "transfers": transfers}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_client.initiate_bulk_transfer(
        transfer_source=transfer_source, transfers=transfers
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("customer_id", "from_date", "to_date", "per_page", "page"),
    [
        ("CUST_testid", date(2012, 12, 12), date(2012, 12, 12), 1, 10),
        (None, None, None, None, None),
    ],
)
async def test_list_transfers(
    async_transfers_client,
    mocked_responses,
    customer_id,
    from_date,
    to_date,
    per_page,
    page,
):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/transfer"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "customer": customer_id,
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
    response = await async_transfers_client.list_transfers(
        per_page=per_page,
        page=page,
        customer_id=customer_id,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_transfer(async_transfers_client, mocked_responses):
    """Test for synchronous Customers"""
    transfer_id = "test-trnasfer-id"
    url = f"https://api.paystack.co/transfer/{transfer_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_client.fetch_transfer(id_or_code=transfer_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_verify_transfer(async_transfers_client, mocked_responses):
    """Test for synchronous Customers"""
    reference = "test-reference"
    url = f"https://api.paystack.co/transfer/verify/{reference}"
    response_data = {"status": "success"}

    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transfers_client.verify_transfer(reference=reference)
    mocked_responses.assert_called()
    assert response is not None
