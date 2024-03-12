paystackease.async\_apis.acustomers module
------------------------------------------

.. :py:currentmodule:: paystackease.async_apis.acustomers


Wrapper for Asynchronous Paystack Customers API. The Customers API allows you to create and manage customers on your integration.

----------------------------------------------------------------

.. py:class:: AsyncCustomerClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Customer API Reference: `Customer`_

    .. py:method:: async create_customer(email: str, first_name: str, last_name: str, phone: str, metadata: Dict[str, Any] | None = None)→ dict

        Create a new customer.

        :param email: The customer's email address.
        :type email: str
        :param first_name: The customer's first name.
        :type first_name: str
        :param last_name: The customer's last name.
        :type last_name: str
        :param phone: The customer's phone number.
        :type phone: str
        :param metadata: The metadata of the customer in JSON format. (Set key as: {“custom_fields”: [{ “label”: “First Name”, “value”: “John” }] })
        :type metadata: dict, optional

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async deactivate_authorization(authorization_code: str)→ dict

        Deactivate an authorization.

        :param authorization_code: The authorization code.
        :type authorization_code: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: async fetch_customer(email_or_code: str)→ dict

        Fetch a customer.

        :param email_or_code: The customer's email or code.
        :type email_or_code: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: async list_customers(per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ dict

        List customers.

        :param per_page: The number of customers to return per page.
        :type per_page: int, optional
        :param page: The page to return.
        :type page: int, optional
        :param from_date: The customer's from date.
        :type from_date: date, optional
        :param to_date: The customer's to date.
        :type to_date: date, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: async update_customer(customer_code: str, first_name: str | None = None, last_name: str | None = None, phone: str | None = None, metadata: Dict[str, Any] | None = None)→ dict

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
        :rtype: dict

    .. py:method:: async validate_customer(email_or_code: str, first_name: str, last_name: str, account_type: str, country: str, bank_code: str, account_number: str, bvn: str, customer_id_num: str | None = None, middle_name: str | None = None)→ dict

        Validate a customer.

        :param email_or_code: The customer's code.
        :type email_or_code: str
        :param first_name: The customer's first name.
        :type first_name: str
        :param last_name: The customer's last name.
        :type last_name: str
        :param account_type: The type of account. Only bank_account is currently supported.
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
        :rtype: dict

    .. py:method:: async whitelist_blacklist_customer(email_or_code: str, risk_action: str | None = None)→ dict

        Whitelist or blacklist a customer.

        :param email_or_code: The customer's code.
        :type email_or_code: str
        :param risk_action: The action to take on the customer. value: RiskAction.value.value = “allow” pr “deny”
        :type risk_action: str, optional

        :return: The response from the API
        :rtype: dict



.. _Customer: https://paystack.com/docs/api/customer/
