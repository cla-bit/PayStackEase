===========================================
Async Transfer Recipients Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.atransfer_recipients


Wrapper for Asynchronous Paystack Transfer Recipient APIs. The Transfer Recipients API allows you to create and manage beneficiaries that you send money to.

-------------------------------------------------------------

.. py:class:: AsyncTransferRecipientsClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Transfer Recipients API Reference: `Transfer Recipients`_

    .. py:method:: async bulk_create_transfer_recipient(batch: List[Dict[str, Any]])→ ClientResponse

        Create multiple transfer recipients in batches.

        :param batch: A list of transfer recipient dict keys [ { ``type``, ``name``, ``account_number``, ``bank_code``, ``currency`` etc. }]
        :type batch: List[Dict[str, Any]]

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async create_transfer_recipients(recipient_type: str, recipient_name: str, account_number: str, bank_code: str, description: str | None = None, currency: str | None = None, authorization_code: str | None = None, metadata: Dict[str, str] | None = None)→ ClientResponse

        Create a transfer recipient

        :param recipient_type: The type of transfer recipient:[ ``nuban`` | ``ghipss`` | ``mobile_money`` | ``basa`` ]
        :type recipient_type: str
        :param recipient_name: The name of the transfer recipient according to their registration
        :type recipient_name: str
        :param account_number: transfer recipient’s account number. Required for all recipient types except authorization
        :type account_number: str
        :param bank_code: transfer recipient’s bank code. Required for all recipient types except authorization
        :type bank_code: str
        :param description:
        :type description: str, optional
        :param currency:
        :type currency: str, optional
        :param authorization_code: transfer recipient’s authorization code from previous transaction
        :type authorization_code: str, optional
        :param metadata:
        :type metadata: dict, optional

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async delete_transfer_recipient(id_or_code: str)→ ClientResponse

        Delete a transfer recipient

        :param id_or_code: The id or code of the transfer recipient
        :type id_or_code: str

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async fetch_transfer_recipient(id_or_code: str)→ ClientResponse

        Fetch details of a transfer recipient

        :param id_or_code: The id or code of the transfer recipient
        :type id_or_code: str

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async list_transfer_recipients(per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ ClientResponse

        List of all transfer recipients

        :param per_page: The number of records to return per page.
        :type per_page: int, optional
        :param page: The page to return.
        :type page: int, optional
        :param from_date: The customer's from date.
        :type from_date: date, optional
        :param to_date: The customer's to date.
        :type to_date: date, optional

        :return: The response from the API
        :rtype: ClientResponse object

    .. py:method:: async update_transfer_recipient(id_or_code: str, recipient_name: str, recipient_email: str | None = None)→ ClientResponse

        Update a transfer recipient

        :param id_or_code:
        :type id_or_code: str
        :param recipient_name:
        :type recipient_name: str
        :param recipient_email:
        :type recipient_email: str

        :return: The response from the API
        :rtype: ClientResponse object


.. _Transfer Recipients: https://paystack.com/docs/api/transfer-recipient/
