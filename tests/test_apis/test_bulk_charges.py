""" Tests for synchronous Bulk Charges """

import json
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
    "per_page", "page", "from_date", "to_date", [
        (True, 1, 1),  # Testing with all parameters provided
        (False, 1, 2),  # Testing with all parameters provided
        (True, None, None),  # Testing with only use_cursor parameter provided
        (False, None, None),  # Testing with only use_cursor parameter provided
    ]
)
@responses.activate
def test_list_domains(apple_pay_client, use_cursor, next_page, previous_page):
    """
    This function tests the behavior of the list_domains method with various combinations
    of parameters, including scenarios where some parameters are None.
    """
    url = "https://api.paystack.co/apple-pay/domain"
    response_data = {"status": "success"}

    # mock the API response
    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = apple_pay_client.list_domains(use_cursor, next_page, previous_page)
    expected_params = {
        "use_cursor": str(use_cursor).lower(),
        "next": next_page,
        "previous": previous_page,
    }
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url + "?" + "&".join(
        f"{key}={value}" for key, value in expected_params.items() if value is not None
    )
    assert response is not None
