===========================================
Async Verification Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.averification


Wrapper for Asynchronous Paystack Verification APIs The Verification API allows you to perform KYC processes.

-----------------------------------------------------

.. py:class:: AsyncVerificationClientAPI(secret_key: str = None)[source]

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Verification API Reference: `Verification`_

    .. py:method:: async resolve_account(account_number: str, bank_code: str)→ dict

        Confirm an account belongs to the right customer. This feature is available to business in Nigeria and Ghana.

        :param account_number: The account number to be confirmed
        :type account_number: str
        :param bank_code: The bank code to be confirmed
        :type bank_code: str

        :return: The response from the API
        :rtype: dict


    .. py:method:: async resolve_card_bin(bin_code: str)→ dict

        Resolve a card BIN

        :param bin_code: The card bin to be resolved
        :type bin_code: str

        :return: The response from the API
        :rtype: dict


    .. py:method:: async validate_account(account_name: str, account_number: str, account_type: str, bank_code: str, country_code: str, document_type: str, document_number: str)→ dict

        Confirm the authenticity of a customer’s account number before sending money. This feature is only available to businesses in South Africa.

        :param account_name: The account name to be confirmed
        :type account_name: str
        :param account_number: The account number to be confirmed
        :type account_number: str
        :param account_type: The account type to be confirmed
        :type account_type: str
        :param bank_code: The bank code to be confirmed
        :type bank_code: str
        :param country_code: The country code to be confirmed
        :type country_code: str
        :param document_type: The document type to be confirmed
        :type document_type: str
        :param document_number: The document number to be confirmed
        :type document_number: str

        :return: The response from the API
        :rtype: dict

.. _Verification: https://paystack.com/docs/api/verification/
