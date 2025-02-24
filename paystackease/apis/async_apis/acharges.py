"""
Wrapper for Asynchronous Paystack Charges API.

The Charge API allows you to configure payment channel of your choice when initiating a payment.
"""

from datetime import date
from typing import Optional, Union, Dict

from paystackease.src import PayStackResponse, AsyncRequestAPI
from paystackease.helpers import (
    convert_to_string, BulkChargeObject, VirtualPaymentModel,
    CustomMetaData, charges_endpoint, ExpiryInfo, BankDetails, PWT, Bearer
)


class AsyncChargesClientAPI(AsyncRequestAPI):
    """
    Paystack Charges API
    Reference: https://paystack.com/docs/api/charge/
    """

    async def create_charge(
            self,
            email: str,
            metadata: CustomMetaData,
            auth_ref: Optional[BulkChargeObject] = None,
            bank: Optional[BankDetails] = None,
            bank_transfer: Optional[Union[ExpiryInfo, Dict[PWT, str]]] = None,
            virtual_pay: Optional[VirtualPaymentModel] = None,
            split_code: Optional[str] = None,
            subaccount: Optional[str] = None,
            transaction_charge: Optional[int] = None,
            bearer: Optional[Bearer] = Bearer.ACCOUNT,
            pin: Optional[int] = None,
            device_id: Optional[str] = None,
    ) -> PayStackResponse:
        """
        Initiates a new charge on Paystack.

        This function allows you to create a new charge with the provided parameters.
        It validates the input data and sends a POST request to the Paystack Charges API endpoint.

        Parameters:
            email (str): The email address of the customer.
            metadata (CustomMetaData): Custom metadata to be associated with the charge.
            auth_ref (BulkChargeObject, optional): An BulkChargeObject type containing the amount, authorization and reference to charge.
            bank (BankDetails, optional): Bank details to charge. Defaults to None.
            bank_transfer (ExpiryInfo or dict, optional): Takes the settings for the Pay with Transfer (PwT) channel.
            virtual_pay (VirtualPaymentModel, optional): Virtual payment details for virtual payment methods (qr, ussd, and mobile money). Defaults to None.
            split_code (str, optional): The split code of a previously created split.
            subaccount (str, optional): The code for the subaccount that owns the payment
            transaction_charge (int, optional): An amount used to override the split configuration for a single split payment
            bearer (Bearer, optional): Bearer type for who bears the charge.
            pin (int, optional): PIN for 3D Secure authentication. Defaults to None.
            device_id (str, optional): Device ID for 3D Secure authentication. Defaults to None.

        Returns:
            PayStackResponse: The response from the Paystack API.
        """
        data = {
            "email": email,
            "metadata": metadata.model_dump(),
            **auth_ref.model_dump(by_alias=True, exclude_none=True),
            "bank": bank if bank else None,
            "bank_transfer": bank_transfer if bank_transfer else None,
            **(virtual_pay.model_dump(exclude_none=True) if virtual_pay else {}),
            "split_code": split_code,
            "subaccount": subaccount,
            "transaction_charge": transaction_charge,
            "bearer": bearer,
            "pin": pin,
            "device_id": device_id,
        }
        return await self._post_request(charges_endpoint, data=data)

    async def submit_pin(self, pin: int, reference: str) -> PayStackResponse:
        """
        Submit a PIN for a charge

        Parameters:
            pin (int): The PIN submitted by user.
            reference (str): Reference for transaction that requested pin

        Returns:
            The PayStackResponse object from the API
        """
        data = {
            "pin": pin,
            "reference": reference,
        }
        return await self._post_request(f"{charges_endpoint}submit_pin", data=data)

    async def submit_otp(self, otp: int, reference: str) -> PayStackResponse:
        """
        Submit OTP to complete a charge

        Parameters:
            otp (int): OTP to submitted by user
            reference (str): Reference for ongoing transaction.

        Returns:
            The PayStackResponse object from the API
        """
        data = {
            "otp": otp,
            "reference": reference,
        }
        return await self._post_request(f"{charges_endpoint}submit_otp", data=data)

    async def submit_phone(self, phone: str, reference: str) -> PayStackResponse:
        """
        Submit a phone number to complete a charge

        Parameters:
            phone (str): Phone number submitted by user
            reference (str): Reference for ongoing transaction.

        Returns:
            The PayStackResponse object from the API
        """
        data = {
            "phone": phone,
            "reference": reference,
        }
        return await self._post_request(f"{charges_endpoint}submit_phone", data=data)

    async def submit_birthday(self, birthday: date, reference: str) -> PayStackResponse:
        """
        Submit birthday when required

        Parameters:
            birthday (date): Date of birth submitted by user
            reference (str): Reference for ongoing transaction.

        Returns:
            The PayStackResponse object from the API
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

        Parameters:
            reference (str): Reference for ongoing transaction.
            address (str): Address submitted by user.
            city (str): City submitted by user.
            state (str): State submitted by user.
            zipcode (str): Zipcode submitted by user.

        Returns:
            The PayStackResponse object from the API
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

        Parameters:
            reference (str): Reference to check.

        Returns:
            The PayStackResponse object from the API
        """
        return await self._get_request(f"{charges_endpoint}{reference}")
