""" Test for synchronous Customers """

import json
from datetime import date
import pytest

from tests.conftest import async_payment_pages_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("name", "description", "amount", "split_code", "page_slug", "redirect_url", "metadata", "custom_fields"),
    [
        ("test-page", "Testing", 1000, "SPLIT_test1234", "test-page-slug", "http://test-redirect.com", {"page_nickname": "tester_page"}, ["test-any-other"]),
        ("test-page", None, None, None, None, None, None, None),
    ]
)
async def test_create_payment_page(async_payment_pages_client, mocked_responses, name, description, amount, split_code, page_slug, redirect_url, metadata, custom_fields):
    """ Test for synchronous Customers """
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
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_pages_client.create_payment_page(
        name=name,
        description=description,
        amount=amount,
        split_code=split_code,
        page_slug=page_slug,
        redirect_url=redirect_url,
        metadata=metadata,
        custom_fields=custom_fields,
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
async def test_list_pages(async_payment_pages_client, mocked_responses, from_date, to_date, per_page, page):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/page"
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
    response = await async_payment_pages_client.list_payment_pages(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_list_pages(async_payment_pages_client, mocked_responses):
    """ Test for synchronous Customers """
    id_or_slug = 'payment_pages'
    url = f"https://api.paystack.co/page/{id_or_slug}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_pages_client.fetch_payment_page(page_id_or_slug=id_or_slug)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("name", "description", "amount", "active"),
    [
        ("test-page", "Testing", 1000, True),
        (None, None, None, True),
    ]
)
async def test_update_page(async_payment_pages_client, mocked_responses, name, description, amount, active):
    """ Test for synchronous Customers """
    page_id_slug = "test-page-id"
    url = f"https://api.paystack.co/page/{page_id_slug}"
    response_data = {"status": "success"}
    expected_data = {
        "name": name,
        "description": description,
        "amount": amount,
        "active": str(active).lower(),
    }

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_pages_client.update_payment_page(
        page_id_or_slug=page_id_slug,
        name=name,
        description=description,
        amount=amount,
        active=active,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_check_slug(async_payment_pages_client, mocked_responses):
    """ Test for synchronous Customers """
    id_or_slug = 'payment_pages'
    url = f"https://api.paystack.co/page/check_slug_availability/{id_or_slug}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_pages_client.check_slug_available(page_slug=id_or_slug)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(("products",), [([12]), ([112])])
async def test_check_slug(async_payment_pages_client,mocked_responses, products):
    """ Test for synchronous Customers """
    payment_id = 12
    url = f"https://api.paystack.co/page/{payment_id}/product"
    response_data = {"status": "success"}

    expected_data = {"product": products}

    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_payment_pages_client.add_products(payment_id=payment_id, product=products)
    mocked_responses.assert_called()
    assert response is not None
