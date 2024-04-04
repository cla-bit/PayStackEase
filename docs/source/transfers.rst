===========================================
Transfers Module
===========================================

.. :py:currentmodule:: paystackease.apis.transfers


Wrapper for Paystack Transfers APIs. The Transfers API allows you to automate sending money to your customers.

--------------

.. py:class:: TransfersClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Transfers API Reference: `Transfers`_

    .. py:method:: fetch_transfer(id_or_code: str)→ Response

        Get details of a transfer

        :param id_or_code: The transfer id or code
        :type id_or_code: str

        :return: The response from the API
        :rtype: Response object

    .. py:method:: finalize_transfer(transfer_code: str, otp: str)→ Response

        Finalize an initiated transfer

        :param transfer_code: The code of the transfer to finalize
        :type transfer_code: str
        :param otp: The OTP sent to the business phone to verify transfer
        :type otp: str

        :return: The response from the API
        :rtype: Response object

    .. py:method:: initiate_bulk_transfer(transfer_source: str, transfers: List[Dict[str, Any]])→ Response

        Batch multiple transfers in a single request

        :param transfer_source: Where should we transfer from? Only balance for now
        :type transfer_source: str
        :param transfers: A list of transfer objects keys [ { amount | recipient | reference | reason } ]
        :type transfers: List[Dict[str, Any]]

        :return: The response from the API
        :rtype: Response object

    .. py:method:: initiate_transfer(transfer_source: str, amount: int, transfer_recipient: str, reason: str | None = None, currency: str | None = None, reference: str | None = None)→ Response

        Initiate a transfer. Upgrade your business to a Registered Business to use

        :param transfer_source: Where should we transfer from? Only balance for now
        :type transfer_source: str
        :param amount: Amount to transfer in kobo if currency is NGN and pesewas if currency is GHS.
        :type amount: int
        :param transfer_recipient: The code of the recipient
        :type transfer_recipient: str
        :param reason: The reason for the transfer
        :type reason: str, optional
        :param currency: The currency of the transfer
        :type currency: str, optional
        :param reference: The reference for the transfer
        :type reference: str, optional

        :return: The response from the API
        :rtype: Response object

    .. py:method:: list_transfers(per_page: int | None = None, page: int | None = None, customer_id: str | None = None, from_date: date | None = None, to_date: date | None = None)→ Response

        List transfers

        :param per_page: The number of records to return per page.
        :type per_page: int, optional
        :param page: The page to return.
        :type page: int, optional
        :param customer_id: The id of the customer
        :type customer_id: str, optional
        :param from_date: The date from which to list transfers
        :type from_date: date, optional
        :param to_date: The date until which to list transfers
        :type to_date: date, optional

        :return: The response from the API
        :rtype: Response object


    .. py:method:: verify_transfer(reference: str)→ Response

        Verify a transfer

        :param reference: The reference of the transfer to verify

        :return: The response from the API
        :rtype: Response object

.. _Transfers: https://paystack.com/docs/api/transfer/
