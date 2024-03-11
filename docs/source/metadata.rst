What are the metadata to be passed in the request data?
=============================================================


Metadata are additional parameters to the request data, some of which are:

* cart ID
* order ID

In Paystack there are two ways to add metadata parameters or objects:

1. **Key/Value pair** :

    .. code-block:: python

        metadata = {
            "key1": "value1",
            "key2": "value2"
        }

2. **Custom Fields** :
    This contains three (3) keys: ``display_name``, ``variable_name`` and ``value``.

   .. code-block:: python

        metadata = {
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


You can check the Paystack Metadata for more use on what values to pass: `Paystack Metadata`_


.. _Paystack Metadata: https://paystack.com/docs/payments/metadata/