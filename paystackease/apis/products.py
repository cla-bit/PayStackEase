"""
Wrapper for Paystack Products API

The Products API allows you to create and manage inventories on your integration.
"""
from requests import Response

from datetime import date
from typing import Optional
from paystackease._base import PayStackBaseClientAPI


class ProductClientAPI(PayStackBaseClientAPI):
    """
    Paystack Product API
    Reference: https://paystack.com/docs/api/product/
    """

    def create_product(
            self,
            name: str,
            description: str,
            amount: int,
            currency: str,
            unlimited: Optional[bool] = None,
            quantity: Optional[int] = None,
    ) -> Response:
        """
        Create a product

        :param: name: Name of the product
        :param: description: Description of the product
        :param: amount: Price of the product
        :param: currency: Currency of the product
        :param: unlimited: Set true if the product has unlimited stock,
        :param: quantity: Quantity of the product in stock Use if unlimited is false

        :return: The response from the API
        :rtype: Response object
        """

        # convert bool to string
        unlimited = self._convert_to_string(unlimited)

        data = {
            "name": name,
            "description": description,
            "price": amount,
            "currency": currency,
            "unlimited": unlimited,
            "quantity": quantity,
        }
        return self._post_request("/product", data=data)

    def list_products(
            self,
            per_page: Optional[int] = 50,
            page: Optional[int] = 1,
            from_date: Optional[date] = None,
            to_date: Optional[date] = None,
    ) -> Response:
        """
        List all the products

        :param: per_page: Number of records to return
        :param: page:  number to return
        :param: from_date: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param: to_date: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        :return: The response from the API
        :rtype: Response object
        """

        # convert date to strings
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {"perPage": per_page, "page": page, "from": from_date, "to": to_date}
        return self._get_request("/product", params=params)

    def fetch_product(self, product_id: str) -> Response:
        """
        Get details of a product

        :param: product_id: ID or Code of the product

        :return: The response from the API
        :rtype: Response object
        """
        return self._get_request(f"/product/{product_id}")

    def update_product(
            self,
            product_id: str,
            name: str,
            description: str,
            amount: int,
            currency: str,
            unlimited: Optional[bool] = None,
            quantity: Optional[int] = None,
    ) -> Response:
        """
        Update a product detail

        :param: product_id: ID or Code of the product
        :param: name: Name of the product
        :param: description: Description of the product
        :param: amount: Price of the product
        :param: currency: Currency of the product
        :param: unlimited: Set true if the product has unlimited stock,
        :param: quantity: Quantity of the product in stock Use if unlimited is false

        :return: The response from the API
        :rtype: Response object
        """

        # convert bool to string
        unlimited = self._convert_to_string(unlimited)

        data = {
            "name": name,
            "description": description,
            "price": amount,
            "currency": currency,
            "unlimited": unlimited,
            "quantity": quantity,
        }
        return self._put_request(f"/product/{product_id}", data=data)
