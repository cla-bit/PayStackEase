===========================================
Async SubAccounts Module
===========================================

.. :py:currentmodule:: paystackease.async_apis.asubaccounts


Wrapper for Asynchronous Paystack SubAccounts API. The Subaccounts API allows you to create and manage subaccounts on your integration. Subaccounts can be used to split payment between two accounts (your main account and a subaccount).

------------

.. py:class:: AsyncSubAccountClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack SubAccount API Reference: `Subaccount`_

    .. py:method:: async create_subaccount(business_name: str, settlement_bank: str, account_number: str, percentage_charge: float, description: str, primary_contact_email: str | None = None, primary_contact_name: str | None = None, primary_contact_phone: str | None = None, metadata: Dict[str, List[Dict[str, Any]]] | None = None)→ ClientResponse

        Create a subaccount

        :param business_name: The business name of the subaccount
        :type business_name: str
        :param settlement_bank: Bank code for the bank
        :type settlement_bank: str
        :param account_number:
        :type account_number: str
        :param percentage_charge: The percentage charge receives from each payment made to the subaccount
        :type percentage_charge: float
        :param description: The description of the subaccount
        :type description: str
        :param primary_contact_email: A contact email for the subaccount
        :type primary_contact_email: str, optional
        :param primary_contact_name: A name for the contact person for this subaccount
        :type primary_contact_name: str, optional
        :param primary_contact_phone: A phone number to call for this subaccount
        :type primary_contact_phone: str, optional
        :param metadata: Metadata associated with the subaccount. It is a dictionary of custom fields type of metadata
        :type metadata: Dict[str, List[Dict[str, Any]]] | None,

        :return: A response from the API
        :rtype: ClientResponse object

    .. py:method:: async fetch_subaccount(id_or_code: str)→ ClientResponse

        Fetch a subaccount

        :param id_or_code: The id or code of the subaccount
        :type id_or_code: str

        :return: A response from the API
        :rtype: ClientResponse object

    .. py:method:: async list_subaccounts(per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ ClientResponse

        List subaccounts

        :param per_page: The number of subaccounts to return. (default: 50)
        :type per_page: int, optional
        :param page: The page to return. (default: 1)
        :type page: int, optional
        :param from_date: The date from which to list subaccounts
        :type from_date: date, optional
        :param to_date: The date until which to list subaccounts
        :type to_date: date, optional

        :return: A response from the API
        :rtype: ClientResponse object

    .. py:method:: async update_subaccount(id_or_code: str, business_name: str, settlement_bank: str, account_number: str, active: bool | None = None, percentage_charge: float | None = None, description: str | None = None, primary_contact_email: str | None = None, primary_contact_name: str | None = None, primary_contact_phone: str | None = None, settlement_schedule: str | None = None, metadata: Dict[str, List[Dict[str, Any]]] | None = None)→ ClientResponse

        Update a subaccount

        :param id_or_code: The id or code of the subaccount
        :type id_or_code: str
        :param business_name: The business name of the subaccount
        :type business_name: str
        :param settlement_bank: Bank code for the bank
        :type settlement_bank: str
        :param account_number:
        :type account_number: str
        :param active: Whether the subaccount is active or not. (default: True)
        :type active: bool, optional
        :param percentage_charge: The percentage charge receives from each payment made to the subaccount
        :type percentage_charge: float, optional
        :param description: The description of the subaccount
        :type description: str, optional
        :param primary_contact_email: A contact email for the subaccount
        :type primary_contact_email: str, optional
        :param primary_contact_name: A name for the contact person for this subaccount
        :type primary_contact_name: str, optional
        :param primary_contact_phone: A phone number to call for this subaccount
        :type primary_contact_phone: str, optional
        :param settlement_schedule: The settlement schedule of the subaccount. (default: auto)
        :type settlement_schedule: str, optional
        :param metadata: Metadata associated with the subaccount. It is a dictionary of custom fields type
        :type metadata: Dict[str, List[Dict[str, Any]]] | None,

        :return: A response from the API
        :rtype: ClientResponse object

.. note::

    ``auto`` means payout is T+1 Manual means payout to the subaccount should only be made when requested.

Ensure you check use the string values of the enum classes. See :doc:`toolkit` documentation for more information.

.. _Subaccount: https://paystack.com/docs/api/subaccount/
