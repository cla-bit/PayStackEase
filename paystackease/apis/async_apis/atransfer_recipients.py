"""
Wrapper for Asynchronous Paystack Transfer Recipient APIs

The Transfer Recipients API allows you to create and manage beneficiaries that you send money to.
"""

from typing import Optional, Union

from paystackease.src import AsyncRequestAPI, PayStackResponse
from paystackease.helpers import Currency, transfer_recipients_endpoint, MetaDataModel, BatchModel, DatePageModel, \
    PageModel


class AsyncTransferRecipientsClientAPI(AsyncRequestAPI):
    """
    Paystack Transfer Recipients API
    Reference: https://paystack.com/docs/api/transfer-recipient/
    """

    async def create_transfer_recipients(
            self,
            recipient_type: str,
            recipient_name: str,
            account_number: str,
            bank_code: str,
            description: Optional[Union[str, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            authorization_code: Optional[Union[str, None]] = None,
            metadata: Optional[MetaDataModel] = None,
    ) -> PayStackResponse:
        """
        Create a transfer recipient

        :param: recipient_type: The type of transfer recipient:[ nuban | ghipss | mobile_money | basa ]
        :param: recipient_name: The name of the transfer recipient according to their account registration
        :param: account_number: transfer recipient's account number.
                                Required for all recipient types except authorization
        :param: bank_code: transfer recipient's bank code. Required for all recipient types except authorization
        :param: description:
        :param: currency: transfer recipient's currency. [Currency.value.value ]
        :param: authorization_code: transfer recipient's authorization code from previous transaction
        :param: metadata: transfer recipient's metadata

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "type": recipient_type,
            "name": recipient_name,
            "account_number": account_number,
            "bank_code": bank_code,
            "description": description,
            "currency": currency,
            "authorization_code": authorization_code,
            **(metadata.model_dump() if metadata else {}),
        }
        return await self._post_request(transfer_recipients_endpoint, data=data)

    async def bulk_create_transfer_recipient(self, batch: BatchModel) -> PayStackResponse:
        """
        Create multiple transfer recipients in batches.

        :param: batch: A list of transfer recipient object
                        keys [ { type, name, account_number, bank_code, currency etc. }]

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {**batch.model_dump()}
        return await self._post_request(f"{transfer_recipients_endpoint}bulk", data=data)

    async def list_transfer_recipients(
            self,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
    ) -> PayStackResponse:
        """
        List transfer recipients

        :param: per_page: The number of records to return per page.
        :param: page: The page number to retrieve.
        :param: from_date:
        :param: to_date:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        params = {
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
        }
        return await self._get_request(transfer_recipients_endpoint, params=params)

    async def fetch_transfer_recipient(self, id_or_code: str) -> PayStackResponse:
        """
        Fetch details of a transfer recipient

        :param: id_or_code: The id or code of the transfer recipient

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"{transfer_recipients_endpoint}{id_or_code}")

    async def update_transfer_recipient(
            self,
            id_or_code: str,
            recipient_name: str,
            recipient_email: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
        """
        Update a transfer recipient

        :param: id_or_code: The id or code of the transfer recipient
        :param: recipient_name: The name of the transfer recipient
        :param: recipient_email: The email of the transfer recipient

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"name": recipient_name, "email": recipient_email}
        return await self._put_request(f"{transfer_recipients_endpoint}{id_or_code}", data=data)

    async def delete_transfer_recipient(self, id_or_code: str) -> PayStackResponse:
        """
        Delete a transfer recipient

        :param: id_or_code: The id or code of the transfer recipient

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._delete_request(f"{transfer_recipients_endpoint}{id_or_code}")
