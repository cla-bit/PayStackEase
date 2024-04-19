===========================================
Async Verification Module
===========================================

This wrapper class facilitates asynchronous integration with Paystack Verification APIs The Verification API allows you to perform KYC processes.

------------------

.. py:class:: AsyncVerificationClientAPI(secret_key: str = None)

    Paystack Verification API Reference: `Verification`_

    .. py:method:: async resolve_account(account_number: str, bank_code: str)→ PayStackResponse

        Confirm an account belongs to the right customer. This feature is available to business in Nigeria and Ghana.

        :param account_number: The account number to be confirmed
        :type account_number: str
        :param bank_code: The bank code to be confirmed
        :type bank_code: str

        :return: The response from the API
        :rtype: PayStackResponse object


    .. py:method:: async resolve_card_bin(bin_code: str)→ PayStackResponse

        Resolve a card BIN

        :param bin_code: The card bin to be resolved
        :type bin_code: str

        :return: The response from the API
        :rtype: PayStackResponse object


    .. py:method:: async validate_account(account_name: str, account_number: str, account_type: str, bank_code: str, country_code: str, document_type: str, document_number: str)→ PayStackResponse

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
        :rtype: PayStackResponse object

.. _Verification: https://paystack.com/docs/api/verification/
