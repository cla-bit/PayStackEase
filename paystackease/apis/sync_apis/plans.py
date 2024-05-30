"""
Wrapper for Paystack Plans API

The Plans API allows you to create and manage installment payment options on your integration.
"""

from typing import Optional, Union

from paystackease.core import PayStackResponse, SyncRequestAPI
from paystackease.helpers import Interval


class PlanClientAPI(SyncRequestAPI):
    """
    Paystack Plan API
    Reference: https://paystack.com/docs/api/plan/
    """

    def create_plan(
            self,
            name: str,
            amount: int,
            interval: Interval,
            currency: str,
            invoice_limit: int,
            send_invoices: bool,
            send_sms: bool,
            description: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
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

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
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
        return self._post_request("/plan", data=data)

    def list_plans(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            status: Optional[Union[str, None]] = 'active',
            interval: Optional[Union[Interval, None]] = None,
            amount: Optional[Union[int, None]] = None,
    ) -> PayStackResponse:
        """
        List all the plans

        :param: per_page: Number of records to return
        :param: page:  number to return
        :param: status: Filter list by plans with specified status
        :param: interval: Filter list by plans with specified interval
        :param: amount

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        params = {
            "perPage": per_page,
            "page": page,
            "status": status,
            "interval": interval,
            "amount": amount,
        }
        return self._get_request("/plan", params=params)

    def fetch_plan(self, id_or_code: str) -> PayStackResponse:
        """
        Get details of a plan

        :param: id_or_code: ID or Code of the plan

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"/plan/{id_or_code}")

    def update_plan(
            self,
            id_or_code: str,
            name: str,
            amount: int,
            interval: Interval,
            send_invoices: bool,
            send_sms: bool,
            currency: str,
            invoice_limit: int,
            description: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
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

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
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
        return self._put_request(f"/plan/{id_or_code}", data=data)
