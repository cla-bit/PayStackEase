""" Wrapper for Asynchronous Paystack SubAccounts API
The Subaccounts API allows you to create and manage subaccounts on your integration.
Subaccounts can be used to split payment between two accounts (your main account and a subaccount).
"""

from datetime import date
from typing import Optional, Dict, List, Any
from paystackease.abase import AsyncPayStackBaseClientAPI


class AsyncSubAccountClientAPI(AsyncPayStackBaseClientAPI):
    """Paystack SubAccount API
    Reference: https://paystack.com/docs/api/subaccount/
    """

    async def create_subaccount(
        self,
        business_name: str,
        settlement_bank: str,
        account_number: str,
        percentage_charge: float,
        description: str,
        primary_contact_email: Optional[str] = None,
        primary_contact_name: Optional[str] = None,
        primary_contact_phone: Optional[str] = None,
        metadata: Optional[Dict[str, List[Dict[str, Any]]]] = None,
    ) -> dict:
        """Create a subaccount
        :param business_name: The business name of the subaccount.
        :param settlement_bank: Bank Code for the bank
        :param account_number: The account number of the subaccount.
        :param percentage_charge: The percentage charge receives from each payment made to the subaccount
        :param description: The description of the subaccount.
        :param primary_contact_email: A contact email for the subaccount
        :param primary_contact_name: A name for the contact person for this subaccount
        :param primary_contact_phone: A phone number to call for this subaccount
        :param metadata: Stringified JSON object. {"custom_fields": [{"name": "value"}]}

        :return: The response from the API
        :rtype: dict
        """
        data = {
            "business_name": business_name,
            "settlement_bank": settlement_bank,
            "account_number": account_number,
            "percentage_charge": percentage_charge,
            "description": description,
            "primary_contact_email": primary_contact_email,
            "primary_contact_name": primary_contact_name,
            "primary_contact_phone": primary_contact_phone,
            "metadata": metadata,
        }
        return await self._post_request("/subaccount", data=data)

    async def update_subaccount(
        self,
        id_or_code: str,
        business_name: str,
        settlement_bank: str,
        account_number: str,
        active: Optional[bool] = None,
        percentage_charge: Optional[float] = None,
        description: Optional[str] = None,
        primary_contact_email: Optional[str] = None,
        primary_contact_name: Optional[str] = None,
        primary_contact_phone: Optional[str] = None,
        settlement_schedule: Optional[str] = None,
        metadata: Optional[Dict[str, List[Dict[str, Any]]]] = None,
    ) -> dict:
        """Update a subaccount
        :param id_or_code: The id or code of the subaccount.
        :param business_name: The business name of the subaccount.
        :param settlement_bank: The settlement bank of the subaccount.
        :param account_number:
        :param active: [ True or False ]
        :param percentage_charge:
        :param description:
        :param primary_contact_email:
        :param primary_contact_name:
        :param primary_contact_phone:
        :param settlement_schedule: Values: [ auto, weekly, `monthly`, `manual` ].
        Auto means payout is T+1
        Manual means payout to the subaccount should only be made when requested. async defaults to auto
        :param metadata: Stringified JSON object. {"custom_fields": [{"name": "value"}]}

        :return: The response from the API
        :rtype: dict
        """
        active = self._convert_to_string(active)

        data = {
            "business_name": business_name,
            "settlement_bank": settlement_bank,
            "account_number": account_number,
            "active": active,
            "percentage_charge": percentage_charge,
            "description": description,
            "primary_contact_email": primary_contact_email,
            "primary_contact_name": primary_contact_name,
            "primary_contact_phone": primary_contact_phone,
            "settlement_schedule": settlement_schedule,
            "metadata": metadata,
        }
        return await self._put_request(f"/subaccount/{id_or_code}", data=data)

    async def list_subaccounts(
        self,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
    ) -> dict:
        """List all subaccounts
        :param per_page: The number of records to return per page.
        :param page: The number to retrieve.
        :param from_date:
        :param to_date:

        :return: The response from the API
        :rtype: dict
        """
        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {"perPage": per_page, "page": page, "from": from_date, "to": to_date}
        return await self._get_request("/subaccount", params=params)

    async def fetch_subaccount(self, id_or_code: str) -> dict:
        """Fetch details of a specific subaccount
        :param id_or_code: The id or code of the subaccount.

        :return: The response from the API
        :rtype: dict
        """
        return await self._get_request(f"/subaccount/{id_or_code}")
