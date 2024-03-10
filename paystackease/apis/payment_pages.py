"""
Wrapper for Paystack Payment Pages API.

The Payment Pages API provides a quick and secure way to collect payment for products.
"""

from datetime import date
from typing import Optional, Dict, List
from paystackease.apis.base import PayStackBaseClientAPI


class PaymentPagesClientAPI(PayStackBaseClientAPI):
    """
    Paystack Payment Pages API
    Reference: https://paystack.com/docs/api/page/
    """

    def create_payment_page(
            self,
            name: str,
            description: Optional[str] = None,
            amount: Optional[int] = None,
            split_code: Optional[str] = None,
            page_slug: Optional[str] = None,
            redirect_url: Optional[str] = None,
            metadata: Optional[Dict[str, str]] = None,
            custom_fields: Optional[List[str]] = None,
    ) -> dict:
        """
        Create a payment page

        :param: name: Name of the page
        :param: description: Description of the page
        :param: amount: Amount of the page
        :param: split_code: Split code of the transaction split
        :param: page_slug: URL slug you would like to be associated with this page.
        
        note::

            Page will be accessible at https://paystack.com/pay/page_slug

        :param: redirect_url: If you would like Paystack to redirect someplace
        upon successful payment, specify the URL here.
        :param: metadata: Extra data to configure the payment page including subaccount,logo image, transaction charge
        :param: custom_fields: If you would like to accept custom fields, specify them here.

        :return: The response from the API
        :rtype: dict
        """
        data = {
            "name": name,
            "description": description,
            "amount": amount,
            "split_code": split_code,
            "slug": page_slug,
            "redirect_url": redirect_url,
            "metadata": metadata,
            "custom_fields": custom_fields,
        }
        return self._post_request("/page", data=data)

    def list_payment_pages(
            self,
            per_page: Optional[int] = None,
            page: Optional[int] = None,
            from_date: Optional[date] = None,
            to_date: Optional[date] = None,
    ) -> dict:
        """
        List all the payment pages

        :param: per_page: Number of records to return
        :param: page: number to return
        :param: from_date: A timestamp from which to start listing page
        :param: to_date: A timestamp from which to start listing page

        :return: The response from the API
        :rtype: dict

        note::
            Date Time value is in this format: 2016-09-24T00:00:05.000Z, 2016-09-21
        """

        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {"perPage": per_page, "page": page, "from": from_date, "to": to_date}
        return self._get_request("/page", params=params)

    def fetch_payment_page(self, page_id_or_slug: str) -> dict:
        """
        Get details of a payment page

        :param: page_id_or_slug: ID or slug of the payment page

        :return: The response from the API
        :rtype: dict
        """
        return self._get_request(f"/page/{page_id_or_slug}")

    def update_payment_page(
            self,
            page_id_or_slug: str,
            name: Optional[str] = None,
            description: Optional[str] = None,
            amount: Optional[int] = None,
            active: Optional[bool] = None,
    ) -> dict:
        """
        Update a payment page detail

        :param: page_id_or_slug: ID or slug of the payment page
        :param: name: Name of the page
        :param: description: Description of the page
        :param: amount: Amount of the page
        :param: active: Set false to deactivate the page url

        :return: The response from the API
        :rtype: dict
        """

        # convert bool to string
        active = self._convert_to_string(active)

        data = {
            "name": name,
            "description": description,
            "amount": amount,
            "active": active,
        }
        return self._put_request(f"/page/{page_id_or_slug}", data=data)

    def check_slug_available(self, page_slug: str) -> dict:
        """
        Check if a slug is available

        :param: page_slug: URL slug you would like to be associated with this page.

        :return: The response from the API
        :rtype: dict
        """
        return self._get_request(f"/page/check_slug_availability/{page_slug}")

    def add_products(self, payment_id: int, product: List[int]) -> dict:
        """
        Add products to a payment page

        :param: payment_id: ID of the payment page
        :param: product: List of IDS of all the products

        :return: The response from the API
        :rtype: dict
        """
        data = {"product": product}
        return self._post_request(f"/page/{payment_id}/product", data=data)
