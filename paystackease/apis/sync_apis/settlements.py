"""
Wrapper for Paystack Settlements API

The Settlements API allows you to gain insights into payouts made by Paystack to your bank account.
"""

from datetime import date
from typing import Optional, Union

from paystackease.core import PayStackResponse, SyncRequestAPI
from paystackease.helpers import STATUS


class SettlementClientAPI(SyncRequestAPI):
    """
    Paystack Settlement API
    Reference: https://paystack.com/docs/api/settlement/
    """

    def list_settlements(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            status: Optional[Union[STATUS, None]] = None,
            subaccount: Optional[Union[str, None]] = None,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
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

        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "perPage": per_page,
            "page": page,
            "status": status,
            "subaccount": subaccount,
            "from": from_date,
            "to": to_date,
        }
        return self._get_request("/settlement", params=params)

    def list_settlement_transactions(
            self,
            settlement_id: int,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
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

        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {"perPage": per_page, "page": page, "from": from_date, "to": to_date}
        return self._get_request(
            f"/settlement/{settlement_id}/transactions", params=params
        )
