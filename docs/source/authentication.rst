Authentication
=====================

With your secret key, paystackease can authenticate your API calls in the `Authorization header` of your request.

.. code-block:: python

    {
        "Authorization": f"Bearer {secret_key}",
    }

.. attention::
    The secret key should be in your environment variable.


Secret Keys and Public Secret Keys
=====================================

Paystackease uses a secret key to authenticate your API calls, while the public key is meant for your front-end, when integrating
Paystack Inline and in Mobile SDKs only.
