""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import async_verification_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("account_number", "bank_code"),
    [
        ("0000000000", "053"),
    ],
)
async def test_resolve_account(
    async_verification_client, mocked_responses, account_number, bank_code
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/bank/resolve"
    response_data = {"status": "success"}
    url_params = {"account_number": account_number, "bank_code": bank_code}
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
    response = await async_verification_client.resolve_account(
        account_number=account_number, bank_code=bank_code
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_resolve_card(async_verification_client, mocked_responses):
    """Test for synchronous Customers"""
    bin_code = "test-bin-code"
    url = f"https://api.paystack.co/decision/bin/{bin_code}"
    response_data = {"status": "success"}
    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_verification_client.resolve_card_bin(bin_code=bin_code)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    (
        "account_name",
        "account_number",
        "account_type",
        "bank_code",
        "country_code",
        "document_type",
        "document_number",
    ),
    [
        (
            "Test Account",
            "0000000000",
            "personal",
            "053",
            "NGN",
            "identityNumber",
            "RDF1234TEST",
        )
    ],
)
async def test_validate_account(
    async_verification_client,
    mocked_responses,
    account_name,
    account_number,
    account_type,
    bank_code,
    country_code,
    document_type,
    document_number,
):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/bank/validate"
    response_data = {"status": "success"}
    expected_data = {
        "account_name": account_name,
        "account_number": account_number,
        "account_type": account_type,
        "bank_code": bank_code,
        "country_code": country_code,
        "document_type": document_type,
        "document_number": document_number,
    }

    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_verification_client.validate_account(
        account_name=account_name,
        account_number=account_number,
        account_type=account_type,
        bank_code=bank_code,
        country_code=country_code,
        document_type=document_type,
        document_number=document_number,
    )
    mocked_responses.assert_called()
    assert response is not None
