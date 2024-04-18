"""
Wrapper for Asynchronous Paystack Refund API

The Refunds API allows you to create and manage transaction refunds.
"""

from datetime import date
from typing import Optional, Union

from paystackease.core import AsyncRequestAPI, PayStackResponse
from paystackease.helpers import Currency


class AsyncRefundClientAPI(AsyncRequestAPI):
    """
    Paystack Refund API
    Reference: https://paystack.com/docs/api/refund/
    """

    async def create_refund(
            self,
            transaction_ref_or_id: str,
            amount: Optional[Union[int, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            customer_note: Optional[Union[str, None]] = None,
            merchant_note: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
        """
        Create a refund

        :param: transaction_ref_or_id: The transaction id or reference to fetch
        :param: amount: The amount to refund
        :param: currency: The currency to refund { Currency.value.value }
        :param: customer_note: The customer note or reason
        :param: merchant_note: The merchant note or reason

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "transaction": transaction_ref_or_id,
            "amount": amount,
            "currency": currency,
            "customer_note": customer_note,
            "merchant_note": merchant_note,
        }
        return await self._post_request("/refund", data=data)

    async def list_refunds(
            self,
            reference: Optional[Union[str, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
    ) -> PayStackResponse:
        """
        List refunds

        :param: reference: The transaction reference to fetch for the refund
        :param: currency: The currency to refund
        :param: per_page
        :param: page
        :param: from_date: A timestamp at which to stop listing refund
        :param: to_date: A timestamp at which to stop listing refund

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object

        note::

            Date time format: 2016-09-21
        """

        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "reference": reference,
            "currency": currency,
            "perPage": per_page,
            "page": page,
            "from": from_date,
            "to": to_date,
        }
        return await self._get_request("/refund", params=params)

    async def fetch_refund(self, reference: str) -> PayStackResponse:
        """
        Fetch a refund

        :param: reference: The transaction reference to fetch for the refund

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"/refund/{reference}")
