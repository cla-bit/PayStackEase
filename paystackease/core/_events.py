"""
This handles the events from paystack
"""

from typing import Literal, Dict, Any


class Event:
    """
    This represents the events from paystack
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

    def __init__(self, event_type: _type, data: Dict[str, Any]):
        """
        Initialize the event_type and data
        :param event_type:
        :param data:
        """
        self._event_type: Event._type = event_type
        self._event_data: Dict[str, Any] = data

    @classmethod
    def _get_event(cls, payload_data: Dict[str, Any]) -> "Event":
        """
        Get the event from the payload data
        :param payload_data:
        :return:
        """
        event_type = payload_data.get("event")
        data = payload_data.get("data", {})
        if not event_type:
            raise ValueError("Event type is required")
        return cls(event_type, data)

    @property
    def type(self) -> _type:
        """
        Get the type of the event
        :return:
        """
        return self._event_type

    @property
    def event_data(self) -> Dict[str, Any]:
        """
        Get the data of the event
        :return:
        """
        return self._event_data
