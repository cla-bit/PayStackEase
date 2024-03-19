"""
Wrapper for Paystack Integration API

The Integration API allows you manage some settings on your integration.
"""

from paystackease._base import PayStackBaseClientAPI


class IntegrationClientAPI(PayStackBaseClientAPI):
    """
    Paystack Integration API
    Reference: https://paystack.com/docs/api/integration/
    """

    def fetch_timeout(self) -> dict:
        """
        Fetch payment session timeout

        :return: The response from the API
        :rtype: dict
        """
        return self._get_request("/integration/payment_session_timeout")

    def update_timeout(self, timeout: int) -> dict:
        """
        Update payment session timeout

        :param: timeout: The new payment session timeout before session
        
        note::

            timeout is in seconds. Set 0 to cancel the timeout

        :return: The response from the API
        :rtype: dict
        """

        data = {"timeout": timeout}
        return self._put_request("/integration/payment_session_timeout", data=data)
