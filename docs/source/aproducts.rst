===========================================
Async Products Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.aproducts


Wrapper for Asynchronous Paystack Products API The Products API allows you to create and manage inventories on your integration.

-----------------------------------------------------------


.. py:class:: AsyncProductClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Product API Reference: `Products`_

    .. py:method:: async create_product(name: str, description: str, amount: int, currency: str, unlimited: bool | None = None, quantity: int | None = None)→ dict[source]

        Create a product

        :param name: The name of the product
        :type name: str
        :param description: The description of the product
        :type description: str
        :param amount: The amount of the product
        :type amount: int
        :param currency: The currency of the product
        :type currency: str
        :param unlimited: Whether or not the product is unlimited
        :type unlimited: bool, optional
        :param quantity: The quantity of the product
        :type quantity: int, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: async fetch_product(product_id: str)→ dict

        Fetch a product

        :param product_id: The ID of the product
        :type product_id: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: async list_products(per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ dict

        List products

        :param per_page: The number of products to return per page
        :type per_page: int, optional
        :param page: The page to return
        :type page: int, optional
        :param from_date: The date from which to list products
        :type from_date: date, optional
        :param to_date: The date until which to list products
        :type to_date: date, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: async update_product(product_id: str, name: str, description: str, amount: int, currency: str, unlimited: bool | None = None, quantity: int | None = None)→ dict

        Update a product

        :param product_id: The ID of the product
        :type product_id: str
        :param name: The name of the product
        :type name: str
        :param description: The description of the product
        :type description: str
        :param amount: The amount of the product
        :type amount: int
        :param currency: The currency of the product
        :type currency: str
        :param unlimited: Whether the product is unlimited
        :type unlimited: bool, optional
        :param quantity: The quantity of the product
        :type quantity: int, optional

        :return: The response from the API
        :rtype: dict


.. _Products: https://paystack.com/docs/api/product/
