===========================================
Async Transactions Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.atransactions


Wrapper for Asynchronous Paystack Transactions API. The Transactions API allows you to create and manage payments on your integration.

.. note::

    You can use ``convert_currency()`` to convert to subunit. ``Authorization code`` are generated upon a successful card transaction.

-----------

.. py:class:: AsyncTransactionClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Transaction API Reference: `Transaction`_

    .. py:method:: async charge_authorization(email: str, amount: int, authorization_code: str, reference: str | None = None, currency: str | None = None, channels: List[str] | None = None, subaccount: str | None = None, transaction_charge: int | None = None, bearer: str | None = None, queue: bool | None = None, metadata: Dict[str, List[Dict[str, Any]]] | None = None)→ ClientResponse

        Charge an authorization transaction

        :param email: The email of the customer
        :type email: str
        :param amount: amount should be in subunit in this case 10000 kobo = 100 naira.
        :type amount: int
        :param authorization_code: Value: AUTH***************RW2
        :type authorization_code: str
        :param reference: This is a unique reference.
        :type reference: str, optional
        :param currency:
        :type currency: str, optional
        :param channels: ``Channels.value.value``
        :type channels: list, optional
        :param subaccount:
        :type subaccount: str, optional
        :param transaction_charge: Amount of transaction charge to charge
        :type transaction_charge: int, optional
        :param bearer: Who bears Paystack charges? Two options: ``account`` | ``subaccount``
        :type bearer: str, optional
        :param queue: If set to true, the transaction will be queued for processing
        :type queue: bool, optinoal
        :param metadata: JSON object of custom data.
        :type metadata: Dict[str, List[Dict[str, Any]]]

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async export_transactions(per_page: int | None = 50, page: int | None = 1, customer: int | None = None, currency: str | None = None, amount: int | None = None, status: str | None = None, settled: bool | None = None, settlement: int | None = None, payment_page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ ClientResponse

        Export transactions

        :param per_page: The number of transaction records to return per page.
        :type per_page: int, optional
        :param page: The page to return.
        :type page: int, optional
        :param customer:
        :type customer: str, optional
        :param currency:
        :type currency: str, optional
        :param amount:
        :type amount: int, optional
        :param status:
        :type status: str, optional
        :param settled:
        :type settled: bool,optional
        :param settlement:
        :type settlement: int, optional
        :param payment_page:
        :type payment_page: int, optional
        :param from_date: The customer's from date.
        :type from_date: date, optional
        :param to_date: The customer's to date.
        :type to_date: date, optional

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async fetch_transaction(transaction_id: int)→ ClientResponse

        Fetch details of a specific transaction

        :param transaction_id: ID of the transaction
        :type transaction_id: int

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async initialize(email: str, amount: int, currency: str | None = None, reference: str | None = None, callback_url: str | None = None, plan: str | None = None, invoice_limit: int | None = None, channels: List[str] | None = None, split_code: str | None = None, subaccount: str | None = None, transaction_charge: int | None = None, bearer: str | None = None, metadata: Dict[str, Any] | None = None)→ ClientResponse

        Initiate a transaction

        :param email:
        :type email: str
        :param amount:
        :type amount: int
        :param currency:
        :type currency: str, optional
        :param reference: This is a unique identifier. You can create of your choice
        :type reference: str, optional
        :param callback_url: Use this to override the callback url provided on the dashboard: https://example.com/callback
        :type callback_url: str, optional
        :param plan: If transaction is to create a subscription to a predefined plan, provide plan code here.
        :type plan: str, optional
        :param invoice_limit: Number of times to charge customer during subscription to plan
        :type invoice_limit: int, optional
        :param channels: ``Channels.value.value``
        :type channels: list, optional
        :param split_code: Transaction split code
        :type split_code: str, optional
        :param subaccount: The code for the subaccount that owns the payment.
        :type subaccount: str, optional
        :param transaction_charge: An amount used to override the split configuration for a # single split payment
        :type transaction_charge: str, optional
        :param bearer: Who bears Paystack charges? Two options are (``account`` | ``subaccount``)
        :type bearer: str, optional
        :metadata: JSON object of the custom data
        :type metadata: dict, optional

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async list_transactions(per_page: int | None = 50, page: int | None = 1, customer: int | None = None, terminal_id: str | None = None, amount: int | None = None, status: str | None = None, from_date: date | None = None, to_date: date | None = None)→ ClientResponse

        List all transactions

        :param per_page: The number of transaction records to return per page.
        :type per_page: int, optional
        :param page: The page to return.
        :type page: int, optional
        :param customer: Specify an ID for the customer whose transactions you want to retrieve
        :type customer: str, optional
        :param terminal_id: Specify an ID for the terminal whose transactions you want to retrieve
        :type termianl_id: str, optional
        :param amount:
        :type amount: int, optional
        :param status: Specify a status for the transactions you want to retrieve [``success``, ``failed``, ``abandoned``]
        :type status: str, optional
        :param from_date: A timestamp from which to start listing transaction
        :type from_date: date, optional
        :param to_date: A timestamp at which to stop listing transaction
        :type to_date: date, optional

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async partial_debit(email: str, authorization_code: str, amount: int, currency: str, reference: str | None = None, at_least: int | None = None)→ ClientResponse

        Charge a partial debit transaction

        :param email: The email of the customer
        :type email: str
        :param amount: amount should be in subunit in this case 10000 kobo = 100 naira.
        :type amount: int
        :param authorization_code: Value: AUTH***************RW2
        :type authorization_code: str
        :param reference: This is a unique reference.
        :type reference: str, optional
        :param currency:
        :type currency: str, optional
        :param at_least: Minimum amount to charge
        :type at_least: int, optional

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async transaction_timeline(id_or_reference: str)→ ClientResponse

        Get the timeline of a transaction

        :param id_or_reference: The id or reference of the transaction you want to get

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async transaction_totals(per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ ClientResponse

        Get total of all transactions

        :param per_page: The number of transaction records to return per page.
        :type per_page: int, optional
        :param page: The page to return.
        :type page: int, optional
        :param from_date: A timestamp from which to start listing transaction
        :type from_date: date, optional
        :param to_date: A timestamp at which to stop listing transaction
        :type to_date: date, optional

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async verify_transaction(reference: str)→ ClientResponse

        Verify a transaction by reference

        :param reference:
        :type reference: str

        :return: The response from the API
        :rtype: ClientResponse object

You can use the tool kit in the helpers module as reference: :doc:`paystackease.helpers`

.. _Transaction: https://paystack.com/docs/api/transaction/
