What are the metadata to be passed in the request data?
=============================================================


Metadata are additional parameters to the request data, some of which are:

* cart ID
* order ID
* cancel_action
* custom_filters

In Paystack there are two ways to add metadata parameters or objects:

Key/Value pair
====================

.. code-block:: python

    "metadata": {
        "key1": "value1",
        "key2": "value2"
    }

This is acceptable as a metadata object:

.. code-block:: python

    "metadata": {
        "key1": "value1",
        "key2": "value2",
        "custom_fields": [
            {
                "display_name": "value",
                "variable_name": "value",
                "value": 100
            }
        ],
        "order_id": "1234567890",
        "cart_id": "1234567890",
        "cancel_action": "http://example.com/cancel",
        "custom_filters": {"recurring": True}
    }

Custom Fields
====================

This contains three (3) keys: ``display_name``, ``variable_name`` and ``value``.

.. code-block:: python

    "metadata": {
        "custom_fields": [
            {
                "display_name": "your_value",
                "variable_name": "your_value",
                "value": "your_value"
            },
            {
                "display_name": "your_value",
                "variable_name": "your_value",
                "value": "your_value"
            }
        ]
    }

.. note::

    The custom_fields key is reserved for an array of custom fields that should show on the dashboard when you click the transaction.

Redirecting users from Paystack payment page to you application or your desired choice, if users cancel a payment process.
This is done by passing a ``cancel_action`` parameter in the metadata.

.. code-block:: python

    "metadata": {
        "cancel_action": "http://example.com/cancel"
    }

If you want control on how a transaction is completed, use ``custom_filters`` object passed in the metadata object.
To directly debit your users in future, set ``recurring=True`` in the ``custom_filters`` object.
This ensures the acceptance of only Verve cards that support recurring billing and
force a bank authentication for MasterCard and VISA.

.. code-block:: python

    "metadata": {
        "recurring": True
    }

You can use the banks parameter to specify an array of bank codes if you only want certain bank cards to be accepted for a transaction.

.. code-block:: python

    "metadata": {
        "banks": ["057", "024"]
    }

If you only want certain card brand(s) to be accepted for a transaction, specify the brands in the card_brands array:

.. code-block:: python

    "metadata": {
        "card_brands": ["visa", "verve", "mastercard"]
    }

.. note::

    Verve is only supported in Nigeria.

Sometimes, you want to give preference to only certain mobile money providers.

.. code-block:: python

    "metadata": {
        "supported_mobile_money_providers": ["mtn", "atl", "vod"]
    }

.. note::

    Mobile money is only supported in Ghana.
