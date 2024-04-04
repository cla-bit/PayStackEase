""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import transactions_client


@pytest.mark.parametrize(
    (
        "email",
        "amount",
        "currency",
        "reference",
        "callback_url",
        "plan",
        "invoice_limit",
        "channels",
        "split_code",
        "subaccount",
        "transaction_charge",
        "bearer",
        "metadata",
    ),
    [
        (
            "test@email.com",
            10000,
            "NGN",
            "test-reference",
            "https://example.com/callback",
            "PLAN_test1234",
            10,
            ["ussd", "card"],
            "SPLIT_test123",
            "SUBACCT_test123",
            100,
            "account",
            {
                "status": "success",
                "custom": ["test-reference", "test-reference", "test-reference"],
            },
        ),
        (
            "test@email.com",
            10000,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ),
    ],
)
@responses.activate
def test_initialize_transaction(
    transactions_client,
    email,
    amount,
    currency,
    reference,
    callback_url,
    plan,
    invoice_limit,
    channels,
    split_code,
    subaccount,
    transaction_charge,
    bearer,
    metadata,
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transaction/initialize"
    response_data = {"status": "success"}
    expected_data = {
        "email": email,
        "amount": amount,
        "currency": currency,
        "reference": reference,
        "callback_url": callback_url,
        "plan": plan,
        "invoice_limit": invoice_limit,
        "channels": channels,
        "split_code": split_code,
        "subaccount": subaccount,
        "transaction_charge": transaction_charge,
        "bearer": bearer,
        "metadata": metadata,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transactions_client.initialize(
        email=email,
        amount=amount,
        currency=currency,
        reference=reference,
        callback_url=callback_url,
        plan=plan,
        invoice_limit=invoice_limit,
        channels=channels,
        split_code=split_code,
        subaccount=subaccount,
        transaction_charge=transaction_charge,
        bearer=bearer,
        metadata=metadata,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    (
        "email",
        "amount",
        "authorization_code",
        "reference",
        "currency",
        "channels",
        "subaccount",
        "transaction_charge",
        "bearer",
        "queue",
        "metadata",
    ),
    [
        (
            "test@email.com",
            10000,
            "AUTH_test1234",
            "test-reference",
            "NGN",
            ["ussd", "card"],
            "SUBACCT_test123",
            100,
            "account",
            True,
            {"status": [{"success": "ok"}]},
        ),
        (
            "test@email.com",
            10000,
            "AUTH_test1234",
            None,
            None,
            None,
            None,
            None,
            None,
            True,
            None,
        ),
    ],
)
@responses.activate
def test_charge_authorization(
    transactions_client,
    email,
    amount,
    authorization_code,
    reference,
    currency,
    channels,
    subaccount,
    transaction_charge,
    bearer,
    queue,
    metadata,
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transaction/charge_authorization"
    response_data = {"status": "success"}
    expected_data = {
        "email": email,
        "amount": amount,
        "authorization_code": authorization_code,
        "reference": reference,
        "currency": currency,
        "channels": channels,
        "subaccount": subaccount,
        "transaction_charge": transaction_charge,
        "bearer": bearer,
        "queue": str(queue),
        "metadata": metadata,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transactions_client.charge_authorization(
        email=email,
        amount=amount,
        authorization_code=authorization_code,
        reference=reference,
        currency=currency,
        channels=channels,
        subaccount=subaccount,
        transaction_charge=transaction_charge,
        bearer=bearer,
        queue=queue,
        metadata=metadata,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("email", "amount", "authorization_code", "reference", "currency", "at_least"),
    [
        ("test@email.com", 10000, "AUTH_test1234", "test-reference", "NGN", 1000),
        ("test@email.com", 10000, "AUTH_test1234", None, "NGN", None),
    ],
)
@responses.activate
def test_partial_debit(
    transactions_client,
    email,
    amount,
    authorization_code,
    reference,
    currency,
    at_least,
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/transaction/partial_debit"
    response_data = {"status": "success"}
    expected_data = {
        "email": email,
        "authorization_code": authorization_code,
        "amount": amount,
        "currency": currency,
        "reference": reference,
        "at_least": at_least,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = transactions_client.partial_debit(
        email=email,
        authorization_code=authorization_code,
        amount=amount,
        currency=currency,
        reference=reference,
        at_least=at_least,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    (
        "per_page",
        "page",
        "customer",
        "terminal_id",
        "amount",
        "status",
        "from_date",
        "to_date",
    ),
    [
        (
            1,
            10,
            12,
            "TERMINAL_testid",
            1000,
            "success",
            date(2012, 12, 12),
            date(2012, 12, 12),
        ),
        (None, None, None, None, None, None, None, None),
    ],
)
@responses.activate
def test_list_transactions(
    transactions_client,
    customer,
    terminal_id,
    amount,
    status,
    from_date,
    to_date,
    per_page,
    page,
):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/transaction"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "customer": customer,
        "terminalid": terminal_id,
        "amount": amount,
        "status": status,
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
    response = transactions_client.list_transactions(
        per_page=per_page,
        page=page,
        customer=customer,
        terminal_id=terminal_id,
        amount=amount,
        status=status,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_verify_transaction(transactions_client):
    """Test for synchronous Customers"""
    reference = "test-reference"
    url = f"https://api.paystack.co/transaction/verify/{reference}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = transactions_client.verify_transaction(reference=reference)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@responses.activate
def test_fetch_transaction(transactions_client):
    """Test for synchronous Customers"""
    transaction_id = "test-transaction-id"
    url = f"https://api.paystack.co/transaction/{transaction_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = transactions_client.fetch_transaction(transaction_id=transaction_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@responses.activate
def test_transaction_timeline(transactions_client):
    """Test for synchronous Customers"""
    transaction_id = "test-transaction-id"
    url = f"https://api.paystack.co/transaction/timeline/{transaction_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = transactions_client.transaction_timeline(id_or_reference=transaction_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    ("per_page", "page", "from_date", "to_date"),
    [(1, 10, date(2012, 12, 12), date(2012, 12, 12)), (None, None, None, None)],
)
@responses.activate
def test_list_transactions(transactions_client, from_date, to_date, per_page, page):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/transaction/totals"
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
    response = transactions_client.transaction_totals(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@pytest.mark.parametrize(
    (
        "per_page",
        "page",
        "customer",
        "currency",
        "amount",
        "status",
        "settled",
        "settlement",
        "payment_page",
        "from_date",
        "to_date",
    ),
    [
        (
            1,
            10,
            12,
            "NGN",
            1000,
            "success",
            True,
            12000,
            12,
            date(2012, 12, 12),
            date(2012, 12, 12),
        ),
        (None, None, None, None, None, None, True, None, None, None, None),
    ],
)
@responses.activate
def test_export_transactions(
    transactions_client,
    customer,
    currency,
    amount,
    status,
    settled,
    settlement,
    payment_page,
    from_date,
    to_date,
    per_page,
    page,
):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/transaction/export"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "customer": customer,
        "currency": currency,
        "amount": amount,
        "status": status,
        "settled": str(settled),
        "settlement": settlement,
        "payment_page": payment_page,
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
    response = transactions_client.export_transactions(
        per_page=per_page,
        page=page,
        customer=customer,
        currency=currency,
        amount=amount,
        status=status,
        settled=settled,
        settlement=settlement,
        payment_page=payment_page,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None
