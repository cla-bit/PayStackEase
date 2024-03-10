""" Wrapper for Paystack Terminal APIs
The Terminal API allows you to build delightful in-person payment experiences.
"""

from typing import Optional, Dict
from paystackease.apis.base import PayStackBaseClientAPI


class TerminalClientAPI(PayStackBaseClientAPI):
    """Paystack Terminal API
    Reference: https://paystack.com/docs/api/terminal/
    """

    def send_event(
        self,
        terminal_id: str,
        event_type: str,
        terminal_action: str,
        data_object: Dict[str, str],
    ) -> dict:
        """Send an event from your application to the Paystack Terminal
        :param terminal_id: The terminal iD the event is sent to
        :param event_type: The type of event to send. We currently support [ invoice | transaction ]
        :param terminal_action: The action to perform on the terminal
        [invoice type]:the action can either be [ process || view ]
         [transaction type], the action can either be [ process || print ].
         :param data_object: parameters needed to perform the specified action.
         [invoice type]: you need to pass {id: invoice_id, reference: offline_reference}.
         [transaction type], you can pass {id: transaction_id}

        :return: The response from the API
        :rtype: dict
        """
        data = {"type": event_type, "action": terminal_action, "data": data_object}
        return self._post_request(f"/terminal/{terminal_id}/event", data=data)

    def commission_terminal(self, serial_number: str) -> dict:
        """Activate debug device by linking it to your integration
        :param serial_number: The serial number of the device

        :return: The response from the API
        :rtype: dict
        """
        data = {"serial_number": serial_number}
        return self._post_request("/terminal/commission_device", data=data)

    def decommission_terminal(self, serial_number: str) -> dict:
        """Deactivate debug device by unlinking it from your integration
        :param serial_number: The serial number of the device

        :return: The response from the API
        :rtype: dict
        """
        data = {"serial_number": serial_number}
        return self._post_request("/terminal/decommission_device", data=data)

    def update_terminal(
        self, terminal_id: str, terminal_name: str, terminal_address: str
    ) -> dict:
        """Update details of a terminal
        :param terminal_id: The terminal iD the event is sent to
        :param terminal_name: Name of the terminal
        :param terminal_address: Address of the terminal

        :return: The response from the API
        :rtype: dict
        """
        data = {"name": terminal_name, "address": terminal_address}
        return self._put_request(f"/terminal/{terminal_id}", data=data)

    def fetch_event_status(self, terminal_id: str, event_id: str) -> dict:
        """Fetch details of a specific event status sent to the terminal
        :param terminal_id: iD of the terminal the event is sent to
        :param event_id: The event id sent to the terminal

        :return: The response from the API
        :rtype: dict
        """
        return self._get_request(f"/terminal/{terminal_id}/event/{event_id}")

    def fetch_terminal_status(self, terminal_id: str) -> dict:
        """Fetch the availability of a terminal before sending an event
        :param terminal_id: The terminal iD the event is sent to

        :return: The response from the API
        :rtype: dict
        """
        return self._get_request(f"/terminal/{terminal_id}/presence")

    def list_terminals(
        self,
        per_page: int,
        next_cursor: Optional[str] = None,
        previous_cursor: Optional[str] = None,
    ) -> dict:
        """List the Terminals available on your integration
        :param per_page: The number of records to return. Default value is 50
        :param next_cursor:
        :param previous_cursor:

        :return: The response from the API
        :rtype: dict
        """
        params = {"perPage": per_page, "next": next_cursor, "previous": previous_cursor}
        return self._get_request("/terminal", params=params)

    def fetch_terminal(self, terminal_id: str) -> dict:
        """Get the details of a terminal
        :param terminal_id: The terminal iD the event is sent to

        :return: The response from the API
        :rtype: dict
        """
        return self._get_request(f"/terminal/timeline/{terminal_id}")
