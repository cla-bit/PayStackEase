""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import plans_client


@pytest.mark.parametrize(
    (
        "name",
        "amount",
        "interval",
        "currency",
        "invoice_limit",
        "send_invoices",
        "send_sms",
        "description",
    ),
    [
        ("Test", 10000, "annually", "NGN", 10, True, True, "Testing"),
        ("Test", 10000, "annually", "NGN", 10, True, True, None),
    ],
)
@responses.activate
def test_create_plan(
    plans_client,
    name,
    amount,
    interval,
    currency,
    invoice_limit,
    send_invoices,
    send_sms,
    description,
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/plan"
    response_data = {"status": "success"}
    expected_data = {
        "name": name,
        "amount": amount,
        "interval": interval,
        "description": description,
        "send_invoices": send_invoices,
        "send_sms": send_sms,
        "currency": currency,
        "invoice_limit": invoice_limit,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = plans_client.create_plan(
        name=name,
        amount=amount,
        interval=interval,
        description=description,
        send_invoices=send_invoices,
        send_sms=send_sms,
        currency=currency,
        invoice_limit=invoice_limit,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("per_page", "page", "status", "interval", "amount"),
    [(1, 10, "pending", "annually", 1000), (None, None, None, None, None)],
)
@responses.activate
def test_list_plans(plans_client, per_page, page, status, interval, amount):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/plan"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "status": status,
        "interval": interval,
        "amount": amount,
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
    response = plans_client.list_plans(
        per_page=per_page,
        page=page,
        status=status,
        interval=interval,
        amount=amount,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_fetch_plan(plans_client):
    """Test for synchronous Customers"""
    plan_id = "test-plan-id"
    url = f"https://api.paystack.co/plan/{plan_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = plans_client.fetch_plan(id_or_code=plan_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    (
        "name",
        "amount",
        "interval",
        "send_invoices",
        "send_sms",
        "currency",
        "invoice_limit",
        "description",
    ),
    [
        ("Test", 10000, "annually", True, True, "NGN", 10, "Testing"),
        ("Test", 10000, "annually", True, True, "NGN", 10, None),
    ],
)
@responses.activate
def test_update_plan(
    plans_client,
    name,
    amount,
    interval,
    send_invoices,
    send_sms,
    currency,
    invoice_limit,
    description,
):
    """Test for synchronous Customers"""
    plan_id_code = "test-plan-id-code"
    url = f"https://api.paystack.co/plan/{plan_id_code}"
    response_data = {"status": "success"}
    expected_data = {
        "name": name,
        "amount": amount,
        "interval": interval,
        "description": description,
        "send_invoices": send_invoices,
        "send_sms": send_sms,
        "currency": currency,
        "invoice_limit": invoice_limit,
    }

    responses.add(
        responses.PUT,
        url,
        status=200,
        json=response_data,
    )
    response = plans_client.update_plan(
        id_or_code=plan_id_code,
        name=name,
        amount=amount,
        interval=interval,
        description=description,
        send_invoices=send_invoices,
        send_sms=send_sms,
        currency=currency,
        invoice_limit=invoice_limit,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None
