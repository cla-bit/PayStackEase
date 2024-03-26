""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import async_payment_requests_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("customer", "amount", "draft", "has_invoice", "send_notification", "due_date", "description", "line_items", "tax", "currency", "invoice_number", "split_code"),
    [
        ("Test", 10000, True, True, True, date(2012, 12, 12), "Testing",
         [{"name":"item 1", "amount":2000, "quantity": 1}], [{"name":"VAT", "amount":200}], "NGN", 1234, "SPLIT_test1234"),
        ("Test", 10000, True, True, True, None, None, None, None, None, None, None)
    ]
)
async def test_create_payment_request(async_payment_requests_client, mocked_responses, customer, amount, draft, has_invoice, send_notification, due_date, description,
                      line_items, tax, currency, invoice_number, split_code):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/paymentrequest"
    response_data = {"status": "success"}
    expected_data = {
        "customer": customer,
        "amount": amount,
        "due_date": due_date.strftime("%Y-%m-%d") if due_date else None,
        "description": description,
        "line_items": line_items,
        "tax": tax,
        "currency": currency,
        "send_notification": send_notification,
        "draft": draft,
        "has_invoice": has_invoice,
        "invoice_number": invoice_number,
        "split_code": split_code,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_requests_client.create_payment_request(
        customer=customer,
        amount=amount,
        draft=draft,
        has_invoice=has_invoice,
        send_notification=send_notification,
        due_date=due_date,
        description=description,
        line_items=line_items,
        tax=tax,
        currency=currency,
        invoice_number=invoice_number,
        split_code=split_code
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page", "customer", "status", "currency", "include_archive"),
    [
        (date(2012, 12, 12), date(2012, 12, 12), 1, 10, "Test", "pending", "NGN", "True"),
        (None, None, None, None, None, None, None, None)
    ]
)
async def test_list_payment_requests(async_payment_requests_client, mocked_responses, from_date, to_date, per_page, page, customer, status, currency, include_archive):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/paymentrequest"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "customer": customer,
        "status": status,
        "currency": currency,
        "include_archive": include_archive,
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
    response = await async_payment_requests_client.list_payment_requests(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
        customer=customer,
        status=status,
        currency=currency,
        include_archive=include_archive
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_payment_request(async_payment_requests_client, mocked_responses):
    """ Test for synchronous Customers """
    payment_id = "test-payment-id"
    url = f"https://api.paystack.co/paymentrequest/{payment_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_requests_client.fetch_payment_request(id_or_code=payment_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_verify_payment(async_payment_requests_client, mocked_responses):
    """ Test for synchronous Customers """
    payment_code = "test-payment-code"
    url = f"https://api.paystack.co/paymentrequest/verify/{payment_code}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_requests_client.verify_payment_request(code=payment_code)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_send_notification(async_payment_requests_client, mocked_responses):
    """ Test for synchronous Customers """
    payment_code = "test-payment-code"
    url = f"https://api.paystack.co/paymentrequest/notify/{payment_code}"
    response_data = {"status": "success"}

    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_requests_client.send_notification(code=payment_code)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_request_totals(async_payment_requests_client, mocked_responses):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/paymentrequest/totals"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_requests_client.payment_request_total()
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(("notice",), [(True,), (False,)])
async def test_finalize_payment(async_payment_requests_client, mocked_responses, notice):
    """ Test for synchronous Customers """
    payment_code = "test-payment-code"
    url = f"https://api.paystack.co/paymentrequest/finalize/{payment_code}"
    response_data = {"status": "success"}
    expected_data = {"send_notification": notice}

    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_requests_client.finalize_payment_request(code=payment_code, send_notification=notice)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("customer", "amount", "draft", "send_notification", "due_date", "description", "line_items", "tax", "currency", "invoice_number", "split_code"),
    [
        ("Test", 10000, True, True, date(2012, 12, 12), "Testing",
         [{"name":"item 1", "amount":2000, "quantity": 1}], [{"name":"VAT", "amount":200}], "NGN", 1234, "SPLIT_test1234"),
        ("Test", 10000, True, True, None, None, None, None, None, None, None),
        (None, None, True, True, None, None, None, None, None, None, None)
    ]
)
async def test_update_payment_request(async_payment_requests_client, mocked_responses, customer, amount, draft, send_notification, due_date, description, line_items,
                                tax, currency, invoice_number, split_code):
    """ Test for synchronous Customers """
    payment_id_code = "test-payment-id-code"
    url = f"https://api.paystack.co/paymentrequest/{payment_id_code}"
    response_data = {"status": "success"}
    expected_data = {
        "customer": customer,
        "amount": amount,
        "due_date": due_date.strftime("%Y-%m-%d") if due_date else None,
        "description": description,
        "line_items": line_items,
        "tax": tax,
        "currency": currency,
        "send_notification": send_notification,
        "draft": draft,
        "invoice_number": invoice_number,
        "split_code": split_code,
    }

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_requests_client.update_payment_request(
        id_or_code=payment_id_code,
        customer=customer,
        amount=amount,
        due_date=due_date,
        description=description,
        line_items=line_items,
        tax=tax,
        currency=currency,
        send_notification=send_notification,
        draft=draft,
        invoice_number=invoice_number,
        split_code=split_code
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_archive_request(async_payment_requests_client, mocked_responses):
    """ Test for synchronous Customers """
    payment_code = "test-payment_code"
    url = f"https://api.paystack.co/paymentrequest/archive/{payment_code}"
    response_data = {"status": "success"}

    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_requests_client.archive_payment_request(code=payment_code)
    mocked_responses.assert_called()
    assert response is not None
