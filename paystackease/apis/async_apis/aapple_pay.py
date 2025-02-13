"""
Wrapper class for Asynchronous Paystack Apple Pay API.

The Apple Pay API allows you register your application's top-level domain or subdomain.
"""

from paystackease.src import PayStackResponse, AsyncRequestAPI
from paystackease.helpers import (
    apple_pay_endpoint, DomainNameModel, ListDomainNamesModel
)


class AsyncApplePayClientAPI(AsyncRequestAPI):
    """
    Paystack Apple Pay API
    Reference: https://paystack.com/docs/api/apple-pay/
    """

    async def register_domain(self, domain_name: DomainNameModel) -> PayStackResponse:
        """
        Register a domain or subdomain for Apple Pay

        :param: domain_name  # domain name or subdomain

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        validated_data = domain_name.model_dump(by_alias=True)
        return await self._post_request(apple_pay_endpoint, data=validated_data)

    async def list_domains(
            self,
            domain_values: ListDomainNamesModel
    ) -> PayStackResponse:
        """
        List all registered domains

        :param: use_cursor  # use cursor for pagination
        :param: next_page  # next page
        :param: previous_page  # previous page

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        validated_params = domain_values.model_dump(by_alias=True, exclude_none=True)
        return await self._get_request(apple_pay_endpoint, params=validated_params)

    async def unregister_domain(self, domain_name: DomainNameModel) -> PayStackResponse:
        """
        Unregister a domain or subdomain for Apple Pay

        :param: domain_name  # domain name or subdomain

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        validated_data = domain_name.model_dump(by_alias=True)
        return await self._delete_request(apple_pay_endpoint, data=validated_data)
