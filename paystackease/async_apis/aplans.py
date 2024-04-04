"""
Wrapper for Asynchronous Paystack Plans API

The Plans API allows you to create and manage installment payment options on your integration.
"""
from aiohttp import ClientResponse

from typing import Optional
from paystackease._abase import AsyncPayStackBaseClientAPI
from paystackease.helpers.tool_kit import Interval


class AsyncPlanClientAPI(AsyncPayStackBaseClientAPI):
    """
    Paystack Plan API
    Reference: https://paystack.com/docs/api/plan/
    """

    async def create_plan(
            self,
            name: str,
            amount: int,
            interval: Interval,
            currency: str,
            invoice_limit: int,
            send_invoices: bool,
            send_sms: bool,
            description: Optional[str] = None,
    ) -> ClientResponse:
        """
        Create a plan

        :param: name: Name of the plan
        :param: amount: Amount of the plan
        :param: interval: Interval of the plan. Values [Interval.value.value]
        :param: description: Description of the plan
        :param: send_invoices: Send invoices to customer
        :param: send_sms: Send SMS to customer
        :param: currency: Currency of the plan
        :param: invoice_limit: Invoice limit of the plan

        :return: The response from the API
        :rtype: ClientResponse object
        """
        # convert to strings
        send_invoices = self._convert_to_string(send_invoices)
        send_sms = self._convert_to_string(send_sms)

        data = {
            "name": name,
            "amount": amount,
            "interval": interval,
            "description": description,
            "send_invoices": send_invoices,
            "send_sms": send_sms,
            "currency": currency,
            "invoice_limit": invoice_limit,
        }
        return await self._post_request("/plan", data=data)

    async def list_plans(
            self,
            per_page: Optional[int] = 50,
            page: Optional[int] = 1,
            status: Optional[str] = None,
            interval: Optional[Interval] = None,
            amount: Optional[int] = None,
    ) -> ClientResponse:
        """
        List all the plans

        :param: per_page: Number of records to return
        :param: page:  number to return
        :param: status: Filter list by plans with specified status
        :param: interval: Filter list by plans with specified interval
        :param: amount

        :return: The response from the API
        :rtype: ClientResponse object
        """
        params = {
            "perPage": per_page,
            "page": page,
            "status": status,
            "interval": interval,
            "amount": amount,
        }
        return await self._get_request("/plan", params=params)

    async def fetch_plan(self, id_or_code: str) -> ClientResponse:
        """
        Get details of a plan

        :param: id_or_code: ID or Code of the plan

        :return: The response from the API
        :rtype: ClientResponse object
        """
        return await self._get_request(f"/plan/{id_or_code}")

    async def update_plan(
            self,
            id_or_code: str,
            name: str,
            amount: int,
            interval: Interval,
            send_invoices: bool,
            send_sms: bool,
            currency: str,
            invoice_limit: int,
            description: Optional[str] = None,
    ) -> ClientResponse:
        """
        Update a plan detail

        :param: id_or_code: ID or Code of the plan
        :param: name: Name of the plan
        :param: amount: Amount of the plan
        :param: interval: Interval of the plan. [Interval.value.value]
        :param: description:
        :param: send_invoices:
        :param: send_sms:
        :param: currency:
        :param: invoice_limit:

        :return: The response from the API
        :rtype: ClientResponse object
        """
        # convert to strings
        send_invoices = self._convert_to_string(send_invoices)
        send_sms = self._convert_to_string(send_sms)

        data = {
            "name": name,
            "amount": amount,
            "interval": interval,
            "description": description,
            "send_invoices": send_invoices,
            "send_sms": send_sms,
            "currency": currency,
            "invoice_limit": invoice_limit,
        }
        return await self._put_request(f"/plan/{id_or_code}", data=data)
