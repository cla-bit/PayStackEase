from typing import Literal, Dict, Any


class Event:
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
        self._event_type: Event._type = event_type
        self._event_data: Dict[str, Any] = data

    @classmethod
    def _get_event(cls, payload_data: Dict[str, Any]) -> "Event":
        event_type = payload_data.get("event")
        data = payload_data.get("data", {})
        if not event_type:
            raise ValueError("Event type is required")
        return cls(event_type, data)

    @property
    def type(self) -> _type:
        return self._event_type

    @property
    def event_data(self) -> Dict[str, Any]:
        return self._event_data
