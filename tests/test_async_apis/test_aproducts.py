""" Test for synchronous Customers """

import json
from datetime import date
import pytest

from tests.conftest import async_products_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("name", "description", "amount", "currency", "unlimited", "quantity"),
    [
        ("Test", "Testing", 10000, "NGN", True, 10),
        ("Test", "Testing", 10000, "NGN", False, None)
    ]
)
async def test_create_payment_request(async_products_client, mocked_responses, name, description, amount, currency, unlimited, quantity):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/product"
    response_data = {"status": "success"}
    expected_data = {
        "name": name,
        "description": description,
        "price": amount,
        "currency": currency,
        "unlimited": str(unlimited),
        "quantity": quantity,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_products_client.create_product(
        name=name,
        description=description,
        amount=amount,
        currency=currency,
        unlimited=unlimited,
        quantity=quantity
    )
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
async def test_list_products(async_products_client, mocked_responses, from_date, to_date, per_page, page):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/product"
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
    response = await async_products_client.list_products(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_payment_request(async_products_client, mocked_responses):
    """ Test for synchronous Customers """
    product_id = "test-product-id"
    url = f"https://api.paystack.co/product/{product_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_products_client.fetch_product(product_id=product_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("name", "description", "amount", "currency", "unlimited", "quantity"),
    [
        ("Test", "Testing", 10000, "NGN", True, 10),
        ("Test", "Testing", 10000, "NGN", False, None)
    ]
)
async def test_update_payment_request(async_products_client, mocked_responses, name, description, amount, currency, unlimited, quantity):
    """ Test for synchronous Customers """
    product_id = "test-product_id"
    url = f"https://api.paystack.co/product/{product_id}"
    response_data = {"status": "success"}
    expected_data = {
        "name": name,
        "description": description,
        "price": amount,
        "currency": currency,
        "unlimited": str(unlimited),
        "quantity": quantity,
    }

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_products_client.update_product(
        product_id=product_id,
        name=name,
        description=description,
        amount=amount,
        currency=currency,
        unlimited=unlimited,
        quantity=quantity
    )
    mocked_responses.assert_called()
    assert response is not None
