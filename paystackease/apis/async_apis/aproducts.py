"""
Wrapper for Asynchronous Paystack Products API

The Products API allows you to create and manage inventories on your integration.
"""

from typing import Optional, Union

from paystackease.helpers import product_endpoint, PageModel, DatePageModel
from paystackease.src import AsyncRequestAPI, PayStackResponse


class AsyncProductClientAPI(AsyncRequestAPI):
    """
    Paystack Product API
    Reference: https://paystack.com/docs/api/product/
    """

    async def create_product(
            self,
            name: str,
            description: str,
            amount: int,
            currency: str,
            unlimited: Optional[Union[bool, None]] = True,
            quantity: Optional[Union[int, None]] = None,
    ) -> PayStackResponse:
        """
        Create a product

        :param: name: Name of the product
        :param: description: Description of the product
        :param: amount: Price of the product
        :param: currency: Currency of the product
        :param: unlimited: Set true if the product has unlimited stock,
        :param: quantity: Quantity of the product in stock Use if unlimited is false

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        data = {
            "name": name,
            "description": description,
            "price": amount,
            "currency": currency,
            "unlimited": unlimited,
            "quantity": quantity,
        }
        return await self._post_request(product_endpoint, data=data)

    async def list_products(
            self,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
    ) -> PayStackResponse:
        """
        List all the products

        :param: per_page: Number of records to return
        :param: page:  number to return
        :param: from_date: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param: to_date: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        params = {
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
        }
        return await self._get_request(product_endpoint, params=params)

    async def fetch_product(self, product_id: str) -> PayStackResponse:
        """
        Get details of a product

        :param: product_id: ID or Code of the product

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"{product_endpoint}{product_id}")

    async def update_product(
            self,
            product_id: str,
            name: str,
            description: str,
            amount: int,
            currency: str,
            unlimited: Optional[Union[bool, None]] = True,
            quantity: Optional[Union[int, None]] = None,
    ) -> PayStackResponse:
        """
        Update a product detail

        :param: product_id: ID or Code of the product
        :param: name: Name of the product
        :param: description: Description of the product
        :param: amount: Price of the product
        :param: currency: Currency of the product
        :param: unlimited: Set true if the product has unlimited stock,
        :param: quantity: Quantity of the product in stock Use if unlimited is false

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        data = {
            "name": name,
            "description": description,
            "price": amount,
            "currency": currency,
            "unlimited": unlimited,
            "quantity": quantity,
        }
        return await self._put_request(f"{product_endpoint}{product_id}", data=data)
