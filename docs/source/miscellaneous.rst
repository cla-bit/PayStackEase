===========================================
Miscellaneous Module
===========================================

.. :py:currentmodule:: paystackease.apis.miscellaneous


Wrapper for Paystack Miscellaneous API. The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs.

You can use the tool kit in the helpers module as reference: :doc:`paystackease.helpers`

----------------------------------------------------------------------


.. py:class:: MiscellaneousClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Miscellaneous API Reference: `Miscellaneous`_

    .. py:classmethod:: list_banks(country: str | None = None, use_cursor: bool | None = False, per_page: int | None = None, pay_with_bank_transfer: bool | None = None, pay_with_bank: bool | None = None, enabled_for_verification: bool | None = None, next_cursor: str | None = None, previous_cursor: str | None = None, gateway: str | None = None, channel_type: str | None = None, currency: str | None = None)→ dict

        Get a list of all supported banks and their properties

        :param country: The country to obtain the list of supported banks. Values: ``Country.value.value``
        :type country: str, optional
        :param use_cursor: Use cursor to paginate through the list of supported banks. (default = False)
        :type use_cursor: bool, optional
        :param per_page: Number of banks to return per page.
        :type per_page: int, optional
        :param pay_with_bank_transfer: filter for available banks a customer can make a transfer to complete a payment
        :type pay_with_bank_transfer: bool, optional
        :param pay_with_bank: filter for banks a customer can pay directly from
        :type pay_with_bank: bool, optional
        :param enabled_for_verification: filter the banks that are supported for account verification
        :type enabled_for_verification: bool, optional
        :param next_cursor: The cursor for the next page.
        :type next_cursor: str, optional
        :param previous_cursor: The cursor for the previous page.
        :type previous_cursor: str, optional
        :param gateway: filter for banks that support the specified gateway. Values: (emandate or digitalbankmandate)
        :type gateway: str, optional
        :param channel_type: filter for banks that support the specified channel type. Values: ``Channels.value.value``
        :type channel_type: str, optional
        :param currency: filter for banks that support the specified currency. Values: ``Currency.value.value``
        :type currency: str, optional

        :return: The response from the API.
        :rtype: dict

    .. py:method:: list_countries()→ dict

        Get a list of all supported countries and their properties

        :return: The response from the API.
        :rtype: dict

   .. py:method:: list_states(country: str)→ dict

        Get a list of all supported states and their properties

        :param country: The country to obtain the list of supported states.
        :type country: str

        :return: The response from the API.
        :rtype: dict

.. note::

    ``enable_for_verification`` is supported only for South Africa and combine with currency or country filter.
    If you set ``country`` as Ghana, please use either ``mobile_money`` for mobile money channels OR ``ghipps`` for bank channels type.


.. _Miscellaneous: https://paystack.com/docs/api/miscellaneous/
