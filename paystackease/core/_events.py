from typing import Literal, Dict, Any


class Event:
    EventType = Literal[
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

    def __init__(self, event_type: EventType, data: Dict[str, Any]):
        self.event_type: Event.EventType = event_type
        self.data: Dict[str, Any] = data

    @classmethod
    def get_event(cls, payload_data: Dict[str, Any]) -> "Event":
        event_type = payload_data.get("event")
        data = payload_data.get("data")
        return cls(event_type, data)

    @property
    def get_type(self) -> EventType:
        return self.event_type

    @property
    def get_data(self) -> Dict[str, Any]:
        return self.data
