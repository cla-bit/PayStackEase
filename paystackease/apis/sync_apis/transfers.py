"""
Wrapper for Paystack Transfers APIs

The Transfers API allows you to automate sending money to your customers.
"""

from typing import Optional, List, Union

from paystackease.src import PayStackResponse, SyncRequestAPI
from paystackease.helpers import Currency, transfer_endpoint, PageModel, DatePageModel, TransferBulkModel


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
        return self._post_request(transfer_endpoint, data=data)

    def finalize_transfer(self, transfer_code: str, otp: str) -> PayStackResponse:
        """
        Finalize an initiated transfer

        :param: transfer_code: The code of the transfer to finalize
        :param: otp: The OTP sent to the business phone to verify transfer

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"transfer_code": transfer_code, "otp": otp}
        return self._post_request(f"{transfer_endpoint}finalize_transfer", data=data)

    def initiate_bulk_transfer(
            self, transfer_source: str, transfers: Union[TransferBulkModel, List[TransferBulkModel]]
    ) -> PayStackResponse:
        """
        Batch multiple transfers in a single request

        :param: transfer_source: Where should we transfer from? Only balance for now
        :param: transfers: A list of transfer objects keys [ { amount | recipient | reference | reason } ]

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        if isinstance(transfers, TransferBulkModel):
            transfers = [transfers]

        if not isinstance(transfers, list) or not all(isinstance(obj, TransferBulkModel) for obj in transfers):
            raise ValueError("transfers must be a list of TransferBulkModel or TransferBulkModel")

        if not transfers:
            raise ValueError("The list of transfer bulks can not be empty.")

        transfer_bulk = [obj.model_dump() for obj in transfers]

        data = {"source": transfer_source, "transfers": transfer_bulk}
        return self._post_request(f"{transfer_endpoint}bulk", data=data)

    def list_transfers(
            self,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
            customer_id: Optional[Union[str, None]] = None,
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

        params = {
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
            "customer": customer_id,
        }
        return self._get_request(transfer_endpoint, params=params)

    def fetch_transfer(self, id_or_code: str) -> PayStackResponse:
        """
        Get details of a transfer

        :param: id_or_code: The id or code of the transfer

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"{transfer_endpoint}{id_or_code}")

    def verify_transfer(self, reference: str) -> PayStackResponse:
        """
        Verify a transfer

        :param: reference: The reference of the transfer to verify

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._post_request(f"{transfer_endpoint}verify/{reference}")
