paystackease.abase module
-------------------------

.. currentmodule:: paystackease.abase


Async Base client API for Paystack API with methods for handling asynchronous AIOHTTP requests,
authentication using a secret key, constructing HTTP headers,
joining URLs with the API base URL, and logging response information.


..  py:class:: AsyncBaseClientAPI(secret_key: str = None)

    Bases: :py:class:`~object`

    Base Client API for Paystack API

----------------------------------------------------------------

..  py:class:: AsyncPayStackBaseClientAPI(secret_key: str = None)


    Bases: :py:class:`~paystackease.abase.AsyncBaseClientAPI`

    Requests methods to Paystack API

