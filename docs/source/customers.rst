===========================================
Customers Module
===========================================


This wrapper class facilitates asynchronous interaction with Paystack Customers API. The Customers API allows you to create and manage
customers on your integration.

To access the Customers API methods, you need to call the ``customers`` instance method from ``PayStackBase``.

Check example on :doc:`paystack`

----------------------------------------------------------------

.. py:class:: CustomerClientAPI(secret_key: str = None)

    Paystack Customer API Reference: `Customer`_

    .. py:method:: create_customer(email: str, first_name: str, last_name: str, phone: str, metadata: Dict[str, Any] | None = None)→ PayStackResponse

        Create a new customer.

        :param email: The customer's email address.
        :type email: str
        :param first_name: The customer's first name.
        :type first_name: str
        :param last_name: The customer's last name.
        :type last_name: str
        :param phone: The customer's phone number.
        :type phone: str
        :param metadata: The metadata of the customer in JSON format.
        :type metadata: dict, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: deactivate_authorization(authorization_code: str)→ PayStackResponse

        Deactivate an authorization.

        :param authorization_code: The authorization code.
        :type authorization_code: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: fetch_customer(email_or_code: str)→ PayStackResponse

        Fetch a customer.

        :param email_or_code: The customer's email or code.
        :type email_or_code: str

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: list_customers(per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ PayStackResponse

        List customers.

        :param per_page: The number of customers to return per page (default: 50).
        :type per_page: int, optional
        :param page: The page to return (default: 1).
        :type page: int, optional
        :param from_date: The customer's from date.
        :type from_date: date, optional
        :param to_date: The customer's to date.
        :type to_date: date, optional

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: update_customer(customer_code: str, first_name: str | None = None, last_name: str | None = None, phone: str | None = None, metadata: Dict[str, Any] | None = None)→ PayStackResponse

        Update a customer.

        :param customer_code: The customer's code.
        :type customer_code: str
        :param first_name: The customer's first name.
        :type first_name: str, optional
        :param last_name: The customer's last name.
        :type last_name: str, optional
        :param phone: The customer's phone number.
        :type phone: str, optional
        :param metadata: The customer's metadata.
        :type metadata: dict, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: validate_customer(email_or_code: str, first_name: str, last_name: str, account_type: str, country: str, bank_code: str, account_number: str, bvn: str, customer_id_num: str | None = None, middle_name: str | None = None)→ PayStackResponse

        Validate a customer.

        :param email_or_code: The customer's code.
        :type email_or_code: str
        :param first_name: The customer's first name.
        :type first_name: str
        :param last_name: The customer's last name.
        :type last_name: str
        :param account_type: The type of account. Only ``"bank_account"`` is currently supported.
        :type account_type: str
        :param country: The country of the customer. 2-letter country code of identification issuer
        :type country: str
        :param bank_code: The customer's bank code.
        :type bank_code: str
        :param account_number: The customer's account number.
        :type account_number: str
        :param bvn: The customer's bvn [Bank Verification Number]
        :type bvn: str
        :param customer_id_num: The customer identification number
        :type customer_id_num: str, optional
        :param middle_name: The customer's middle name.
        :type middle_name: str, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: whitelist_blacklist_customer(email_or_code: str, risk_action: str | None = None)→ PayStackResponse

        Whitelist or blacklist a customer.

        :param email_or_code: The customer's code.
        :type email_or_code: str
        :param risk_action: The action to take on the customer.
        :type risk_action: str, optional

        :return: The response from the API
        :rtype: PayStackResponse object


.. _Customer: https://paystack.com/docs/api/customer/

In creating a customer, the ``metadata`` parameter is of the ``key-value pair`` metadata type. See more on :doc:`metadata`.

.. code-block:: console

    >>> {
    >>>     "metadata": {
    >>>         'key': "value"
    >>>     }
    >>> }

The ``risk_action`` parameter takes in a string value of the ``Risk Action`` enum member. See more on :doc:`toolkit`

.. code-block:: python

    >>> from paystackease import RiskAction
    >>> risk_action = RiskAction.DENY.value
    >>> print(risk_action)

.. code-block:: console

    $ python
    >>> 'deny'
