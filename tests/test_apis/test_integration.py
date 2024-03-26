""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from tests.conftest import integration_client


@responses.activate
def test_fetch_timeout(integration_client):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/integration/payment_session_timeout"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = integration_client.fetch_timeout()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(("timeout",), [(10,), (20,), (30,)])
@responses.activate
def test_update_dispute(integration_client, timeout):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/integration/payment_session_timeout"
    response_data = {"status": "success"}
    expected_data = {
        "timeout":  timeout
    }

    responses.add(
        responses.PUT,
        url,
        status=200,
        json=response_data,
    )
    response = integration_client.update_timeout(
        timeout=timeout,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None
