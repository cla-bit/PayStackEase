paystackease.async\_apis.aapple\_pay module
-------------------------------------------

.. :py:currentmodule:: paystackease.async_apis.aapple_pay

.. attention::
    Ensure you have access to use the Apple Pay endpoint, else call Paystack Customer service.

Wrapper class for Asynchronous Paystack Apple Pay API. The Apple Pay API allows you register your application’s top-level domain or subdomain.

------------------------------------------------------------------------------

.. py:class:: AsyncApplePayClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Apple Pay API Reference: `Apple Pay`_

    .. py:method:: async list_domains(use_cursor: bool | None = False, next_page: int | None = None, previous_page: int | None = None)→ dict

        List all domains registered with the Apple Pay API.

        :param use_cursor: Use cursor for pagination (default: False).
        :type use_cursor: bool, optional
        :param next_page: Next page.
        :type next_page: int, optional
        :param previous_page: Previous page.
        :type previous_page: int, optional

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async register_domain(domain_name: str)→ dict

        Register a domain with the Apple Pay API.

        :param domain_name: The domain name.
        :type domain_name: str

        :return: The response from the API.
        :rtype: dict



    .. py:method:: async unregister_domain(domain_name: str)→ dict

        Unregister a domain with the Apple Pay API.

        :param domain_name: The domain name.
        :type domain_name: str

        :return: The response from the API.
        :rtype: dict


.. _Apple Pay: https://paystack.com/docs/api/apple-pay/

.. important::

    The :py:meth:`~paystackease.async_apis.aapple_pay.AsyncApplePayClientAPI.register_domain` method can only be called with one domain or subdomain at a time.
