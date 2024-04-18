===========================================
Async Disputes Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.adisputes


Wrapper for Asynchronous Paystack Disputes API The Disputes API allows you manage transaction disputes on your integration.

You can use the tool kit in the helpers module as reference: :doc:`paystackease.helpers`

-------------

.. py:class:: AsyncDisputesClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Customer API Reference: `Disputes`_

    .. py:method:: async add_evidence(dispute_id: str, customer_email: str, customer_name: str, customer_phone: str, service_details: str, delivery_address: str | None = None, delivery_date: date | None = None)→ PayStackResponse

        Add evidence to a dispute.

        :param dispute_id: The ID of the dispute to fetch
        :type dispute_id: str
        :param customer_email: The customer's email
        :type customer_email: str
        :param customer_name: The customer's name
        :type customer_name: str
        :param customer_phone: The customer's phone
        :type customer_phone: str
        :param service_details: The service details
        :type service_details: str
        :param delivery_address: The delivery address
        :type delivery_address: str, optional
        :param delivery_date: The delivery date
        :type delivery_date: date, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async export_disputes(per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None, transaction_id: str | None = None, status: str | None = None)→ PayStackResponse

        Export disputes.

        :param per_page: The number of disputes to return per page.
        :type per_page: int, optional
        :param page: The page to return.
        :type page: int, optional
        :param from_date: The date from which to fetch disputes.
        :type from_date: date, optional
        :param to_date: The date until which to fetch disputes.
        :type to_date: date, optional
        :param transaction_id: The ID of the transaction.
        :type transaction_id: str, optional
        :param status: The dispute status.
        :type status: str, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async fetch_dispute(dispute_id: str)→ PayStackResponse

        Fetch a dispute.

        :param dispute_id: The ID of the dispute to fetch
        :type dispute_id: str

        :return: The response from the API
        :rtype: ClientEPayStackResponse object

    .. py:method:: async get_upload_url(dispute_id: str, uploaded_filename: str)→ PayStackResponse

        Get the upload URL for a dispute.

        :param dispute_id: The ID of the dispute to fetch
        :type dispute_id: str
        :param uploaded_filename: The name of the uploaded file with the extension
        :type uploaded_filename: str

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async list_disputes(from_date: date | None = None, to_date: date | None = None, per_page: int | None = 50, page: int | None = 1, transaction_id: str | None = None, status: str | None = None)→ PayStackResponse

        List disputes.

        :param from_date: The date from which to fetch disputes.
        :type from_date: date, optional
        :param to_date: The date until which to fetch disputes.
        :type to_date: date, optional
        :param per_page: The number of disputes to return per page.
        :type per_page: int, optional
        :param page: The page to return
        :type page: int, optional
        :param transaction_id: The ID of the transaction.
        :type transaction_id: str, optional
        :param status: The dispute status.
        :type status: str, optional

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async list_transaction_disputes(transaction_id: str)→ PayStackResponse

        List disputes for a transaction.

        :param transaction_id: The ID of the transaction.
        :type transaction_id: str

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async resolve_dispute(dispute_id: str, resolution: str, message: str, refund_amount: int, uploaded_filename: str, evidence: int | None = None)→ PayStackResponse

        Resolve a dispute.

        :param dispute_id: The ID of the dispute to resolve
        :type dispute_id: str
        :param resolution: The resolution to resolve the dispute. Values to pass: ``Resolution.value.value``
        :type resolution: str
        :param message: The message for resolution.
        :type message: str
        :param refund_amount: The refund amount to the customer
        :type refund_amount: int
        :param uploaded_filename: filename of attachment returned via response from method ``get_upload_url``
        :type uploaded_filename: str
        :param evidence: The evidence
        :type evidence: int, optional

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async update_dispute(dispute_id: str, refund_amount: int, uploaded_filename: str | None = None)→ PayStackResponse

        Update a dispute.

        :param dispute_id: The ID of the dispute to update
        :type dispute_id: str
        :param refund_amount: The refund amount to the customer
        :type refund_amount: int
        :param uploaded_filename: filename of attachment returned via response from method ``get_upload_url``
        :type uploaded_filename: str, optional

        :return: The response from the API
        :rtype: PayStackResponse object


.. _Disputes:  https://paystack.com/docs/api/dispute/

The ``status`` parameter has the string value of the ``DisputeStatus`` enum class.
Also, the ``resolution`` parameter has the string value of the ``Resolution`` enum class.
See documentation at :doc:`toolkit`.

.. important::

    Always ensure you use the filename gotten from the response of the ``get_upload_url`` method when uploading filename.
