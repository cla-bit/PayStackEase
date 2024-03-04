""" Wrapper for Asynchronous Paystack Products API
The Products API allows you to create and manage inventories on your integration.
"""

from datetime import date
from typing import Optional
from paystackease.abase import AsyncPayStackBaseClientAPI


class AsyncProductClientAPI(AsyncPayStackBaseClientAPI):
    """Paystack Product API
    Reference: https://paystack.com/docs/api/product/
    """

    async def create_product(
        self,
        name: str,
        description: str,
        amount: int,
        currency: str,
        unlimited: Optional[bool] = None,
        quantity: Optional[int] = None,
    ) -> dict:
        """Create a product
        :param name: Name of the product
        :param description: Description of the product
        :param amount: Price of the product
        :param currency: Currency of the product
        :param unlimited: Set true if the product has unlimited stock,
        :param quantity: Quantity of the product in stock Use if unlimited is false

        :return: The response from the API
        :rtype: dict
        """
        # convert bool to string
        unlimited = self.convert_to_string(unlimited)

        data = {
            "name": name,
            "description": description,
            "price": amount,
            "currency": currency,
            "unlimited": unlimited,
            "quantity": quantity,
        }
        return await self.post_request("/product", data=data)

    async def list_products(
        self,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
    ) -> dict:
        """List all the products
        :param per_page: Number of records to return per page
        :param page:  number to return
        :param from_date: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param to_date: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        :return: The response from the API
        :rtype: dict
        """
        # convert date to string
        from_date = self.convert_to_string(from_date)
        to_date = self.convert_to_string(to_date)

        params = {"perPage": per_page, "page": page, "from": from_date, "to": to_date}
        return await self.get_request("/product", params=params)

    async def fetch_product(self, product_id: str) -> dict:
        """Get details of a product
        :param product_id: ID or Code of the product

        :return: The response from the API
        :rtype: dict
        """
        return await self.get_request(f"/product/{product_id}")

    async def update_product(
        self,
        product_id: str,
        name: str,
        description: str,
        amount: int,
        currency: str,
        unlimited: Optional[bool] = None,
        quantity: Optional[int] = None,
    ) -> dict:
        """Update a product detail
        :param product_id: ID or Code of the product
        :param name: Name of the product
        :param description: Description of the product
        :param amount: Price of the product
        :param currency: Currency of the product
        :param unlimited: Set true if the product has unlimited stock,
        :param quantity: Quantity of the product in stock Use if unlimited is false

        :return: The response from the API
        :rtype: dict
        """
        # convert bool to string
        unlimited = self.convert_to_string(unlimited)

        data = {
            "name": name,
            "description": description,
            "price": amount,
            "currency": currency,
            "unlimited": unlimited,
            "quantity": quantity,
        }
        return await self.put_request(f"/product/{product_id}", data=data)
