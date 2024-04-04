""" Tests for asynchronous Bulk Charges """

import json
import pytest
from datetime import date

from tests.conftest import async_bulk_charges_client, mocked_responses
from paystackease import STATUS


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "objects",
    [[{"authorization_code": "123456", "amount": 1000, "reference": "123456"}]],
)
async def test_initialize_bulk_charges(
    async_bulk_charges_client, mocked_responses, objects
):
    """
    This function tests the behavior of the initialize_bulk_charges method
    """
    url = "https://api.paystack.co/bulkcharge"
    expected_data = [
        {"authorization_code": "123456", "amount": 1000, "reference": "123456"}
    ]

    # mock the API response
    mocked_responses.post(url, status=200, payload=expected_data)
    response = await async_bulk_charges_client.initiate_bulk_charge(objects=objects)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("per_page", "page", "from_date", "to_date"),
    [
        (10, 1, date(2024, 2, 23), date(2024, 2, 23)),
        (None, None, None, None),
    ],
)
async def test_list_bulk_charge_batches(
    async_bulk_charges_client, mocked_responses, per_page, page, from_date, to_date
):
    """Tests for list_bulk_charge_batches"""
    url = "https://api.paystack.co/bulkcharge"
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

    # mock the API response
    mocked_responses.get(
        expected_url,
        payload=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected params
    response = await async_bulk_charges_client.list_bulk_charge_batches(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_bulk_charge_batch(async_bulk_charges_client, mocked_responses):
    """Tests for fetch_bulk_charge_batch"""
    response_data = {"status": "success"}
    id_or_code = "test"
    url = f"https://api.paystack.co/bulkcharge/{id_or_code}"
    mocked_responses.get(
        url,
        payload=response_data,
        status=200,
    )
    response = await async_bulk_charges_client.fetch_bulk_charge_batch(
        id_or_code=id_or_code
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("status", "per_page", "page", "from_date", "to_date"),
    [
        (STATUS.SUCCESS.value, 10, 1, date(2024, 2, 23), date(2024, 2, 23)),
        (None, None, None, None, None),
    ],
)
async def test_fetch_charge_bulk_batch(
    async_bulk_charges_client,
    mocked_responses,
    status,
    per_page,
    page,
    from_date,
    to_date,
):
    """Tests for fetch_charge_bulk_batch"""
    response_data = {"status": "success"}
    id_or_code = "test"
    url = f"https://api.paystack.co/bulkcharge/{id_or_code}/charges"
    url_params = {
        "status": status,
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

    mocked_responses.get(
        expected_url,
        payload=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected params
    response = await async_bulk_charges_client.fetch_charge_bulk_batch(
        id_or_code=id_or_code,
        status=status,
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_pause_bulk_charge(async_bulk_charges_client, mocked_responses):
    """Tests for pause_bulk_charge"""
    response_data = {"status": "success"}
    batch_code = "test"
    url = f"https://api.paystack.co/bulkcharge/pause/{batch_code}"
    mocked_responses.get(
        url,
        payload=response_data,
        status=200,
    )
    response = await async_bulk_charges_client.pause_bulk_charge_batch(
        batch_code="test"
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_resume_bulk_charge(async_bulk_charges_client, mocked_responses):
    """Tests for resume_bulk_charge"""
    response_data = {"status": "success"}
    batch_code = "test"
    url = f"https://api.paystack.co/bulkcharge/resume/{batch_code}"

    mocked_responses.get(
        url,
        payload=response_data,
        status=200,
    )
    response = await async_bulk_charges_client.resume_bulk_charge_batch(
        batch_code="test"
    )
    mocked_responses.assert_called()
    assert response is not None
