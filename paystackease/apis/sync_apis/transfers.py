"""
Wrapper for Paystack Transfers APIs

The Transfers API allows you to automate sending money to your customers.
"""

from datetime import date
from typing import Optional, List, Dict, Any, Union

from paystackease.core import PayStackResponse, SyncRequestAPI
from paystackease.helpers import Currency


class TransfersClientAPI(SyncRequestAPI):
    """
    Paystack Transfers API
    Reference: https://paystack.com/docs/api/transfer/
    """

    def initiate_transfer(
            self,
            transfer_source: str,
            amount: int,
            transfer_recipient: str,
            reason: Optional[Union[str, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            reference: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
        """
        Initiate a transfer. Upgrade your business to a Registered Business to use

        :param: transfer_source: Where should we transfer from? Only balance for now
        :param: amount: Amount to transfer in kobo if currency is NGN and pesewas if currency is GHS.
        :param: transfer_recipient: The code of the recipient
        :param: currency: The currency of the transfer
        :param: reason: The reason for the transfer
        :param: reference: If specified, the field should be a unique identifier (in lowercase) for the object.
                            Only -,_ and alphanumeric characters allowed.

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
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

    def finalize_transfer(self, transfer_code: str, otp: str) -> PayStackResponse:
        """
        Finalize an initiated transfer

        :param: transfer_code: The code of the transfer to finalize
        :param: otp: The OTP sent to the business phone to verify transfer

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"transfer_code": transfer_code, "otp": otp}
        return self._post_request("/transfer/finalize_transfer", data=data)

    def initiate_bulk_transfer(
            self, transfer_source: str, transfers: List[Dict[str, Any]]
    ) -> PayStackResponse:
        """
        Batch multiple transfers in a single request

        :param: transfer_source: Where should we transfer from? Only balance for now
        :param: transfers: A list of transfer objects keys [ { amount | recipient | reference | reason } ]

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"source": transfer_source, "transfers": transfers}
        return self._post_request("/transfer/bulk", data=data)

    def list_transfers(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            customer_id: Optional[Union[str, None]] = None,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
    ) -> PayStackResponse:
        """
        List transfers

        :param: per_page: The number of records to return per page.
        :param: page: The page number to retrieve.
        :param: customer_id
        :param: from_date
        :param: to_date

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
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

    def fetch_transfer(self, id_or_code: str) -> PayStackResponse:
        """
        Get details of a transfer

        :param: id_or_code: The id or code of the transfer

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"/transfer/{id_or_code}")

    def verify_transfer(self, reference: str) -> PayStackResponse:
        """
        Verify a transfer

        :param: reference: The reference of the transfer to verify

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._post_request(f"/transfer/verify/{reference}")
