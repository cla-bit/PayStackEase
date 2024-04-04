""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses
from paystackease.helpers.tool_kit import EventAction, EventType
from tests.conftest import terminal_client


@pytest.mark.parametrize(
    ("event_type", "terminal_action", "data_obj"),
    [
        (
            EventType.INVOICE.value,
            EventAction.PROCESS.value,
            {"id": "invoice_id", "reference": "offline_reference"},
        ),
    ],
)
@responses.activate
def test_create_event(terminal_client, event_type, terminal_action, data_obj):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal-id"
    url = f"https://api.paystack.co/terminal/{terminal_id}/event"
    response_data = {"status": "success"}
    expected_data = {"type": event_type, "action": terminal_action, "data": data_obj}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = terminal_client.send_event(
        terminal_id=terminal_id,
        event_type=event_type,
        terminal_action=terminal_action,
        data_object=data_obj,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("serial_number",),
    [
        ("123qwe456",),
        ("12zxvsdqwer23",),
    ],
)
@responses.activate
def test_commission(terminal_client, serial_number):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/terminal/commission_device"
    response_data = {"status": "success"}
    expected_data = {"serial_number": serial_number}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = terminal_client.commission_terminal(serial_number=serial_number)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("serial_number",),
    [
        ("123qwe456",),
        ("12zxvsdqwer23",),
    ],
)
@responses.activate
def test_decommission(terminal_client, serial_number):
    """Test for synchronous Customers"""
    url = f"https://api.paystack.co/terminal/decommission_device"
    response_data = {"status": "success"}
    expected_data = {"serial_number": serial_number}
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = terminal_client.decommission_terminal(serial_number=serial_number)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("per_page", "next_cursor", "prev_cursor"),
    [
        (1, True, False),
        (3, False, False),
    ],
)
@responses.activate
def test_list_terminals(terminal_client, per_page, next_cursor, prev_cursor):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/terminal"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "next": str(next_cursor),
        "previous": str(prev_cursor),
    }
    # Construct the expected URL with parameters
    query_string = "&".join(
        f"{key}={value}" for key, value in url_params.items() if value is not None
    )
    expected_url = url + ("?" + query_string if query_string else "")

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = terminal_client.list_terminals(
        per_page=per_page, next_cursor=next_cursor, previous_cursor=prev_cursor
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_fetch_event_status(terminal_client):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal-id"
    event_id = "test-event-id"
    url = f"https://api.paystack.co/terminal/{terminal_id}/event/{event_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = terminal_client.fetch_event_status(
        terminal_id=terminal_id, event_id=event_id
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@responses.activate
def test_fetch_terminal_status(terminal_client):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal-id"
    url = f"https://api.paystack.co/terminal/{terminal_id}/presence"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = terminal_client.fetch_terminal_status(terminal_id=terminal_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@responses.activate
def test_fetch_terminal(terminal_client):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal-id"
    url = f"https://api.paystack.co/terminal/timeline/{terminal_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = terminal_client.fetch_terminal(terminal_id=terminal_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    ("terminal_name", "terminal_address"),
    [
        ("Testing-terminal", "Testing-address"),
    ],
)
@responses.activate
def test_update_terminal(terminal_client, terminal_name, terminal_address):
    """Test for synchronous Customers"""
    terminal_id = "test-terminal_id"
    url = f"https://api.paystack.co/terminal/{terminal_id}"
    response_data = {"status": "success"}
    expected_data = {"name": terminal_name, "address": terminal_address}

    responses.add(
        responses.PUT,
        url,
        status=200,
        json=response_data,
    )
    response = terminal_client.update_terminal(
        terminal_id=terminal_id,
        terminal_name=terminal_name,
        terminal_address=terminal_address,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None
