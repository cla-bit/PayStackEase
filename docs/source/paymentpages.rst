===========================================
Payment Pages Module
===========================================

.. :py:currentmodule:: paystackease.apis.payment_pages


Wrapper for Paystack Payment Pages API. The Payment Pages API provides a quick and secure way to collect payment for products.

-----------

.. py:class:: PaymentPagesClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Miscellaneous API Reference: `Payment Pages`_

    .. py:method:: add_products(payment_id: int, product: List[int])→ PayStackResponse

        Add products to a payment page

        :param payment_id: ID of the payment page
        :type payment_id: int
        :param product: List of product IDs
        :type product: list

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: check_slug_available(page_slug: str)→ PayStackResponse

        Check if a page slug is available

        :param page_slug: URL slug you would like to be associated with this page.
        :type page_slug: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: create_payment_page(name: str, description: str | None = None, amount: int | None = None, split_code: str | None = None, page_slug: str | None = None, redirect_url: str | None = None, metadata: Dict[str, Any] | None = None, custom_fields: List[Dict[str, Any]] | None = None)→ PayStackResponse

        Create a new payment page

        :param name: Name of the payment page
        :type name: str
        :param description: Description of the payment page
        :type description: str, optional
        :param amount: Amount of the payment page
        :type amount: int, optional
        :param split_code: Split code of the transaction split
        :type split_code: str, optional
        :param page_slug: URL slug you would like to be associated with this page.
        :type page_slug: str, optional
        :param redirect_url: If you would like Paystack to redirect someplace upon successful payment, specify the URL here.
        :type redirect_url: str, optional
        :param metadata:  Extra data to configure the payment page.
        :type metadata: dict, optional
        :param custom_fields: List of custom fields you would like to add to the payment page
        :type custom_fields: list, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: fetch_payment_page(page_id_or_slug: str)→ PayStackResponse

        Fetch a payment page

        :param page_id_or_slug: ID or slug of the payment page
        :type page_id_or_slug: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: list_payment_pages(per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ PayStackResponse

        List all payment pages

        :param per_page: Number of payment pages per page
        :type per_page: int, optional
        :param page: Page number
        :type page: int, optional
        :param from_date: Date from which to list payment pages
        :type from_date: date, optional
        :param to_date: Date to which to list payment pages
        :type to_date: date, optional

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: update_payment_page(page_id_or_slug: str, name: str | None = None, description: str | None = None, amount: int | None = None, active: bool | None = None)→ PayStackResponse

        Update a payment page

        :param page_id_or_slug: ID or slug of the payment page
        :type page_id_or_slug: str
        :param name: Name of the payment page
        :type name: str, optional
        :param description: Description of the payment page
        :type description: str, optional
        :param amount: Amount of the payment page
        :type amount: int, optional
        :param active: Whether the payment page url should be deactivated or not. Set False to deactivate
        :type active: bool, optional

        :return: The response from the API.
        :rtype: PayStackResponse object


.. _Payment Pages: https://paystack.com/docs/api/page/

.. note::

    The ``page_slug`` parameter in the ``create_payment_page`` method will be accessible at ``https://paystack.com/pay/[page_slug]``

    The ``metadata`` can include subaccount, logo image, transaction charge etc. See documentation on how to set
    the ``custom_fields`` parameter: :doc:`metadata`.
