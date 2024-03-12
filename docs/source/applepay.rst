paystackease.apis.apple\_pay module
-----------------------------------

.. currentmodule:: paystackease.apis.apple_pay

.. attention::
    Ensure you have access to use the Apple Pay endpoint, else call Paystack Customer service.


Wrapper class for Paystack Apple Pay API.

The Apple Pay API allows you register your application’s top-level domain or subdomain.

.. py:class:: ApplePayClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Apple Pay API Reference: `Apple Pay`_

    .. py:method:: list_domains(use_cursor: bool | None = False, next_page: int | None = None, previous_page: int | None = None)→ dict

        :param use_cursor: Use cursor for pagination (default: False).
        :type use_cursor: bool, optional
        :param next_page: Next page.
        :type next_page: int, optional
        :param previous_page: Previous page.
        :type previous_page: int, optional

        :return: The response from the API.
        :rtype: dict

    .. py:method:: register_domain(domain_name: str)→ dict

        :param domain_name: The domain name.
        :type domain_name: str

        :return: The response from the API.
        :rtype: dict

    .. important::
        The :py:meth:`~paystackease.apis.apple_pay.ApplePayClientAPI.register_domain` method can only be called with one domain or subdomain at a time.

    .. py:method:: unregister_domain(domain_name: str)→ dict

        :param domain_name: The domain name.
        :type domain_name: str

        :return: The response from the API.
        :rtype: dict


.. _Apple Pay: https://paystack.com/docs/api/apple-pay/
