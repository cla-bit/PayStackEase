===========================================
Async Integration Module
===========================================


This wrapper class facilitates asynchronous interaction with Paystack Integration API. The Integration API allows you manage some settings on your integration.

-------------------------------------------------------------------------

.. py:class:: AsyncIntegrationClientAPI(secret_key: str = None)

    Paystack Integration API Reference: `Integration`_

    .. py:method:: async fetch_timeout()→ PayStackResponse

        Fetch payment session timeout

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async update_timeout(timeout: int)→ PayStackResponse

        Update payment session timeout

        :param timeout: The new payment session timeout before session
        :type timeout: int

        :return: The response from the API.
        :rtype: PayStackResponse object

.. note::

    ``timeout`` is in seconds. Set 0 to cancel the timeout


.. _Integration: https://paystack.com/docs/api/integration/
