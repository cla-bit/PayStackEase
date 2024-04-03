===========================================
Async Miscellaneous Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.amiscellaneous


Wrapper for Asynchronous Paystack Miscellaneous API. The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs.

You can use the tool kit in the helpers module as reference: :doc:`paystackease.helpers`

-------------


.. py:class:: AsyncMiscellaneousClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Miscellaneous API Reference: `Miscellaneous`_

    .. py:classmethod:: async list_banks(country: str | None = None, use_cursor: bool | None = False, per_page: int | None = 50, pay_with_bank_transfer: bool | None = False, pay_with_bank: bool | None = False, enabled_for_verification: bool | None = False, next_cursor: str | None = None, previous_cursor: str | None = None, gateway: str | None = None, channel_type: str | None = None, currency: str | None = None)→ ClientResponse

        Get a list of all supported banks and their properties

        :param country: The country to obtain the list of supported banks.
        :type country: str, optional
        :param use_cursor: Use cursor to paginate through the list of supported banks. (default: False)
        :type use_cursor: bool, optional
        :param per_page: Number of banks to return per page. (default: 50)
        :type per_page: int, optional
        :param pay_with_bank_transfer: filter for available banks a customer can make a transfer to complete a payment. (default: False)
        :type pay_with_bank_transfer: bool, optional
        :param pay_with_bank: filter for banks a customer can pay directly from. (default: False)
        :type pay_with_bank: bool, optional
        :param enabled_for_verification: filter the banks that are supported for account verification. (default: False)
        :type enabled_for_verification: bool, optional
        :param next_cursor: The cursor for the next page.
        :type next_cursor: str, optional
        :param previous_cursor: The cursor for the previous page.
        :type previous_cursor: str, optional
        :param gateway: filter for banks that support the specified gateway.
        :type gateway: str, optional
        :param channel_type: filter for banks that support the specified channel type.
        :type channel_type: str, optional
        :param currency: filter for banks that support the specified currency.
        :type currency: str, optional

        :return: The response from the API.
        :rtype: ClientResponse object

    .. py:method:: async list_countries()→ ClientResponse

        Get a list of all supported countries and their properties

        :return: The response from the API.
        :rtype: ClientResponse object

   .. py:method:: async list_states(country: str)→ ClientResponse

        Get a list of all supported states and their properties

        :param country: The country to obtain the list of supported states.
        :type country: str

        :return: The response from the API.
        :rtype: ClientResponse object

.. note::

    ``enable_for_verification`` is supported only for South Africa and combine with currency or country filter.
    If you set ``country`` as Ghana, please use either ``mobile_money`` for mobile money channels OR ``ghipps`` for bank channels type.

See documentation to get the string values for gateway, channel_type and currency enum classes: :doc:`toolkit`

.. _Miscellaneous: https://paystack.com/docs/api/miscellaneous/
