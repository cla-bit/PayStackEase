paystackease.apis.bulk\_charges module
--------------------------------------

.. :py:currentmodule:: paystackease.apis.bulk_charges


Wrapper for Synchronous Paystack Bulk Charges API. The Bulk Charges API allows you to create and manage multiple recurring payments from your customers.

------------------------------------------------------------------------------

.. py:class:: BulkChargesClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Bulk Charges API Reference: `Bulk Charges`_

    .. py:method:: fetch_bulk_charge_batch(id_or_code: str)→ dict

        Fetch a bulk charge of a specific batch

        :param id_or_code: An ID or code for the charge whose batches you want to retrieve.
        :type id_or_code: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: fetch_charge_bulk_batch(id_or_code: str, status: str | None = None, per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ dict

        Fetch a bulk charge of a specific batch

        :param id_or_code: An ID or code for the charge whose batches you want to retrieve
        :type id_or_code: str
        :param status: The status of the bulk charge batch.
        :type status: str, optional
        :param per_page: The number of records to return per page.
        :type per_page: int, optional
        :param page: The page to return.
        :type page: int, optional
        :param from_date: The starting date of the bulk charge batch.
        :type from_date: date, optional
        :param to_date: The ending date of the bulk charge batch.
        :type to_date: date, optional

        :return: The response from the API.
        :rtype: dict

        .. note::

            ``Date and Time format``: 2016-09-24T00:00:05.000Z, 2016-09-21

            ``status``: STATUS.value.value

    .. py:method:: initiate_bulk_charge(objects: List[Dict[str, str]] = None)→ dict

        Initiate a bulk charge

        :param objects: An array of objects with authorization codes and amount.
        :type objects: List[Dict[str, str]]

        :return: The response from the API.
        :rtype: dict

        .. code-block::

            [{"authorization_code": "123456", "amount": 1000, "reference": "123456" }]

        .. important::

            A list of dictionary with ``authorization codes``, ``amount`` and ``reference`` as keys

    .. py:method:: list_bulk_charge_batches(per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ dict

        List bulk charge batches

        :param per_page: The number of records to return per page.
        :type per_page: int, optional
        :param page: The page to return.
        :type page: int, optional
        :param from_date: The starting date of the bulk charge batch.
        :type from_date: date, optional
        :param to_date: The ending date of the bulk charge batch.
        :type to_date: date, optional

        :return: The response from the API.
        :rtype: dict

        .. note::

            ``Date and Time format``: 2016-09-24T00:00:05.000Z, 2016-09-21

    .. py:method:: pause_bulk_charge_batch(batch_code: str)→ dict

        Pause a bulk charge of a specific batch

        :param batch_code: The code of the bulk charge batch you want to pause.
        :type batch_code: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: resume_bulk_charge_batch(batch_code: str)→ dict

        Resume a bulk charge of a specific batch

        :param batch_code: The code of the bulk charge batch you want to resume.
        :type batch_code: str

        :return: The response from the API
        :rtype: dict


.. _Bulk Charges: https://paystack.com/docs/api/bulk-charge/
