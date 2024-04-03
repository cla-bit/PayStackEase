""" Test for synchronous Customers """

from datetime import date
import pytest

from tests.conftest import async_dva_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("customer_id_or_code", "preferred_bank", "subaccount",
     "split_code", "first_name", "last_name", "phone"),
    [
        ("test_id_code", None, None, None, None, None, None),
        ("test_id_code", "test-wema-bank", "SUB_test123", "SPLIT_test123", "test-first-name", "test-last-name", "08012345678")
    ]
)
async def test_create_virtual_account(async_dva_client, mocked_responses, customer_id_or_code, preferred_bank, subaccount, split_code, first_name, last_name, phone):
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
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_dva_client.create_virtual_account(
        customer_id_or_code=customer_id_or_code,
        preferred_bank=preferred_bank,
        subaccount=subaccount,
        split_code=split_code,
        first_name=first_name,
        last_name=last_name,
        phone=phone
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
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
async def test_assign_dvs(async_dva_client, mocked_responses, email, first_name, last_name, phone,
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
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_dva_client.assign_dedicated_virtual_account(
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
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("active", "currency", "provider_slug", "bank_id", "customer_id"),
    [
        (True, "NGN", "wema-bank", "737", "CUST_test1234"),
        (True, None, None, None, None),
        (False, None, None, None, None),
    ]
)
async def test_list_dvas(async_dva_client, mocked_responses, active, currency, provider_slug, bank_id, customer_id):
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

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_dva_client.list_dedicated_account(
        active=active,
        currency=currency,
        provider_slug=provider_slug,
        bank_id=bank_id,
        customer_id=customer_id
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_dedicated_account(async_dva_client, mocked_responses):
    """ Test for synchronous Customers """
    dedicated_account_id = 1234
    url = f"https://api.paystack.co/dedicated_account/{dedicated_account_id}"
    response_data = {"status": "success"}
    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_dva_client.fetch_dedicated_account(dedicated_account_id=dedicated_account_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("account_number", "provider_slug", "date_transfer"),
    [
        ("0000000000", "wema-bank", date(2013, 12, 12)),
        (None, None, None)
    ]
)
async def test_requery_dva(async_dva_client, mocked_responses, account_number, provider_slug, date_transfer):
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

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_dva_client.requery_dedicated_account(
        account_number=account_number,
        provider_slug=provider_slug,
        date_transfer=date_transfer
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_deactivate_dedicated_account(async_dva_client, mocked_responses):
    """ Test for synchronous Customers """
    dedicated_account_id = 1234
    url = f"https://api.paystack.co/dedicated_account/{dedicated_account_id}"
    response_data = {"status": "success"}
    mocked_responses.delete(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_dva_client.deactivate_dedicated_account(dedicated_account_id=dedicated_account_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("customer_id_code", "subaccount", "split_code", "preferred_bank"),
    [
        ("test-id-code", "SUB_test1234", "SPLIT_test1234", "wema-bank"),
        ("test-id-code", None, None, None)
    ]
)
async def test_requery_dva(async_dva_client, mocked_responses, customer_id_code, subaccount, split_code, preferred_bank):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/dedicated_account/split"
    response_data = {"status": "success"}
    expected_data = {
        "customer": customer_id_code,
        "preferred_bank": preferred_bank,
        "subaccount": subaccount,
        "split_code": split_code,
    }

    mocked_responses.post(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_dva_client.split_dedicated_account(
        customer_id_or_code=customer_id_code,
        subaccount=subaccount,
        split_code=split_code,
        preferred_bank=preferred_bank
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize("account_number", ["0000000000"])
async def test_remove_split(async_dva_client, mocked_responses, account_number):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/dedicated_account/split"
    response_data = {"status": "success"}
    mocked_responses.delete(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_dva_client.remove_split_dedicated_account(account_number=account_number)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_bank_providers(async_dva_client, mocked_responses):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/dedicated_account/available_providers"
    response_data = {"status": "success"}
    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_dva_client.fetch_bank_providers()
    mocked_responses.assert_called()
    assert response is not None
