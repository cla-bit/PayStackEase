=========================
Async Charge Module
=========================


This wrapper class facilitates asynchronous interaction with Paystack Charges API. The Charge API allows you to configure payment
channel of your choice when initiating a payment.

To access the Charges API methods, you need to call the ``charges`` instance method from ``AsyncPayStackBase``.

Check example on :doc:`apaystack`

-------------

.. py:class:: AsyncChargesClientAPI()

    Paystack Charges API Reference: `Charges`_

    .. py:method:: async check_pending_charge(reference: str)→ PayStackResponse

        Check pending charge

        :param reference: The reference to check
        :type reference: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async create_charge(email: str, metadata: CustomMetaData, auth_ref: Optional[BulkChargeObject] = None, bank: Optional[BankDetails] = None, bank_transfer: Optional[Union[ExpiryInfo, Dict[PWT, str]]] = None, virtual_pay: Optional[VirtualPaymentModel] = None, split_code: Optional[str] = None, subaccount: Optional[str] = None, transaction_charge: Optional[int] = None, bearer: Optional[Bearer] = Bearer.ACCOUNT, pin: Optional[int] = None, device_id: str | None = None)→ PayStackResponse

        Create a new charge

        :param email: The email of the customer
        :type email: str
        :param metadata: The metadata of the charge. A JSON object
        :type metadata: CustomMetaData
        :param auth_ref: A BulkChargeObject type containing the amount, authorization and reference to charge.
        :type auth_ref: BulkChargeObject, optional
        :param bank: Bank account to charge
        :type bank: BankDetails, optional
        :param bank_transfer: Takes the settings for the Pay with Transfer (PwT) channel
        :type bank_transfer: ExpiryInfo, Dict[PWT, str], optional
        :param virtual_pay: Virtual payment details for virtual payment methods (qr, ussd, and mobile money)
        :type virtual_pay: VirtualPaymentModel, optional
        :param split_code: The split code of a previously created split.
        :type split_code: str, optional
        :param subaccount: The code for the subaccount that owns the payment
        :type subaccount: str, optional
        :param transaction_charge: An amount used to override the split configuration for a single split payment
        :type transaction_charge: int, optional
        :param bearer: Bearer type for who bears the charge. Default is Bearer.ACCOUNT
        :type bearer: Bearer, optional
        :param pin: The pin of the customer
        :type pin: int, optional
        :param device_id: The device id of the customer
        :type device_id: str, optional

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async submit_address(reference: str, address: str, city: str, state: str, zipcode: str)→ PayStackResponse

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

    .. py:method:: async submit_birthday(birthday: date, reference: str)→ PayStackResponse

        Submit birthday when required

        :param birthday: The birthday of the customer
        :type birthday: date
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async submit_otp(otp: int, reference: str)→ PayStackResponse

        Submit otp to complete a charge

        :param otp: The otp of the customer
        :type otp: int
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async submit_phone(phone: str, reference: str)→ PayStackResponse

        Submit a phone number to complete a charge

        :param phone: The phone of the customer
        :type phone: str
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: PayStackResponse object

    .. py:method:: async submit_pin(pin: int, reference: str)→ PayStackResponse

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
:doc:`atransactions`.
