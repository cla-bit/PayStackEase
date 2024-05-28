import hmac
import json
import pytest
from hashlib import sha512
from paystackease.core import PayStackSignatureVerifyError
from paystackease.core import PayStackWebhook, PayStackSignature
from paystackease.core import Event


# Sample secret key and payload for tests
SECRET_KEY = "test_secret_key"
PAYLOAD = json.dumps({"event": "payment.success", "data": {"id": 12345, "status": "success"}})
SIGNATURE = hmac.new(SECRET_KEY.encode('utf-8'), msg=PAYLOAD.encode('utf-8'), digestmod=sha512).hexdigest()


def test_get_event_data_valid():
    payload_type = PAYLOAD.encode('utf-8')
    signature_header = SIGNATURE
    data = PayStackWebhook.get_event_data(SECRET_KEY, payload_type, signature_header)

    assert isinstance(data, Event)
    assert data.type == 'payment.success'
    assert data.event_data == {'id': 12345, 'status': 'success'}


def test_get_event_data_invalid_signature():
    payload_type = PAYLOAD.encode('utf-8')
    signature_header = "invalid_signature"

    with pytest.raises(PayStackSignatureVerifyError) as excinfo:
        PayStackWebhook.get_event_data(SECRET_KEY, payload_type, signature_header)

    assert "Invalid signature" in str(excinfo.value)


def test_get_event_data_no_signature():
    payload_type = PAYLOAD.encode('utf-8')
    signature_header = None

    with pytest.raises(PayStackSignatureVerifyError) as excinfo:
        PayStackWebhook.get_event_data(SECRET_KEY, payload_type, signature_header)

    assert "No signature" in str(excinfo.value)


def test_get_event_data_decoded_payload():
    payload_type = PAYLOAD  # this is already a string
    signature_header = SIGNATURE
    data = PayStackWebhook.get_event_data(SECRET_KEY, payload_type, signature_header)

    assert isinstance(data, Event)
    assert data.type == 'payment.success'
    assert data.event_data == {'id': 12345, 'status': 'success'}


def test_make_signature():
    signature = PayStackSignature._make_signature(PAYLOAD, SECRET_KEY)
    assert signature == SIGNATURE


def test_verify_headers_valid():
    assert PayStackSignature.verify_headers(PAYLOAD, SECRET_KEY, SIGNATURE) is True


def test_verify_headers_invalid():
    with pytest.raises(PayStackSignatureVerifyError) as excinfo:
        PayStackSignature.verify_headers(PAYLOAD, SECRET_KEY, "invalid_signature")

    assert "Invalid signature" in str(excinfo.value)


def test_verify_headers_no_signature():
    with pytest.raises(PayStackSignatureVerifyError) as excinfo:
        PayStackSignature.verify_headers(PAYLOAD, SECRET_KEY, None)

    assert "No signature" in str(excinfo.value)
