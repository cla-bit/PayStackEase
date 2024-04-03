"""
Wrapper for Paystack Integration API

The Integration API allows you manage some settings on your integration.
"""
from requests import Response
from paystackease._base import PayStackBaseClientAPI


class IntegrationClientAPI(PayStackBaseClientAPI):
    """
    Paystack Integration API
    Reference: https://paystack.com/docs/api/integration/
    """

    def fetch_timeout(self) -> Response:
        """
        Fetch payment session timeout

        :return: The response from the API
        :rtype: Response object
        """
        return self._get_request("/integration/payment_session_timeout")

    def update_timeout(self, timeout: int) -> Response:
        """
        Update payment session timeout

        :param: timeout: The new payment session timeout before session
        
        note::

            timeout is in seconds. Set 0 to cancel the timeout

        :return: The response from the API
        :rtype: Response object
        """

        data = {"timeout": timeout}
        return self._put_request("/integration/payment_session_timeout", data=data)
