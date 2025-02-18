"""
Wrapper for Asynchronous Paystack Settlements API

The Settlements API allows you to gain insights into payouts made by Paystack to your bank account.
"""

from typing import Optional, Union

from paystackease.src import AsyncRequestAPI, PayStackResponse
from paystackease.helpers import STATUS, settlement_endpoint, PageModel, DatePageModel


class AsyncSettlementClientAPI(AsyncRequestAPI):
    """
    Paystack Settlement API
    Reference: https://paystack.com/docs/api/settlement/
    """

    async def list_settlements(
            self,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
            status: Optional[Union[STATUS, None]] = None,
            subaccount: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
        """
        List settlements made to your settlement accounts

        :param: per_page: The number of records to return per page.
        :param: page: the number to retrieve.
        :param: status: Value can be one of success, processing, pending or failed.
        :param: subaccount:
        :param: from_date: A timestamp from which to start listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param: to_date: A timestamp from which to start listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        params = {
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
            "status": status,
            "subaccount": subaccount,
        }
        return await self._get_request(settlement_endpoint, params=params)

    async def list_settlement_transactions(
            self,
            settlement_id: int,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
    ) -> PayStackResponse:
        """
        Get the transactions that make up a particular settlement

        :param: settlement_id: The id of the settlement.
        :param: per_page: The number of records to return per page.
        :param: page: the number to retrieve.
        :param: from_date: A timestamp from which to start listing settlements
        :param: to_date: A timestamp from which to start listing settlements

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object

        note::

            Date and time format: 2016-09-24T00:00:05.000Z, 2016-09-21

        """

        params = {
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
        }
        return await self._get_request(
            f"{settlement_endpoint}{settlement_id}/transactions", params=params
        )
