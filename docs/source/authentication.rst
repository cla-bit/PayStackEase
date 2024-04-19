Authentication
=====================

With your secret key, paystackease can authenticate your API calls in the `Authorization header` of your request.

.. attention::
    The secret key should be in your environment variable.


**Secret Keys and Public Secret Keys**

For Paystack integrations, the choice between secret key (ideal for secure server-side processing with PaystackEase authentication)
and public key (suitable for front-end Paystack Inline integrations but not compatible with PaystackEase)
depends on your application's processing needs.
