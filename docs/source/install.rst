================================
How to Install paystackease
================================

To use paystackease:

*   Create a virtual environment on Windows:

..  code-block:: console

    >>> py -m venv <environment_name>

* Activate the virtual environment:

..  code-block:: console

    >>> <environment_name>\Scripts\activate

*   Create a virtual environment on Unix/macOS:

..  code-block:: console

    >>> python3 -m venv <environment_name>

* Activate the virtual environment:

..  code-block:: console

    >>> <environment_name>/bin/activate

* Install paystackease using pip from PYPI:

.. code-block:: console

    >>> $ pip install paystackease

.. note::

    Create an account on Paystack or login if you already have an account,
    to generate a secret key for your application to interact with Paystack.

    You can create an account on Paystack here: `Paystack Create Account`_

    After which, go to your settings page >> API keys and Webhook section

.. warning::

    Do not expose your secret key or commit your secret key to git, or use them in client-side code.

.. hint::

    Paystack offers both public and secret keys. While the public key is used for front-end integration with Paystack Inline,
    the **paystackease** library only requires your secret key.

    With you secret key gotten from your Paystack account, set your secret key as environment variable named *PAYSTACK_SECRET_KEY*

.. _Paystack Create Account: https://paystack.com/
