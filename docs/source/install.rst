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

    >>> (venv) $ pip install paystackease

.. note::

    Create an account on Paystack or login if you already have an account,
    to generate a secret key for your application to interact with Paystack.

    You can create an account on Paystack here: `Paystack Create Account`_

    After which, go to your settings page >> API keys and Webhook section

.. warning::

    Do not expose your secret key or commit your secret key to git, or use them in client-side code.

.. hint::
    Public key is to be used from your front-end when integrating using Paystack Inline. In this case you have to use you secret key

    Set your environment variable as *PAYSTACK_SECRET_KEY*

.. _Paystack Create Account: https://paystack.com/
