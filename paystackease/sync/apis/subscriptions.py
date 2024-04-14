"""
Wrapper for Paystack Subscriptions API

The Subscriptions API allows you to create and manage recurring payment on your integration.
"""

from datetime import date
from typing import Optional, Union
from paystackease._api_http_response import Response
from paystackease.sync._api_http_request import PayStackBaseClientAPI


class SubscriptionClientAPI(PayStackBaseClientAPI):
    """
    Paystack Subscription API
    Reference: https://paystack.com/docs/api/subscription/
    """

    def create_subscription(
            self,
            customer: str,
            plan_code: str,
            authorization: str,
            start_date: Optional[Union[date, None]] = None,
    ) -> Response:
        """
        Create a subscription

        :param: customer: Email or Code of the customer
        :param: plan_code: Code of the plan
        :param: authorization: Code of the authorization
        :param: start_date: Start date of the subscription

        :return: The response from the API
        :rtype: Response object
        """

        # convert date to string
        start_date = self._convert_to_string(start_date)

        data = {
            "customer": customer,
            "plan": plan_code,
            "authorization": authorization,
            "start_date": start_date,
        }
        return self._post_request("/subscription", data=data)

    def list_subscriptions(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            customer: Optional[Union[int, None]] = None,
            plan_code: Optional[Union[int, None]] = None,
    ) -> Response:
        """
        List all the subscriptions

        :param: per_page: Number of records to return per page.
        :param: page: THe number to return
        :param: customer:
        :param: plan_code:

        :return: The response from the API
        :rtype: Response object
        """
        params = {
            "perPage": per_page,
            "page": page,
            "customer": customer,
            "plan": plan_code,
        }
        return self._get_request("/subscription", params=params)

    def fetch_subscription(self, id_or_code: str) -> Response:
        """
        Get details of a subscription

        :param: id_or_code: ID or Code of the subscription

        :return: The response from the API
        :rtype: Response object
        """
        return self._get_request(f"/subscription/{id_or_code}")

    def enable_subscription(self, subscription_code: str, token: str) -> Response:
        """
        Enable a subscription

        :param: subscription_code: Code of the subscription
        :param: token: Email token of the customer

        :return: The response from the API
        :rtype: Response object
        """
        data = {"code": subscription_code, "token": token}
        return self._post_request("/subscription/enable", data=data)

    def disable_subscription(self, subscription_code: str, token: str) -> Response:
        """
        Disable a subscription

        :param: subscription_code: Code of the subscription
        :param: token: Email token of the customer

        :return: The response from the API
        :rtype: Response object
        """
        data = {"code": subscription_code, "token": token}
        return self._post_request("/subscription/disable", data=data)

    def generate_update_subscription(self, subscription_code: str) -> Response:
        """
        Generate a link for updating the card on subscription

        :param: subscription_code: Code of the subscription

        :return: The response from the API
        :rtype: Response object
        """
        return self._post_request(f"/subscription/{subscription_code}/manage/link")

    def send_update_subscription_link(self, subscription_code: str) -> Response:
        """
        Email a customer a link for updating the card on their subscription

        :param: subscription_code: Code of the subscription

        :return: The response from the API
        :rtype: Response object
        """
        return self._post_request(f"/subscription/{subscription_code}/manage/email")
