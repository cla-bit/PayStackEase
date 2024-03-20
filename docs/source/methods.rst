What HTTP request methods are supported?
=========================================================

Below are the following http methods that are supported:

* GET
* POST
* PUT
* DELETE


Supported Http Codes
======================

* **200** : Request was successful and intended action was carried out.

    .. note::
        Note that we will always send a 200 if a charge or verify request was made.
        Do check the data object to know how the charge went (i.e. successful or failed).

* **201** : A resource has successfully been created.
* **400** : A validation or client side error occurred and the request was not fulfilled.
* **401** : The request was not authorized. This can be triggered by passing an invalid secret key in the authorization header or the lack of one.
* **404** : Request could not be fulfilled as the request resource does not exist.
* **5xx** : Request could not be fulfilled due to an error on Paystack's end.

    .. attention::
        This shouldn't happen so please report as soon as you encounter any instance of this.


Request body data and response data formats supported
=======================================================

Both request body data and response data are formatted as JSON. All responses will be formatted as:

.. code-block:: console

    {
        "status": [boolean],
        "message": [string],
        "data": [object]
    }


