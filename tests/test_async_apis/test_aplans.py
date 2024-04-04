""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import async_plans_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("name", "amount", "interval", "currency", "invoice_limit", "send_invoices", "send_sms", "description"),
    [
        ("Test", 10000, "annually", 'NGN', 10, True, True, "Testing"),
        ("Test", 10000, "annually", 'NGN', 10, True, True, None),
    ]
)
async def test_create_plan(async_plans_client, mocked_responses, name, amount, interval, currency, invoice_limit, send_invoices, send_sms, description):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/plan"
    response_data = {"status": "success"}
    expected_data = {
        "name": name,
        "amount": amount,
        "interval": interval,
        "description": description,
        "send_invoices": str(send_invoices),
        "send_sms": str(send_sms),
        "currency": currency,
        "invoice_limit": invoice_limit,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_plans_client.create_plan(
        name=name,
        amount=amount,
        interval=interval,
        description=description,
        send_invoices=send_invoices,
        send_sms=send_sms,
        currency=currency,
        invoice_limit=invoice_limit,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("per_page", "page", "status", "interval", "amount"),
    [
        (1, 10, "pending", "annually", 1000),
        (None, None, None, None, None)
    ]
)
async def test_list_plans(async_plans_client, mocked_responses, per_page, page, status, interval, amount):
    """ Test for synchronous Customers """
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
    query_string = '&'.join(f'{key}={value}' for key, value in url_params.items() if value is not None)
    expected_url = url + ('?' + query_string if query_string else '')

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_plans_client.list_plans(
        per_page=per_page,
        page=page,
        status=status,
        interval=interval,
        amount=amount,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_plan(async_plans_client, mocked_responses):
    """ Test for synchronous Customers """
    plan_id = "test-plan-id"
    url = f"https://api.paystack.co/plan/{plan_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_plans_client.fetch_plan(id_or_code=plan_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("name", "amount", "interval", "send_invoices", "send_sms", "currency", "invoice_limit", "description"),
    [
        ("Test", 10000, "annually", True, True, "NGN", 10, "Testing"),
        ("Test", 10000, "annually", True, True, "NGN", 10, None),
    ]
)
async def test_update_plan(async_plans_client, mocked_responses, name, amount, interval, send_invoices, send_sms, currency, invoice_limit, description):
    """ Test for synchronous Customers """
    plan_id_code = "test-plan-id-code"
    url = f"https://api.paystack.co/plan/{plan_id_code}"
    response_data = {"status": "success"}
    expected_data = {
        "name": name,
        "amount": amount,
        "interval": interval,
        "description": description,
        "send_invoices": str(send_invoices),
        "send_sms": str(send_sms),
        "currency": currency,
        "invoice_limit": invoice_limit,
    }

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_plans_client.update_plan(
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
    mocked_responses.assert_called()
    assert response is not None

