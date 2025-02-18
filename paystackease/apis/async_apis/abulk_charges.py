"""
Wrapper for Asynchronous Paystack Bulk Charges API.

The Bulk Charges API allows you to create and manage multiple recurring payments from your customers.
"""

from typing import List, Dict, Optional, Any, Union

from paystackease.src import PayStackResponse, AsyncRequestAPI
from paystackease.helpers import STATUS, AuthReferenceObject, bulk_charge_endpoint, PageModel, DatePageModel


class AsyncBulkChargesClientAPI(AsyncRequestAPI):
    """
    Paystack Bulk Charges API
    Reference: https://paystack.com/docs/api/bulk-charge/
    """

    async def initiate_bulk_charge(self, objects: Union[AuthReferenceObject, List[AuthReferenceObject]]) -> PayStackResponse:
        """
        Send an array of objects with authorization codes and amount

        :param: objects

        note::

            A list of dictionary with authorization codes, amount and reference as keys
            [{"authorization": "123456", "amount": 1000, "reference": "123456" }]

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        # ensure objects is a list
        if isinstance(objects, AuthReferenceObject):
            objects = [objects]  # converts the single instance to a list

        if not isinstance(objects, list) or not all(isinstance(obj, AuthReferenceObject) for obj in objects):
            raise ValueError("Expected a single AuthReferenceObject or a list of AuthReferenceObject instances.")

        if not objects:
            raise ValueError("The list of charge objects cannot be empty.")

        validated_data = [obj.model_dump() for obj in objects]
        return await self._post_request(bulk_charge_endpoint, data=validated_data)

    async def list_bulk_charge_batches(
            self,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
    ) -> PayStackResponse:
        """
        List all bulk charges

        :param: per_page
        :param: page
        :param: from_date
        :param: to_date

        note::

            Date Time format: 2016-09-24T00:00:05.000Z, 2016-09-21

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        validated_params = {
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
        }

        return await self._get_request(bulk_charge_endpoint, validated_params)

    async def fetch_bulk_charge_batch(self, id_or_code: str) -> PayStackResponse:
        """
        Fetch a bulk charge of a specific batch

        :param: id_or_code

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"{bulk_charge_endpoint}{id_or_code}")

    async def fetch_charge_bulk_batch(
            self,
            id_or_code: str,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
            status: Optional[Union[STATUS, None]] = None,
    ) -> PayStackResponse:
        """
        Fetch a bulk charge of a specific batch

        :param: id_or_code
        :param: status:  {STATUS.value.value}
        :param: per_page
        :param: page
        :param: from_date
        :param: to_date

        note::

            Date Time format: 2016-09-24T00:00:05.000Z, 2016-09-21
            status: STATUS.value.value

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        validated_params = {
            "status": status,
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
        }

        return await self._get_request(f"{bulk_charge_endpoint}{id_or_code}/charges", params=validated_params)

    async def pause_bulk_charge_batch(self, batch_code: str) -> PayStackResponse:
        """
        Pause a bulk charge of a specific batch

        :param: batch_code

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"{bulk_charge_endpoint}pause/{batch_code}")

    async def resume_bulk_charge_batch(self, batch_code: str) -> PayStackResponse:
        """
        Resume a bulk charge of a specific batch

        :param: batch_code

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"{bulk_charge_endpoint}resume/{batch_code}")
