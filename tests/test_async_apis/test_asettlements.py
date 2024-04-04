""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses
from paystackease.helpers.tool_kit import STATUS
from tests.conftest import async_settlements_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("status", "subaccounts", "from_date", "to_date", "per_page", "page"),
    [
        (
            STATUS.FAILED.value,
            "SUB_ACCT_testing1234",
            date(2012, 12, 12),
            date(2012, 12, 12),
            1,
            10,
        ),
        (None, None, None, None, None, None),
    ],
)
async def test_list_settlement(
    async_settlements_client,
    mocked_responses,
    status,
    subaccounts,
    from_date,
    to_date,
    per_page,
    page,
):
    """Test for synchronous Customers"""
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
    query_string = "&".join(
        f"{key}={value}" for key, value in url_params.items() if value is not None
    )
    expected_url = url + ("?" + query_string if query_string else "")

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_settlements_client.list_settlements(
        per_page=per_page,
        page=page,
        status=status,
        subaccount=subaccounts,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page"),
    [(date(2012, 12, 12), date(2012, 12, 12), 1, 10), (None, None, None, None)],
)
async def test_list_settlement_trans(
    async_settlements_client, mocked_responses, from_date, to_date, per_page, page
):
    """Test for synchronous Customers"""
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
    query_string = "&".join(
        f"{key}={value}" for key, value in url_params.items() if value is not None
    )
    expected_url = url + ("?" + query_string if query_string else "")

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_settlements_client.list_settlement_transactions(
        settlement_id=settlement_id,
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None
