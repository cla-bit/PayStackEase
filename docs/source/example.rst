Example
=======

Go checkout how to install paystackease :ref:`installation`


.. hint::
    You must have generated a secret key from your paystack account and set the secret key as your environment variable:
    ``PAYSTACK_SECRET_KEY``.


The paystackease library to perform asynchronous and synchronous operations respectively:

* Synchronous support:

.. code-block:: python

    from paystackease import PayStackBase

    paystack_sync = PayStackBase()


* Asynchronous support:

.. code-block:: python

    from paystackease import AsyncPayStackBase

    async with AsyncPayStackBase() as paystack_async:
        # call any of the API wrappers here


----------------------------------------------------------------

Let's say you want to perform a transaction synchronously, you will have to call the transaction API wrapper.

.. code-block:: python

    create_transaction = paystack_sync.transactions.initialize(
    email="johndoe@email.com",
    amount=100000
    )

    print(f"Created Transaction: {create_transaction}")

>>> status_code: 200
{
    "status": true,
    "message": "Authorization URL created",
    "data": {
        "authorization_url": "https://checkout.paystack.com/0peioxfhpn",
        "access_code": "0peioxfhpn",
        "reference": "7PVGX8MEk85tgeEpVDtD"
    }
}

Click on the ``authorization_url`` link value on your terminal, this will open on your browser to complete the transaction.

.. note::
    You can get the ``authorization_url`` link value and return the value for users in your web application to
    complete their transaction process.
