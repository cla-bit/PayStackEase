"""
Wrapper class for Asynchronous Paystack Apple Pay API.

The Apple Pay API allows you register your application's top-level domain or subdomain.
"""

from typing import Optional
from paystackease._abase import AsyncPayStackBaseClientAPI


class AsyncApplePayClientAPI(AsyncPayStackBaseClientAPI):
    """
    Paystack Apple Pay API
    Reference: https://paystack.com/docs/api/apple-pay/
    """

    async def register_domain(self, domain_name: str) -> dict:
        """
        Register a domain or subdomain for Apple Pay

        :param: domain_name  # domain name or subdomain

        :return: The response from the API
        :rtype: dict
        """
        data = {
            "domainName": domain_name,
        }
        return await self._post_request("/apple-pay/domain", data=data)

    async def list_domains(
        self,
            use_cursor: Optional[bool] = False,
            next_page: Optional[int] = None,
            previous_page: Optional[int] = None,
    ) -> dict:
        """
        List all registered domains

        :param: use_cursor  # use cursor for pagination
        :param: next_page  # next page
        :param: previous_page  # previous page

        :return: The response from the API
        :rtype: dict
        """

        # convert bool to string
        use_cursor = self._convert_to_string(use_cursor)

        params = {
            "use_cursor": use_cursor,
            "next": next_page,
            "previous": previous_page,
        }
        return await self._get_request("/apple-pay/domain", params=params)

    async def unregister_domain(self, domain_name: str) -> dict:
        """
        Unregister a domain or subdomain for Apple Pay

        :param: domain_name  # domain name or subdomain

        :return: The response from the API
        :rtype: dict
        """
        data = {
            "domainName": domain_name,
        }
        return await self._delete_request("/apple-pay/domain", data=data)
