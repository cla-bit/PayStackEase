"""
Wrapper for Asynchronous Paystack Transfer Control APIs

The Transfers Control API allows you manage settings of your transfers.
"""

from paystackease.core import AsyncRequestAPI, PayStackResponse


class AsyncTransferControlClientAPI(AsyncRequestAPI):
    """
    Paystack Transfers Control API
    Reference: https://paystack.com/docs/api/transfer-control/
    """

    async def check_balance(self) -> PayStackResponse:
        """
        Get the available balance

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request("/balance")

    async def fetch_balance_ledger(self) -> PayStackResponse:
        """
        Fetch all pay-ins and pay-outs that occurred on your integration

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request("/balance/ledger")

    async def resend_otp(self, transfer_code: str, reason: str) -> PayStackResponse:
        """
        Generates a new OTP and sends to customer in the event
        they are having trouble receiving one.

        :param: transfer_code: The code of the transfer to finalize
        :param: reason: Either resend_otp or transfer as the value of this field

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"transfer_code": transfer_code, "reason": reason}
        return await self._post_request("/transfer/resend_otp", data=data)

    async def disable_otp(self) -> PayStackResponse:
        """
        This is used in the event that you want to be able to
         complete transfers programmatically without use of OTPs

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._post_request("/transfer/disable_otp")

    async def finalize_disable_otp(self, otp: str) -> PayStackResponse:
        """
        Finalize the request to disable OTP on your transfers.

        :param: otp: The OTP sent to the business phone to verify disabling of OTP

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"otp": otp}
        return await self._post_request("/transfer/disable_otp_finalize", data=data)

    async def enable_otp(self) -> PayStackResponse:
        """
        This is used in the event that you want to stop
        being able to complete transfers programmatically with use of OTPs

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._post_request("/transfer/enable_otp")
