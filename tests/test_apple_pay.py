""" Tests for paystackease.apis.apple_pay.py """

import json

import pytest
import responses
from paystackease.apis import ApplePayClientAPI


@pytest.fixture(scope="session", name="apple_pay_client")
@responses.activate
def apple_pay_client_test():
    """Fixture for ApplePayClientAPI"""
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/apple-pay/domain",
        json=response_data,
        status=200,
    )
    client = ApplePayClientAPI()
    return client


@pytest.mark.parametrize("domain_name", ["test.com"])
@responses.activate
def test_register_domain(apple_pay_client, domain_name):
    """ Test for register_domain """
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        "https://api.paystack.co/apple-pay/domain",
        json=response_data,
        status=200,
    )
    response = apple_pay_client.register_domain(domain_name=domain_name)
    assert len(responses.calls) == 1
    expected_data = {"domainName": domain_name}
    assert responses.calls[0].request.url == "https://api.paystack.co/apple-pay/domain"
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize("domain_name", ["test.com"])
@responses.activate
def test_unregister_domain(apple_pay_client, domain_name):
    """ Test for unregister_domain """
    response_data = {"status": "success"}
    responses.add(
        responses.DELETE,
        "https://api.paystack.co/apple-pay/domain",
        json=response_data,
        status=200,
    )
    response = apple_pay_client.unregister_domain(domain_name=domain_name)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == "https://api.paystack.co/apple-pay/domain"
    assert response is not None


@pytest.mark.parametrize(
    "use_cursor, next_page, previous_page", [(True, 1, 1), (False, 1, 2), (True, 2, 3)]
)
@responses.activate
def test_list_domains(apple_pay_client, use_cursor, next_page, previous_page):
    """ Test for list_domains """
    response_data = {"status": "success"}
    responses.add(
        responses.GET,
        "https://api.paystack.co/apple-pay/domain",
        json=response_data,
        status=200,
    )
    # You can make some parameters optional in both the response and expected params
    response = apple_pay_client.list_domains(use_cursor=use_cursor, next_page=next_page)
    expected_params = {"use_cursor": str(use_cursor).lower(), "next": next_page}
    expected_url = "https://api.paystack.co/apple-pay/domain"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url + "?" + "&".join(
        f"{key}={value}" for key, value in expected_params.items() if value is not None
    )
    assert response is not None
