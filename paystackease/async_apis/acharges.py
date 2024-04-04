"""
Wrapper for Asynchronous Paystack Charges API.

The Charge API allows you to configure payment channel of your choice when initiating a payment.
"""
from aiohttp import ClientResponse

from datetime import date
from typing import Optional, Dict, Any, List
from paystackease._abase import AsyncPayStackBaseClientAPI
from paystackease.helpers.tool_kit import PWT


class AsyncChargesClientAPI(AsyncPayStackBaseClientAPI):
    """
    Paystack Charges API
    Reference: https://paystack.com/docs/api/charge/
    """

    async def create_charge(
        self,
            email: str,
            amount: int,
            pin: Optional[int] = None,
            authorization_code: Optional[str] = None,
            reference: Optional[str] = None,
            device_id: Optional[str] = None,
            bank: Optional[Dict[str, str]] = None,
            bank_transfer: Optional[Dict[PWT, Any]] = None,
            qr: Optional[Dict[str, str]] = None,
            ussd: Optional[Dict[str, str]] = None,
            mobile_money: Optional[Dict[str, str]] = None,
            metadata: Optional[Dict[str, List[Dict[str, Any]]]] = None,
    ) -> ClientResponse:
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

        :return: The response from the API
        :rtype: ClientResponse object
        """
        data = {
            "email": email,
            "amount": amount,
            "authorization_code": authorization_code,
            "bank": bank,
            "bank_transfer": bank_transfer,
            "qr": qr,
            "pin": pin,
            "reference": reference,
            "ussd": ussd,
            "mobile_money": mobile_money,
            "device_id": device_id,
            "metadata": metadata,
        }
        return await self._post_request("/charge", data=data)

    async def submit_pin(self, pin: int, reference: str) -> ClientResponse:
        """
        Submit a PIN for a charge

        :param: pin
        :param: reference

        :return: The response from the API
        :rtype: ClientResponse object
        """
        data = {
            "pin": pin,
            "reference": reference,
        }
        return await self._post_request("/charge/submit_pin", data=data)

    async def submit_otp(self, otp: int, reference: str) -> ClientResponse:
        """
        Submit OTP to complete a charge

        :param: otp
        :param: reference

        :return: The response from the API
        :rtype: ClientResponse object
        """
        data = {
            "otp": otp,
            "reference": reference,
        }
        return await self._post_request("/charge/submit_otp", data=data)

    async def submit_phone(self, phone: str, reference: str) -> ClientResponse:
        """
        Submit a phone number to complete a charge

        :param: phone
        :param: reference

        :return: The response from the API
        :rtype: ClientResponse object
        """
        data = {
            "phone": phone,
            "reference": reference,
        }
        return await self._post_request("/charge/submit_phone", data=data)

    async def submit_birthday(self, birthday: date, reference: str) -> ClientResponse:
        """
        Submit birthday when required

        :param: birthday
        :param: reference

        note::

            Birthday submitted by user e.g. 2016-09-21

        :return: The response from the API
        :rtype: ClientResponse object
        """
        birthday = self._convert_to_string(birthday)

        data = {
            "birthday": birthday,
            "reference": reference,
        }
        return await self._post_request("/charge/submit_birthday", data=data)

    async def submit_address(
        self, reference: str, address: str, city: str, state: str, zipcode: str
    ) -> ClientResponse:
        """
        Submit address to continue a charge

        :param: reference
        :param: address
        :param: city
        :param: state
        :param: zipcode

        :return: The response from the API
        :rtype: ClientResponse object
        """
        data = {
            "reference": reference,
            "address": address,
            "city": city,
            "state": state,
            "zip_code": zipcode,
        }
        return await self._post_request("/charge/submit_address", data=data)

    async def check_pending_charge(self, reference: str) -> ClientResponse:
        """
        Check pending charge

        :param: reference

        :return: The response from the API
        :rtype: ClientResponse object
        """
        return await self._get_request(f"/charge/{reference}")
