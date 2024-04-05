===========================================
Async Transfers Control Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.atransfers_control


Wrapper for Asynchronous Paystack Transfer Control APIs. The Transfers Control API allows you manage settings of your transfers.

-----------

.. py:class:: AsyncTransferControlClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Transfers Control API Reference: `Transfer Control`_

    .. py:method:: async check_balance()→ Response

        Get the available balance

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async disable_otp()→ Response

        This is used in the event that you want to be able to complete transfers programmatically without use of OTPs

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async enable_otp()→ Response

        This is used in the event that you want to stop being able to complete transfers programmatically with use of OTPs

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async fetch_balance_ledger()→ Response

        Fetch all pay-ins and pay-outs that occurred on your integration

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async finalize_disable_otp(otp: str)→ Response

        Finalize the request to disable OTP on your transfers.

        :param otp: The OTP sent to the business phone to verify disabling of OTP

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async resend_otp(transfer_code: str, reason: str)→ Response

        Generates a new OTP and sends to customer in the event they are having trouble receiving one.

        :param transfer_code: The transfer code to resend
        :type transfer_code: str
        :param reason: The reason for the resend
        :type reason: str

        :return: The response from the API
        :rtype: Response object


.. _Transfer Control: https://paystack.com/docs/api/transfer-control/

