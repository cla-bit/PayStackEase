"""
Wrapper for Asynchronous Paystack Refund API

The Refunds API allows you to create and manage transaction refunds.
"""

from datetime import date
from typing import Optional, Union

from paystackease.src import AsyncRequestAPI, PayStackResponse
from paystackease.helpers import Currency, refund_endpoint, PageModel, DatePageModel


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
        return await self._post_request(refund_endpoint, data=data)

    async def list_refunds(
            self,
            reference: Optional[Union[str, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
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

        params = {
            "reference": reference,
            "currency": currency,
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
        }
        return await self._get_request(refund_endpoint, params=params)

    async def fetch_refund(self, reference: str) -> PayStackResponse:
        """
        Fetch a refund

        :param: reference: The transaction reference to fetch for the refund

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"{refund_endpoint}{reference}")
