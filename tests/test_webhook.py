import unittest
from unittest.mock import patch, Mock
from paystackease.core._webhook import PayStackWebhook
from paystackease.core._api_errors import PayStackSignatureVerifyError
from paystackease.core._event import Event


class TestPayStackWebhook(unittest.TestCase):

    @patch('paystackease.core._webhook.PayStackSignature.verify_headers')
    def test_create_event_with_empty_signature_header(self, mock_verify_headers):
        mock_verify_headers.side_effect = PayStackSignatureVerifyError("No signature", None)
        with self.assertRaises(PayStackSignatureVerifyError) as context:
            PayStackWebhook.create_event("secret_key", "payload_type", "")
        self.assertEqual(str(context.exception), "No signature")

    @patch('paystackease.core.paystack_signature.PayStackSignature.verify_headers')
    def test_create_event_with_missing_signature_header(self, mock_verify_headers):
        mock_verify_headers.side_effect = PayStackSignatureVerifyError("No signature")
        with self.assertRaises(PayStackSignatureVerifyError) as context:
            PayStackWebhook.create_event("secret_key", "payload_type", None)
        self.assertEqual(str(context.exception), "No signature")

    @patch('paystackease.core._webhook.PayStackSignature.verify_headers')
    def test_create_event_with_valid_signature_header(self, mock_verify_headers):
        mock_verify_headers.return_value = True
        event = PayStackWebhook.create_event("secret_key", "payload_type", "valid_signature_header")
        self.assertIsInstance(event, Event)

    @patch('paystackease.core.paystack_signature.PayStackSignature.verify_headers')
    def test_create_event_with_invalid_signature_header(self, mock_verify_headers):
        mock_verify_headers.return_value = False
        with self.assertRaises(PayStackSignatureVerifyError) as context:
            PayStackWebhook.create_event("secret_key", "payload_type", "invalid_signature_header")
        self.assertEqual(str(context.exception), "Invalid signature")

    @patch('paystackease.core.paystack_signature.PayStackSignature.verify_headers')
    def test_create_event_with_invalid_payload_type(self, mock_verify_headers):
        mock_verify_headers.return_value = True
        with self.assertRaises(ValueError) as context:
            PayStackWebhook.create_event("secret_key", "invalid_payload_type", "valid_signature_header")
        self.assertEqual(str(context.exception), "Invalid payload type")