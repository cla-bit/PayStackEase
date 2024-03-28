===========================================
Charge Module
===========================================

.. :py:currentmodule:: paystackease.apis.charges

Wrapper for Paystack Charges API. The Charge API allows you to configure payment channel of your
choice when initiating a payment.

To access the Charges API methods, you need to call the ``charges`` instance method from ``PayStackBase``.

Check example on :doc:`paystack`

------------------------------------------------------------------------------------

.. important::
    Mobile Money is only available in Ghana and Kenya


.. py:class:: ChargesClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Charges API Reference: `Charges`_

    .. py:method:: check_pending_charge(reference: str)→ dict

        Check pending charge

        :param reference: The reference to check
        :type reference: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: create_charge(email: str, amount: int, pin: int | None = None, authorization_code: str | None = None, reference: str | None = None, device_id: str | None = None, bank: Dict[str, str] | None = None, bank_transfer: Dict[str, Any] | None = None, qr: Dict[str, str] | None = None, ussd: Dict[str, str] | None = None, mobile_money: Dict[str, str] | None = None, metadata: Dict[str, str] | None = None)→ dict

        Create a new charge

        :param email: The email of the customer
        :type email: str
        :param amount: The amount to charge
        :type amount: int
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
        :param metadata: The metadata of the charge. A JSON object
        :type metadata: dict, optional

        :return: The response from the API.
        :rtype: dict

    .. py:method:: submit_address(reference: str, address: str, city: str, state: str, zipcode: str)→ dict

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
        :rtype: dict

    .. py:method:: submit_birthday(birthday: date, reference: str)→ dict

        Submit birthday when required

        :param birthday: The birthday of the customer
        :type birthday: date
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: submit_otp(otp: int, reference: str)→ dict

        Submit otp to complete a charge

        :param otp: The otp of the customer
        :type otp: int
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: submit_phone(phone: str, reference: str)→ dict

        Submit a phone number to complete a charge

        :param phone: The phone of the customer
        :type phone: str
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: dict

    .. py:method:: submit_pin(pin: int, reference: str)→ dict

        Submit a PIN for a charge

        :param pin: The pin of the customer
        :type pin: int
        :param reference: The reference of the charge
        :type reference: str

        :return: The response from the API.
        :rtype: dict


.. _Charges: https://paystack.com/docs/api/charge/

In creating a charge, there are rules guiding this as well to ensure a successful API request to PayStack,
of which they are as follows:

A. Do not send or use the following if charging an authorization code:
    * `bank`
    * `ussd`
    * `mobile_money`

B. Do not send or use the following if charging an authorization code, bank or card:
    * `ussd`
    * `mobile_money`

C. Send with a non-reusable authorization code:
    * `pin`

Kindly note that authorization_code are gotten after a successful card transaction. Check here to read more
:doc:`transactions`.
