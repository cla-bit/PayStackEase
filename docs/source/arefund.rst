===========================================
Async Refund Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.arefund


Wrapper for Asynchronous Paystack Refund API. The Refunds API allows you to create and manage transaction refunds.

You can use the tool kit in the helpers module as reference: :ref:`helpers`

--------------------------------------------------------------------

.. py:class:: AsyncRefundClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Refund API Reference: `Refund`_

    .. py:method:: async create_refund(transaction_ref_or_id: str, amount: int | None = None, currency: str | None = None, customer_note: str | None = None, merchant_note: str | None = None)→ dict[source]

        Create a refund

        :param transaction_ref_or_id: The transaction id or reference to fetch
        :type transactin_ref_or_id: str
        :param amount: The amount to refund
        :type amount: int, optional
        :param currency: The currency to refund. Values: ``Currency.value.value``
        :type currency: str, optional
        :param customer_note: The customer note or reason
        :type custome_note: str, optional
        :param merchant_note: The merchant note or reason
        :type merchant_note: str, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: async fetch_refund(reference: str)→ dict

        Fetch a refund

        :param reference: The transaction reference to fetch for refund
        :type reference: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: async list_refunds(reference: str | None = None, currency: str | None = None, per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ dict

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
        :rtype: dict


.. _Refund: https://paystack.com/docs/api/refund/
