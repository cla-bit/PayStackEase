""" Tests for synchronous Bulk Charges """

import json
from datetime import date
import pytest
import responses
from paystackease import STATUS

from tests.conftest import bulk_charges_client


@pytest.mark.parametrize(
    "objects",
    [[{"authorization_code": "123456", "amount": 1000, "reference": "123456"}]],
)
@responses.activate
def test_initiate_bulk_charge(bulk_charges_client, objects):
    """
    This function tests the behavior of the initiate bulk charge method with various combinations
    of parameters,
    """
    url = "https://api.paystack.co/bulkcharge"
    response_data = {"status": "success"}

    # mock the API response
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = bulk_charges_client.initiate_bulk_charge(objects=objects)
    expected_params = [
        {"authorization_code": "123456", "amount": 1000, "reference": "123456"}
    ]
    assert len(responses.calls) == 1
    assert json.loads(responses.calls[0].request.body) == expected_params
    assert response is not None


@pytest.mark.parametrize(
    "per_page, page, from_date, to_date",
    [(10, 1, date(2024, 2, 23), date(2024, 2, 23)), (None, None, None, None)],
)
@responses.activate
def test_list_bulk_charge_batches(
    bulk_charges_client, per_page, page, from_date, to_date
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
    responses.add(
        responses.GET,
        expected_url,
        json=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected params
    response = bulk_charges_client.list_bulk_charge_batches(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response == response_data


@responses.activate
def test_fetch_bulk_charge_batch(bulk_charges_client):
    """Tests for fetch_bulk_charge_batch"""
    response_data = {"status": "success"}
    id_or_code = "test"
    url = f"https://api.paystack.co/bulkcharge/{id_or_code}"
    responses.add(
        responses.GET,
        url,
        json=response_data,
        status=200,
    )
    response = bulk_charges_client.fetch_bulk_charge_batch(id_or_code=id_or_code)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response == response_data


@pytest.mark.parametrize(
    ("status", "per_page", "page", "from_date", "to_date"),
    [
        (STATUS.SUCCESS.value, 10, 1, date(2024, 2, 23), date(2024, 2, 23)),
        (None, None, None, None, None),
    ],
)
# pylint: disable=too-many-arguments
@responses.activate
def test_fetch_charge_bulk_batch(
    bulk_charges_client, status, per_page, page, from_date, to_date
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

    responses.add(
        responses.GET,
        url,
        json=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected params
    response = bulk_charges_client.fetch_charge_bulk_batch(
        id_or_code=id_or_code,
        status=status,
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response == response_data


@responses.activate
def test_pause_bulk_charge(bulk_charges_client):
    """Tests for pause_bulk_charge"""
    response_data = {"status": "success"}
    batch_code = "test"
    url = f"https://api.paystack.co/bulkcharge/pause/{batch_code}"
    responses.add(
        responses.GET,
        url,
        json=response_data,
        status=200,
    )
    response = bulk_charges_client.pause_bulk_charge_batch(batch_code="test")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response == response_data


@responses.activate
def test_resume_bulk_charge(bulk_charges_client):
    """Tests for resume_bulk_charge"""
    response_data = {"status": "success"}
    batch_code = "test"
    url = f"https://api.paystack.co/bulkcharge/resume/{batch_code}"

    responses.add(
        responses.GET,
        url,
        json=response_data,
        status=200,
    )
    response = bulk_charges_client.resume_bulk_charge_batch(batch_code="test")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response == response_data
