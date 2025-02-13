"""
Wrapper for Asynchronous Paystack Charges API.

The Charge API allows you to configure payment channel of your choice when initiating a payment.
"""

from datetime import date
from typing import Optional, Union

from paystackease.src import PayStackResponse, AsyncRequestAPI
from paystackease.helpers import convert_to_string, AuthReferenceObject, ChargeBankModel, VirtualPaymentModel, CustomMetaData, charges_endpoint


class AsyncChargesClientAPI(AsyncRequestAPI):
    """
    Paystack Charges API
    Reference: https://paystack.com/docs/api/charge/
    """

    async def create_charge(
            self,
            email: str,
            metadata: CustomMetaData,
            auth_ref: AuthReferenceObject,
            bank_charge: Optional[ChargeBankModel] = None,
            virtual_pay: Optional[VirtualPaymentModel] = None,
            pin: Optional[Union[int, None]] = None,
            device_id: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
        """
        Create a charge

        :param: email
        :param: amount
        :param: bank. (Set key ass: {code, account_number})
        :param: bank_transfer. (Set key as: {account_expires_at} and value: {datetime iso format})
        :param: qr (Set key as: {provider})
        :param: authorization_code
        :param: pin
        :param: reference
        :param: ussd (Set key as: {type})
        :param: mobile_money (Set Keys as: {phone, provider}, and value {phone_number, MobileMoney.value.value})
        :param: device_id
        :param: metadata A JSON object, which is passed as-is to your integration API

        note::

            Do not send or use the following if charging an authorization code:
            * bank
            * ussd
            * mobile_money

            Do not send or use the following if charging an authorization code, bank or card:
            * ussd
            * mobile_money

            Send with a non-reusable authorization code:
            * pin

            mobile_money is only available in Ghana and Kenya

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        validated_data = {
            "email": email,
            "metadata": metadata.model_dump(),
            **auth_ref.model_dump(exclude_none=True),
            **bank_charge.model_dump(exclude_none=True),
            **virtual_pay.model_dump(exclude_none=True),
            "pin": pin,
            "device_id": device_id,
        }
        return await self._post_request(charges_endpoint, data=validated_data)

    async def submit_pin(self, pin: int, reference: str) -> PayStackResponse:
        """
        Submit a PIN for a charge

        :param: pin
        :param: reference

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "pin": pin,
            "reference": reference,
        }
        return await self._post_request(f"{charges_endpoint}submit_pin", data=data)

    async def submit_otp(self, otp: int, reference: str) -> PayStackResponse:
        """
        Submit OTP to complete a charge

        :param: otp
        :param: reference

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "otp": otp,
            "reference": reference,
        }
        return await self._post_request(f"{charges_endpoint}submit_otp", data=data)

    async def submit_phone(self, phone: str, reference: str) -> PayStackResponse:
        """
        Submit a phone number to complete a charge

        :param: phone
        :param: reference

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "phone": phone,
            "reference": reference,
        }
        return await self._post_request(f"{charges_endpoint}submit_phone", data=data)

    async def submit_birthday(self, birthday: date, reference: str) -> PayStackResponse:
        """
        Submit birthday when required

        :param: birthday
        :param: reference

        note::

            Birthday submitted by user e.g. 2016-09-21

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        birthday = convert_to_string(birthday)

        data = {
            "birthday": birthday,
            "reference": reference,
        }
        return await self._post_request(f"{charges_endpoint}submit_birthday", data=data)

    async def submit_address(
            self, reference: str, address: str, city: str, state: str, zipcode: str
    ) -> PayStackResponse:
        """
        Submit address to continue a charge

        :param: reference
        :param: address
        :param: city
        :param: state
        :param: zipcode

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "reference": reference,
            "address": address,
            "city": city,
            "state": state,
            "zip_code": zipcode,
        }
        return await self._post_request(f"{charges_endpoint}submit_address", data=data)

    async def check_pending_charge(self, reference: str) -> PayStackResponse:
        """
        Check pending charge

        :param: reference

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"{charges_endpoint}{reference}")
