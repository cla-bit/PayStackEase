===========================================
Async Integration Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.aintegration


Wrapper for Asynchronous Paystack Integration API The Integration API allows you manage some settings on your integration.

-------------------------------------------------------------------------

.. py:class:: AsyncIntegrationClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Integration API Reference: `Integration`_

    .. py:method:: async fetch_timeout()→ PayStackPayStackResponse

        Fetch payment session timeout

        :return: The response from the API.
        :rtype: PayStackPayStackResponse object

    .. py:method:: async update_timeout(timeout: int)→ PayStackPayStackResponse

        Update payment session timeout

        :param timeout: The new payment session timeout before session
        :type timeout: int

        :return: The response from the API.
        :rtype: PayStackPayStackResponse object

.. note::

    ``timeout`` is in seconds. Set 0 to cancel the timeout


.. _Integration: https://paystack.com/docs/api/integration/
