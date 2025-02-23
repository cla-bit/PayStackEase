"""
Module: _events.py
======================

This handles the events from paystack
"""

from typing import Literal, Dict, Any


class Event:
    """
    Represents events from Paystack.

    This class provides a way to handle and process events received from Paystack.
    It includes methods to initialize an event with a specific type and data,
    as well as retrieve the type and data of an event.
    """

    _type = Literal[
        "charge.dispute.create",
        "charge.dispute.remind",
        "charge.dispute.resolve",
        "charge.success",
        "customeridentification.failed",
        "customeridentification.success",
        "dedicatedaccount.assign.failed",
        "dedicatedaccount.assign.success",
        "invoice.create",
        "invoice.payment_failed",
        "invoice.update",
        "paymentrequest.pending",
        "paymentrequest.success",
        "refund.failed",
        "refund.pending",
        "refund.processed",
        "refund.processing",
        "subscription.create",
        "subscription.disable",
        "subscription.expiring_cards",
        "subscription.not_renew",
        "transfer.failed",
        "transfer.success",
        "transfer.reversed"
    ]

    def __init__(self, event_type: _type, data: Dict[str, Any]) -> None:
        """
        Initialize the Event instance.

        Parameters:
            event_type (Event._type): The type of the event.
            data (Dict[str, Any]): The data associated with the event.
        """

        self._event_type: Event._type = event_type
        self._event_data: Dict[str, Any] = data

    @classmethod
    def _get_event(cls, payload_data: Dict[str, Any]) -> "Event":
        """
        Create an Event instance from payload data.

        Parameters:
            payload_data (Dict[str, Any]): The payload data containing event information.

        Returns:
            Event: An Event instance.

        Raises:
            ValueError: If the event type is not provided in the payload data.
        """

        event_type = payload_data.get("event")
        data = payload_data.get("data", {})
        if not event_type:
            raise ValueError("Event type is required")
        return cls(event_type, data)

    @property
    def type(self) -> _type:
        """
        Get the type of the event.

        Returns:
            _type: The event type.
        """

        return self._event_type

    @property
    def event_data(self) -> Dict[str, Any]:
        """
        Get the data associated with the event.

        Returns:
            Dict[str, Any]: The event data.
        """

        return self._event_data
