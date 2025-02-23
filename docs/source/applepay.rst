==================
Apple Pay Module
==================


This wrapper class enables synchronous interaction with the Paystack Apple Pay API.
The Apple Pay API allows you to register your application's top-level domain or subdomain,
enabling customers to make secure payment processing using Apple Pay on IOS and Safari.

To access the Apple Pay API methods, you need to call the ``apple_pay`` instance method from ``PayStackBase``.

See how to call the instance here: :doc:`paystack`

------------------------------------------------------------------------------

.. py:class:: ApplePayClientAPI()

    Paystack Apple Pay API Reference: `Apple Pay`_

    .. py:method:: list_domains(list_domains: Optional[ListDomainNamesModel] = None)→ PayStackResponse

        List all domains registered with the Apple Pay API.

        :param list_domains: A ListDomainNamesModel model representing parameters for listing domain names.
        :type list_domains: ListDomainNamesModel: a pydantic model class, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: register_domain(domain_name: DomainNameModel)→ PayStackResponse

        Register a domain with the Apple Pay API.

        :param domain_name: The domain name.
        :type domain_name: DomainNameModel pydantic model class.

        :return: The response from the API.
        :rtype: PayStackResponse object



    .. py:method:: unregister_domain(domain_name: DomainNameModel)→ PayStackResponse

        Unregister a domain with the Apple Pay API.

        :param domain_name: The domain name.
        :type domain_name: DomainNameModel pydantic model class.

        :return: The response from the API.
        :rtype: PayStackResponse object


.. _Apple Pay: https://paystack.com/docs/api/apple-pay/

.. important::

    The ``register_domain()`` method can only be called with one domain or subdomain at a time.

**Apple Pay Access**

1. **Requirement**: To use the Apple Pay functionality, you must have access to the Apple Pay endpoint.
2. **Verification**: If you're unsure about your access, please contact Paystack customer service for verification.
3. **Testing Environment**: Apple Pay might not be available on your testing environment. If you're using a testing environment and don't see the Apple Pay channel as an option, switch to a live environment and follow these instructions: https://paystack.com/docs/payments/apple-pay/
