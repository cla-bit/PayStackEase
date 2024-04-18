===========================================
Async Payment Requests Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.apayment_requests


Wrapper for Asynchronous Paystack Payment Requests API. The Payment Requests API allows you manage requests for payment of goods and services.

-------------

.. py:class:: AsyncPaymentRequestClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Payment Request API Reference: `Payment Requests`_

    .. py:method:: async archive_payment_request(code: str)→ PayStackResponse

        Archive a payment request

        :param code: Payment request code
        :type code: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async create_payment_request(customer: str, amount: int, draft: bool, has_invoice: bool, send_notification: bool, due_date: date | None = None, description: str | None = None, line_items: List[Dict[str, Any]] | None = None, tax: List[Dict[str, Any]] | None = None, currency: str | None = None, invoice_number: int | None = None, split_code: str | None = None)→ PayStackResponse

        Create a payment request for a transaction

        :param customer: Customer'S ID
        :type customer: str
        :param amount: Amount of the payment request
        :type amount: int
        :param draft: Whether the payment request is a draft
        :type draft: bool
        :param has_invoice: Whether the payment request has an invoice
        :type has_invoice: bool
        :param send_notification: Whether the payment request should send a notification
        :type send_notification: bool
        :param due_date: Due date of the payment request
        :type due_date: date, optional
        :param description: Description of the payment request
        :type description: str, optional
        :param line_items: List of line items of the payment request
        :type line_items: List[Dict[str, Any]], optional
        :param tax: List of taxes of the payment request
        :type tax: List[Dict[str, Any]], optional
        :param currency: Currency of the payment request
        :type currency: str, optional
        :param invoice_number: Invoice number of the payment request
        :type invoice_number: int, optional
        :param split_code: Split code of the transaction split
        :type split_code: str, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async fetch_payment_request(id_or_code: str)→ PayStackResponse

        Fetch a payment request

        :param id_or_code: Payment request ID or code
        :type id_or_code: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async finalize_payment_request(code: str, send_notification: bool)→ PayStackResponse

        Finalize a payment request

        :param code: Payment request code
        :type code: str
        :param send_notification: Whether the notification should be sent
        :type send_notification: bool

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async list_payment_requests(per_page: int | None = 50, page: int | None = 1, customer: str | None = None, status: str | None = None, currency: str | None = None, include_archive: bool | None = True, from_date: date | None = None, to_date: date | None = None)→ PayStackResponse

        List payment requests

        :param per_page: Number of results per page. (default: 50)
        :type per_page: int, optional
        :param page: Page number. (default: 1)
        :type page: int, optional
        :param customer: Filter by Customer ID
        :type customer: str, optional
        :param status: Filter by payment request status
        :type status: str, optional
        :param currency: Filter by currency
        :type currency: str, optional
        :param include_archive: Whether to include archived payment requests. (default: True)
        :type include_archive: bool, optional
        :param from_date: Filter by from date
        :type from_date: date, optional
        :param to_date: Filter by to date
        :type to_date: date, optional

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async payment_request_total()→ PayStackResponse

        Get the total number of payment requests

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async send_notification(code: str)→ PayStackResponse

        Send a notification to a payment request to a customer

        :param code: Payment request code
        :type code: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async update_payment_request(id_or_code: str, customer: str | None = None, amount: int | None = None, description: str | None = None, line_items: List[Dict[str, Any]] | None = None, tax: List[Dict[str, Any]] | None = None, currency: str | None = None, due_date: date | None = None, send_notification: bool | None = True, draft: bool | None = True, invoice_number: int | None = None, split_code: str | None = None)→ PayStackResponse

        Update a payment request

        :param id_or_code: Payment request ID or code
        :type id_or_code: str
        :param customer: Customer ID
        :type customer: str, optional
        :param amount: Amount of the payment request
        :type amount: int, optional
        :param description: Description of the payment request
        :type description: str, optional
        :param line_items: List of line items of the payment request
        :type line_items: List[Dict[str, Any]], optional
        :param tax: List of taxes of the payment request
        :type tax: List[Dict[str, Any]], optional
        :param currency: Currency of the payment request
        :type currency: str, optional
        :param due_date: Due date of the payment request
        :type due_date: date, optional
        :param send_notification: Whether the notification should be sent. (default: True)
        :type send_notification: bool, optional
        :param draft: Whether the payment request is a draft. (default: True)
        :type draft: bool, optional
        :param invoice_number: Invoice number of the payment request
        :type invoice_number: int, optional
        :param split_code: Split code of the transaction split
        :type split_code: str, optional

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async verify_payment_request(code: str)→ PayStackResponse

        Verify a payment request

        :param code: Payment request code
        :type code: str

        :return: The response from the API.
        :rtype: PayStackResponse object


.. _Payment Requests: https://paystack.com/docs/api/payment-request/

The ``line_items`` is a List type that contains a dictionary of key-value pairs as seen in the usage.
The keys are: ``name``, ``amount`` and ``quantity``.

**Usage**

.. code-block:: bash

    [{“name”:”item 1”, “amount”:2000, “quantity”: 1}]

The ``tax`` is follows same as ``list_items`` parameter except with the keys are different.
The keys are: ``name`` and ``amount``.

**Usage**

.. code-block:: bash

    [{“name”:”VAT”, “amount”:200}]

See documentation on how to pass string values of enum classes :doc:`toolkit` in the ``status`` parameter.
