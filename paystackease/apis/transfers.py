""" Wrapper for Paystack Transfers APIs
The Transfers API allows you to automate sending money to your customers.
"""

from datetime import date
from typing import Optional, List, Dict

from paystackease.base import PayStackBaseClientAPI


class TransfersClientAPI(PayStackBaseClientAPI):
    """Paystack Transfers API
    Reference: https://paystack.com/docs/api/transfer/
    """

    def initiate_transfer(
        self,
        transfer_source: str,
        amount: int,
        transfer_recipient: str,
        reason: Optional[str] = None,
        currency: Optional[str] = None,
        reference: Optional[str] = None,
    ) -> dict:
        """Initiate a transfer. Upgrade your business to a Registered Business to use
        :param transfer_source: Where should we transfer from? Only balance for now
        :param amount: Amount to transfer in kobo if currency is NGN and pesewas if currency is GHS.
        :param transfer_recipient: The code of the recipient
        :param currency: The currency of the transfer
        :param reason: The reason for the transfer
        :param reference: If specified, the field should be a unique identifier (in lowercase) for the object.
        Only -,_ and alphanumeric characters allowed.

        :return: The response from the API
        :rtype: dict
        """
        data = {
            "source": transfer_source,
            "amount": amount,
            "recipient": transfer_recipient,
            "reason": reason,
            "currency": currency,
            "reference": reference,
        }
        return self._post_request("/transfer", data=data)

    def finalize_transfer(self, transfer_code: str, otp: str) -> dict:
        """Finalize an initiated transfer
        :param transfer_code: The code of the transfer to finalize
        :param otp: The OTP sent to the business phone to verify transfer

        :return: The response from the API
        :rtype: dict
        """
        data = {"transfer_code": transfer_code, "otp": otp}
        return self._post_request("/transfer/finalize_transfer", data=data)

    def initiate_bulk_transfer(
        self, transfer_source: str, transfers: List[Dict[str, str]]
    ) -> dict:
        """Batch multiple transfers in a single request
        :param transfer_source: Where should we transfer from? Only balance for now
        :param transfers: A list of transfer objects keys [ { amount | recipient | reference | reason } ]

        :return: The response from the API
        :rtype: dict
        """
        data = {"source": transfer_source, "transfers": transfers}
        return self._post_request("/transfer/bulk", data=data)

    def list_transfers(
        self,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        customer_id: Optional[str] = None,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
    ) -> dict:
        """List transfers
        :param per_page: The number of records to return per page.
        :param page: The page number to retrieve.
        :param customer_id:
        :param from_date:
        :param to_date:

        :return: The response from the API
        :rtype: dict
        """
        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "perPage": per_page,
            "page": page,
            "customer": customer_id,
            "from": from_date,
            "to": to_date,
        }
        return self._get_request("/transfer", params=params)

    def fetch_transfer(self, id_or_code: str) -> dict:
        """Get details of a transfer
        :param id_or_code: The id or code of the transfer

        :return: The response from the API
        :rtype: dict
        """
        return self._get_request(f"/transfer/{id_or_code}")

    def verify_transfer(self, reference: str) -> dict:
        """Verify a transfer
        :param reference: The reference of the transfer to verify

        :return: The response from the API
        :rtype: dict
        """
        return self._post_request(f"/transfer/verify/{reference}")
