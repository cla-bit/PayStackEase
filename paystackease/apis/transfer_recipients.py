"""
Wrapper for Paystack Transfer Recipient APIs

The Transfer Recipients API allows you to create and manage beneficiaries that you send money to.
"""

from datetime import date
from typing import Optional, Dict, List, Any, Union
from paystackease._base import PayStackBaseClientAPI
from paystackease._utils import Response
from paystackease.helpers.tool_kit import Currency


class TransferRecipientsClientAPI(PayStackBaseClientAPI):
    """
    Paystack Transfer Recipients API
    Reference: https://paystack.com/docs/api/transfer-recipient/
    """

    def create_transfer_recipients(
            self,
            recipient_type: str,
            recipient_name: str,
            account_number: str,
            bank_code: str,
            description: Optional[Union[str, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            authorization_code: Optional[Union[str, None]] = None,
            metadata: Optional[Union[Dict[str, Any], None]] = None,
    ) -> Response:
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

        :return: The response from the API
        :rtype: Response object
        """
        data = {
            "type": recipient_type,
            "name": recipient_name,
            "account_number": account_number,
            "bank_code": bank_code,
            "description": description,
            "currency": currency,
            "authorization_code": authorization_code,
            "metadata": metadata,
        }
        return self._post_request("/transferrecipient", data=data)

    def bulk_create_transfer_recipient(self, batch: List[Dict[str, Any]]) -> Response:
        """
        Create multiple transfer recipients in batches.

        :param: batch: A list of transfer recipient object
                        keys [ { type, name, account_number, bank_code, currency etc. }]

        :return: The response from the API
        :rtype: Response object
        """
        data = {"batch": batch}
        return self._post_request("/transferrecipient/bulk", data=data)

    def list_transfer_recipients(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
    ) -> Response:
        """
        List transfer recipients

        :param: per_page: The number of records to return per page.
        :param: page: The page number to retrieve.
        :param: from_date:
        :param: to_date:

        :return: The response from the API
        :rtype: Response object
        """

        # convert date to strings
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {"perPage": per_page, "page": page, "from": from_date, "to": to_date}
        return self._get_request("/transferrecipient", params=params)

    def fetch_transfer_recipient(self, id_or_code: str) -> Response:
        """
        Fetch details of a transfer recipient

        :param: id_or_code: The id or code of the transfer recipient

        :return: The response from the API
        :rtype: Response object
        """
        return self._get_request(f"/transferrecipient/{id_or_code}")

    def update_transfer_recipient(
            self,
            id_or_code: str,
            recipient_name: str,
            recipient_email: Optional[Union[str, None]] = None,
    ) -> Response:
        """
        Update a transfer recipient

        :param: id_or_code: The id or code of the transfer recipient
        :param: recipient_name: The name of the transfer recipient
        :param: recipient_email: The email of the transfer recipient

        :return: The response from the API
        :rtype: Response object
        """
        data = {"name": recipient_name, "email": recipient_email}
        return self._put_request(f"/transferrecipient/{id_or_code}", data=data)

    def delete_transfer_recipient(self, id_or_code: str) -> Response:
        """
        Delete a transfer recipient

        :param: id_or_code: The id or code of the transfer recipient

        :return: The response from the API
        :rtype: Response object
        """
        return self._delete_request(f"/transferrecipient/{id_or_code}")
