""" Test for synchronous Customers """

from datetime import date
import pytest

from paystackease.helpers.tool_kit import DisputeStatus, Resolution
from tests.conftest import async_disputes_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("from_date", "to_date", "per_page", "page", "transaction_id", "status"),
    [
        (date(2012, 12, 12), date(2012, 12, 12), 1, 10, "TRANS_1234qwer", DisputeStatus.RESOLVED.value),
        (None, None, None, None, None, None)
    ]
)
async def test_list_disputes(async_disputes_client, mocked_responses, from_date, to_date, per_page, page, transaction_id, status):
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

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_disputes_client.list_disputes(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
        transaction_id=transaction_id,
        status=status
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_fetch_dispute(async_disputes_client, mocked_responses):
    """ Test for synchronous Customers """
    dispute_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/{dispute_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_disputes_client.fetch_dispute(dispute_id=dispute_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
async def test_list_trans_disputes(async_disputes_client, mocked_responses):
    """ Test for synchronous Customers """
    transaction_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/transaction/{transaction_id}"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_disputes_client.list_transaction_disputes(transaction_id=transaction_id)
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("refund_amount", "uploaded_file"),
    [
        (10000, "123qweasd.pdf"),
        (1000, None)
    ]
)
async def test_update_dispute(async_disputes_client, mocked_responses, refund_amount, uploaded_file):
    """ Test for synchronous Customers """
    dispute_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/{dispute_id}"
    response_data = {"status": "success"}
    expected_data = {
        "refund_amount": refund_amount,
        "uploaded_filename": uploaded_file,
    }

    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_disputes_client.update_dispute(
        dispute_id=dispute_id,
        refund_amount=refund_amount,
        uploaded_filename=uploaded_file
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("customer_email", "customer_name", "customer_phone", "service_details",
     "delivery_address", "delivery_date"),
    [
        ("test@email.com", "test", "08012345678", "Testing", "Testing address", date(2012, 12, 12)),
        ("test@email.com", "test", "08012345678", "Testing", None, None),
    ]
)
async def test_add_evidence(async_disputes_client, mocked_responses, customer_email, customer_name,
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
    mocked_responses.post(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_disputes_client.add_evidence(
        dispute_id=dispute_id,
        customer_email=customer_email,
        customer_name=customer_name,
        customer_phone=customer_phone,
        service_details=service_details,
        delivery_address=delivery_address,
        delivery_date=delivery_date,
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(("uploaded_filename",), [("1234qwerasdf.pdf",)])
async def test_get_upload_url(async_disputes_client, mocked_responses, uploaded_filename):
    """ Test for synchronous Customers """
    dispute_id = "test-dispute-id"
    url = f"https://api.paystack.co/dispute/{dispute_id}/upload_url"
    response_data = {"status": "success"}
    url_params = {"uploaded_filename": uploaded_filename}

    # Construct the expected URL with parameters
    query_string = '&'.join(f'{key}={value}' for key, value in url_params.items() if value is not None)
    expected_url = url + ('?' + query_string if query_string else '')

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_disputes_client.get_upload_url(
        dispute_id=dispute_id,
        uploaded_filename=uploaded_filename
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("resolution", "message", "refund_amount", "uploaded_filename", "evidence"),
    [
        (Resolution.DECLINED.value, "Resolved", 1000, "test_asd1234.pdf", 1234),
        (Resolution.MERCHANT.value, "Resolved", 1000, "test_asd1234.pdf", None),
    ]
)
async def test_resolve_dispute(async_disputes_client, mocked_responses, resolution, message, refund_amount, uploaded_filename, evidence):
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
    mocked_responses.put(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_disputes_client.resolve_dispute(
        dispute_id=dispute_id,
        resolution=resolution,
        message=message,
        refund_amount=refund_amount,
        uploaded_filename=uploaded_filename,
        evidence=evidence
    )
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("per_page", "page", "from_date", "to_date", "transaction_id", "status"),
    [
        (1, 20, date(2012, 12, 12), date(2012, 12, 12),
         "TRANS_test1234", DisputeStatus.BANK_FEEDBACK.value),
        (None, None, None, None, None, None)
    ]
)
async def test_export_dispute(async_disputes_client, mocked_responses, per_page, page, from_date, to_date,
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

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_disputes_client.export_disputes(
        per_page=per_page,
        page=page,
        from_date=from_date,
        to_date=to_date,
        transaction_id=transaction_id,
        status=status
    )
    mocked_responses.assert_called()
    assert response is not None
