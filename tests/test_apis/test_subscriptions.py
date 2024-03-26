""" Test for synchronous Customers """

import json
import urllib.parse
from datetime import date
import pytest
import responses

from tests.conftest import subscriptions_client


@pytest.mark.parametrize(
    ("customer", "plan_code", "authorization", "start_date"),
    [
        ("test@email.com", "PLAN_test1234", "AUTH_test1234", date(2012, 12, 12)),
        ("test@email.com", "PLAN_test1234", "AUTH_test1234", None),
    ]
)
@responses.activate
def test_create_subscription(subscriptions_client, customer, plan_code, authorization, start_date):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/subscription"
    response_data = {"status": "success"}
    expected_data = {
        "customer": customer,
        "plan": plan_code,
        "authorization": authorization,
        "start_date": start_date.strftime("%Y-%m-%d") if start_date else None,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = subscriptions_client.create_subscription(
        customer=customer,
        plan_code=plan_code,
        authorization=authorization,
        start_date=start_date
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("customer", "plan_code", "per_page", "page"),
    [
        ("test@email.com", "PLAN_test1234", 1, 10),
        (None, None, None, None)
    ]
)
@responses.activate
def test_list_subscription(subscriptions_client, customer, plan_code, per_page, page):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/subscription"
    response_data = {"status": "success"}

    url_params = {
        "perPage": per_page,
        "page": page,
        "customer": urllib.parse.quote(customer) if customer else None,
        "plan": plan_code,
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
    response = subscriptions_client.list_subscriptions(
        per_page=per_page,
        page=page,
        customer=customer,
        plan_code=plan_code,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_fetch_subscription(subscriptions_client):
    """ Test for synchronous Customers """
    sub_id = "test-subscription-id"
    url = f"https://api.paystack.co/subscription/{sub_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = subscriptions_client.fetch_subscription(id_or_code=sub_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    ("subscription_code", "token"),
    [
        ("SUB_test1234", "1234qwer"),
        ("SUB_234_testing", "1234qwer"),
    ]
)
@responses.activate
def test_enable_subscription(subscriptions_client, subscription_code, token):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/subscription/enable"
    response_data = {"status": "success"}
    expected_data = {
        "code": subscription_code,
        "token": token,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = subscriptions_client.enable_subscription(
        subscription_code=subscription_code,
        token=token
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("subscription_code", "token"),
    [
        ("SUB_test1234", "1234qwer"),
        ("SUB_234_testing", "1234qwer"),
    ]
)
@responses.activate
def test_disable_subscription(subscriptions_client, subscription_code, token):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/subscription/disable"
    response_data = {"status": "success"}
    expected_data = {
        "code": subscription_code,
        "token": token,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = subscriptions_client.disable_subscription(
        subscription_code=subscription_code,
        token=token
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@responses.activate
def test_generate_update_subscription(subscriptions_client):
    """ Test for synchronous Customers """
    sub_code = "test-sub-code"
    url = f"https://api.paystack.co/subscription/{sub_code}/manage/link"
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = subscriptions_client.generate_update_subscription(subscription_code=sub_code)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response == response_data
    assert response is not None


@responses.activate
def test_send_update_subscription(subscriptions_client):
    """ Test for synchronous Customers """
    sub_code = "test-sub-code"
    url = f"https://api.paystack.co/subscription/{sub_code}/manage/email"
    response_data = {"status": "success"}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = subscriptions_client.send_update_subscription_link(subscription_code=sub_code)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response == response_data
    assert response is not None
