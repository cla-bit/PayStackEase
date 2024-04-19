===========================================
Async Dedicated Virtual Accounts Module
===========================================


This wrapper class facilitates asynchronous interaction with Paystack Dedicated Virtual Account API.
The Dedicated Virtual Account API enables Nigerian merchants to manage unique payment accounts of their customers.

.. note::

    Ensure Dedicated NUBAN is available for your business. Contact Paystack Support

-----------

.. py:class:: AsyncDedicatedVirtualAccountClientAPI(secret_key: str = None)

    Paystack Customer API Reference: `Dedicated Virtual Account`_

    .. py:method:: async assign_dedicated_virtual_account(email: str, first_name: str, last_name: str, phone: str, preferred_bank: str, country: str, account_number: str | None = None, bvn: str | None = None, bank_code: str | None = None, subaccount: str | None = None, split_code: str | None = None)→ PayStackResponse

        Ensure Dedicated NUBAN is available for your business. Contact Paystack Support

        :param email: The email address associated to the customer
        :type email: str
        :param first_name: The first name of the customer
        :type first_name: str
        :param last_name: The last name of the customer
        :type last_name: str
        :param phone: The phone number associated to the customer
        :type phone: str
        :param preferred_bank: The preferred bank slug for the virtual account
        :type preferred_bank: str
        :param country: The country of the customer
        :type country: str
        :param account_number: The account number associated to the customer
        :type account_number: str, optional
        :param bvn: The bvn of the customer
        :type bvn: str, optional
        :param bank_code: The bank code associated to the customer
        :type bank_code: str, optional
        :param subaccount: Subaccount code of the account you want to split the transaction.
        :type subaccount: str, optional
        :param split_code: The split code of the account you want to split the transaction
        :type split_code: str, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async create_virtual_account(customer_id_or_code: str, preferred_bank: str | None = None, subaccount: str | None = None, split_code: str | None = None, first_name: str | None = None, last_name: str | None = None, phone: str | None = None)→ PayStackResponse

        Create a dedicated virtual account for existing customers. Currently, support Wema Bank and Titan Paystack.

        :param customer_id_or_code: The customer ID or code
        :type customer_id_or_code: str
        :param preferred_bank: Preferred bank slug for the virtual account.
        :type preferred_bank: str, optional
        :param subaccount: Subaccount code of the account you want to split the transaction.
        :type subaccount: str, optional
        :param split_code: The split code of the account you want to split the transaction
        :type split_code: str, optional
        :param first_name: The first name of the customer
        :type first_name: str, optional
        :param last_name: The last name of the customer
        :type last_name: str, optional
        :param phone: The phone number of the customer
        :type phone: str, optional

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async deactivate_dedicated_account(dedicated_account_id: int)→ PayStackResponse

        Deactivate a dedicated virtual account

        :param dedicated_account_id: The id of the dedicated virtual account
        :type dedicated_account_id: int

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async fetch_bank_providers()→ PayStackResponse

        Fetch bank providers

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async fetch_dedicated_account(dedicated_account_id: int)→ PayStackResponse

        Get details of a dedicated virtual account

        :param dedicated_account_id: The id of the dedicated virtual account
        :type dedicated_account_id: int

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async list_dedicated_account(active: bool | None = True, currency: str | None = None, provider_slug: str | None = None, bank_id: str | None = None, customer_id: str | None = None)→ PayStackResponse

        List dedicated accounts

        :param active: Shows the status of the dedicated virtual account. (default: True)
        :type active: bool, optional
        :param currency: The currency of the dedicated virtual account
        :type currency: str, optional
        :param provider_slug: The preferred bank slug for the dedicated virtual account in lowercase
        :type provider_slug: str, optional
        :param bank_id: The bank code for the dedicated virtual account
        :type bank_id: str, optional
        :param customer_id: The customer code for the dedicated virtual account
        :type customer_id: str, optional

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async remove_split_dedicated_account(account_number: str)→ PayStackResponse

        Remove a split dedicated virtual account

        :param account_number: The account number for the dedicated virtual account
        :type account_number: str

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: async requery_dedicated_account(account_number: str | None = None, provider_slug: str | None = None, date_transfer: date | None = None)→ PayStackResponse

        Requery a dedicated virtual account for new transactions

        :param account_number: Virtual account number to requery
        :type account_number: str, optional
        :param provider_slug: Virtual account preferred bank in lowercase
        :type provider_slug: str, optional
        :param date_transfer: Date of the transaction made
        :type date_transfer: date, optional

        :return: The response from the API
        :rtype: PayStackResponse object


.. _Dedicated Virtual Account: https://paystack.com/docs/api/dedicated-virtual-account/

.. important::

    The ``preferred_bank`` parameter currently support Wema Bank and Titan Paystack.

    The ``country`` parameter currently accepts NG only.
