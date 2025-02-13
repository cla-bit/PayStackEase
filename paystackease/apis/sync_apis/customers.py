"""
Wrapper for Paystack Customers API.

The Customers API allows you to create and manage customers on your integration.
"""

from typing import Optional, Dict, Any, Union

from paystackease.src import PayStackResponse, SyncRequestAPI
from paystackease.helpers import RiskAction, customer_endpoint, CustomerDetails, PageModel, DatePageModel


class CustomerClientAPI(SyncRequestAPI):
    """
    Paystack Customer API
    Reference: https://paystack.com/docs/api/customer/
    """

    def create_customer(
            self, 
            email: str,
            customer_details: CustomerDetails,
            metadata: Optional[Union[Dict[str, Any], None]] = None
    ) -> PayStackResponse:
        """
        Create a customer

        :param: email: The email associated with the customer.
        :param: first_name: The first name of the customer.
        :param: last_name: The last name of the customer.
        :param: phone: The phone number of the customer.
        :param: metadata: The metadata of the customer in JSON format.

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        validated_data = {
            "email": email,
            **customer_details.model_dump(exclude={"middle_name"}),
            "metadata": metadata,
        }
        return self._post_request(customer_endpoint, data=validated_data)

    def validate_customer(
            self,
            email_or_code: str,
            customer_details: CustomerDetails,
            country: str,
            bank_code: str,
            account_number: str,
            bvn: str,
            account_type: str = "bank_account",
            customer_id_num: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
        """
        Validate a customer's identity

        :param: email_or_code: The email or code of the customer.
        :param: first_name: The first name of the customer.
        :param: last_name: The last name of the customer.
        :param: middle_name: The middle name of the customer.
        :param: account_type: The type of account. Only bank_account is currently supported.
        :param: customer_id_num: The customer identification number
        :param: country: The country of the customer. 2-letter country code of identification issuer
        :param: bvn: The Bank Verification Number
        :param: bank_code: The bank code of the customer
        :param: account_number: The account number of the customer

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            **customer_details.model_dump(exclude={"phone"}, exclude_none=True),
            "type": account_type,
            "value": customer_id_num,
            "country": country,
            "bvn": bvn,
            "bank_code": bank_code,
            "account_number": account_number,
        }
        return self._post_request(f"{customer_endpoint}{email_or_code}/identification", data=data)

    def whitelist_blacklist_customer(
            self, email_or_code: str, risk_action: Optional[Union[RiskAction, None]] = None
    ) -> PayStackResponse:
        """
        Whitelist or blacklist a customer

        :param: email_or_code: The code or email of the customer.
        :param: risk_action: The action to take on the customer. value: RiskAction.value.value = "allow" pr "deny"

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "customer": email_or_code,
            "risk_action": risk_action
        }
        return self._post_request(f"{customer_endpoint}set_risk_action", data=data)

    def deactivate_authorization(self, authorization_code: str) -> PayStackResponse:
        """
        Deactivate an authorization when the card needs to be forgotten

        :param: authorization_code: The authorization code to be deactivated.

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {"authorization_code": authorization_code}
        return self._post_request(f"{customer_endpoint}deactivate_authorization", data=data)

    def update_customer(
            self,
            customer_code: str,
            customer_details: CustomerDetails,
            metadata: Optional[Union[Dict[str, Any], None]] = None
    ) -> PayStackResponse:
        """
        Update a customer

        :param: customer_code: The code of the customer.
        :param: first_name: The first name of the customer.
        :param: last_name: The last name of the customer.
        :param: phone: The phone number of the customer.
        :param: metadata: The metadata of the customer in JSON format. {"key1": "value1", "key2": "value2"}

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        validated_data = {
            **customer_details.model_dump(exclude={"middle_name"}, exclude_none=True),
            "metadata": metadata,
        }
        return self._put_request(f"{customer_endpoint}{customer_code}", data=validated_data)

    def fetch_customer(self, email_or_code: str) -> PayStackResponse:
        """
        Fetch details of a specific customer

        :param: email_or_code: The email or code of the customer.

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"{customer_endpoint}{email_or_code}")

    def list_customers(
            self,
            page_model: Optional[PageModel] = None,
            date_model: Optional[DatePageModel] = None,
    ) -> PayStackResponse:
        """
        List all customers

        :param: per_page: The number of records to return.
        :param: page: The page number to return.
        :param: from_date: The date to start returning customers from
        :param: to_date: The date to stop returning customers from

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        validated_params = {
            **page_model.model_dump(exclude_none=True, by_alias=True),
            **date_model.model_dump(exclude_none=True, by_alias=True)
        }
        return self._get_request("/customer", params=validated_params)
