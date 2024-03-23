""" Tests for synchronous Bulk Charges """

import json
import urllib.parse
from datetime import date
import pytest
import responses
from tests.conftest import bulk_charges_client


@pytest.mark.parametrize(
    "objects", [
        [{"authorization_code": "123456", "amount": 1000, "reference": "123456"}]
    ]
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
    expected_params = [{"authorization_code": "123456", "amount": 1000, "reference": "123456"}]
    assert len(responses.calls) == 1
    assert json.loads(responses.calls[0].request.body) == expected_params
    assert response is not None


@pytest.mark.parametrize(
    "per_page, page, from_date, to_date",
    [
        (
            10,
            1,
            date(2024, 2, 23),
            date(2024, 2, 23),
        )
    ],
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
    expected_url = f"{url}?{'&'.join(f'{key}={value}' for key, value in url_params.items() if value is not None)}"

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
