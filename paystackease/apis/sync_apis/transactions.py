"""
Wrapper for Paystack Transactions API

The Transactions API allows you to create and manage payments on your integration.
"""

from typing import List, Optional, Union

from paystackease.src import PayStackResponse, SyncRequestAPI
from paystackease.helpers import Channels, Currency, Bearer, TransactionStatus, transaction_endpoint, MetaDataModel, \
    CustomMetaData, convert_to_string, AuthReferenceObject, PageModel, DatePageModel


class TransactionClientAPI(SyncRequestAPI):
    """
    Paystack Transaction API
    Reference: https://paystack.com/docs/api/transaction/
    """

    def initialize(
            self,
            email: str,
            amount: int,
            currency: Optional[Union[Currency, None]] = Currency.NGN.value,
            reference: Optional[Union[str, None]] = None,
            callback_url: Optional[Union[str, None]] = None,
            plan: Optional[Union[str, None]] = None,
            invoice_limit: Optional[Union[int, None]] = None,
            channels: Optional[Union[List[Channels], None]] = None,
            split_code: Optional[Union[str, None]] = None,
            subaccount: Optional[Union[str, None]] = None,
            transaction_charge: Optional[Union[int, None]] = None,
            bearer: Optional[Union[Bearer, None]] = Bearer.ACCOUNT.value,
            metadata: Optional[MetaDataModel] = None,
    ) -> PayStackResponse:
        """
        Initialize a transaction

        :param: email:
        :param: amount: amount should be in subunit in this case 10000 kobo = 100 naira.
                        Use convert_currency() to convert to subunit
        :param: currency:  # Currency.value.value
        :param: reference:
        :param: callback_url: # Use this to override the callback url provided on the  dashboard
                            # https://example.com/callback
        :param: plan:  # If transaction is to create a subscription to a predefined plan, provide plan code here.
        :param: invoice_limit:  # Number of times to charge customer during subscription to plan
        :param: channels:  # [Channels.value.value, Channels.value.value, ...]
        :param: split_code:  # The split code of the transaction split. e.g. SPL_98WF13Eb3w
        :param: subaccount:  # The code for the subaccount that owns the payment. e.g. ACCT_8f4s1eq7ml6rlzj
        :param: transaction_charge: # An amount used to override the split configuration for a
                                    # single split payment
        :param: bearer:  # Who bears Paystack charges? Two options: account, subaccount
        :param: metadata:  # Stringified JSON object of custom data. {"foo": "bar" }

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "email": email,
            "amount": amount,
            "currency": currency,
            "reference": reference,
            "callback_url": callback_url,
            "plan": plan,
            "invoice_limit": invoice_limit,
            "channels": channels,
            "split_code": split_code,
            "subaccount": subaccount,
            "transaction_charge": transaction_charge,
            "bearer": bearer,
            **(metadata.model_dump() if metadata else {})
        }
        return self._post_request(f"{transaction_endpoint}initialize", data=data)

    def charge_authorization(
            self,
            email: str,
            auth_model: AuthReferenceObject,
            currency: Optional[Union[Currency, None]] = None,
            channels: Optional[Union[List[Channels], None]] = None,
            subaccount: Optional[Union[str, None]] = None,
            transaction_charge: Optional[int] = None,
            bearer: Optional[Union[Bearer, None]] = Bearer.ACCOUNT.value,
            queue: Optional[Union[bool, None]] = True,
            metadata: Optional[CustomMetaData] = None,
    ) -> PayStackResponse:
        """
        Charge an authorization transaction

        :param: email:
        :param: amount: amount should be in subunit in this case 10000 kobo = 100 naira.
                        Use convert_currency() to convert to subunit
        :param: authorization_code:  # value = AUTH_1234234WRFW
        :param: reference:
        :param: currency:  # value = Currency.value.value
        :param: channels:  # [Channels.value.value, Channels.value.value, ...]
        :param: subaccount:  # value = ACCT_8f4s1eq7ml6rlzj
        :param: transaction_charge:
        :param: bearer:  # Who bears Paystack charges? Two options: account, subaccount
        :param: queue:  # If set to true, the transaction will be queued for processing
        :param: metadata:  # Stringified JSON object of custom data. {"foo": "bar" }

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        # convert bool to string
        queue = convert_to_string(queue)

        data = {
            "email": email,
            **auth_model.model_dump(),
            "currency": currency,
            "channels": channels,
            "subaccount": subaccount,
            "transaction_charge": transaction_charge,
            "bearer": bearer,
            "queue": queue,
            **(metadata.model_dump() if metadata else {}),
        }
        return self._post_request(f"{transaction_endpoint}charge_authorization", data=data)

    def partial_debit(
            self,
            email: str,
            auth_model: AuthReferenceObject,
            currency: str,
            at_least: Optional[Union[int, None]] = None,
    ) -> PayStackResponse:
        """
        Charge a partial debit transaction

        :param: email:
        :param: authorization_code:  # value = AUTH_1234234WRFW
        :param: amount: amount should be in subunit in this case 10000 kobo = 100 naira.
                        Use convert_currency() to convert to subunit
        :param: currency:  # value = Currency.value.value
        :param: reference:  # Unique transaction reference.
        :param: at_least:  # Minimum amount to charge

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        data = {
            "email": email,
            **auth_model.model_dump(),
            "currency": currency,
            "at_least": at_least,
        }
        return self._post_request(f"{transaction_endpoint}partial_debit", data=data)

    def list_transactions(
            self,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
            customer: Optional[Union[int, None]] = None,
            terminal_id: Optional[Union[str, None]] = None,
            amount: Optional[Union[int, None]] = None,
            status: Optional[Union[TransactionStatus, None]] = None,
    ) -> PayStackResponse:
        """
        List all transactions

        :param: per_page:  # Specify how many records you want to retrieve per page.
        :param: page:  # Specify a page number to retrieve
        :param: customer:  # Specify an ID for the customer whose transactions you want to retrieve
        :param: terminal_id:  # Specify an ID for the terminal whose transactions you want to retrieve
        :param: amount:  # Specify an amount for the transactions you want to retrieve
        :param: status:  # Specify a status for the transactions you want to retrieve [success, failed, abandoned]
        :param: from_date:  # A timestamp from which to start listing transaction 2016-09-24T00:00:05.000Z, 2016-09-21
        :param: to_date:  # A timestamp at which to stop listing transaction 2016-09-24T00:00:05.000Z

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        params = {
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
            "customer": customer,
            "terminalid": terminal_id,
            "amount": amount,
            "status": status,
        }
        return self._get_request(transaction_endpoint, params=params)

    def verify_transaction(self, reference: str) -> PayStackResponse:
        """
        Verify a transaction by reference

        :param: reference:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"{transaction_endpoint}verify/{reference}")

    def fetch_transaction(self, transaction_id: int) -> PayStackResponse:
        """
        Fetch details of a specific transaction

        :param: transaction_id:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"{transaction_endpoint}{transaction_id}")

    def transaction_timeline(self, id_or_reference: str) -> PayStackResponse:
        """
        Get the timeline of a transaction

        :param: id_or_reference:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"{transaction_endpoint}timeline/{id_or_reference}")

    def transaction_totals(
            self,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
    ) -> PayStackResponse:
        """
        Get totals of all transactions

        :param: per_page:
        :param: page:
        :param: from_date:
        :param: to_date:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        params = {
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
        }
        return self._get_request(f"{transaction_endpoint}totals", params=params)

    def export_transactions(
            self,
            page_model: Optional[PageModel] = None,
            date_page: Optional[DatePageModel] = None,
            customer: Optional[Union[int, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            amount: Optional[Union[int, None]] = None,
            status: Optional[Union[TransactionStatus, None]] = None,
            settled: Optional[Union[bool, None]] = True,
            settlement: Optional[Union[int, None]] = None,
            payment_page: Optional[Union[int, None]] = None,
    ) -> PayStackResponse:
        """
        Export transactions

        :param: per_page:
        :param: page:
        :param: customer:
        :param: currency:  # value = Currency.value.value
        :param: amount:
        :param: status:
        :param: settled:  # true or false
        :param: settlement:
        :param: payment_page:
        :param: from_date:  # 2016-09-24T00:00:05.000Z
        :param: to_date:  # 2016-09-24T00:00:05.000Z

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        # convert date and bool to string
        settled = convert_to_string(settled)

        params = {
            **page_model.model_dump(by_alias=True, exclude_none=True),
            **date_page.model_dump(by_alias=True, exclude_none=True),
            "customer": customer,
            "currency": currency,
            "amount": amount,
            "status": status,
            "settled": settled,
            "settlement": settlement,
            "payment_page": payment_page,
        }
        return self._get_request(f"{transaction_endpoint}export", params=params)
