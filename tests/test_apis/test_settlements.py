""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses
from paystackease.helpers.tool_kit import STATUS
from tests.conftest import settlements_client


@pytest.mark.parametrize(
    ("status", "subaccounts", "from_date", "to_date", "per_page", "page"),
    [
        (STATUS.PENDING.value, "SUB_ACCT_testing1234", date(2012, 12, 12), date(2012, 12, 12), 1, 10),
        (None, None, None, None, None, None)
    ]
)
@responses.activate
def test_list_settlement(settlements_client, status, subaccounts, from_date, to_date, per_page, page):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/settlement"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "status": status,
        "subaccount": subaccounts,
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
    response = settlements_client.list_settlements(
        per_page=per_page,
        page=page,
        status=status,
        subaccount=subaccounts,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page"),
    [
        (date(2012, 12, 12), date(2012, 12, 12), 1, 10),
        (None, None, None, None)
    ]
)
@responses.activate
def test_list_settlement_trans(settlements_client, from_date, to_date, per_page, page):
    """ Test for synchronous Customers """
    settlement_id = "testing_id"
    url = f"https://api.paystack.co/settlement/{settlement_id}/transactions"
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
    response = settlements_client.list_settlement_transactions(
        settlement_id=settlement_id,
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None
