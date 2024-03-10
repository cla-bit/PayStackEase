"""
Wrapper for Paystack Miscellaneous API.

The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs.
"""

from typing import Optional
from paystackease.async_apis.abase import AsyncPayStackBaseClientAPI


class AsyncMiscellaneousClientAPI(AsyncPayStackBaseClientAPI):
    """
    Paystack Miscellaneous API
    Reference: https://paystack.com/docs/api/miscellaneous/
    """

    async def list_banks(
            self,
            country: Optional[str] = None,
            use_cursor: Optional[bool] = False,
            per_page: Optional[int] = None,
            pay_with_bank_transfer: Optional[bool] = None,
            pay_with_bank: Optional[bool] = None,
            enabled_for_verification: Optional[bool] = None,
            next_cursor: Optional[str] = None,
            previous_cursor: Optional[str] = None,
            gateway: Optional[str] = None,
            channel_type: Optional[str] = None,
            currency: Optional[str] = None,
    ) -> dict:
        """
        Get a list of all supported banks and their properties

        :param: country: The country to obtain the list of supported banks:
        Values { country=ghana or country=nigeria }
        :param: use_cursor: Use cursor to paginate through the list of supported banks
        :param: per_page: The number of records to return per page: 10, 20 or 50
        :param: pay_with_bank_transfer: filter for available banks a customer can make a
         transfer to complete a payment
        :param: pay_with_bank: filter for banks a customer can pay directly from
        :param: enabled_for_verification: filter the banks that are supported for account
        verification in South Africa. Combine with currency or country filter
        :param: next_cursor: The cursor for the next page of results
        :param: previous_cursor: The cursor for the previous page of results
        :param: gateway: filters for banks that support a specific payment gateway:
        { emandate or digitalbankmandate }
        :param: currency: filter for banks that support a specific currency
        :param: channel_type: Type of financial channel. { Channels.value.value}

        note::

            For Ghanaian channels, please use either mobile_money for mobile money channels OR ghipps for bank channels

        :return: The response from the API
        :rtype: dict
        """
        params = {
            "country": country,
            "use_cursor": use_cursor,
            "perPage": per_page,
            "supports_transfer": pay_with_bank_transfer,
            "pay_with_bank": pay_with_bank,
            "enabled_for_verification": enabled_for_verification,
            "next": next_cursor,
            "previous": previous_cursor,
            "gateway": gateway,
            "type": channel_type,
            "currency": currency,
        }
        return await self._get_request("/bank", params=params)

    async def list_countries(self) -> dict:
        """
        Get a list of all supported countries and their properties

        :return: The response from the API
        :rtype: dict
        """
        return await self._get_request("/country")

    async def list_states(self, country: str) -> dict:
        """
        Get a list of all supported states and their properties

        :param: country: The country code from which to obtain the list of supported states

        :return: The response from the API
        :rtype: dict
        """
        params = {"country": country}
        return await self._get_request("/address_verification/states", params=params)
