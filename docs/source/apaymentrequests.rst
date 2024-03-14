paystackease.async\_apis.apayment\_requests module
--------------------------------------------------

.. :py:currentmodule:: paystackease.async_apis.apayment_requests


Wrapper for Asynchronous Paystack Payment Requests API. The Payment Requests API allows you manage requests for payment of goods and services.

---------------------------------------------------


.. py:class:: AsyncPaymentRequestClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Payment Request API Reference: `Payment Requests`_

    .. py:method:: async archive_payment_request(code: str)→ dict

        Archive a payment request

        :param code: Payment request code
        :type code: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async create_payment_request(customer: str, amount: int, draft: bool, has_invoice: bool, send_notification: bool, due_date: date | None = None, description: str | None = None, line_items: List[Dict[str, str]] | None = None, tax: List[Dict[str, str]] | None = None, currency: str | None = None, invoice_number: int | None = None, split_code: str | None = None)→ dict

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
        :type line_items: List[Dict[str, str]], optional
        :param tax: List of taxes of the payment request
        :type tax: List[Dict[str, str]], optional
        :param currency: Currency of the payment request
        :type currency: str, optional
        :param invoice_number: Invoice number of the payment request
        :type invoice_number: int, optional
        :param split_code: Split code of the transaction split
        :type split_code: str, optional

        :return: The response from the API.
        :rtype: dict

    .. hint::

        ``line_items`` is in this format:  [{“name”:”item 1”, “amount”:2000, “quantity”: 1}]

        ``tax`` is in this format: [{“name”:”VAT”, “amount”:200}]

    .. py:method:: async fetch_payment_request(id_or_code: str)→ dict

        Fetch a payment request

        :param id_or_code: Payment request ID or code
        :type id_or_code: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async finalize_payment_request(code: str, send_notification: bool)→ dict

        Finalize a payment request

        :param code: Payment request code
        :type code: str
        :param send_notification: Whether the notification should be sent
        :type send_notification: bool

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async list_payment_requests(per_page: int | None = None, page: int | None = None, customer: str | None = None, status: str | None = None, currency: str | None = None, include_archive: str | None = None, from_date: date | None = None, to_date: date | None = None)→ dict

        List payment requests

        :param per_page: Number of results per page
        :type per_page: int, optional
        :param page: Page number
        :type page: int, optional
        :param customer: Filter by Customer ID
        :type customer: str, optional
        :param status: Filter by payment request status
        :type status: str, optional
        :param currency: Filter by currency
        :type currency: str, optional
        :param include_archive: Whether to include archived payment requests
        :type include_archive: str, optional
        :param from_date: Filter by from date
        :type from_date: date, optional
        :param to_date: Filter by to date
        :type to_date: date, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: async payment_request_total()→ dict

        Get the total number of payment requests

        :return: The response from the API
        :rtype: dict

    .. py:method:: async send_notification(code: str)→ dict

        Send a notification to a payment request to a customer

        :param code: Payment request code
        :type code: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async update_payment_request(id_or_code: str, customer: str | None = None, amount: int | None = None, description: str | None = None, line_items: List[Dict[str, str]] | None = None, tax: List[Dict[str, str]] | None = None, currency: str | None = None, due_date: date | None = None, send_notification: bool | None = None, draft: bool | None = None, invoice_number: int | None = None, split_code: str | None = None)→ dict

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
        :type line_items: List[Dict[str, str]], optional
        :param tax: List of taxes of the payment request
        :type tax: List[Dict[str, str]], optional
        :param currency: Currency of the payment request
        :type currency: str, optional
        :param due_date: Due date of the payment request
        :type due_date: date, optional
        :param send_notification: Whether the notification should be sent
        :type send_notification: bool, optional
        :param draft: Whether the payment request is a draft
        :type draft: bool, optional
        :param invoice_number: Invoice number of the payment request
        :type invoice_number: int, optional
        :param split_code: Split code of the transaction split
        :type split_code: str, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: async verify_payment_request(code: str)→ dict

        Verify a payment request

        :param code: Payment request code
        :type code: str

        :return: The response from the API.
        :rtype: dict


.. _Payment Requests: https://paystack.com/docs/api/payment-request/
