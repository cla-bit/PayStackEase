""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import products_client


@pytest.mark.parametrize(
    ("name", "description", "amount", "currency", "unlimited", "quantity"),
    [
        ("Test", "Testing", 10000, "NGN", True, 10),
        ("Test", "Testing", 10000, "NGN", False, None)
    ]
)
@responses.activate
def test_create_payment_request(products_client, name, description, amount, currency, unlimited, quantity):
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
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = products_client.create_product(
        name=name,
        description=description,
        amount=amount,
        currency=currency,
        unlimited=unlimited,
        quantity=quantity
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page"),
    [
        (date(2012, 12, 12), date(2012, 12, 12), 1, 10),
        (None, None, None, None)
    ]
)
@responses.activate
def test_list_products(products_client, from_date, to_date, per_page, page):
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

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = products_client.list_products(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_fetch_payment_request(products_client):
    """ Test for synchronous Customers """
    product_id = "test-product-id"
    url = f"https://api.paystack.co/product/{product_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = products_client.fetch_product(product_id=product_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    ("name", "description", "amount", "currency", "unlimited", "quantity"),
    [
        ("Test", "Testing", 10000, "NGN", True, 10),
        ("Test", "Testing", 10000, "NGN", False, None)
    ]
)
@responses.activate
def test_update_payment_request(products_client, name, description, amount, currency, unlimited, quantity):
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

    responses.add(
        responses.PUT,
        url,
        status=200,
        json=response_data,
    )
    response = products_client.update_product(
        product_id=product_id,
        name=name,
        description=description,
        amount=amount,
        currency=currency,
        unlimited=unlimited,
        quantity=quantity
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None
