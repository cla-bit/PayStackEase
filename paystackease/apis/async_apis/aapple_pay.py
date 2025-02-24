"""
Wrapper class for Asynchronous Paystack Apple Pay API.

The Apple Pay API allows you register your application's top-level domain or subdomain.
"""
from typing import Optional

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

        Parameters:
            domain_name (DomainNameModel):  domain name or subdomain which is a DomainNameModel type.

        Returns:
            PayStackResponse: The PayStackResponse object from the API
        """

        data = domain_name.model_dump(by_alias=True)
        return await self._post_request(apple_pay_endpoint, data=data)

    async def list_domains(
            self,
            list_domains: Optional[ListDomainNamesModel] = None
    ) -> PayStackResponse:
        """
        List all registered domains

        Parameters:
            list_domains (Optional[ListDomainNamesModel]): This is a model with attributes use_cursor, next_page and previous_page

        Returns:
            PayStackResponse: The PayStackResponse object from the API
        """

        params = (list_domains.model_dump(by_alias=True, exclude_none=True) if list_domains else {})
        return await self._get_request(apple_pay_endpoint, params=params)

    async def unregister_domain(self, domain_name: DomainNameModel) -> PayStackResponse:
        """
        Unregister a domain or subdomain for Apple Pay

        Parameters:
            domain_name (DomainNameModel):  domain name or subdomain which is a DomainNameModel type.

        Returns:
            PayStackResponse: The PayStackResponse object from the API
        """

        data = domain_name.model_dump(by_alias=True)
        return await self._delete_request(apple_pay_endpoint, data=data)
