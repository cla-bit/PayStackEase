========================
How to use paystackease
========================

Go checkout how to install paystackease :doc:`install`.


.. hint::
    You must have generated a secret key from your paystack account and set the secret key as your environment variable:
    ``PAYSTACK_SECRET_KEY``.


As earlier said, paystackease performs both asynchronous and synchronous operations respectively.
You will import and instantiate the asynchronous and synchronous call wrappers as seen below:

* Synchronous support:

.. code-block:: python

    from paystackease import PayStackBase

    paystack_sync = PayStackBase()


* Asynchronous support:

.. code-block:: python

    from paystackease import AsyncPayStackBase

    async with AsyncPayStackBase() as paystack_async:
        # call any of the API wrappers here


Let's say you want to perform a transaction synchronously, you will have to call the transaction API wrapper.

.. code-block:: python

    create_transaction = paystack_sync.transactions.initialize(
    email="johndoe@email.com",
    amount=100000
    )

    print(f"Created Transaction: {create_transaction}")

The response from the server will be as follows:

.. code-block:: console

    status_code: 200
    {
        "status": true,
        "message": "Authorization URL created",
        "data": {
            "authorization_url": "https://checkout.paystack.com/0peioxfhpn",
            "access_code": "0peioxfhpn",
            "reference": "7PVGX8MEk85tgeEpVDtD"
        }
    }

To redirect the user to Paystack checkout page to make payments, you will need to call
the ``url`` method from your instance and pass a ``301`` ``status code`` parameter


**See Example**

This is a django example of how to redirect users to Paystack checkout page to proceed with payment.

.. code-block:: python

    session = paystack_client.transactions.initialize(
    email=order.email, amount=amount, currency="NGN",
    callback_url=success_url, metadata=metadata)

    return redirect(session.url, code=301)

Also the ``webbrowser`` module is another approach to redirect users to Paystack checkout page. Which ever is your
choice is best.

.. code-block:: python

    import webbrowser

    webbrowser.open(session.url)
