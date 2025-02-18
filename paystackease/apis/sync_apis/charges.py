"""
Wrapper for Paystack Charges API.

The Charge API allows you to configure payment channel of your choice when initiating a payment.
"""

from datetime import date
from typing import Optional, Union

from paystackease.src import PayStackResponse, SyncRequestAPI
from paystackease.helpers import convert_to_string, AuthReferenceObject, ChargeBankModel, VirtualPaymentModel, CustomMetaData, charges_endpoint


class ChargesClientAPI(SyncRequestAPI):
    """
    Paystack Charges API
    Reference: https://paystack.com/docs/api/charge/
    """

    def create_charge(
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
        Initiates a new charge on Paystack.

        This function allows you to create a new charge with the provided parameters.
        It validates the input data and sends a POST request to the Paystack Charges API endpoint.

        Parameters:
        - email (str): The email address of the customer.
        - metadata (CustomMetaData): Custom metadata to be associated with the charge.
        - auth_ref (AuthReferenceObject): Authentication reference object containing the payment method and other details.
        - bank_charge (ChargeBankModel, optional): Bank charge details for bank-based payment methods. Defaults to None.
        - virtual_pay (VirtualPaymentModel, optional): Virtual payment details for virtual payment methods. Defaults to None.
        - pin (int, optional): PIN for 3D Secure authentication. Defaults to None.
        - device_id (str, optional): Device ID for 3D Secure authentication. Defaults to None.

        Returns:
        - PayStackResponse: The response from the Paystack API.
        """
        validated_data = {
            "email": email,
            "metadata": metadata.model_dump(),
            **auth_ref.model_dump(exclude_none=True),
            **(bank_charge.model_dump(exclude_none=True) if bank_charge else {}),
            **(virtual_pay.model_dump(exclude_none=True) if virtual_pay else {}),
            "pin": pin,
            "device_id": device_id,
        }
        return self._post_request(charges_endpoint, data=validated_data)

    def submit_pin(self, pin: int, reference: str) -> PayStackResponse:
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
        return self._post_request(f"{charges_endpoint}submit_pin", data=data)

    def submit_otp(self, otp: int, reference: str) -> PayStackResponse:
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
        return self._post_request(f"{charges_endpoint}submit_otp", data=data)

    def submit_phone(self, phone: str, reference: str) -> PayStackResponse:
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
        return self._post_request(f"{charges_endpoint}submit_phone", data=data)

    def submit_birthday(self, birthday: date, reference: str) -> PayStackResponse:
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
        return self._post_request(f"{charges_endpoint}submit_birthday", data=data)

    def submit_address(
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
        return self._post_request(f"{charges_endpoint}submit_address", data=data)

    def check_pending_charge(self, reference: str) -> PayStackResponse:
        """
        Check pending charge

        :param: reference

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"{charges_endpoint}{reference}")
