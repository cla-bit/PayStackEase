"""
Wrapper for Paystack Settlements API

The Settlements API allows you to gain insights into payouts made by Paystack to your bank account.
"""
from requests import Response

from datetime import date
from typing import Optional
from paystackease._base import PayStackBaseClientAPI
from paystackease.helpers.tool_kit import STATUS


class SettlementClientAPI(PayStackBaseClientAPI):
    """
    Paystack Settlement API
    Reference: https://paystack.com/docs/api/settlement/
    """

    def list_settlements(
            self,
            per_page: Optional[int] = 50,
            page: Optional[int] = 1,
            status: Optional[STATUS] = None,
            subaccount: Optional[str] = None,
            from_date: Optional[date] = None,
            to_date: Optional[date] = None,
    ) -> Response:
        """
        List settlements made to your settlement accounts

        :param: per_page: The number of records to return per page.
        :param: page: the number to retrieve.
        :param: status: Value can be one of success, processing, pending or failed.
        :param: subaccount:
        :param: from_date: A timestamp from which to start listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param: to_date: A timestamp from which to start listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        :return: The response from the API
        :rtype: Response object
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
            per_page: Optional[int] = 50,
            page: Optional[int] = 1,
            from_date: Optional[date] = None,
            to_date: Optional[date] = None,
    ) -> Response:
        """
        Get the transactions that make up a particular settlement

        :param: settlement_id: The id of the settlement.
        :param: per_page: The number of records to return per page.
        :param: page: the number to retrieve.
        :param: from_date: A timestamp from which to start listing settlements
        :param: to_date: A timestamp from which to start listing settlements

        :return: The response from the API
        :rtype: Response object
        
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
