"""
Wrapper for Asynchronous Paystack Bulk Charges API.

The Bulk Charges API allows you to create and manage multiple recurring payments from your customers.
"""

from datetime import date

from typing import List, Dict, Optional, Any, Union
from paystackease._abase import AsyncPayStackBaseClientAPI
from paystackease._utils import Response
from paystackease.helpers.tool_kit import STATUS


class AsyncBulkChargesClientAPI(AsyncPayStackBaseClientAPI):
    """
    Paystack Bulk Charges API
    Reference: https://paystack.com/docs/api/bulk-charge/
    """

    async def initiate_bulk_charge(self, objects: List[Dict[str, Any]]) -> Response:
        """
        Send an array of objects with authorization codes and amount

        :param: objects

        note::

            A list of dictionary with authorization codes, amount and reference as keys
            [{"authorization_code": "123456", "amount": 1000, "reference": "123456" }]

        :return: The response from the API
        :rtype: Response object
        """
        return await self._post_request("/bulkcharge", data=objects)

    async def list_bulk_charge_batches(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
    ) -> Response:
        """
        List all bulk charges

        :param: per_page
        :param: page
        :param: from_date
        :param: to_date

        note::

            Date Time format: 2016-09-24T00:00:05.000Z, 2016-09-21

        :return: The response from the API
        :rtype: Response object
        """

        # Convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "perPage": per_page,
            "page": page,
            "from": from_date,
            "to": to_date,
        }
        return await self._get_request("/bulkcharge", params=params)

    async def fetch_bulk_charge_batch(self, id_or_code: str) -> Response:
        """
        Fetch a bulk charge of a specific batch

        :param: id_or_code

        :return: The response from the API
        :rtype: Response object
        """
        return await self._get_request(f"/bulkcharge/{id_or_code}")

    async def fetch_charge_bulk_batch(
            self,
            id_or_code: str,
            status: Optional[Union[STATUS, None]] = None,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
    ) -> Response:
        """
        Fetch a bulk charge of a specific batch

        :param: id_or_code
        :param: status:  {STATUS.value.value}
        :param: per_page
        :param: page
        :param: from_date
        :param: to_date

        note::

            Date Time format: 2016-09-24T00:00:05.000Z, 2016-09-21
            status: STATUS.value.value

        :return: The response from the API
        :rtype: Response object
        """

        # Convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "status": status,
            "perPage": per_page,
            "page": page,
            "from": from_date,
            "to": to_date,
        }
        return await self._get_request(f"/bulkcharge/{id_or_code}/charges", params=params)

    async def pause_bulk_charge_batch(self, batch_code: str) -> Response:
        """
        Pause a bulk charge of a specific batch

        :param: batch_code

        :return: The response from the API
        :rtype: Response object
        """
        return await self._get_request(f"/bulkcharge/pause/{batch_code}")

    async def resume_bulk_charge_batch(self, batch_code: str) -> Response:
        """
        Resume a bulk charge of a specific batch

        :param: batch_code

        :return: The response from the API
        :rtype: Response object
        """
        return await self._get_request(f"/bulkcharge/resume/{batch_code}")
