""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import async_subaccounts_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("business_name", "settlement_bank", "account_number", "percent_charge", "description", "primary_contact_email", "primary_contact_name", "primary_contact_phone", "metadata"),
    [
        ("Test", "053", "0000000000", 0.5, "Testing", "testing_email.com", "Testing Primary Name", "80812345678", {"custom_fields": [{"name": "value"}]}),
        ("Test", "053", "0000000000", 0.5, "Testing", None, None, None, None),
    ]
)
async def test_create_subaccount(async_subaccounts_client, mocked_responses, business_name, settlement_bank, account_number, percent_charge, description, primary_contact_email, primary_contact_name, primary_contact_phone, metadata):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/subaccount"
    response_data = {"status": "success"}
    expected_data = {
        "business_name": business_name,
        "settlement_bank": settlement_bank,
        "account_number": account_number,
        "percentage_charge": percent_charge,
        "description": description,
        "primary_contact_email": primary_contact_email,
        "primary_contact_name": primary_contact_name,
        "primary_contact_phone": primary_contact_phone,
        "metadata": metadata,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_subaccounts_client.create_subaccount(
        business_name=business_name,
        settlement_bank=settlement_bank,
        account_number=account_number,
        percentage_charge=percent_charge,
        description=description,
        primary_contact_email=primary_contact_email,
        primary_contact_name=primary_contact_name,
        primary_contact_phone=primary_contact_phone,
        metadata=metadata
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
async def test_list_subaccount(async_subaccounts_client, mocked_responses, from_date, to_date, per_page, page):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/subaccount"
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
    response = await async_subaccounts_client.list_subaccounts(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_subaccount(async_subaccounts_client, mocked_responses):
    """ Test for synchronous Customers """
    subaccount_id = "test-subaccoutn-id"
    url = f"https://api.paystack.co/subaccount/{subaccount_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_subaccounts_client.fetch_subaccount(id_or_code=subaccount_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("business_name", "settlement_bank", "account_number", "active", "percent_charge", "description", "primary_contact_email", "primary_contact_name", "primary_contact_phone", "settlement_schedule", "metadata"),
    [
        ("Test", "053", "0000000000", True, 0.5, "Testing", "testing_email.com", "Testing Primary Name", "80812345678", "weekly", {"custom_fields": [{"name": "value"}]}),
        ("Test", "053", "0000000000", True, None, None, None, None, None, None, None),
    ]
)
async def test_update_subaccount(async_subaccounts_client, mocked_responses, business_name, settlement_bank, account_number, active, percent_charge, description, primary_contact_email, primary_contact_name, primary_contact_phone, settlement_schedule, metadata):
    """ Test for synchronous Customers """
    subaccount_id = "test-subaccount_id"
    url = f"https://api.paystack.co/subaccount/{subaccount_id}"
    response_data = {"status": "success"}
    expected_data = {
        "business_name": business_name,
        "settlement_bank": settlement_bank,
        "account_number": account_number,
        "active": str(active).lower(),
        "percentage_charge": percent_charge,
        "description": description,
        "primary_contact_email": primary_contact_email,
        "primary_contact_name": primary_contact_name,
        "primary_contact_phone": primary_contact_phone,
        "settlement_schedule": settlement_schedule,
        "metadata": metadata,
    }

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_subaccounts_client.update_subaccount(
        id_or_code=subaccount_id,
        business_name=business_name,
        settlement_bank=settlement_bank,
        account_number=account_number,
        active=active,
        percentage_charge=percent_charge,
        description=description,
        primary_contact_email=primary_contact_email,
        primary_contact_name=primary_contact_name,
        primary_contact_phone=primary_contact_phone,
        settlement_schedule=settlement_schedule,
        metadata=metadata
    )
    mocked_responses.assert_called()
    assert response is not None
