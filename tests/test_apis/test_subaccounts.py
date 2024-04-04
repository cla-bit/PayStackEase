""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import subaccounts_client


@pytest.mark.parametrize(
    (
        "business_name",
        "settlement_bank",
        "account_number",
        "percent_charge",
        "description",
        "primary_contact_email",
        "primary_contact_name",
        "primary_contact_phone",
        "metadata",
    ),
    [
        (
            "Test",
            "053",
            "0000000000",
            0.5,
            "Testing",
            "testing_email.com",
            "Testing Primary Name",
            "80812345678",
            {"custom_fields": [{"name": "value"}]},
        ),
        ("Test", "053", "0000000000", 0.5, "Testing", None, None, None, None),
    ],
)
@responses.activate
def test_create_subaccount(
    subaccounts_client,
    business_name,
    settlement_bank,
    account_number,
    percent_charge,
    description,
    primary_contact_email,
    primary_contact_name,
    primary_contact_phone,
    metadata,
):
    """Test for synchronous Customers"""
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
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = subaccounts_client.create_subaccount(
        business_name=business_name,
        settlement_bank=settlement_bank,
        account_number=account_number,
        percentage_charge=percent_charge,
        description=description,
        primary_contact_email=primary_contact_email,
        primary_contact_name=primary_contact_name,
        primary_contact_phone=primary_contact_phone,
        metadata=metadata,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page"),
    [(date(2012, 12, 12), date(2012, 12, 12), 1, 10), (None, None, None, None)],
)
@responses.activate
def test_list_subaccount(subaccounts_client, from_date, to_date, per_page, page):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/subaccount"
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

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = subaccounts_client.list_subaccounts(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_fetch_subaccount(subaccounts_client):
    """Test for synchronous Customers"""
    subaccount_id = "test-subaccoutn-id"
    url = f"https://api.paystack.co/subaccount/{subaccount_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = subaccounts_client.fetch_subaccount(id_or_code=subaccount_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    (
        "business_name",
        "settlement_bank",
        "account_number",
        "active",
        "percent_charge",
        "description",
        "primary_contact_email",
        "primary_contact_name",
        "primary_contact_phone",
        "settlement_schedule",
        "metadata",
    ),
    [
        (
            "Test",
            "053",
            "0000000000",
            True,
            0.5,
            "Testing",
            "testing_email.com",
            "Testing Primary Name",
            "80812345678",
            "weekly",
            {"custom_fields": [{"name": "value"}]},
        ),
        ("Test", "053", "0000000000", True, None, None, None, None, None, None, None),
    ],
)
@responses.activate
def test_update_subaccount(
    subaccounts_client,
    business_name,
    settlement_bank,
    account_number,
    active,
    percent_charge,
    description,
    primary_contact_email,
    primary_contact_name,
    primary_contact_phone,
    settlement_schedule,
    metadata,
):
    """Test for synchronous Customers"""
    subaccount_id = "test-subaccount_id"
    url = f"https://api.paystack.co/subaccount/{subaccount_id}"
    response_data = {"status": "success"}
    expected_data = {
        "business_name": business_name,
        "settlement_bank": settlement_bank,
        "account_number": account_number,
        "active": str(active),
        "percentage_charge": percent_charge,
        "description": description,
        "primary_contact_email": primary_contact_email,
        "primary_contact_name": primary_contact_name,
        "primary_contact_phone": primary_contact_phone,
        "settlement_schedule": settlement_schedule,
        "metadata": metadata,
    }

    responses.add(
        responses.PUT,
        url,
        status=200,
        json=response_data,
    )
    response = subaccounts_client.update_subaccount(
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
        metadata=metadata,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None
