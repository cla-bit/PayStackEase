""" Tests for synchronous Apple Pay """

import json
import pytest
import responses
from tests.conftest import apple_pay_client


@pytest.mark.parametrize(
    "use_cursor, next_page, previous_page", [
        (True, 1, 1),  # Testing with all parameters provided
        (False, 1, 2),  # Testing with all parameters provided
        (True, None, None),  # Testing with only use_cursor parameter provided
        (False, None, None),  # Testing with only use_cursor parameter provided
    ]
)
@responses.activate
def test_list_domains(apple_pay_client, use_cursor, next_page, previous_page):
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
    expected_url = f"{url}?{'&'.join(f'{key}={value}' for key, value in url_params.items() if value is not None)}"

    # mock the API response
    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = apple_pay_client.list_domains(use_cursor, next_page, previous_page)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@pytest.mark.parametrize("domain_name", ["test-apple-domain-name"])
@responses.activate
def test_register_domain(apple_pay_client, domain_name):
    """
    This function tests the behavior of the register_domains method with domain_name
    """
    url = "https://api.paystack.co/apple-pay/domain"
    response_data = {"status": "success"}
    expected_data = {"domainName": domain_name}

    # mock the API response
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = apple_pay_client.register_domain(domain_name=domain_name)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize("domain_name", ["test-apple-domain-name"])
@responses.activate
def test_unregister_domain(apple_pay_client, domain_name):
    """
    This function tests the behavior of the unregister_domains method with domain_name
    """
    url = "https://api.paystack.co/apple-pay/domain"
    response_data = {"status": "success"}
    responses.add(
        responses.DELETE,
        url,
        status=200,
        json=response_data,
    )
    response = apple_pay_client.unregister_domain(domain_name=domain_name)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None
