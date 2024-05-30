"""
Wrapper for Paystack Miscellaneous API.

The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs.
"""

from typing import Optional, Union

from paystackease.core import PayStackResponse, SyncRequestAPI
from paystackease.helpers import GateWay, Channels, Currency


class MiscellaneousClientAPI(SyncRequestAPI):
    """
    Paystack Miscellaneous API
    Reference: https://paystack.com/docs/api/miscellaneous/
    """

    def list_banks(
            self,
            country: Optional[Union[str, None]] = None,
            use_cursor: Optional[Union[bool, None]] = False,
            per_page: Optional[Union[int, None]] = 50,
            pay_with_bank_transfer: Optional[Union[bool, None]] = False,
            pay_with_bank: Optional[Union[bool, None]] = False,
            enabled_for_verification: Optional[Union[bool, None]] = False,
            next_cursor: Optional[Union[str, None]] = None,
            previous_cursor: Optional[Union[str, None]] = None,
            gateway: Optional[Union[GateWay, None]] = None,
            channel_type: Optional[Union[Channels, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
    ) -> PayStackResponse:
        """
        Get a list of all supported banks and their properties

        :param: country: The country to obtain the list of supported banks.
                        Values { country=ghana or country=nigeria }
        :param: use_cursor: Use cursor to paginate through the list of supported banks
        :param: per_page: The number of records to return per page: 10, 20 or 50
        :param: pay_with_bank_transfer: filter for available banks a customer can make a transfer to complete a payment
        :param: pay_with_bank: filter for banks a customer can pay directly from
        :param: enabled_for_verification: filter the banks that are supported for account
                                            verification in South Africa. Combine with currency or country filter
        :param: next_cursor: The cursor for the next page of results
        :param: previous_cursor: The cursor for the previous page of results
        :param: gateway: filters for banks that support a specific payment gateway:
                        { emandate or digitalbankmandate }
        :param: currency: filter for banks that support a specific currency
        :param: channel_type: Type of financial channel. { Channels.value.value}

        **note::**

        For Ghanaian channels, please use either mobile_money for mobile money channels OR ghipps for bank channels

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        # convert to strings
        use_cursor = self._convert_to_string(use_cursor)
        pay_with_bank_transfer = self._convert_to_string(pay_with_bank_transfer)
        pay_with_bank = self._convert_to_string(pay_with_bank)
        enabled_for_verification = self._convert_to_string(enabled_for_verification)

        params = {
            "country": country,
            "use_cursor": use_cursor,
            "perPage": per_page,
            "pay_with_bank_transfer": pay_with_bank_transfer,
            "pay_with_bank": pay_with_bank,
            "enabled_for_verification": enabled_for_verification,
            "next": next_cursor,
            "previous": previous_cursor,
            "gateway": gateway,
            "type": channel_type,
            "currency": currency,
        }
        return self._get_request("/bank", params=params)

    def list_countries(self) -> PayStackResponse:
        """
        Get a list of all supported countries and their properties

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request("/country")

    def list_states(self, country: str) -> PayStackResponse:
        """
        Get a list of all supported states and their properties

        :param: country: The country code from which to obtain the list of supported states

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        params = {"country": country}
        return self._get_request("/address_verification/states", params=params)
