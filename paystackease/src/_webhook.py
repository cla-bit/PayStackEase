"""
Module: _webhooks.py
=======================

This module provides functionality to handle PayStack webhooks, including verifying signatures and extracting event data.
"""

import json
import hmac
from typing import Union
from collections import OrderedDict
from hashlib import sha512

from paystackease.src._api_errors import PayStackSignatureVerifyError
from paystackease.src._events import Event


class PayStackWebhook(object):
    """
    A class to handle PayStack webhooks, including verifying signatures and extracting event data.

    Methods
    -------
    get_event_data(secret_key, payload_type, signature_header)
        Verifies the signature of the webhook payload using the provided secret key,
        decodes the payload if necessary, and extracts event data.

    """
    @staticmethod
    def get_event_data(
            secret_key: str,
            payload_type: Union[str, bytes],
            signature_header: str
    ) -> Event:
        """
        Retrieves event data from a Paystack webhook payload.
        Verifies the signature of the webhook payload using the provided secret key,
        decodes the payload if necessary, and extracts event data.

        This method decodes the payload if necessary, verifies the signature header,
        and parses the payload into an event dictionary.

        Parameters:
            secret_key (str): The secret key used for verifying the signature.
            payload_type (Union[str, bytes]): The payload received from the webhook.
            signature_header (str): The signature header received from the webhook.

        Raises:
            ValueError: If the signature verification fails.

        Returns:
            Event: An instance of the Event class representing the extracted event data.
        """

        if hasattr(payload_type, 'decode'):
            payload_type = payload_type.decode("utf-8")

        PayStackSignature.verify_headers(payload_type, secret_key, signature_header)

        data = json.loads(payload_type, object_pairs_hook=lambda pairs: OrderedDict(pairs))
        event = Event._get_event(data)
        return event


class PayStackSignature(object):
    """
    A class to handle Paystack signature verification.

    This class provides methods to create and verify signatures for Paystack webhook payloads.

    Methods
    -------
    _make_signature(payload, secret_key)
        Generates a SHA512 hash signature for the given payload using the provided secret key.

    verify_headers(payload, secret, signature_header)
        Verifies the signature header of a webhook payload using the provided secret key.
        Raises a PayStackSignatureVerifyError if the signature is invalid or missing.
    """

    @staticmethod
    def _make_signature(payload: str, secret_key: str) -> str:
        """
        Creates a HMAC SHA-512 signature for the given payload using the secret key.

        Parameters:
            payload (str): The payload to be signed.
            secret_key (str): The secret key used to create the signature.

        Returns:
            str: The hexadecimal representation of the HMAC SHA-512 signature.
        """

        hash_hex = hmac.new(
            secret_key.encode('utf-8'),
            msg=payload.encode('utf-8'),
            digestmod=sha512
        ).hexdigest()
        return hash_hex

    @classmethod
    def verify_headers(cls, payload: str, secret: str, signature_header: str) -> bool:
        """
        Verifies the signature header of a webhook payload using the provided secret key.
        Raises a PayStackSignatureVerifyError if the signature is invalid or missing.

        Parameters:
            payload (str): The payload received from the webhook.
            secret (str): The secret key used for verifying the signature.
            signature_header (str): The signature header received from the webhook.

        Raises:
            PayStackSignatureVerifyError: If the signature verification fails or if the signature header is missing.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """

        if not signature_header:
            raise PayStackSignatureVerifyError(
                "No signature",
                signature_header,
                http_body=payload,
            )
        expected_payload = cls._make_signature(payload, secret)
        if signature_header != expected_payload:
            raise PayStackSignatureVerifyError(
                "Invalid signature",
                signature_header,
                http_body=payload,
            )
        return True
