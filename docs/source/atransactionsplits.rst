===========================================
Async Transaction Splits Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.atransaction_splits


Wrapper for Asynchronous Paystack Transaction Splits APIs. The Transaction Splits API enables merchants split the settlement for a transaction across their payout account, and one or more subaccounts.

You can use the tool kit in the helpers module as reference: :doc:`toolkit`

-------------------

.. py:class:: AsyncTransactionSplitClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Transaction Split API Reference: `Transaction Splits`_

    .. py:method:: async add_or_update_subaccount_split(split_id: str, subaccount: str, transaction_share: int)→ Response

        Add a Subaccount to a Transaction Split, or update the share of an existing Subaccount in a Transaction Split

        :param split_id: The ID of the transaction split
        :type split_id: str
        :param subaccount: The Subaccount code
        :type subaccount: str
        :param transaction_share: The number of shares
        :type transaction_share: int

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async create_split(transaction_split_name: str, transaction_split_type: str, currency: str, subaccounts: List[Dict[str, Any]], bearer_type: str, bearer_subaccount: str)→ Response

        Create a split payment on your integration

        :param transaction_split_name: Name of the transaction split
        :type transaction_split_name: str
        :param transaction_split_type: Type of transaction split you want to create. Value: ``SplitType.value.value``
        :type transaction_split_type: str
        :param currency: Value: ``Currency.value.value``
        :type currency: str
        :param subaccounts: A list of object containing subaccount code and number of shares.
        :type subaccounts: List[Dict[str, Any]]
        :param bearer_type: Any of: ``subaccount`` | ``account`` | ``all-proportional`` | ``all``
        :type bearer_type: str
        :param bearer_subaccount: Subaccount Code
        :type bearer_subaccount: str

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async fetch_split(split_id: str)→ Response

        Fetch details of a specific transaction split

        :param split_id: The transaction split ID
        :type split_id: str

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async list_split(split_name: str | None = None, active: bool | None = None, sort_by: str | None = None, per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ Response

        List all the transaction splits

        :param split_name: Name of the transaction split
        :type split_name: str, optional
        :param active: Either True or False
        :type active: bool, optional
        :param sort_by: Sort by name, defaults to createdAt date
        :type sort_by: str, optional
        :param per_page: Number of transactions split records per page
        :type per_page: int, optional
        :param page:
        :type page: int, optional
        :param from_date:
        :type from_date: date, optional
        :param to_date:
        :type to_date: date, optional

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async remove_sub_account_split(split_id: str, subaccount: str)→ Response

        Remove a Sub Account from a transaction split

        :param split_id: the transaction split ID
        :type split_id: str
        :param subaccount: the subaccount code
        :type subaccount: str

        :return: The response from the API
        :rtype: Response object

    .. py:method:: async update_split(split_id: str, transaction_split_name: str, active: bool, bearer_type: str | None = None, bearer_subaccount: str | None = None)→ Response

        Update a specific transaction split details

        :param split_id: the id of the transaction split to update
        :type split_id: str
        :param transaction_split_name: the name of the transaction split
        :type transaction_split_name: str
        :param active:
        :type active: bool
        :param bearer_type:
        :type bearer_type: str, optional
        :param bearer_subaccount:
        :type bearer_subaccount: str, optional

        :return: The response from the API
        :rtype: Response object


.. _Transaction Splits: https://paystack.com/docs/api/split/
