===========================================
Refund Module
===========================================

.. :py:currentmodule:: paystackease.apis.refund


Wrapper for Paystack Refund API. The Refunds API allows you to create and manage transaction refunds.

You can use the tool kit in the helpers module as reference: :doc:`paystackease.helpers`

--------------------------------------------------------------------

.. py:class:: RefundClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Refund API Reference: `Refund`_

    .. py:method:: create_refund(transaction_ref_or_id: str, amount: int | None = None, currency: str | None = None, customer_note: str | None = None, merchant_note: str | None = None)→ Response

        Create a refund

        :param transaction_ref_or_id: The transaction id or reference to fetch
        :type transactin_ref_or_id: str
        :param amount: The amount to refund
        :type amount: int, optional
        :param currency: The currency to refund.
        :type currency: str, optional
        :param customer_note: The customer note or reason
        :type custome_note: str, optional
        :param merchant_note: The merchant note or reason
        :type merchant_note: str, optional

        :return: The response from the API
        :rtype: Response object

    .. py:method:: fetch_refund(reference: str)→ Response

        Fetch a refund

        :param reference: The transaction reference to fetch for refund
        :type reference: str

        :return: The response from the API
        :rtype: Response object

    .. py:method:: list_refunds(reference: str | None = None, currency: str | None = None, per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ Response

        List refunds

        :param reference: The transaction reference to fetch for the refund
        :type reference: str, optional
        :param currency:
        :type currency: str, optional
        :param per_page: The number of plans per page
        :type per_page: int, optional
        :param page: The page number
        :type page: int, optional
        :param from_date:
        :type from_date:
        :param to_date:
        :type to_date:

        :return: The response from the API
        :rtype: Response object


.. _Refund: https://paystack.com/docs/api/refund/
