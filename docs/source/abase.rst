paystackease.abase module
-------------------------


Async Base client API for Paystack API with methods for handling asynchronous AIOHTTP requests,
authentication using a secret key, constructing HTTP headers,
joining URLs with the API base URL, and logging response information.


..  py:class:: paystackease.abase.AsyncBaseClientAPI(secret_key: str = None)

    Bases: :py:class:`~object`

    Base Client API for Paystack API


..  py:class:: paystackease.abase.AsyncPayStackBaseClientAPI(secret_key: str = None)


    Bases: :py:class:`~paystackease.abase.AsyncBaseClientAPI`

    Requests methods to Paystack API

