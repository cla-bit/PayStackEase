=========================
Async Bulk Charges Module
=========================

.. :py:currentmodule:: paystackease.async_apis.abulk_charges

Wrapper for Asynchronous Paystack Bulk Charges API. The Bulk Charges API allows you to create and manage multiple recurring payments from your customers.

------------------------------------------------------------------------------

.. py:class:: AsyncBulkChargesClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Bulk Charges API Reference: `Bulk Charges`_

    .. py:method:: async fetch_bulk_charge_batch(id_or_code: str)→ dict

        Fetch a bulk charge of a specific batch

        :param id_or_code: An ID or code for the charge whose batches you want to retrieve.
        :type id_or_code: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async fetch_charge_bulk_batch(id_or_code: str, status: str | None = None, per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ dict

        Fetch a bulk charge of a specific batch

        :param id_or_code: An ID or code for the charge whose batches you want to retrieve
        :type id_or_code: str
        :param status: The status of the bulk charge batch.
        :type status: str, optional
        :param per_page: The number of records to return per page (default: 50).
        :type per_page: int, optional
        :param page: The page to return (default: 1).
        :type page: int, optional
        :param from_date: The starting date of the bulk charge batch.
        :type from_date: date, optional
        :param to_date: The ending date of the bulk charge batch.
        :type to_date: date, optional

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async initiate_bulk_charge(objects: List[Dict[str, str]] = None)→ dict

        Initiate a bulk charge

        :param objects: An array of objects with authorization codes and amount.
        :type objects: List[Dict[str, str]]

        :return: The response from the API.
        :rtype: dict

        .. code-block::

            [{"authorization_code": "123456", "amount": 1000, "reference": "123456" }]

        .. important::

            A list of dictionary with ``authorization codes``, ``amount`` and ``reference`` as keys

    .. py:method:: async list_bulk_charge_batches(per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ dict

        List bulk charge batches

        :param per_page: The number of records to return per page (default: 50).
        :type per_page: int, optional
        :param page: The page to return (default: 1).
        :type page: int, optional
        :param from_date: The starting date of the bulk charge batch.
        :type from_date: date, optional
        :param to_date: The ending date of the bulk charge batch.
        :type to_date: date, optional

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async pause_bulk_charge_batch(batch_code: str)→ dict

        Pause a bulk charge of a specific batch

        :param batch_code: The code of the bulk charge batch you want to pause.
        :type batch_code: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async resume_bulk_charge_batch(batch_code: str)→ dict

        Resume a bulk charge of a specific batch

        :param batch_code: The code of the bulk charge batch you want to resume.
        :type batch_code: str

        :return: The response from the API
        :rtype: dict


.. _Bulk Charges: https://paystack.com/docs/api/bulk-charge/

.. note::

    ``Date and Time format``: 2016-09-24T00:00:05.000Z, 2016-09-21

    ``status``: STATUS.value.value
