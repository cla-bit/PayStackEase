.. This is the synchronous base client and request API wrapper for paystackease

===================================
Synchronous Base Client Wrappers
===================================

This contains a robust foundation for building synchronous applications that interact seamlessly with the Paystack API.
From authentication and request handling to error management and extensibility, these classes empower developers to
integrate payment processing functionality efficiently, paving the way for enhanced user experiences and streamlined transaction management.


.. currentmodule:: paystackease.base


The **BaseClientAPI** class serves as the foundation for interacting with the Paystack API.
It encapsulates essential functionalities such as handling HTTP requests, managing authentication,
and providing utility methods for data conversion and URL manipulation.
This class acts as a base for more specialized client APIs and establishes a standardized approach to communicate with the Paystack API.


..  py:class:: BaseClientAPI(secret_key: str = None)

    Bases: :py:class:`~object`

    Base Client API for Paystack API

----------------------------------------------------------------

The **PayStackBaseClientAPI** class extends the BaseClientAPI class and provides specific request methods for
interacting with the Paystack API endpoints synchronously. It handles the requests: ``GET``, ``POST``, ``PUT``, and ``DELETE``.

..  py:class:: PayStackBaseClientAPI(secret_key: str = None)


    Bases: :py:class:`~paystackease.base.BaseClientAPI`

    Requests methods to Paystack API

