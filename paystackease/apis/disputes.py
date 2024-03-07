""" Wrapper for Paystack Disputes API
The Disputes API allows you manage transaction disputes on your integration.
"""

from datetime import date
from typing import Optional
from paystackease.base import PayStackBaseClientAPI


class DisputesClientAPI(PayStackBaseClientAPI):
    """Paystack Disputes API
    Reference: https://paystack.com/docs/api/dispute/
    """

    def list_disputes(
        self,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        transaction_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> dict:
        """List disputes filed against you
        :param from_date: A timestamp from which to start listing dispute e.g. 2016-09-21
        :param to_date: A timestamp from which to start listing dispute e.g. 2016-09-21
        :param per_page:
        :param page:
        :param transaction_id:
        :param status: Dispute Status. Acceptable values:
        { awaiting-merchant-feedback | awaiting-bank-feedback | pending | resolved }

        :return: The response from the API
        :rtype: dict
        """
        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "perPage": per_page,
            "page": page,
            "from": from_date,
            "to": to_date,
            "transaction": transaction_id,
            "status": status,
        }
        return self._get_request("/dispute", params=params)

    def fetch_dispute(self, dispute_id: str) -> dict:
        """Fetch details about a dispute
        :param dispute_id: The dispute ID to fetch

        :return: The response from the API
        :rtype: dict
        """
        return self._get_request(f"/dispute/{dispute_id}")

    def list_transaction_disputes(self, transaction_id: str) -> dict:
        """List disputes for a transaction
        :param transaction_id: The transaction id to fetch

        :return: The response from the API
        :rtype: dict
        """
        return self._get_request(f"/dispute/transaction/{transaction_id}")

    def update_dispute(
        self,
        dispute_id: str,
        refund_amount: int,
        uploaded_filename: Optional[str] = None,
    ) -> dict:
        """Update details of a dispute
        :param dispute_id: The dispute id to fetch
        :param refund_amount: The amount to refund to the customer
        :param uploaded_filename: filename of attachment returned via
        response from upload url(GET /dispute/:id/upload_url)

        :return: The response from the API
        :rtype: dict
        """
        data = {"refund_amount": refund_amount, "uploaded_filename": uploaded_filename}
        return self._put_request(f"/dispute/{dispute_id}", data=data)

    def add_evidence(
        self,
        dispute_id: str,
        customer_email: str,
        customer_name: str,
        customer_phone: str,
        service_details: str,
        delivery_address: Optional[str] = None,
        delivery_date: Optional[date] = None,
    ) -> dict:
        """Add evidence to a dispute
        :param dispute_id: The dispute id to fetch
        :param customer_email: The customer email
        :param customer_name: The customer name
        :param customer_phone: The customer phone
        :param service_details: The service details
        :param delivery_address: The delivery address
        :param delivery_date: The delivery date: YYYY-MM-DD
        """
        # convert date to string
        delivery_date = self._convert_to_string(delivery_date)

        data = {
            "customer_email": customer_email,
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "service_details": service_details,
            "delivery_address": delivery_address,
            "delivery_date": delivery_date,
        }
        return self._post_request(f"/dispute/{dispute_id}/evidence", data=data)

    def get_upload_url(self, dispute_id: str, uploaded_filename: str) -> dict:
        """Get upload url for dispute evidence
        :param dispute_id: The dispute id to fetch
        :param uploaded_filename: The file name, with its extension, that you want to upload. e.g. filename.pdf

        :return: The response from the API
        :rtype: dict
        """
        params = {"uploaded_filename": uploaded_filename}
        return self._get_request(f"/dispute/{dispute_id}/upload_url", params=params)

    def resolve_dispute(
        self,
        dispute_id: str,
        resolution: str,
        message: str,
        refund_amount: int,
        uploaded_filename: str,
        evidence: Optional[int] = None,
    ) -> dict:
        """Resolve a dispute
        :param dispute_id: The dispute id to fetch
        :param resolution: The resolution to resolve the dispute: Accepted values: { merchant-accepted | declined }.
        :param message: The message for resolution
        :param refund_amount: The amount to refund to the customer
        :param uploaded_filename: filename of attachment returned via response from method get_upload_url
        :param evidence: The evidence id for fraud claims

        :return: The response from the API
        :rtype: dict
        """
        data = {
            "resolution": resolution,
            "message": message,
            "refund_amount": refund_amount,
            "uploaded_filename": uploaded_filename,
            "evidence": evidence,
        }
        return self._put_request(f"/dispute/{dispute_id}/resolve", data=data)

    def export_disputes(
        self,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
        transaction_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> dict:
        """Export disputes
        :param per_page:
        :param page:
        :param from_date: The start date to fetch disputes from
        :param to_date: The end date to fetch disputes from
        :param transaction_id: The transaction ID
        :param status: The dispute status:
        Acceptable values: { awaiting-merchant-feedback | awaiting-bank-feedback | pending | resolved }
        """
        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "perPage": per_page,
            "page": page,
            "from": from_date,
            "to": to_date,
            "transaction": transaction_id,
            "status": status,
        }
        return self._get_request("/dispute/export", params=params)
