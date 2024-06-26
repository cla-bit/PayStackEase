=========================
Async Bulk Charges Module
=========================


This wrapper class facilitates asynchronous interaction with Paystack Bulk Charges API. The Bulk Charges API allows you
to create and manage multiple recurring payments from your customers.

To access the Bulk Charges API methods, you need to call the ``bulk_charges`` instance method from ``AsyncPayStackBase``.

------------------------

.. py:class:: AsyncBulkChargesClientAPI(secret_key: str = None)

    Paystack Bulk Charges API Reference: `Bulk Charges`_

    .. py:method:: async fetch_bulk_charge_batch(id_or_code: str)→ PayStackResponse

        Fetch a bulk charge of a specific batch

        :param id_or_code: An ID or code for the charge whose batches you want to retrieve.
        :type id_or_code: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async fetch_charge_bulk_batch(id_or_code: str, status: str | None = None, per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ PayStackResponse

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
        :rtype: PayStackResponse object

    .. py:method:: async initiate_bulk_charge(objects: List[Dict[str, str]])→ PayStackResponse

        Initiate a bulk charge

        :param objects: An array of objects with authorization, amount and reference.
        :type objects: List[Dict[str, Any]]

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async list_bulk_charge_batches(per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ PayStackResponse

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
        :rtype: PayStackResponse object

    .. py:method:: async pause_bulk_charge_batch(batch_code: str)→ PayStackResponse

        Pause a bulk charge of a specific batch

        :param batch_code: The code of the bulk charge batch you want to pause.
        :type batch_code: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async resume_bulk_charge_batch(batch_code: str)→ PayStackResponse

        Resume a bulk charge of a specific batch

        :param batch_code: The code of the bulk charge batch you want to resume.
        :type batch_code: str

        :return: The response from the API
        :rtype: PayStackResponse object


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
``authorization``, ``amount`` and ``reference``. These keys are passed alongside with their values into a
List. You can initiate multiple bulk charge at the same time also. The ``authorization`` is gotten after a successful card transaction.
The ``reference`` is a unique set of characters you can create as your desired choice.

You can also check to ensure that the amount passed into is in subunit. See the documentation
on :doc:`convert`.

**For example**

.. code-block:: python

    >>> import asyncio
    >>> from paystackease import AsyncPayStackBase

    >>> objects = [
    { "authorization": "AUTH_test1234", "amount": 10000, "reference": "test1234" },
    { "authorization": "AUTH_tester4176", "amount": 2000, "reference": "tester1234" },
    ]

    >>> async def paystack_client():
    >>>     async with AsyncPayStackBase() as client:
    >>>         response = await client.bulk_charges.initiate_bulk_charge(objects)
    >>>         print(response)


    >>> asyncio.run(paystack_client())
