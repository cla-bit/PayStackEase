""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import verification_client


@pytest.mark.parametrize(
    ("account_number", "bank_code"),
    [
        ("0000000000", "053"),
    ],
)
@responses.activate
def test_resolve_account(verification_client, account_number, bank_code):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/bank/resolve"
    response_data = {"status": "success"}
    url_params = {"account_number": account_number, "bank_code": bank_code}
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
    response = verification_client.resolve_account(
        account_number=account_number, bank_code=bank_code
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_resolve_card(verification_client):
    """Test for synchronous Customers"""
    bin_code = "test-bin-code"
    url = f"https://api.paystack.co/decision/bin/{bin_code}"
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = verification_client.resolve_card_bin(bin_code=bin_code)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


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
@responses.activate
def test_validate_account(
    verification_client,
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

    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = verification_client.validate_account(
        account_name=account_name,
        account_number=account_number,
        account_type=account_type,
        bank_code=bank_code,
        country_code=country_code,
        document_type=document_type,
        document_number=document_number,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None
