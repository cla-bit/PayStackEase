""" Wrapper for Asynchronous Paystack Refund API
The Refunds API allows you to create and manage transaction refunds.
"""

from datetime import date
from typing import Optional
from paystackease.abase import AsyncPayStackBaseClientAPI


class AsyncRefundClientAPI(AsyncPayStackBaseClientAPI):
    """Paystack Refund API
    Reference: https://paystack.com/docs/api/refund/
    """

    async def create_refund(
        self,
        transaction_ref_or_id: str,
        amount: Optional[int] = None,
        currency: Optional[str] = None,
        customer_note: Optional[str] = None,
        merchant_note: Optional[str] = None,
    ) -> dict:
        """Create a refund
        :param transaction_ref_or_id: The transaction id or reference to fetch
        :param amount: The amount to refund
        :param currency: The currency to refund { Currency.value.value }
        :param customer_note: The customer note or reason
        :param merchant_note: The merchant note or reason

        :return: The response from the API
        :rtype: dict
        """
        data = {
            "transaction": transaction_ref_or_id,
            "amount": amount,
            "currency": currency,
            "customer_note": customer_note,
            "merchant_note": merchant_note,
        }
        return await self.post_request("/refund", data=data)

    async def list_refunds(
        self,
        reference: Optional[str] = None,
        currency: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
    ) -> dict:
        """List refunds
        :param reference: The transaction reference to fetch for the refund
        :param currency: The currency to refund
        :param per_page:
        :param page:
        :param from_date: A timestamp at which to stop listing refund e.g. 2016-09-21
        :param to_date: A timestamp at which to stop listing refund e.g. 2016-09-21

        :return: The response from the API
        :rtype: dict
        """
        # convert date to string
        from_date = self.convert_to_string(from_date)
        to_date = self.convert_to_string(to_date)

        params = {
            "reference": reference,
            "currency": currency,
            "perPage": per_page,
            "page": page,
            "from": from_date,
            "to": to_date,
        }
        return await self.get_request("/refund", params=params)

    async def fetch_refund(self, reference: str) -> dict:
        """Fetch a refund
        :param reference: The transaction reference to fetch for the refund

        :return: The response from the API
        :rtype: dict
        """
        return await self.get_request(f"/refund/{reference}")
