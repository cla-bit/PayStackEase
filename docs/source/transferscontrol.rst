paystackease.apis.transfers\_control module
-------------------------------------------

.. :py:currentmodule:: paystackease.apis.transfers_control


Wrapper for Paystack Transfer Control APIs. The Transfers Control API allows you manage settings of your transfers.

---------------------------------------------------------

.. py:class:: TransferControlClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Transfers Control API Reference: `Transfer Control`_

    .. py:method:: check_balance()→ dict

        Get the available balance

        :return: The response from the API
        :rtype: dict

    .. py:method:: disable_otp()→ dict

        This is used in the event that you want to be able to complete transfers programmatically without use of OTPs

        :return: The response from the API
        :rtype: dict

    .. py:method:: enable_otp()→ dict

        This is used in the event that you want to stop being able to complete transfers programmatically with use of OTPs

        :return: The response from the API
        :rtype: dict

    .. py:method:: fetch_balance_ledger()→ dict

        Fetch all pay-ins and pay-outs that occurred on your integration

        :return: The response from the API
        :rtype: dict

    .. py:method:: finalize_disable_otp(otp: str)→ dict

        Finalize the request to disable OTP on your transfers.

        :param otp: The OTP sent to the business phone to verify disabling of OTP

        :return: The response from the API
        :rtype: dict

    .. py:method:: resend_otp(transfer_code: str, reason: str)→ dict

        Generates a new OTP and sends to customer in the event they are having trouble receiving one.

        :param transfer_code: The transfer code to resend
        :type transfer_code: str
        :param reason: The reason for the resend
        :type reason: str

        :return: The response from the API
        :rtype: dict


.. _Transfer Control: https://paystack.com/docs/api/transfer-control/
