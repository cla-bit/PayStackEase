""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import transfers_client


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
@responses.activate
def test_create_transfer(
    transfers_client,
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
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_client.initiate_transfer(
        transfer_source=transfer_source,
        amount=amount,
        transfer_recipient=transfer_recipient,
        reason=reason,
        currency=currency,
        reference=reference,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("transfer_code", "otp"), [("testing-transfer-code", "testing-otp")]
)
@responses.activate
def test_finalize_transfer(transfers_client, transfer_code, otp):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/finalize_transfer"
    response_data = {"status": "success"}
    expected_data = {"transfer_code": transfer_code, "otp": otp}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_client.finalize_transfer(transfer_code=transfer_code, otp=otp)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("transfer_source", "transfers"),
    [("balance", [{"amount": 1000, "reason": "balance"}])],
)
@responses.activate
def test_bulk_transfer(transfers_client, transfer_source, transfers):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transfer/bulk"
    response_data = {"status": "success"}
    expected_data = {"source": transfer_source, "transfers": transfers}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_client.initiate_bulk_transfer(
        transfer_source=transfer_source, transfers=transfers
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("customer_id", "from_date", "to_date", "per_page", "page"),
    [
        ("CUST_testid", date(2012, 12, 12), date(2012, 12, 12), 1, 10),
        (None, None, None, None, None),
    ],
)
@responses.activate
def test_list_transfers(
    transfers_client, customer_id, from_date, to_date, per_page, page
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

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = transfers_client.list_transfers(
        per_page=per_page,
        page=page,
        customer_id=customer_id,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response.status == "success"


@responses.activate
def test_fetch_transfer(transfers_client):
    """Test for synchronous Customers"""
    transfer_id = "test-trnasfer-id"
    url = f"https://api.paystack.co/transfer/{transfer_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_client.fetch_transfer(id_or_code=transfer_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response.status == "success"


@responses.activate
def test_verify_transfer(transfers_client):
    """Test for synchronous Customers"""
    reference = "test-reference"
    url = f"https://api.paystack.co/transfer/verify/{reference}"
    response_data = {"status": "success"}

    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transfers_client.verify_transfer(reference=reference)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None
