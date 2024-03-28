""" Test for synchronous Customers """

from datetime import date
import pytest

from tests.conftest import async_customers_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("email", "first_name", "last_name", "phone", "metadata"),
    [
        ("test@email.com", "test", "test", "08012345678", {"nickname": "tester"}),
        ("test@email.com", "test", "test", "08012345678", None),
        ("test@email.com", "test", "test", "08012345678", {"nickname": [{"nickname": "tester"}]})

    ]
)
async def test_create_customer(async_customers_client, mocked_responses, email, first_name, last_name, phone, metadata):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/customer"
    expected_data = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "metadata": metadata,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data
    )
    response = await async_customers_client.create_customer(email, first_name, last_name, phone, metadata)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("first_name", "last_name", "account_type", "country",
     "bank_code", "account_number", "bvn", "customer_id_num", "middle_name"),
    [
        ("test", "test", "bank_account", "NGN", "737", "0000000000", "1234567890",
         "CUST_test1234", "test-middle-name"),
        ("test", "test", "bank_account", "NGN", "737", "0000000000", "1234567890",
         None, None),

    ]
)
async def test_validate_customer(async_customers_client, mocked_responses, first_name, last_name, account_type,
                       country, bank_code, account_number, bvn, customer_id_num,
                       middle_name):
    """ Test for syncjhronouus Customers """
    email_or_code = "Cust_test-email-or-code"
    url = f"https://api.paystack.co/customer/{email_or_code}/identification"
    expected_data = {
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": middle_name,
        "type": account_type,
        "value": customer_id_num,
        "country": country,
        "bvn": bvn,
        "bank_code": bank_code,
        "account_number": account_number,
    }
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data
    )
    response = await async_customers_client.validate_customer(
        email_or_code=email_or_code, first_name=first_name,
        last_name=last_name,
        account_type=account_type,
        country=country, bank_code=bank_code,
        account_number=account_number, bvn=bvn,
        customer_id_num=customer_id_num, middle_name=middle_name)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("email_or_code", "risk_action"),
    [
        ("test-email-or-code", None),
        ("test-email-or-code", "default"),
        ("test-email-or-code", "allow"),
        ("test-email-or-code", "deny")
    ]
)
async def test_whitelist_blacklist_customer(async_customers_client, mocked_responses, email_or_code, risk_action):
    """ Test for syncjhronouus Customers """
    url = "https://api.paystack.co/customer/set_risk_action"
    expected_data = {
        "customer": email_or_code,
        "risk_action": risk_action
    }
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data
    )
    response = await async_customers_client.whitelist_blacklist_customer(
        email_or_code=email_or_code, risk_action=risk_action)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize("authorization_code", ["AUTH_test1234"])
async def test_deactivate_authorization(async_customers_client, mocked_responses, authorization_code):
    """ Test for syncjhronouus Customers """
    url = "https://api.paystack.co/customer/deactivate_authorization"
    expected_data = {
        "authorization_code": authorization_code
    }
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data
    )
    response = await async_customers_client.deactivate_authorization(authorization_code=authorization_code)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("first_name", "last_name", "phone", "metadata"),
    [
        ("test", "test", "08012345678", {"nickname": "tester"}),
        ("test", "test", "08012345678", None),
        (None, None, None, None)
    ]
)
async def test_update_customer(async_customers_client, mocked_responses, first_name, last_name, phone, metadata):
    """ Test for syncjhronouus Customers """
    customer_code = "customer_code"
    url = f"https://api.paystack.co/customer/{customer_code}"
    expected_data = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "metadata": metadata,
    }
    mocked_responses.put(
        url,
        status=200,
        payload=expected_data
    )
    response = await async_customers_client.update_customer(
        customer_code=customer_code, first_name=first_name,
        last_name=last_name, phone=phone, metadata=metadata)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_customer(async_customers_client, mocked_responses):
    """ Test for syncjhronouus Customers """
    email_or_code = "customer_code"
    url = f"https://api.paystack.co/customer/{email_or_code}"
    expected_data = {"status": "success"}
    mocked_responses.get(
        url,
        status=200,
        payload=expected_data
    )
    response = await async_customers_client.fetch_customer(email_or_code=email_or_code)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("per_page", "page", "from_date", "to_date"), [
        (1, 1, date(2012, 12, 12), date(2012, 12, 12)),  # Testing with all parameters provided
        (20, 10, date(2012, 12, 12), date(2012, 12, 12)),  # Testing with all parameters provided
        (None, None, None, None),  # Testing with only use_cursor parameter provided
    ]
)
async def test_list_customers(async_customers_client, mocked_responses, per_page, page, from_date, to_date):
    """
    This function tests the behavior of the list_domains method with various combinations
    of parameters, including scenarios where some parameters are None.
    """
    url = "https://api.paystack.co/customer"
    response_data = {"status": "success"}

    # Construct the expected URL with parameters
    url_params = {
        "perPage": per_page,
        "page": page,
        "from": from_date,
        "to": to_date,
    }
    # Construct the expected URL with parameters
    query_string = '&'.join(f'{key}={value}' for key, value in url_params.items() if value is not None)
    expected_url = url + ('?' + query_string if query_string else '')

    # mock the API response
    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_customers_client.list_customers(per_page=per_page, page=page, from_date=from_date, to_date=to_date)
    mocked_responses.assert_called()
    assert response is not None
