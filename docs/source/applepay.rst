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

    .. automethod:: list_domains
        :noindex:

    .. automethod:: register_domain
        :noindex:

    .. important::
        The ``paystackease.apis.apple_pay.register_domain`` method can only be called with one domain or subdomain at a time.


    .. automethod:: unregister_domain
        :noindex:


.. _Apple Pay: https://paystack.com/docs/api/apple-pay/


