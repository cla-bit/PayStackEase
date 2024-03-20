=========================================
Synchronous Paystack Wrapper
=========================================


.. currentmodule:: paystackease.paystack


The **PayStackBase** class serves as a comprehensive wrapper around various client APIs, providing a unified interface
to interact with the PayStack API synchronously. It encapsulates individual client APIs for different aspects of PayStack
services, such as payments, customers, disputes, and more, simplifying the integration process and promoting code organization.


..  py:class:: PayStackBase(secret_key=None)

    Bases: :py:class:`PayStackBaseClientAPI`

    PayStackBase acts as a wrapper around various client APIs to interact with the PayStack API


**USAGE**

.. code-block:: python

    >>> from paystackease import PayStackBase

    >>> paystack = PayStackBase()
    >>> response = paystack.apple_pay.register_domain(domain_name="your-domain-name-here")

    >>> print(f"Response: {response}")


.. note::

    You can also pass the parameter ``secret_key`` to the PayStackBase class. This will override the environment variable.
    It is highly recommended to use the set the environment variable as ``PAYSTACK_SECRET_KEY`` and ensure it is safe.
