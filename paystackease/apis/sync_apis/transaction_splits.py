"""
Wrapper for Paystack Transaction Splits APIs

The Transaction Splits API enables merchants split the settlement for a transaction
across their payout account, and one or more subaccounts.
"""

from datetime import date
from typing import Optional, List, Dict, Any, Union

from paystackease.core import PayStackResponse, SyncRequestAPI
from paystackease.helpers import Currency


class TransactionSplitClientAPI(SyncRequestAPI):
    """
    Paystack Transaction Split API
    Reference: https://paystack.com/docs/api/split/
    """

    def create_split(
            self,
            transaction_split_name: str,
            transaction_split_type: str,
            currency: Currency,
            subaccounts: List[Dict[str, Any]],
            bearer_type: str,
            bearer_subaccount: str,
    ) -> PayStackResponse:
        """
        Create a split payment on your integration

        :param: transaction_split_name: Name of the transaction split
        :param: transaction_split_type: The type of transaction split you want to create [ percentage | flat ]
        :param: currency: [ Currency.value.value ]
        :param: subaccounts: A list of object containing subaccount code and number of shares
                            [{subaccount: ‘ACT_xxxxxxxxxx’, share: xxx},{...}]
        :param: bearer_type: Any of subaccount | account | all-proportional | all
        :param: bearer_subaccount: Subaccount code

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "name": transaction_split_name,
            "type": transaction_split_type,
            "currency": currency,
            "subaccounts": subaccounts,
            "bearer_type": bearer_type,
            "bearer_subaccount": bearer_subaccount,
        }
        return self._post_request("/split", data=data)

    def add_or_update_subaccount_split(
            self, split_id: str, subaccount: str, transaction_share: int
    ) -> PayStackResponse:
        """
        Add a Subaccount to a Transaction Split, or update the share of
        an existing Subaccount in a Transaction Split

        :param: split_id: The split ID
        :param: subaccount: The subaccount code
        :param: transaction_share: The number of shares

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"subaccount": subaccount, "share": transaction_share}
        return self._post_request(f"/split/{split_id}/subaccount/add", data=data)

    def remove_sub_account_split(self, split_id: str, subaccount: str) -> PayStackResponse:
        """
        Remove a Sub Account from a transaction split

        :param: split_id: The split ID
        :param: subaccount: The subaccount code

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"subaccount": subaccount}
        return self._post_request(f"/split/{split_id}/subaccount/remove", data=data)

    def update_split(
            self,
            split_id: str,
            transaction_split_name: str,
            active: bool,
            bearer_type: Optional[Union[str, None]] = None,
            bearer_subaccount: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
        """
        Update a specific transaction split details

        :param: split_id: The split ID
        :param: transaction_split_name: Name of the transaction split
        :param: active: True or False
        :param: bearer_type:
        :param: bearer_subaccount:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        # convert bool to string
        active = self._convert_to_string(active)

        data = {
            "name": transaction_split_name,
            "active": active,
            "bearer_type": bearer_type,
            "bearer_subaccount": bearer_subaccount,
        }
        return self._put_request(f"/split/{split_id}", data=data)

    def list_split(
            self,
            split_name: Optional[Union[str, None]] = None,
            active: Optional[Union[bool, None]] = True,
            sort_by: Optional[Union[str, None]] = None,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
    ) -> PayStackResponse:
        """
        List all the transaction splits

        :param: split_name: Name of the transaction split
        :param: active: True or False
        :param: sort_by: Sort by name, defaults to createdAt date,
        :param: per_page:
        :param: page:
        :param: from_date:
        :param: to_date:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        # convert date and bool to string
        active = self._convert_to_string(active)
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "name": split_name,
            "active": active,
            "sort_by": sort_by,
            "perPage": per_page,
            "page": page,
            "from": from_date,
            "to": to_date,
        }
        return self._get_request("/split", params=params)

    def fetch_split(self, split_id: str) -> PayStackResponse:
        """
        Fetch details of a specific transaction split

        :param: split_id: The split ID

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"/split/{split_id}")
