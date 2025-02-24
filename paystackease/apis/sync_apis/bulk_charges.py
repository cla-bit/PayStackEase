""" Wrapper for Paystack Bulk Charges API.

The Bulk Charges API allows you to create and manage multiple recurring payments from your customers.
"""

from typing import List, Optional, Union

from paystackease.src import PayStackResponse, SyncRequestAPI
from paystackease.helpers import STATUS, BulkChargeObject, bulk_charge_endpoint, PageModel, DatePageModel


class BulkChargesClientAPI(SyncRequestAPI):
    """
    Paystack Bulk Charges API
    Reference: https://paystack.com/docs/api/bulk-charge/
    """

    def initiate_bulk_charge(self, objects: Union[BulkChargeObject, List[BulkChargeObject]]) -> PayStackResponse:
        """
        Send an array of objects with authorization codes and amount

        Parameters:
            objects (BulkChargeObject | List[BulkChargeObject]): A single AuthReferenceObject or a list of AuthReferenceObject instances.

        Returns:
            PayStackResponse: The PayStackResponse object from the API.
        """

        # ensure objects is a list
        if isinstance(objects, BulkChargeObject):
            objects = [objects]  # converts the single instance to a list

        if not isinstance(objects, list) or not all(isinstance(obj, BulkChargeObject) for obj in objects):
            raise ValueError("Expected a single BulkChargeObject or a list of BulkChargeObject instances.")

        if not objects:
            raise ValueError("The list of charge objects cannot be empty.")

        data = [obj.model_dump() for obj in objects]
        return self._post_request(bulk_charge_endpoint, data=data)

    def list_bulk_charge_batches(
            self,
            page_values: Optional[PageModel] = None,
            date_values: Optional[DatePageModel] = None,
    ) -> PayStackResponse:
        """
        List all bulk charges

        Parameters
            page_values (Optional[PageModel]): A PageModel instance with page number and per_page.
            date_values (Optional[DatePageModel]): A DatePageModel instance with from_date and to_date.

        Returns:
            PayStackResponse: The PayStackResponse object from the API.
        """

        params = {
            **(page_values.model_dump(by_alias=True, exclude_none=True) if page_values else {}),
            **(date_values.model_dump(by_alias=True, exclude_none=True) if date_values else {}),
        }

        return self._get_request(bulk_charge_endpoint, params=params)

    def fetch_bulk_charge_batch(self, id_or_code: str) -> PayStackResponse:
        """
        Fetch a bulk charge of a specific batch

        Parameters:
            id_or_code (str): The id or code of the Batch object created after initiating a bulk charge.

        Returns:
            PayStackResponse: The PayStackResponse object from the API.
        """
        return self._get_request(f"{bulk_charge_endpoint}{id_or_code}")

    def fetch_charge_bulk_batch(
            self,
            id_or_code: str,
            page_values: Optional[PageModel] = None,
            date_values: Optional[DatePageModel] = None,
            status: Optional[STATUS] = None,
    ) -> PayStackResponse:
        """
        Fetch a bulk charge of a specific batch

        Parameters:
            id_or_code (str): The id or code of the Batch object created after initiating a bulk charge.
            page_values (Optional[PageModel]): A PageModel instance with page number and per_page.
            date_values (Optional[DatePageModel]): A DatePageModel instance with from_date and to_date.
            status (Optional[STATUS]): The status of the charges. Either one of these values: pending, success or failed of the STATUS Enum class

        Returns:
            The PayStackResponse object from the API
        """
        params = {
            **(page_values.model_dump(by_alias=True, exclude_none=True) if page_values else {}),
            **(date_values.model_dump(by_alias=True, exclude_none=True) if date_values else {}),
            "status": status if status else None,
        }

        return self._get_request(f"{bulk_charge_endpoint}{id_or_code}/charges", params=params)

    def pause_bulk_charge_batch(self, batch_code: str) -> PayStackResponse:
        """
        Pause a bulk charge of a specific batch

        Parameters:
            batch_code (str): The code of the Batch object created after initiating a bulk charge.

        Returns:
            The PayStackResponse object from the API
        """
        return self._get_request(f"{bulk_charge_endpoint}pause/{batch_code}")

    def resume_bulk_charge_batch(self, batch_code: str) -> PayStackResponse:
        """
        Resume a bulk charge of a specific batch

        Parameters:
            batch_code (str): The code of the Batch object created after initiating a bulk charge.

        Returns:
            The PayStackResponse object from the API
        """
        return self._get_request(f"{bulk_charge_endpoint}resume/{batch_code}")
