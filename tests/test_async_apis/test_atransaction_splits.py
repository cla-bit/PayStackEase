""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import async_transaction_splits_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("transaction_split_name", "transaction_split_type", "currency", "subaccounts", "bearer_type", "bearer_subaccount"),
    [
        ("Test-split-name", "flat", "NGN", [{"subaccount": "ACT_xxxxxxxxxx", "share": 0.5}], "account", "SUBACCT_test1234"),
        ("Test-split-name", "percentage", "NGN", [{"subaccount": "ACT_xxxxxxxxxx", "share": 0.5}], "account", "SUBACCT_test1234"),
    ]
)
async def test_create_split(async_transaction_splits_client, mocked_responses, transaction_split_name, transaction_split_type, currency, subaccounts, bearer_type, bearer_subaccount):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/split"
    response_data = {"status": "success"}
    expected_data = {
        "name": transaction_split_name,
        "type": transaction_split_type,
        "currency": currency,
        "subaccounts": subaccounts,
        "bearer_type": bearer_type,
        "bearer_subaccount": bearer_subaccount,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transaction_splits_client.create_split(
        transaction_split_name=transaction_split_name,
        transaction_split_type=transaction_split_type,
        currency=currency,
        subaccounts=subaccounts,
        bearer_type=bearer_type,
        bearer_subaccount=bearer_subaccount,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("subaccount", "transaction_share"),
    [
        ("SUBACCT_test1234", 60),
        ("SUBACCT_test1234test", 80),
    ]
)
async def test_add_or_update_split(async_transaction_splits_client, mocked_responses, subaccount, transaction_share):
    """ Test for synchronous Customers """
    split_id = "test-split-id"
    url = f"https://api.paystack.co/split/{split_id}/subaccount/add"
    response_data = {"status": "success"}
    expected_data = {"subaccount": subaccount, "share": transaction_share}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transaction_splits_client.add_or_update_subaccount_split(
        split_id=split_id,
        subaccount=subaccount,
        transaction_share=transaction_share,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(("subaccount",), [("SUBACCT_test1234",), ("SUBACCT_test1234test",)])
async def test_remove_subaccount_split(async_transaction_splits_client, mocked_responses, subaccount):
    """ Test for synchronous Customers """
    split_id = "test-split-id"
    url = f"https://api.paystack.co/split/{split_id}/subaccount/remove"
    response_data = {"status": "success"}
    expected_data = {"subaccount": subaccount}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transaction_splits_client.remove_sub_account_split(
        split_id=split_id,
        subaccount=subaccount,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("split_name", "active", "sort_by", "from_date", "to_date", "per_page", "page"),
    [
        ("SPLIT_test1234", True, "active", date(2012, 12, 12), date(2012, 12, 12), 1, 10),
        (None, True, None, None, None, None, None)
    ]
)
async def test_list_transaction_splits(async_transaction_splits_client, mocked_responses, split_name, active, sort_by, from_date, to_date, per_page, page):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/split"
    response_data = {"status": "success"}
    url_params = {
        "name": split_name,
        "active": str(active),
        "sort_by": sort_by,
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
    response = await async_transaction_splits_client.list_split(
        split_name=split_name,
        active=active,
        sort_by=sort_by,
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_split(async_transaction_splits_client, mocked_responses):
    """ Test for synchronous Customers """
    split_id = "test-split-id"
    url = f"https://api.paystack.co/split/{split_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transaction_splits_client.fetch_split(split_id=split_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("transaction_split_name", "active", "bearer_type", "bearer_subaccount"),
    [
        ("Test-split-name", True, "account", "SUBACCT_test1234"),
    ]
)
async def test_update_split(async_transaction_splits_client, mocked_responses, transaction_split_name, active, bearer_type, bearer_subaccount):
    """ Test for synchronous Customers """
    split_id = "test-split_id"
    url = f"https://api.paystack.co/split/{split_id}"
    response_data = {"status": "success"}
    expected_data = {
        "name": transaction_split_name,
        "active": str(active),
        "bearer_type": bearer_type,
        "bearer_subaccount": bearer_subaccount,
    }

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_transaction_splits_client.update_split(
        split_id=split_id,
        transaction_split_name=transaction_split_name,
        active=active,
        bearer_type=bearer_type,
        bearer_subaccount=bearer_subaccount,
    )
    mocked_responses.assert_called()
    assert response is not None
