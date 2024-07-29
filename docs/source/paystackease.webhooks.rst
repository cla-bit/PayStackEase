-------------------------
PayStackEase Webhooks
-------------------------

This offers a comprehensive use case of paystack webhooks in various applications.
In this case, we'll be using a django web framework e-commerce application,
but the same applies to Flask or ny other frameworks.

.. note::
    It is assumed that you are familiar with django web framework architecture, models, views, templates.
    You'll also need to install the necessary packages ngrok (as this will be used locally to test) and paystackease.

.. important::
    You need to have a paystack account.


1. First, install the necessary packages:
    - ngrok
    - paystackease
    - Django (if you're using it) or any other web framework: Flask, FastAPI etc

2. Create a Django project and an app:

.. code-block:: console

    django-admin startproject your_project_name
    cd your_project_name
    python manage.py startapp your_app_name

3. Set up the PayStack settings:

    In the `your_project_name/settings.py` file, add the following:

.. code-block:: python

        PAYSTACK_SECRET_KEY = "your_paystack_secret_key"

4. Set up the necessary models, views, forms etc in your_app_name. In the views.py, you can use the `initialize` method
   from `PayStackBase.transactions` to start a new transaction and pass the values as arguments. To return a response, use the ``checkout_url`` method, optionally, you can use pass ``301`` as a status code.

5. Start up the ngrok server and include the name the server is listening to the localhost server to the ``ALLOWED_HOSTS`` your_project_name/settings.py, without the "https://".
Include the webhook url in your paystack API KEYS & WEBHOOKS account settings.

6. You can use the PayStackWebhook and PayStackSignatureVerifyError apis to get any event data and verify the server signature.

7. An example is shown on `Medium: Simplify Integration of Paystack API with Python Using PayStackEase & Webhooks! <https://medium.com/p/90432c9d112b>`_:
