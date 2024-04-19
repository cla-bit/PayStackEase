========================
How to use paystackease
========================

For installation instructions, refer to: :doc:`install`.


.. hint::

    Before using the PaystackEase library, you'll need a secret key generated from your Paystack account.
    Set this secret key as an environment variable named **PAYSTACK_SECRET_KEY**.

The PaystackEase library supports both asynchronous and synchronous operations.
To use them, import and instantiate the appropriate wrappers as shown below:

* Synchronous support:

.. code-block:: python

    from paystackease import PayStackBase

    paystack_sync = PayStackBase()


* Asynchronous support:

.. code-block:: python

    from paystackease import AsyncPayStackBase

    async with AsyncPayStackBase() as paystack_async:
        # call any of the API wrappers here


To perform a transaction synchronously, use the transaction API wrapper.
The example below demonstrates the use of the ``initialize`` method in the transaction API wrapper:

.. code-block:: python

    create_transaction = paystack_sync.transactions.initialize(
    email="johndoe@email.com",
    amount=100000
    )

    print(f"Created Transaction: {create_transaction}")

The response from the server will be as follows:

.. code-block:: console

    PayStackResponse(
        status_code=200,
        status=True,
        message="Authorization URL created",
        data={
            "authorization_url": "https://checkout.paystack.com/0peioxfhpn",
            "access_code": "0peioxfhpn",
            "reference": "7PVGX8MEk85tgeEpVDtD"
        }
    )


To redirect the user to Paystack checkout page to make payments, your application should call
the ``url`` method from your response instance and provide a ``301`` ``status code`` parameter (optional).


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
