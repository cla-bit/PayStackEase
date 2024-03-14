paystackease.async\_apis.apayment\_pages module
-----------------------------------------------

.. :py:currentmodule:: paystackease.async_apis.apayment_pages


Wrapper for Asynchronous Paystack Payment Pages API. The Payment Pages API provides a quick and secure way to collect payment for products.

--------------------------------------------------------------


.. py:class:: AsyncPaymentPagesClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Miscellaneous API Reference: `Payment Pages`_

    .. py:method:: async add_products(payment_id: int, product: List[int])→ dict

        Add products to a payment page

        :param payment_id: ID of the payment page
        :type payment_id: int
        :param product: List of product IDs
        :type product: list

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async check_slug_available(page_slug: str)→ dict

        Check if a page slug is available

        :param page_slug: URL slug you would like to be associated with this page.
        :type page_slug: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async create_payment_page(name: str, description: str | None = None, amount: int | None = None, split_code: str | None = None, page_slug: str | None = None, redirect_url: str | None = None, metadata: Dict[str, str] | None = None, custom_fields: List[str] | None = None)→ dict

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
        :param metadata:  Extra data to configure the payment page including subaccount,logo image, transaction charge
        :type metadata: dict, optional
        :param custom_fields: List of custom fields you would like to add to the payment page
        :type custom_fields: list, optional

        :return: The response from the API.
        :rtype: dict

        .. note::

            Page will be accessible at ``https://paystack.com/pay/page_slug``

    .. py:method:: async fetch_payment_page(page_id_or_slug: str)→ dict

        Fetch a payment page

        :param page_id_or_slug: ID or slug of the payment page
        :type page_id_or_slug: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async list_payment_pages(per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ dict

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
        :rtype: dict

    .. py:method:: async update_payment_page(page_id_or_slug: str, name: str | None = None, description: str | None = None, amount: int | None = None, active: bool | None = None)→ dict

        Update a payment page

        :param page_id_or_slug: ID or slug of the payment page
        :type page_id_or_slug: str
        :param name: Name of the payment page
        :type name: str, optional
        :param description: Description of the payment page
        :type description: str, optional
        :param amount: Amount of the payment page
        :type amount: int, optional
        :param active: Whether the payment page url should be deactivated or not. Set False to deativate
        :type active: bool, optional

        :return: The response from the API.
        :rtype: dict


.. _Payment Pages: https://paystack.com/docs/api/page/
