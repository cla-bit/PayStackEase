===========================================
Transfers Control Module
===========================================

This wrapper class facilitates synchronous integration with Paystack Transfer Control APIs. The Transfers Control API allows you manage settings of your transfers.

-------------------

.. py:class:: TransferControlClientAPI(secret_key: str = None)

    Paystack Transfers Control API Reference: `Transfer Control`_

    .. py:method:: check_balance()→ PayStackResponse

        Get the available balance

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: disable_otp()→ PayStackResponse

        This is used in the event that you want to be able to complete transfers programmatically without use of OTPs

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: enable_otp()→ PayStackResponse

        This is used in the event that you want to stop being able to complete transfers programmatically with use of OTPs

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: fetch_balance_ledger()→ PayStackResponse

        Fetch all pay-ins and pay-outs that occurred on your integration

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: finalize_disable_otp(otp: str)→ PayStackResponse

        Finalize the request to disable OTP on your transfers.

        :param otp: The OTP sent to the business phone to verify disabling of OTP

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: resend_otp(transfer_code: str, reason: str)→ PayStackResponse

        Generates a new OTP and sends to customer in the event they are having trouble receiving one.

        :param transfer_code: The transfer code to resend
        :type transfer_code: str
        :param reason: The reason for the resend
        :type reason: str

        :return: The response from the API
        :rtype: PayStackResponse object


.. _Transfer Control: https://paystack.com/docs/api/transfer-control/
