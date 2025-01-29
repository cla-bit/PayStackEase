"""
Module: _webhooks.py
=======================

This module provides functionality to handle PayStack webhooks, including verifying signatures and extracting event data.
"""

import json
import hmac
from collections import OrderedDict
from hashlib import sha512
from paystackease.src._api_errors import PayStackSignatureVerifyError
from paystackease.src._events import Event


class PayStackWebhook(object):

    @staticmethod
    def get_event_data(
            secret_key,
            payload_type,
            signature_header
    ):
        if hasattr(payload_type, 'decode'):
            payload_type = payload_type.decode("utf-8")

        PayStackSignature.verify_headers(payload_type, secret_key, signature_header)

        data = json.loads(payload_type, object_pairs_hook=lambda pairs: OrderedDict(pairs))
        event = Event._get_event(data)
        return event


class PayStackSignature(object):
    @staticmethod
    def _make_signature(payload, secret_key):
        hash_hex = hmac.new(
            secret_key.encode('utf-8'),
            msg=payload.encode('utf-8'),
            digestmod=sha512
        ).hexdigest()
        return hash_hex

    @classmethod
    def verify_headers(cls, payload, secret, signature_header):
        if not signature_header:
            raise PayStackSignatureVerifyError(
                "No signature",
                signature_header,
                payload,
            )
        expected_payload = cls._make_signature(payload, secret)
        if signature_header != expected_payload:
            raise PayStackSignatureVerifyError(
                "Invalid signature",
                signature_header,
                payload,
            )

        return True
