""" Test for synchronous Customers """

import json
from datetime import date
import pytest
import responses

from paystackease.helpers.tool_kit import DisputeStatus, Resolution
from tests.conftest import disputes_client


@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page", "transaction_id", "status"),
    [
        (date(2012, 12, 12), date(2012, 12, 12), 1, 10, "TRANS_1234qwer", DisputeStatus.MERCHANT_FEEDBACK.value),
        (None, None, None, None, None, None)
    ]
)
@responses.activate
def test_list_disputes(disputes_client, from_date, to_date, per_page, page, transaction_id, status):
    """ Test for synchronous Customers """
    url = "https://api.paystack.co/dispute"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "from": from_date,
        "to": to_date,
        "transaction": transaction_id,
        "status": status,
    }
    # Construct the expected URL with parameters
    query_string = '&'.join(f'{key}={value}' for key, value in url_params.items() if value is not None)
    expected_url = url + ('?' + query_string if query_string else '')

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = disputes_client.list_disputes(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
        transaction_id=transaction_id,
        status=status
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@responses.activate
def test_fetch_dispute(disputes_client):
    """ Test for synchronous Customers """
    dispute_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/{dispute_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = disputes_client.fetch_dispute(dispute_id=dispute_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@responses.activate
def test_list_trans_disputes(disputes_client):
    """ Test for synchronous Customers """
    transaction_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/transaction/{transaction_id}"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = disputes_client.list_transaction_disputes(transaction_id=transaction_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(
    ("refund_amount", "uploaded_file"),
    [
        (10000, "123qweasd.pdf"),
        (1000, None)
    ]
)
@responses.activate
def test_update_dispute(disputes_client, refund_amount, uploaded_file):
    """ Test for synchronous Customers """
    dispute_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/{dispute_id}"
    response_data = {"status": "success"}
    expected_data = {
        "refund_amount": refund_amount,
        "uploaded_filename": uploaded_file,
    }

    responses.add(
        responses.PUT,
        url,
        status=200,
        json=response_data,
    )
    response = disputes_client.update_dispute(
        dispute_id=dispute_id,
        refund_amount=refund_amount,
        uploaded_filename=uploaded_file
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("customer_email", "customer_name", "customer_phone", "service_details",
     "delivery_address", "delivery_date"),
    [
        ("test@email.com", "test", "08012345678", "Testing", "Testing address", date(2012, 12, 12)),
        ("test@email.com", "test", "08012345678", "Testing", None, None),
    ]
)
@responses.activate
def test_add_evidence(disputes_client, customer_email, customer_name,
                      customer_phone, service_details, delivery_address,
                      delivery_date):
    """ Test for synchronous Customers """
    dispute_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/{dispute_id}/evidence"
    response_data = {"status": "success"}
    expected_data = {
        "customer_email": customer_email,
        "customer_name": customer_name,
        "customer_phone": customer_phone,
        "service_details": service_details,
        "delivery_address": delivery_address,
        "delivery_date": delivery_date.strftime("%Y-%m-%d") if delivery_date else None,
    }
    responses.add(
        responses.POST,
        url,
        status=200,
        json=response_data,
    )
    response = disputes_client.add_evidence(
        dispute_id=dispute_id,
        customer_email=customer_email,
        customer_name=customer_name,
        customer_phone=customer_phone,
        service_details=service_details,
        delivery_address=delivery_address,
        delivery_date=delivery_date,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(("uploaded_filename",), [("1234qwerasdf.pdf",)])
@responses.activate
def test_get_upload_url(disputes_client, uploaded_filename):
    """ Test for synchronous Customers """
    dispute_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/{dispute_id}/upload_url"
    response_data = {"status": "success"}
    url_params = {"uploaded_filename": uploaded_filename}

    # Construct the expected URL with parameters
    query_string = '&'.join(f'{key}={value}' for key, value in url_params.items() if value is not None)
    expected_url = url + ('?' + query_string if query_string else '')

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = disputes_client.get_upload_url(
        dispute_id=dispute_id,
        uploaded_filename=uploaded_filename
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None


@pytest.mark.parametrize(
    ("resolution", "message", "refund_amount", "uploaded_filename", "evidence"),
    [
        (Resolution.MERCHANT.value, "Resolved", 1000, "test_asd1234.pdf", 1234),
        (Resolution.DECLINED.value, "Resolved", 1000, "test_asd1234.pdf", None),
    ]
)
@responses.activate
def test_resolve_dispute(disputes_client, resolution, message, refund_amount, uploaded_filename, evidence):
    """ Test for synchronous Customers """
    dispute_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/{dispute_id}/resolve"
    response_data = {"status": "success"}
    expected_data = {
        "resolution": resolution,
        "message": message,
        "refund_amount": refund_amount,
        "uploaded_filename": uploaded_filename,
        "evidence": evidence,
    }
    responses.add(
        responses.PUT,
        url,
        status=200,
        json=response_data,
    )
    response = disputes_client.resolve_dispute(
        dispute_id=dispute_id,
        resolution=resolution,
        message=message,
        refund_amount=refund_amount,
        uploaded_filename=uploaded_filename,
        evidence=evidence
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert json.loads(responses.calls[0].request.body) == expected_data
    assert response is not None


@pytest.mark.parametrize(
    ("per_page", "page", "from_date", "to_date", "transaction_id", "status"),
    [
        (1, 20, date(2012, 12, 12), date(2012, 12, 12),
         "TRANS_test1234", DisputeStatus.PENDING.value),
        (None, None, None, None, None, None)
    ]
)
@responses.activate
def test_export_dispute(disputes_client, per_page, page, from_date, to_date,
                        transaction_id, status):
    """ Test for synchronous Customers """
    url = f"https://api.paystack.co/dispute/export"
    response_data = {"status": "success"}
    url_params = {
        "perPage": per_page,
        "page": page,
        "from": from_date,
        "to": to_date,
        "transaction": transaction_id,
        "status": status,
    }

    # Construct the expected URL with parameters
    query_string = '&'.join(f'{key}={value}' for key, value in url_params.items() if value is not None)
    expected_url = url + ('?' + query_string if query_string else '')

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = disputes_client.export_disputes(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
        transaction_id=transaction_id,
        status=status
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response is not None
