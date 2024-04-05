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

It is a matter of choice depending on how you want you application to process payment with Paystack API calls. If you want to use
a server-side independently, using the **secret key** is best suited as this will give you full control and security.
However, if you want to implement using **public key**, kindly note that you are no longer dealing with a server-side but a frontend-side.
As such, paystackease will not be able to authenticate your **public key** with Paystack API calls.

Paystackease uses a **secret key** to authenticate with Paystack API calls, while the **public key** is meant for your front-end, when integrating
Paystack Inline and in Mobile SDKs only.
