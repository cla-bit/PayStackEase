"""
Wrapper for Asynchronous Paystack Integration API

The Integration API allows you manage some settings on your integration.
"""
from paystackease._utils import Response
from paystackease._abase import AsyncPayStackBaseClientAPI


class AsyncIntegrationClientAPI(AsyncPayStackBaseClientAPI):
    """
    Paystack Integration API
    Reference: https://paystack.com/docs/api/integration/
    """

    async def fetch_timeout(self) -> Response:
        """
        Fetch payment session timeout

        :return: The response from the API
        :rtype: Response object
        """
        return await self._get_request("/integration/payment_session_timeout")

    async def update_timeout(self, timeout: int) -> Response:
        """
        Update payment session timeout

        :param: timeout: The new payment session timeout before session

        note::

            timeout is in seconds. Set 0 to cancel the timeout

        :return: The response from the API
        :rtype: Response object
        """

        data = {"timeout": timeout}
        return await self._put_request("/integration/payment_session_timeout", data=data)
