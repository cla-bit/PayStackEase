""" Tests for synchronous Apple Pay """

import pytest

from tests.conftest import async_apple_pay_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize("domain_name", ["test-apple-domain-name"])
async def test_async_register_domain(
    async_apple_pay_client, mocked_responses, domain_name
):
    """
    This function tests the behavior of the register_domains method with domain_name
    """
    url = "https://api.paystack.co/apple-pay/domain"
    expected_data = {"domainName": domain_name}

    # mock the API response
    mocked_responses.post(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_apple_pay_client.register_domain(domain_name=domain_name)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("use_cursor", "next_page", "previous_page"),
    [(True, 1, 1), (False, 1, 2), (True, None, None), (False, None, None)],
)
async def test_list_domains(
    async_apple_pay_client, mocked_responses, use_cursor, next_page, previous_page
):
    """
    This function tests the behavior of the list_domains method with various combinations
    of parameters, including scenarios where some parameters are None.
    """
    url = "https://api.paystack.co/apple-pay/domain"
    response_data = {"status": "success"}

    # Construct the expected URL with parameters
    url_params = {
        "use_cursor": str(use_cursor).lower(),
        "next": next_page,
        "previous": previous_page,
    }
    # Construct the expected URL with parameters
    query_string = "&".join(
        f"{key}={value}" for key, value in url_params.items() if value is not None
    )
    expected_url = url + ("?" + query_string if query_string else "")

    # mock the API response
    mocked_responses.get(expected_url, status=200, payload=response_data)
    response = await async_apple_pay_client.list_domains(
        use_cursor, next_page, previous_page
    )
    mocked_responses.assert_called()
    assert response.status == "success"


@pytest.mark.asyncio
@pytest.mark.parametrize("domain_name", ["test-apple-domain-name"])
async def test_async_unregister_domain(
    async_apple_pay_client, mocked_responses, domain_name
):
    """
    This function tests the behavior of the register_domains method with domain_name
    """
    url = "https://api.paystack.co/apple-pay/domain"
    expected_data = {"domainName": domain_name}

    # mock the API response
    mocked_responses.delete(
        url,
        status=200,
        payload=expected_data,
    )
    response = await async_apple_pay_client.unregister_domain(domain_name=domain_name)
    mocked_responses.assert_called()
    assert response is not None
