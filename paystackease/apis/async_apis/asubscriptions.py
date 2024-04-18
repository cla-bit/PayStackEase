"""
Wrapper for Paystack Subscriptions API

The Subscriptions API allows you to create and manage recurring payment on your integration.
"""

from datetime import date
from typing import Optional, Union

from paystackease.core import AsyncRequestAPI, PayStackResponse


class AsyncSubscriptionClientAPI(AsyncRequestAPI):
    """
    Paystack Subscription API
    Reference: https://paystack.com/docs/api/subscription/
    """

    async def create_subscription(
            self,
            customer: str,
            plan_code: str,
            authorization: str,
            start_date: Optional[Union[date, None]] = None,
    ) -> PayStackResponse:
        """
        Create a subscription

        :param: customer: Email or Code of the customer
        :param: plan_code: Code of the plan
        :param: authorization: Code of the authorization
        :param: start_date: Start date of the subscription

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        # convert date to string
        start_date = self._convert_to_string(start_date)

        data = {
            "customer": customer,
            "plan": plan_code,
            "authorization": authorization,
            "start_date": start_date,
        }
        return await self._post_request("/subscription", data=data)

    async def list_subscriptions(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            customer: Optional[Union[int, None]] = None,
            plan_code: Optional[Union[int, None]] = None,
    ) -> PayStackResponse:
        """
        List all the subscriptions

        :param: per_page: Number of records to return per page.
        :param: page: THe number to return
        :param: customer:
        :param: plan_code:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        params = {
            "perPage": per_page,
            "page": page,
            "customer": customer,
            "plan": plan_code,
        }
        return await self._get_request("/subscription", params=params)

    async def fetch_subscription(self, id_or_code: str) -> PayStackResponse:
        """
        Get details of a subscription

        :param: id_or_code: ID or Code of the subscription

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"/subscription/{id_or_code}")

    async def enable_subscription(self, subscription_code: str, token: str) -> PayStackResponse:
        """
        Enable a subscription

        :param: subscription_code: Code of the subscription
        :param: token: Email token of the customer

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"code": subscription_code, "token": token}
        return await self._post_request("/subscription/enable", data=data)

    async def disable_subscription(self, subscription_code: str, token: str) -> PayStackResponse:
        """
        Disable a subscription

        :param: subscription_code: Code of the subscription
        :param: token: Email token of the customer

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"code": subscription_code, "token": token}
        return await self._post_request("/subscription/disable", data=data)

    async def generate_update_subscription(self, subscription_code: str) -> PayStackResponse:
        """
        Generate a link for updating the card on subscription

        :param: subscription_code: Code of the subscription

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._post_request(f"/subscription/{subscription_code}/manage/link")

    async def send_update_subscription_link(self, subscription_code: str) -> PayStackResponse:
        """
        Email a customer a link for updating the card on their subscription

        :param: subscription_code: Code of the subscription

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._post_request(f"/subscription/{subscription_code}/manage/email")
