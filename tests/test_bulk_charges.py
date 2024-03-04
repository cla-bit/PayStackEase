""" Tests for paystackease.apis.apple_pay.py """

import json
import urllib.parse
from datetime import datetime

import pytest
import responses

from paystackease import STATUS
from paystackease.apis import BulkChargesClientAPI


@pytest.fixture(scope="session", name="bulk_charges_client")
@responses.activate
def bulk_charges_client_test():
    """ Fixture for BulkChargesClientAPI """
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/bulkcharge",
        json=response_data,
        status=200,
    )
    client = BulkChargesClientAPI()
    return client


@pytest.mark.parametrize(
    "objects", [{"authorization_code": "test", "amount": 100, "reference": "test"}]
)
@responses.activate
def test_initiate_bulk_charge(bulk_charges_client, objects):
    """ Test for initiate_bulk_charge """
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/bulkcharge",
        json=response_data,
        status=200,
    )
    response = bulk_charges_client.initiate_bulk_charge(objects)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == "https://api.paystack.co/bulkcharge"
    assert json.loads(responses.calls[0].request.body) == objects
    assert response == response_data


@pytest.mark.parametrize(
    "per_page, page, from_date, to_date",
    [
        (
            10,
            1,
            datetime(2024, 2, 23, 18, 23, 24, 269163),
            datetime(2024, 2, 23, 18, 23, 24, 269163),
        )
    ],
)
@responses.activate
def test_list_bulk_charge_batches(
    bulk_charges_client, per_page, page, from_date, to_date
):
    """Tests for list_bulk_charge_batches"""
    fixed_timestamp = datetime(2024, 2, 23, 18, 23, 24, 269163)
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/bulkcharge",
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
    expected_params = {
        "perPage": 10,
        "page": 1,
        "from": str(from_date.isoformat()),
        "to": str(to_date.isoformat()),
    }
    expected_url = "https://api.paystack.co/bulkcharge"
    encode_datetime = urllib.parse.quote(fixed_timestamp.isoformat())
    assert responses.calls[0].request.url == expected_url + "?" + "&".join(
        f"{key}={value}" for key, value in expected_params.items() if value is not None
    ).replace(fixed_timestamp.isoformat(), encode_datetime)
    assert response == response_data


@responses.activate
def test_fetch_bulk_charge_batch(bulk_charges_client):
    """Tests for fetch_bulk_charge_batch"""
    response_data = {"status": "success"}
    id_or_code = "test"
    responses.add(
        responses.GET,
        f"https://api.paystack.co/bulkcharge/{id_or_code}",
        json=response_data,
        status=200,
    )
    response = bulk_charges_client.fetch_bulk_charge_batch(id_or_code=id_or_code)
    assert len(responses.calls) == 1
    assert (
        responses.calls[0].request.url
        == f"https://api.paystack.co/bulkcharge/{id_or_code}"
    )
    assert response == response_data


@pytest.mark.parametrize(
    "id_or_code, status, per_page, page, from_date, to_date",
    [
        (
            "test",
            STATUS.SUCCESS.value,
            10,
            1,
            datetime(2024, 2, 23, 18, 23, 24, 269163),
            datetime(2024, 2, 23, 18, 23, 24, 269163),
        )
    ],
)
# pylint: disable=too-many-arguments
@responses.activate
def test_fetch_charge_bulk_batch(
    bulk_charges_client, id_or_code, status, per_page, page, from_date, to_date
):
    """Tests for fetch_charge_bulk_batch"""
    fixed_timestamp = datetime(2024, 2, 23, 18, 23, 24, 269163)
    response_data = {"status": "success"}
    # id_or_code = "test"
    responses.add(
        responses.GET,
        f"https://api.paystack.co/bulkcharge/{id_or_code}/charges",
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
    expected_params = {
        "status": status,
        "perPage": per_page,
        "page": page,
        "from": str(from_date.isoformat()),
        "to": str(to_date.isoformat()),
    }
    expected_url = "https://api.paystack.co/bulkcharge"
    encode_datetime = urllib.parse.quote(fixed_timestamp.isoformat())
    assert len(responses.calls) == 1
    assert responses.calls[
        0
    ].request.url == f"{expected_url}/{id_or_code}/charges?" + "&".join(
        f"{key}={value}" for key, value in expected_params.items() if value is not None
    ).replace(
        fixed_timestamp.isoformat(), encode_datetime
    )
    assert response == response_data


@responses.activate
def test_pause_bulk_charge(bulk_charges_client):
    """Tests for pause_bulk_charge"""
    response_data = {"status": "success"}
    batch_code = "test"
    responses.add(
        responses.GET,
        f"https://api.paystack.co/bulkcharge/pause/{batch_code}",
        json=response_data,
        status=200,
    )
    response = bulk_charges_client.pause_bulk_charge_batch(batch_code="test")
    assert len(responses.calls) == 1
    assert (
        responses.calls[0].request.url
        == f"https://api.paystack.co/bulkcharge/pause/{batch_code}"
    )
    assert response == response_data


@responses.activate
def test_resume_bulk_charge(bulk_charges_client):
    """Tests for resume_bulk_charge"""
    response_data = {"status": "success"}
    batch_code = "test"
    responses.add(
        responses.GET,
        f"https://api.paystack.co/bulkcharge/resume/{batch_code}",
        json=response_data,
        status=200,
    )
    response = bulk_charges_client.resume_bulk_charge_batch(batch_code="test")
    assert len(responses.calls) == 1
    assert (
        responses.calls[0].request.url
        == f"https://api.paystack.co/bulkcharge/resume/{batch_code}"
    )
    assert response == response_data
