""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import dva_client


@pytest.mark.parametrize(
    ("customer_id_or_code", "preferred_bank", "subaccount",
     "split_code", "first_name", "last_name", "phone"),
    [
        ("test_id_code", None, None, None, None, None, None),
        ("test_id_code", "test-wema-bank", "SUB_test123", "SPLIT_test123", "test-first-name", "test-last-name", "08012345678")
    ]
)
@responses.activate
def test_create_virtual_account(dva_client, customer_id_or_code, preferred_bank, subaccount, split_code, first_name, last_name, phone):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/dedicated_account"
    response_data = {"status": "success"}
    expected_data = {
        "customer": customer_id_or_code,
        "preferred_bank": preferred_bank,
        "subaccount": subaccount,
        "split_code": split_code,
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = dva_client.create_virtual_account(
        customer_id_or_code=customer_id_or_code,
        preferred_bank=preferred_bank,
        subaccount=subaccount,
        split_code=split_code,
        first_name=first_name,
        last_name=last_name,
        phone=phone
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("email", "first_name", "last_name", "phone", "preferred_bank",
     "country", "account_number", "bvn", "bank_code", "subaccount", "split_code"),
    [
        ("test@email.com", "test", "test", "08012345678", "test-wema-bank",
         "NGN", "0000000000", "1234565789", "737", "SUB_test1234", "SPLIT_1234test"),
        ("test@email.com", "test", "test", "08012345678", "test-wema-bank", "NGN",
         None, None, None, None, None)

    ]
)
@responses.activate
def test_assign_dvs(dva_client, email, first_name, last_name, phone,
                    preferred_bank, country, account_number, bvn, bank_code,
                    subaccount, split_code):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/dedicated_account"
    response_data = {"status": "success"}
    expected_data = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "preferred_bank": preferred_bank,
        "country": country,
        "account_number": account_number,
        "bvn": bvn,
        "bank_code": bank_code,
        "subaccount": subaccount,
        "split_code": split_code,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = dva_client.assign_dedicated_virtual_account(
        email=email,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        preferred_bank=preferred_bank,
        country=country,
        account_number=account_number,
        bvn=bvn,
        bank_code=bank_code,
        subaccount=subaccount,
        split_code=split_code
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("active", "currency", "provider_slug", "bank_id", "customer_id"),
    [
        (True, "NGN", "wema-bank", "737", "CUST_test1234"),
        (True, None, None, None, None),
        (False, None, None, None, None),
    ]
)
@responses.activate
def test_list_dvas(dva_client, active, currency, provider_slug, bank_id, customer_id):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/dedicated_account"
    response_data = {"status": "success"}
    url_params = {
        "active": active,
        "currency": currency,
        "provider_slug": provider_slug,
        "bank_id": bank_id,
        "customer": customer_id,
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
    response = dva_client.list_dedicated_account(
        active=active,
        currency=currency,
        provider_slug=provider_slug,
        bank_id=bank_id,
        customer_id=customer_id
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_fetch_dedicated_account(dva_client):
    """ Test for synchronous Customers """
    dedicated_account_id = 1234
    url = f"https://api.paystack.co/dedicated_account/{dedicated_account_id}"
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = dva_client.fetch_dedicated_account(dedicated_account_id=dedicated_account_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    ("account_number", "provider_slug", "date_transfer"),
    [
        ("0000000000", "wema-bank", date(2013, 12, 12)),
        (None, None, None)
    ]
)
@responses.activate
def test_requery_dva(dva_client, account_number, provider_slug, date_transfer):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/dedicated_account/requery"
    response_data = {"status": "success"}
    url_params = {
        "account_number": account_number,
        "provider_slug": provider_slug,
        "date": date_transfer
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
    response = dva_client.requery_dedicated_account(
        account_number=account_number,
        provider_slug=provider_slug,
        date_transfer=date_transfer
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_deactivate_dedicated_account(dva_client):
    """ Test for synchronous Customers """
    dedicated_account_id = 1234
    url = f"https://api.paystack.co/dedicated_account/{dedicated_account_id}"
    response_data = {"status": "success"}
    responses.add(
        responses.DELETE,
        url,
        status=200,
        json=response_data,
    )
    response = dva_client.deactivate_dedicated_account(dedicated_account_id=dedicated_account_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    ("customer_id_code", "subaccount", "split_code", "preferred_bank"),
    [
        ("test-id-code", "SUB_test1234", "SPLIT_test1234", "wema-bank"),
        ("test-id-code", None, None, None)
    ]
)
@responses.activate
def test_requery_dva(dva_client, customer_id_code, subaccount, split_code, preferred_bank):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/dedicated_account/split"
    response_data = {"status": "success"}
    expected_data = {
        "customer": customer_id_code,
        "preferred_bank": preferred_bank,
        "subaccount": subaccount,
        "split_code": split_code,
    }

    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = dva_client.split_dedicated_account(
        customer_id_or_code=customer_id_code,
        subaccount=subaccount,
        split_code=split_code,
        preferred_bank=preferred_bank
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize("account_number", ["0000000000"])
@responses.activate
def test_remove_split(dva_client, account_number):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/dedicated_account/split"
    response_data = {"status": "success"}
    responses.add(
        responses.DELETE,
        url,
        status=200,
        json=response_data,
    )
    response = dva_client.remove_split_dedicated_account(account_number=account_number)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@responses.activate
def test_fetch_bank_providers(dva_client):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/dedicated_account/available_providers"
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = dva_client.fetch_bank_providers()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None
