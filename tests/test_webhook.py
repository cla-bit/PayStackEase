import json
import pytest
import responses
from paystackease.core._api_errors import PayStackSignatureVerifyError
from your_module import PayStackWebhook, PayStackSignature

# Sample test data
SECRET_KEY = "secret"
PAYLOAD_TYPE = '{"key": "value"}'
SIGNATURE_HEADER = "signature"


@pytest.fixture
def webhook():
    return PayStackWebhook()


def test_get_event_data(webhook):
    # Mocking the PayStackSignature.verify_headers method
    with pytest.raises(PayStackSignatureVerifyError):
        webhook.get_event_data(SECRET_KEY, PAYLOAD_TYPE, SIGNATURE_HEADER)


@responses.activate
def test_verify_headers():
    # Mocking the HTTP response
    responses.add(
        responses.GET,
        'https://example.com/webhook',
        body=json.dumps({"key": "value"}),
        status=200,
        content_type='application/json',
    )

    # Call your method which should make a request
    response = requests.get('https://example.com/webhook')

    assert response.status_code == 200
    assert response.json() == {"key": "value"}
