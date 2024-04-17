""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import payment_pages_client


@pytest.mark.parametrize(
    (
        "name",
        "description",
        "amount",
        "split_code",
        "page_slug",
        "redirect_url",
        "metadata",
        "custom_fields",
    ),
    [
        (
            "test-page",
            "Testing",
            1000,
            "SPLIT_test1234",
            "test-page-slug",
            "http://test-redirect.com",
            {"page_nickname": "tester_page"},
            [{"page_nickname": "tester_page"}],
        ),
        ("test-page", None, None, None, None, None, None, None),
    ],
)
@responses.activate
def test_create_payment_page(
    payment_pages_client,
    name,
    description,
    amount,
    split_code,
    page_slug,
    redirect_url,
    metadata,
    custom_fields,
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/page"
    response_data = {"status": "success"}
    expected_data = {
        "name": name,
        "description": description,
        "amount": amount,
        "split_code": split_code,
        "slug": page_slug,
        "redirect_url": redirect_url,
        "metadata": metadata,
        "custom_fields": custom_fields,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = payment_pages_client.create_payment_page(
        name=name,
        description=description,
        amount=amount,
        split_code=split_code,
        page_slug=page_slug,
        redirect_url=redirect_url,
        metadata=metadata,
        custom_fields=custom_fields,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page"),
    [(date(2012, 12, 12), date(2012, 12, 12), 1, 10), (None, None, None, None)],
)
@responses.activate
def test_list_pages(payment_pages_client, from_date, to_date, per_page, page):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/page"
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
    response = payment_pages_client.list_payment_pages(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response.status == "success"


@responses.activate
def test_list_pages(payment_pages_client):
    """Test for synchronous Customers"""
    id_or_slug = "payment_pages"
    url = f"https://api.paystack.co/page/{id_or_slug}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = payment_pages_client.fetch_payment_page(page_id_or_slug=id_or_slug)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response.status == "success"


@pytest.mark.parametrize(
    ("name", "description", "amount", "active"),
    [
        ("test-page", "Testing", 1000, True),
        (None, None, None, True),
    ],
)
@responses.activate
def test_update_page(payment_pages_client, name, description, amount, active):
    """Test for synchronous Customers"""
    page_id_slug = "test-page-id"
    url = f"https://api.paystack.co/page/{page_id_slug}"
    response_data = {"status": "success"}
    expected_data = {
        "name": name,
        "description": description,
        "amount": amount,
        "active": str(active),
    }

    responses.add(
        responses.PUT,
        url,
        status=200,
        json=response_data,
    )
    response = payment_pages_client.update_payment_page(
        page_id_or_slug=page_id_slug,
        name=name,
        description=description,
        amount=amount,
        active=active,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_check_slug(payment_pages_client):
    """Test for synchronous Customers"""
    id_or_slug = "payment_pages"
    url = f"https://api.paystack.co/page/check_slug_availability/{id_or_slug}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = payment_pages_client.check_slug_available(page_slug=id_or_slug)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response.status == "success"


@pytest.mark.parametrize(("products",), [([12]), ([112])])
@responses.activate
def test_check_slug(payment_pages_client, products):
    """Test for synchronous Customers"""
    payment_id = 12
    url = f"https://api.paystack.co/page/{payment_id}/product"
    response_data = {"status": "success"}

    expected_data = {"product": products}

    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = payment_pages_client.add_products(
        payment_id=payment_id, product=products
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None
