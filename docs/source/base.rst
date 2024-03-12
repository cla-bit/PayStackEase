paystackease.base module
------------------------

.. currentmodule:: paystackease.base


Base client API for Paystack API with methods for handling asynchronous HTTP requests,
authentication using a secret key, constructing HTTP headers,
joining URLs with the API base URL, and logging response information.


..  py:class:: BaseClientAPI(secret_key: str = None)

    Bases: :py:class:`~object`

    Base Client API for Paystack API

----------------------------------------------------------------

..  py:class:: PayStackBaseClientAPI(secret_key: str = None)


    Bases: :py:class:`~paystackease.base.BaseClientAPI`

    Requests methods to Paystack API

