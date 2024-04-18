"""
Wrapper class for Paystack Apple Pay API.

The Apple Pay API allows you register your application's top-level domain or subdomain.
"""

from typing import Optional, Union
from paystackease.core import PayStackResponse, SyncRequestAPI


class ApplePayClientAPI(SyncRequestAPI):
    """
    Paystack Apple Pay API
    Reference: https://paystack.com/docs/api/apple-pay/
    """

    def register_domain(self, domain_name: str) -> PayStackResponse:
        """
        Register a domain or subdomain for Apple Pay

        :param: domain_name  # domain name or subdomain

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "domainName": domain_name,
        }
        return self._post_request("/apple-pay/domain", data=data)

    def list_domains(
            self,
            use_cursor: Optional[Union[bool, None]] = False,
            next_page: Optional[Union[int, None]] = None,
            previous_page: Optional[Union[int, None]] = None,
    ) -> PayStackResponse:
        """
        List all registered domains

        :param: use_cursor  # use cursor for pagination
        :param: next_page  # next page
        :param: previous_page  # previous page

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        # convert bool to string
        use_cursor = self._convert_to_string(use_cursor)

        params = {
            "use_cursor": use_cursor,
            "next": next_page,
            "previous": previous_page,
        }
        return self._get_request("/apple-pay/domain", params=params)

    def unregister_domain(self, domain_name: str) -> PayStackResponse:
        """
        Unregister a domain or subdomain for Apple Pay

        :param: domain_name  # domain name or subdomain

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "domainName": domain_name,
        }
        return self._delete_request("/apple-pay/domain", data=data)
