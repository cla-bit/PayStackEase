.. This is the asynchronous base client and request API wrapper for paystackease

===================================
Asynchronous Base Client Wrappers
===================================

This contains a robust foundation for building asynchronous applications that interact seamlessly with the Paystack API.
From authentication and request handling to error management and extensibility, these classes empower developers to
integrate payment processing functionality efficiently, paving the way for enhanced user experiences and streamlined transaction management.


.. currentmodule:: paystackease.abase


The **AsyncBaseClientAPI** class serves as a base client API for interacting with the Paystack API asynchronously.
It encapsulates essential functionalities such as handling AIOHTTP requests, managing authentication,
and providing utility methods for data conversion and URL manipulation.
This class acts as a base for more specialized client APIs and establishes a standardized approach to communicate with the Paystack API.


..  py:class:: AsyncBaseClientAPI(secret_key: str = None)

    Bases: :py:class:`~object`

    Base Client API for Paystack API

----------------------------------------------------------------

The **AsyncPayStackBaseClientAPI** class extends the AsyncBaseClientAPI class and provides specific request methods for
interacting with the Paystack API endpoints asynchronously. It handles the requests: ``GET``, ``POST``, ``PUT``, and ``DELETE``.

..  py:class:: AsyncPayStackBaseClientAPI(secret_key: str = None)


    Bases: :py:class:`~paystackease.abase.AsyncBaseClientAPI`

    Requests methods to Paystack API

