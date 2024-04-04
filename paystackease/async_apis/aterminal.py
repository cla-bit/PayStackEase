"""
Wrapper for Asynchronous Paystack Terminal APIs

The Terminal API allows you to build delightful in-person payment experiences.
"""
from aiohttp import ClientResponse
from typing import Optional, Dict
from paystackease._abase import AsyncPayStackBaseClientAPI
from paystackease.helpers.tool_kit import EventAction, EventType


class AsyncTerminalClientAPI(AsyncPayStackBaseClientAPI):
    """
    Paystack Terminal API
    Reference: https://paystack.com/docs/api/terminal/
    """

    async def send_event(
            self,
            terminal_id: str,
            event_type: EventType,
            terminal_action: EventAction,
            data_object: Dict[str, str],
    ) -> ClientResponse:
        """
        Send an event from your application to the Paystack Terminal

        :param: terminal_id: The terminal iD the event is sent to
        :param: event_type: The type of event to send. We currently support [ invoice | transaction ]
        :param: terminal_action: The action to perform on the terminal
                                [invoice type]:the action can either be [ process || view ]
                                [transaction type], the action can either be [ process || print ].
        :param: data_object: parameters needed to perform the specified action.
                            [invoice type]: you need to pass {id: invoice_id, reference: offline_reference}.
                            [transaction type], you can pass {id: transaction_id}

        :return: The response from the API
        :rtype: ClientResponse object
        """
        data = {"type": event_type, "action": terminal_action, "data": data_object}
        return await self._post_request(f"/terminal/{terminal_id}/event", data=data)

    async def commission_terminal(self, serial_number: str) -> ClientResponse:
        """
        Activate debug device by linking it to your integration

        :param: serial_number: The serial number of the device

        :return: The response from the API
        :rtype: ClientResponse object
        """
        data = {"serial_number": serial_number}
        return await self._post_request("/terminal/commission_device", data=data)

    async def decommission_terminal(self, serial_number: str) -> ClientResponse:
        """
        Deactivate debug device by unlinking it from your integration

        :param: serial_number: The serial number of the device

        :return: The response from the API
        :rtype: ClientResponse object
        """
        data = {"serial_number": serial_number}
        return await self._post_request("/terminal/decommission_device", data=data)

    async def update_terminal(
            self, terminal_id: str, terminal_name: str, terminal_address: str
    ) -> ClientResponse:
        """
        Update details of a terminal

        :param: terminal_id: The terminal iD the event is sent to
        :param: terminal_name: Name of the terminal
        :param: terminal_address: Address of the terminal

        :return: The response from the API
        :rtype: ClientResponse object
        """
        data = {"name": terminal_name, "address": terminal_address}
        return await self._put_request(f"/terminal/{terminal_id}", data=data)

    async def fetch_event_status(self, terminal_id: str, event_id: str) -> ClientResponse:
        """
        Fetch details of a specific event status sent to the terminal

        :param: terminal_id: iD of the terminal the event is sent to
        :param: event_id: The event id sent to the terminal

        :return: The response from the API
        :rtype: ClientResponse object
        """
        return await self._get_request(f"/terminal/{terminal_id}/event/{event_id}")

    async def fetch_terminal_status(self, terminal_id: str) -> ClientResponse:
        """
        Fetch the availability of a terminal before sending an event

        :param: terminal_id: The terminal iD the event is sent to

        :return: The response from the API
        :rtype: ClientResponse object
        """
        return await self._get_request(f"/terminal/{terminal_id}/presence")

    async def list_terminals(
            self,
            per_page: int = 50,
            next_cursor: Optional[bool] = True,
            previous_cursor: Optional[bool] = True,
    ) -> ClientResponse:
        """
        List the Terminals available on your integration

        :param: per_page: The number of records to return. async default value is 50
        :param: next_cursor:
        :param: previous_cursor:

        :return: The response from the API
        :rtype: ClientResponse object
        """
        # convert toi strings
        next_cursor = self._convert_to_string(next_cursor)
        previous_cursor = self._convert_to_string(previous_cursor)
        params = {"perPage": per_page, "next": next_cursor, "previous": previous_cursor}
        return await self._get_request("/terminal", params=params)

    async def fetch_terminal(self, terminal_id: str) -> ClientResponse:
        """
        Get the details of a terminal

        :param: terminal_id: The terminal iD the event is sent to

        :return: The response from the API
        :rtype: ClientResponse object
        """
        return await self._get_request(f"/terminal/timeline/{terminal_id}")
