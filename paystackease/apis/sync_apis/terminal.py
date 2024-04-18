"""
Wrapper for Paystack Terminal APIs

The Terminal API allows you to build delightful in-person payment experiences.
"""

from typing import Optional, Dict, Union

from paystackease.core import PayStackResponse, SyncRequestAPI
from paystackease.helpers import EventAction, EventType


class TerminalClientAPI(SyncRequestAPI):
    """
    Paystack Terminal API
    Reference: https://paystack.com/docs/api/terminal/
    """

    def send_event(
            self,
            terminal_id: str,
            event_type: EventType,
            terminal_action: EventAction,
            data_object: Dict[str, str],
    ) -> PayStackResponse:
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

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"type": event_type, "action": terminal_action, "data": data_object}
        return self._post_request(f"/terminal/{terminal_id}/event", data=data)

    def commission_terminal(self, serial_number: str) -> PayStackResponse:
        """
        Activate debug device by linking it to your integration

        :param: serial_number: The serial number of the device

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"serial_number": serial_number}
        return self._post_request("/terminal/commission_device", data=data)

    def decommission_terminal(self, serial_number: str) -> PayStackResponse:
        """
        Deactivate debug device by unlinking it from your integration

        :param: serial_number: The serial number of the device

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"serial_number": serial_number}
        return self._post_request("/terminal/decommission_device", data=data)

    def update_terminal(
            self, terminal_id: str, terminal_name: str, terminal_address: str
    ) -> PayStackResponse:
        """
        Update details of a terminal

        :param: terminal_id: The terminal iD the event is sent to
        :param: terminal_name: Name of the terminal
        :param: terminal_address: Address of the terminal

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"name": terminal_name, "address": terminal_address}
        return self._put_request(f"/terminal/{terminal_id}", data=data)

    def fetch_event_status(self, terminal_id: str, event_id: str) -> PayStackResponse:
        """
        Fetch details of a specific event status sent to the terminal

        :param: terminal_id: iD of the terminal the event is sent to
        :param: event_id: The event id sent to the terminal

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"/terminal/{terminal_id}/event/{event_id}")

    def fetch_terminal_status(self, terminal_id: str) -> PayStackResponse:
        """
        Fetch the availability of a terminal before sending an event

        :param: terminal_id: The terminal iD the event is sent to

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"/terminal/{terminal_id}/presence")

    def list_terminals(
            self,
            per_page: int = 50,
            next_cursor: Optional[Union[bool, None]] = True,
            previous_cursor: Optional[Union[bool, None]] = True,
    ) -> PayStackResponse:
        """
        List the Terminals available on your integration

        :param: per_page: The number of records to return. Default value is 50
        :param: next_cursor:
        :param: previous_cursor:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        # convert to strings
        next_cursor = self._convert_to_string(next_cursor)
        previous_cursor = self._convert_to_string(previous_cursor)

        params = {"perPage": per_page, "next": next_cursor, "previous": previous_cursor}
        return self._get_request("/terminal", params=params)

    def fetch_terminal(self, terminal_id: str) -> PayStackResponse:
        """
        Get the details of a terminal

        :param: terminal_id: The terminal iD the event is sent to

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"/terminal/timeline/{terminal_id}")
