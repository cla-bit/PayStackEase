"""
Wrapper for Paystack Integration API

The Integration API allows you manage some settings on your integration.
"""
from paystackease._api_http_response import PayStackResponse
from paystackease.sync._api_http_request import PayStackBaseClientAPI


class IntegrationClientAPI(PayStackBaseClientAPI):
    """
    Paystack Integration API
    Reference: https://paystack.com/docs/api/integration/
    """

    def fetch_timeout(self) -> PayStackResponse:
        """
        Fetch payment session timeout

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request("/integration/payment_session_timeout")

    def update_timeout(self, timeout: int) -> PayStackResponse:
        """
        Update payment session timeout

        :param: timeout: The new payment session timeout before session
        
        note::

            timeout is in seconds. Set 0 to cancel the timeout

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        data = {"timeout": timeout}
        return self._put_request("/integration/payment_session_timeout", data=data)
