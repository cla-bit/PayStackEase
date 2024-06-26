===========================================
Charge Module
===========================================


This wrapper class facilitates synchronous interaction with Paystack Charges API. The Charge API allows you to configure payment channel of your
choice when initiating a payment.

To access the Charges API methods, you need to call the ``charges`` instance method from ``PayStackBase``.

Check example on :doc:`paystack`

-----------

.. py:class:: ChargesClientAPI(secret_key: str = None)

    Paystack Charges API Reference: `Charges`_

    .. py:method:: check_pending_charge(reference: str)→ PayStackResponse

        Check pending charge

        :param reference: The reference to check
        :type reference: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: create_charge(email: str, amount: int, metadata: Dict[str, List[Dict[str, str]]], pin: int | None = None, authorization_code: str | None = None, reference: str | None = None, device_id: str | None = None, bank: Dict[str, str] | None = None, bank_transfer: Dict[str, Any] | None = None, qr: Dict[str, str] | None = None, ussd: Dict[str, str] | None = None, mobile_money: Dict[str, str] | None = None)→ PayStackResponse

        Create a new charge

        :param email: The email of the customer
        :type email: str
        :param amount: The amount to charge
        :type amount: int
        :param metadata: The metadata of the charge. A JSON object
        :type metadata: dict
        :param pin: The pin of the customer
        :type pin: int, optional
        :param authorization_code: The authorization code of the customer
        :type authorization_code: str, optional
        :param reference: The reference of the charge
        :type reference: str, optional
        :param device_id: The device id of the customer
        :type device_id: str, optional
        :param bank: Bank account to charge
        :type bank: dict, optional
        :param bank_transfer: Takes the settings for the Pay with Transfer (PwT) channel
        :type bank_transfer: dict, optional
        :param qr: QR type to charge
        :type qr: dict, optional
        :param ussd: USSD type to charge
        :type ussd: dict, optional
        :param mobile_money: The mobile money details
        :type mobile_money: dict, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: submit_address(reference: str, address: str, city: str, state: str, zipcode: str)→ PayStackResponse

        Submit address to continue a charge

        :param reference: The reference of the charge
        :type reference: str
        :param address: The address of the customer
        :type address: str
        :param city: The city of the customer
        :type city: str
        :param state: The state of the customer
        :type state: str
        :param zipcode: The zipcode of the customer
        :type zipcode: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: submit_birthday(birthday: date, reference: str)→ PayStackResponse

        Submit birthday when required

        :param birthday: The birthday of the customer
        :type birthday: date
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: submit_otp(otp: int, reference: str)→ PayStackResponse

        Submit otp to complete a charge

        :param otp: The otp of the customer
        :type otp: int
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: submit_phone(phone: str, reference: str)→ PayStackResponse

        Submit a phone number to complete a charge

        :param phone: The phone of the customer
        :type phone: str
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: submit_pin(pin: int, reference: str)→ PayStackResponse

        Submit a PIN for a charge

        :param pin: The pin of the customer
        :type pin: int
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: PayStackResponse object


.. _Charges: https://paystack.com/docs/api/charge/

The ``bank`` parameter is a dictionary with the following set as keys: ``code`` and ``account_number``.
This feature is only available in **Nigeria**.

**See example**:

.. code-block:: python

    >>> "bank": {
    >>>     "code": "057",
    >>>     "account_number": "1234567890"
    >>> }

The ``bank_transfer`` parameter is a dictionary with the PWT enum string value set as key: ``PWT.ACCOUNT_EXPIRES_AT.value``.
This feature is only available in **Nigeria** and contact support@paystack.com to enable it on their integration.

**See example**:

.. code-block:: python

    >>> "bank_transfer": {
    >>>     "account_expires_at": "2023-09-12T13:10:00Z"
    >>> }

The ``qr`` parameter is a dictionary with key set to: ``provider``.
This feature is only available in **South Africa** and **Nigeria**.

**See example**:

.. code-block:: python

    >>> "qr": {
    >>>     "provider": "visa"  # Nigeria provider. For South Africa provider use "scan-to-pay"
    >>> }

.. note::

    The scan-to-pay provider supports both SnapScan and Scan to Pay (formerly Masterpass) supported apps for completing a payment.

The ``ussd`` parameter is a dictionary with key set to: ``type``.
This feature is only available in **Nigeria**.

**See example**:

.. code-block:: python

    >>> "ussd": {
    >>>     "type": "737"
    >>> }

The ``mobile_money`` parameter is a dictionary with the following set as keys: ``phone`` and ``provider``.
This feature is only available in **Ghana** and *Kenya**.

**See example**:

.. code-block:: python

    >>> "mobile_money": {
    >>>     "phone": "0551234987",
    >>>     "provider": "mtn"
    >>> }

Refer to this documentation for more information: :doc:`toolkit`.

The ``metadata`` parameter is a JSON object that uses the ``custom_fields`` type of metadata.
See :doc:`metadata` for more information.


To ensure a successful API request to Paystack for creating a charge, follow these essential rules:

A. Do not send or use the following if charging an authorization code:
    * `bank`
    * `ussd`
    * `mobile_money`

B. Do not send or use the following if charging an authorization code, bank or card:
    * `ussd`
    * `mobile_money`

C. Send with a non-reusable authorization code:
    * `pin`

Kindly note that authorization_code is gotten after a successful card transaction. Refer here to read more
:doc:`transactions`.
