""" Tests for TransactionClientAPI  """

import json
import urllib.parse

from datetime import datetime
import pytest
import responses

from paystackease import Channels, Currency
from paystackease.apis import TransactionClientAPI


@pytest.fixture(scope="session", name="transaction_client")
@responses.activate
def transaction_client_test():
    """Fixture for TransactionClientAPI"""
    response_data = {"key": "value"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/transaction/initialize",
        json=response_data,
        status=200,
    )
    client = TransactionClientAPI()
    return client


@responses.activate
def test_initialize(transaction_client):
    """Test for initialize"""
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/transaction/initialize",
        json=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected data
    response = transaction_client.initialize(
        email="test@gmail.com",
        amount=1000,
        currency=Currency.NGN.value,
        reference=None,
        callback_url="https://example.com/callback",
        plan=None,
        invoice_limit=1000,
        channels=[Channels.CARD.value],
        split_code="SPL_98WF13Eb3w",
        subaccount="ACCT_8f4s1eq7ml6rlzj",
        transaction_charge=None,
        bearer="account",
        metadata={"test": "test"},
    )
    assert len(responses.calls) == 1
    assert (
        responses.calls[0].request.url
        == "https://api.paystack.co/transaction/initialize"
    )
    expected_data = {
        "email": "test@gmail.com",
        "amount": 1000,
        "currency": Currency.NGN.value,
        "reference": None,
        "channels": [Channels.CARD.value],
        "callback_url": "https://example.com/callback",
        "plan": None,
        "invoice_limit": 1000,
        "split_code": "SPL_98WF13Eb3w",
        "subaccount": "ACCT_8f4s1eq7ml6rlzj",
        "transaction_charge": None,
        "bearer": "account",
        "metadata": {"test": "test"},
    }
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response == response_data


@responses.activate
def test_charge_authorization(transaction_client):
    """Test for charge_authorization"""
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/transaction/charge_authorization",
        json=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected data
    response = transaction_client.charge_authorization(
        authorization_code="AUTH_1c2b3a4d5",
        email="test@gmail.com",
        amount=1000,
        reference="test",
        currency=Currency.NGN.value,
        channels=[Channels.CARD.value],
        subaccount="ACCT_8f4s1eq7ml6rlzj",
        transaction_charge=100,
        bearer="account",
        queue=True,
        metadata={"test": "test"},
    )
    assert len(responses.calls) == 1
    assert (
        responses.calls[0].request.url
        == "https://api.paystack.co/transaction/charge_authorization"
    )
    expected_data = {
        "authorization_code": "AUTH_1c2b3a4d5",
        "email": "test@gmail.com",
        "amount": 1000,
        "reference": "test",
        "currency": Currency.NGN.value,
        "channels": [Channels.CARD.value],
        "subaccount": "ACCT_8f4s1eq7ml6rlzj",
        "transaction_charge": 100,
        "bearer": "account",
        "queue": "true",
        "metadata": {"test": "test"},
    }
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response == response_data


@responses.activate
def test_partial_debit(transaction_client):
    """Test for partial_debit"""
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/transaction/partial_debit",
        json=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected data
    response = transaction_client.partial_debit(
        authorization_code="AUTH_1c2b3a4d5",
        email="test@gmail.com",
        amount=1000,
        currency=Currency.NGN.value,
        reference="test",
        at_least=100,
    )
    assert len(responses.calls) == 1
    assert (
        responses.calls[0].request.url
        == "https://api.paystack.co/transaction/partial_debit"
    )
    expected_data = {
        "authorization_code": "AUTH_1c2b3a4d5",
        "email": "test@gmail.com",
        "amount": 1000,
        "currency": Currency.NGN.value,
        "reference": "test",
        "at_least": 100,
    }
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response == response_data


@pytest.mark.parametrize(
    "per_page, page, customer, terminal_id, amount, status, from_date, to_date",
    [
        (
            10,
            1,
            2,
            "2",
            1000,
            "success",
            datetime(2024, 2, 23, 18, 23, 24, 269163),
            datetime(2024, 2, 23, 18, 23, 24, 269163),
        )
    ],
)
@responses.activate
def test_list_transactions(
    transaction_client,
    per_page,
    page,
    customer,
    terminal_id,
    amount,
    status,
    from_date,
    to_date,
):
    """Test for list_transactions"""
    fixed_timestamp = datetime(2024, 2, 23, 18, 23, 24, 269163)
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/transaction",
        json=response_data,
        status=200,
    )
    response = transaction_client.list_transactions(
        per_page=per_page,
        page=page,
        customer=customer,
        terminal_id=terminal_id,
        amount=amount,
        status=status,
        from_date=str(from_date.isoformat()),
        to_date=str(to_date.isoformat()),
    )
    assert len(responses.calls) == 1
    expected_params = {
        "perPage": per_page,
        "page": page,
        "customer": customer,
        "terminalid": terminal_id,
        "amount": amount,
        "status": status,
        "from": str(from_date.isoformat()),
        "to": str(to_date.isoformat()),
    }
    expected_url = "https://api.paystack.co/transaction"
    encode_datetime = urllib.parse.quote(fixed_timestamp.isoformat())
    assert responses.calls[0].request.url == expected_url + "?" + "&".join(
        f"{key}={value}" for key, value in expected_params.items() if value is not None
    ).replace(fixed_timestamp.isoformat(), encode_datetime)
    assert response == response_data


@responses.activate
def verify_transaction(transaction_client):
    """Test for verify_transaction"""
    reference = "test"
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        f"https://api.paystack.co/transaction/verify/{reference}",
        json=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected data
    response = transaction_client.verify_transaction(reference=reference)
    assert len(responses.calls) == 1
    assert (
        responses.calls[0].request.url
        == f"https://api.paystack.co/transaction/verify/{reference}"
    )
    assert response == response_data


@responses.activate
def test_fetch_transaction(transaction_client):
    """Test for fetch_transaction"""
    transaction_id = 1
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        f"https://api.paystack.co/transaction/{transaction_id}",
        json=response_data,
        status=200,
    )
    response = transaction_client.fetch_transaction(transaction_id=transaction_id)
    assert len(responses.calls) == 1
    assert (
        responses.calls[0].request.url
        == f"https://api.paystack.co/transaction/{transaction_id}"
    )
    assert response == response_data


@responses.activate
def test_transaction_timeline(transaction_client):
    """Test for transaction_timeline"""
    id_or_reference = "test"
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        f"https://api.paystack.co/transaction/timeline/{id_or_reference}",
        json=response_data,
        status=200,
    )
    response = transaction_client.transaction_timeline(id_or_reference=id_or_reference)
    assert len(responses.calls) == 1
    assert (
        responses.calls[0].request.url
        == f"https://api.paystack.co/transaction/timeline/{id_or_reference}"
    )
    assert response == response_data


@pytest.mark.parametrize(
    "per_page, page, from_date, to_date",
    [
        (
            10,
            1,
            datetime(2024, 2, 23, 18, 23, 24, 269163),
            datetime(2024, 2, 23, 18, 23, 24, 269163),
        )
    ],
)
@responses.activate
def test_transaction_totals(transaction_client, per_page, page, from_date, to_date):
    """Test for transaction_totals"""
    fixed_timestamp = datetime(2024, 2, 23, 18, 23, 24, 269163)
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/transaction/totals",
        json=response_data,
        status=200,
    )
    response = transaction_client.transaction_totals(
        per_page=per_page,
        page=page,
        from_date=str(from_date.isoformat()),
        to_date=str(to_date.isoformat()),
    )
    assert len(responses.calls) == 1
    expected_params = {
        "perPage": per_page,
        "page": page,
        "from": str(from_date.isoformat()),
        "to": str(to_date.isoformat()),
    }
    expected_url = "https://api.paystack.co/transaction/totals"
    encode_datetime = urllib.parse.quote(fixed_timestamp.isoformat())
    assert responses.calls[0].request.url == expected_url + "?" + "&".join(
        f"{key}={value}" for key, value in expected_params.items() if value is not None
    ).replace(fixed_timestamp.isoformat(), encode_datetime)
    assert response == response_data


@pytest.mark.parametrize(
    "per_page, page, customer, currency, amount, status, "
    "settled, settlement, payment_page, from_date, to_date",
    [
        (
            10,
            1,
            2,
            "NGN",
            1000,
            "success",
            True,
            2,
            2,
            datetime(2024, 2, 23, 18, 23, 24, 269163),
            datetime(2024, 2, 23, 18, 23, 24, 269163),
        )
    ],
)
@responses.activate
def test_export_transactions(
    transaction_client,
    per_page,
    page,
    customer,
    currency,
    amount,
    status,
    settled,
    settlement,
    payment_page,
    from_date,
    to_date,
):
    """Test for export_transactions"""
    fixed_timestamp = datetime(2024, 2, 23, 18, 23, 24, 269163)
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/transaction/export",
        json=response_data,
        status=200,
    )
    response = transaction_client.export_transactions(
        per_page=per_page,
        page=page,
        customer=customer,
        currency=currency,
        amount=amount,
        status=status,
        settled=settled,
        settlement=settlement,
        payment_page=payment_page,
        from_date=str(from_date.isoformat()),
        to_date=str(to_date.isoformat()),
    )
    assert len(responses.calls) == 1
    expected_params = {
        "perPage": per_page,
        "page": page,
        "customer": customer,
        "currency": currency,
        "amount": amount,
        "status": status,
        "settled": "true",
        "settlement": settlement,
        "payment_page": payment_page,
        "from": str(from_date.isoformat()),
        "to": str(to_date.isoformat()),
    }
    expected_url = "https://api.paystack.co/transaction/export"
    encode_datetime = urllib.parse.quote(fixed_timestamp.isoformat())
    assert responses.calls[0].request.url == expected_url + "?" + "&".join(
        f"{key}={value}" for key, value in expected_params.items() if value is not None
    ).replace(fixed_timestamp.isoformat(), encode_datetime)
    assert response == response_data
