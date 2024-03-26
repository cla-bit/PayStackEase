""" Test for synchronous Customers """

import json
import pytest

from tests.conftest import async_integration_client, mocked_responses


@pytest.mark.asyncio
async def test_fetch_timeout(async_integration_client, mocked_responses):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/integration/payment_session_timeout"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_integration_client.fetch_timeout()
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(("timeout",), [(10,), (20,), (30,)])
async def test_update_dispute(async_integration_client, mocked_responses, timeout):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/integration/payment_session_timeout"
    response_data = {"status": "success"}
    expected_data = {
        "timeout":  timeout
    }

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_integration_client.update_timeout(
        timeout=timeout,
    )
    mocked_responses.assert_called()
    assert response is not None
