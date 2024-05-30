""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from paystackease.helpers.tool_kit import EventAction, EventType
from tests.conftest import async_terminal_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("event_type", "terminal_action", "data_obj"),
    [
        (
            EventType.TRANSACTION.value,
            EventAction.PRINT.value,
            {"id": "transaction_id", "reference": "offline_reference"},
        ),
    ],
)
async def test_create_event(
    async_terminal_client, mocked_responses, event_type, terminal_action, data_obj
):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal-id"
    url = f"https://api.paystack.co/terminal/{terminal_id}/event"
    response_data = {"status": "success"}
    expected_data = {"type": event_type, "action": terminal_action, "data": data_obj}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_terminal_client.send_event(
        terminal_id=terminal_id,
        event_type=event_type,
        terminal_action=terminal_action,
        data_object=data_obj,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("serial_number",),
    [
        ("123qwe456",),
        ("12zxvsdqwer23",),
    ],
)
async def test_commission(async_terminal_client, mocked_responses, serial_number):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/terminal/commission_device"
    response_data = {"status": "success"}
    expected_data = {"serial_number": serial_number}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_terminal_client.commission_terminal(
        serial_number=serial_number
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("serial_number",),
    [
        ("123qwe456",),
        ("12zxvsdqwer23",),
    ],
)
async def test_decommission(async_terminal_client, mocked_responses, serial_number):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/terminal/decommission_device"
    response_data = {"status": "success"}
    expected_data = {"serial_number": serial_number}
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_terminal_client.decommission_terminal(
        serial_number=serial_number
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("per_page", "next_cursor", "prev_cursor"), [(1, True, False), (3, False, True)]
)
async def test_list_terminals(
    async_terminal_client, mocked_responses, per_page, next_cursor, prev_cursor
):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/terminal"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "next": str(next_cursor).lower(),
        "previous": str(prev_cursor).lower(),
    }
    # Construct the expected URL with parameters
    query_string = "&".join(
        f"{key}={value}" for key, value in url_params.items() if value is not None
    )
    expected_url = url + ("?" + query_string if query_string else "")

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_terminal_client.list_terminals(
        per_page=per_page, next_cursor=next_cursor, previous_cursor=prev_cursor
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_event_status(async_terminal_client, mocked_responses):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal-id"
    event_id = "test-event-id"
    url = f"https://api.paystack.co/terminal/{terminal_id}/event/{event_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_terminal_client.fetch_event_status(
        terminal_id=terminal_id, event_id=event_id
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_terminal_status(async_terminal_client, mocked_responses):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal-id"
    url = f"https://api.paystack.co/terminal/{terminal_id}/presence"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_terminal_client.fetch_terminal_status(
        terminal_id=terminal_id
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_terminal(async_terminal_client, mocked_responses):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal-id"
    url = f"https://api.paystack.co/terminal/timeline/{terminal_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_terminal_client.fetch_terminal(terminal_id=terminal_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("terminal_name", "terminal_address"),
    [
        ("Testing-terminal", "Testing-address"),
    ],
)
async def test_update_terminal(
    async_terminal_client, mocked_responses, terminal_name, terminal_address
):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal_id"
    url = f"https://api.paystack.co/terminal/{terminal_id}"
    response_data = {"status": "success"}
    expected_data = {"name": terminal_name, "address": terminal_address}

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_terminal_client.update_terminal(
        terminal_id=terminal_id,
        terminal_name=terminal_name,
        terminal_address=terminal_address,
    )
    mocked_responses.assert_called()
    assert response is not None
