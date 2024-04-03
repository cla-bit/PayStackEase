===========================================
Bulk Charges Module
===========================================

.. :py:currentmodule:: paystackease.apis.bulk_charges

Wrapper for Synchronous Paystack Bulk Charges API. The Bulk Charges API allows you to
create and manage multiple recurring payments from your customers.

To access the Bulk Charges API methods, you need to call the ``bulk_charges`` instance method from ``PayStackBase``.

Check example on :doc:`paystack`

------------------------------------------------------------------------------

.. py:class:: BulkChargesClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Bulk Charges API Reference: `Bulk Charges`_

    .. py:method:: fetch_bulk_charge_batch(id_or_code: str)→ Response

        Fetch a bulk charge of a specific batch

        :param id_or_code: An ID or code for the charge whose batches you want to retrieve.
        :type id_or_code: str

        :return: The response from the API.
        :rtype: Response object

    .. py:method:: fetch_charge_bulk_batch(id_or_code: str, status: str | None = None, per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ Response

        Fetch a bulk charge of a specific batch

        :param id_or_code: An ID or code for the charge whose batches you want to retrieve
        :type id_or_code: str
        :param status: The status of the bulk charge batch. The ``STATUS`` enum value is passed in here.
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
        :rtype: Response object

    .. py:method:: initiate_bulk_charge(objects: List[Dict[str, str]])→ Response

        Initiate a bulk charge

        :param objects: An array of objects with authorization codes and amount.
        :type objects: List[Dict[str, str]]

        :return: The response from the API.
        :rtype: Response object

    .. py:method:: list_bulk_charge_batches(per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ Response

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
        :rtype: Response object

    .. py:method:: pause_bulk_charge_batch(batch_code: str)→ Response

        Pause a bulk charge of a specific batch

        :param batch_code: The code of the bulk charge batch you want to pause.
        :type batch_code: str

        :return: The response from the API.
        :rtype: Response object

    .. py:method:: resume_bulk_charge_batch(batch_code: str)→ Response

        Resume a bulk charge of a specific batch

        :param batch_code: The code of the bulk charge batch you want to resume.
        :type batch_code: str

        :return: The response from the API
        :rtype: Response object


.. _Bulk Charges: https://paystack.com/docs/api/bulk-charge/


When passing the ``status`` parameter, you can pass the string value of the
``STATUS`` enum member as the type hint is a string, as seen:

.. code-block:: python

    >>> from paystackease import STATUS

    >>> status = STATUS.PENDING.value

    >>> print(status)

.. code-block:: console

    $ python
    >>> 'pending'


In initiating a bulk charge, the values being passed into the dictionary as keys are:
``authorization_code``, ``amount`` and ``reference``. These keys are passed alongside with their values into a
List. You can initiate multiple bulk charge at the same time also. The ``authorization_code`` is gotten after a successful card transaction.
The ``reference`` is a unique set of characters you can create as your desired choice.

You can also check to ensure that the amount passed into is in subunit. See the documentation
on :doc:`convert`.

**For example**

.. code-block:: python

    >>> from paystackease import PayStackBase

    >>> paystack_client = PayStackBase()

    >>> objects = [
    { "authorization_code": "AUTH_test1234", "amount": 10000, "reference": "test1234" },
    { "authorization_code": "AUTH_tester4176", "amount": 2000, "reference": "tester1234" },
    ]

    >>> response = paystack_client.bulk_charges.initiate_bulk_charge(objects)

    >>> print(response)


.. note::

    The date format is given as: `2016-09-21`. Later on we will include passing datetime also.
    Ensure you use the ``date`` module by importing it from ``datetime``.
