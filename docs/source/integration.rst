===========================================
Integration Module
===========================================

.. :py:currentmodule:: paystackease.apis.integration


Wrapper for Paystack Integration API The Integration API allows you manage some settings on your integration.

-------------------------------------------------------------------------

.. py:class:: IntegrationClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Integration API Reference: `Integration`_

    .. py:method:: fetch_timeout()→ Response

        Fetch payment session timeout

        :return: The response from the API.
        :rtype: Response object

    .. py:method:: update_timeout(timeout: int)→ Response

        Update payment session timeout

        :param timeout: The new payment session timeout before session
        :type timeout: int

        :return: The response from the API.
        :rtype: Response object

.. note::

    ``timeout`` is in seconds. Set 0 to cancel the timeout


.. _Integration: https://paystack.com/docs/api/integration/
