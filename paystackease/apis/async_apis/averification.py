"""
Wrapper for Asynchronous Paystack Verification APIs

The Verification API allows you to perform KYC processes.
"""

from paystackease.core import AsyncRequestAPI, PayStackResponse


class AsyncVerificationClientAPI(AsyncRequestAPI):
    """
    Paystack Verification API
    Reference: https://paystack.com/docs/api/verification/
    """

    async def resolve_account(self, account_number: str, bank_code: str) -> PayStackResponse:
        """
        Confirm an account belongs to the right customer.
        This feature is available to business in Nigeria and Ghana.

        :param: account_number: The account number to verify
        :param: bank_code: The bank code to verify

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        params = {"account_number": account_number, "bank_code": bank_code}
        return await self._get_request("/bank/resolve", params=params)

    async def validate_account(
            self,
            account_name: str,
            account_number: str,
            account_type: str,
            bank_code: str,
            country_code: str,
            document_type: str,
            document_number: str,
    ) -> PayStackResponse:
        """
        Confirm the authenticity of a customer's account number before sending money.
        This feature is only available to businesses in South Africa.

        :param: account_name: The account name to validate: first and last name
        :param: account_number: The account number to validate
        :param: account_type: The account type to validate: personal or business
        :param: bank_code: The bank code to validate
        :param: country_code: The country code to validate
        :param: document_type: The customer's mode of identity:
                                identityNumber, passportNumber or businessRegistrationNumber
        :param: document_number: The customer's document number

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "account_name": account_name,
            "account_number": account_number,
            "account_type": account_type,
            "bank_code": bank_code,
            "country_code": country_code,
            "document_type": document_type,
            "document_number": document_number,
        }
        return await self._post_request("/bank/validate", data=data)

    async def resolve_card_bin(self, bin_code: str) -> PayStackResponse:
        """
        Resolve a card BIN

        :param: bin_code: First 6 characters of card

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"/decision/bin/{bin_code}")
