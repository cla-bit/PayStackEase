=========================
Async Bulk Charges Module
=========================


This wrapper class facilitates asynchronous interaction with Paystack Bulk Charges API. The Bulk Charges API allows you
to create and manage multiple recurring payments from your customers.

To access the Bulk Charges API methods, you need to call the ``bulk_charges`` instance method from ``AsyncPayStackBase``.

------------------------

.. py:class:: AsyncBulkChargesClientAPI()

    Paystack Bulk Charges API Reference: `Bulk Charges`_

    .. py:method:: async fetch_bulk_charge_batch(id_or_code: str)→ PayStackResponse

        Fetch a bulk charge of a specific batch

        :param id_or_code: An ID or code for the charge whose batches you want to retrieve.
        :type id_or_code: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async fetch_charge_bulk_batch(id_or_code: str, page_values: Optional[PageModel] = None, date_values: Optional[DatePageModel] = None, status: Optional[STATUS] = None)→ PayStackResponse

        Fetch a bulk charge of a specific batch

        :param id_or_code: An ID or code for the charge whose batches you want to retrieve
        :type id_or_code: str
        :param page_values: Optional page model with page and per_page values.
        :type page_values: Optional[PageModel], optional
        :param date_values: Optional date page model with from_date and to_date values.
        :type date_values: Optional[DatePageModel], optional
        :param status: The status of the bulk charge batch. The ``STATUS`` enum value is passed in here.
        :type status: STATUS, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async initiate_bulk_charge(objects: Union[BulkChargeObject, List[BulkChargeObject]])→ PayStackResponse

        Initiate a bulk charge

        :param objects: An array of objects with authorization, amount and reference.
        :type objects: BulkChargeObject | List[BulkChargeObject]

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async list_bulk_charge_batches(page_values: Optional[PageModel] = None, date_values: Optional[DatePageModel] = None)→ PayStackResponse

        List bulk charge batches

        :param page_values: Optional page model with page and per_page values.
        :type page_values: Optional[PageModel], optional
        :param date_values: Optional date page model with from_date and to_date values.
        :type date_values: Optional[DatePageModel], optional

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
    >>> from paystackease.helpers import BulkChargeObject

    >>> objects = BulkChargeObject(amount=10000, authorization="AUTH_test1234", reference="test1234")
    >>> objects1 = BulkChargeObject(amount=10000, authorization="AUTH_test1234", reference="test1234")

    >>> async def paystack_client():
    >>>     async with AsyncPayStackBase() as client:
    >>>         response = await client.bulk_charges.initiate_bulk_charge(objects)  # pass it as a single BulkChargeObject instance
    >>>         print(response)

    >>> asyncio.run(paystack_client())


    >>> async def paystack_client():
    >>>     async with AsyncPayStackBase() as client:
    >>>         response = await client.bulk_charges.initiate_bulk_charge([objects, objects1])  # pass it as a list BulkChargeObject instances
    >>>         print(response)

    >>> asyncio.run(paystack_client())
