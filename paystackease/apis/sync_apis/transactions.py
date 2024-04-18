"""
Wrapper for Paystack Transactions API

The Transactions API allows you to create and manage payments on your integration.
"""

from datetime import date
from typing import List, Optional, Dict, Any, Union

from paystackease.core import PayStackResponse, SyncRequestAPI
from paystackease.helpers import Channels, Currency, Bearer, TransactionStatus


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
            metadata: Optional[Union[Dict[str, Any], None]] = None,
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
            "metadata": metadata,
        }
        return self._post_request("/transaction/initialize", data=data)

    def charge_authorization(
            self,
            email: str,
            amount: int,
            authorization_code: str,
            reference: Optional[Union[str, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            channels: Optional[Union[List[Channels], None]] = None,
            subaccount: Optional[Union[str, None]] = None,
            transaction_charge: Optional[int] = None,
            bearer: Optional[Union[Bearer, None]] = Bearer.ACCOUNT.value,
            queue: Optional[Union[bool, None]] = True,
            metadata: Optional[Union[Dict[str, List[Dict[str, Any]]], None]] = None,
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
        queue = self._convert_to_string(queue)

        data = {
            "email": email,
            "amount": amount,
            "authorization_code": authorization_code,
            "reference": reference,
            "currency": currency,
            "channels": channels,
            "subaccount": subaccount,
            "transaction_charge": transaction_charge,
            "bearer": bearer,
            "queue": queue,
            "metadata": metadata,
        }
        return self._post_request("/transaction/charge_authorization", data=data)

    def partial_debit(
            self,
            email: str,
            authorization_code: str,
            amount: int,
            currency: str,
            reference: Optional[Union[str, None]] = None,
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
            "authorization_code": authorization_code,
            "amount": amount,
            "currency": currency,
            "reference": reference,
            "at_least": at_least,
        }
        return self._post_request("/transaction/partial_debit", data=data)

    def list_transactions(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            customer: Optional[Union[int, None]] = None,
            terminal_id: Optional[Union[str, None]] = None,
            amount: Optional[Union[int, None]] = None,
            status: Optional[Union[TransactionStatus, None]] = None,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
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

        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "perPage": per_page,
            "page": page,
            "customer": customer,
            "terminalid": terminal_id,
            "amount": amount,
            "status": status,
            "from": from_date,
            "to": to_date,
        }
        return self._get_request("/transaction", params=params)

    def verify_transaction(self, reference: str) -> PayStackResponse:
        """
        Verify a transaction by reference

        :param: reference:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"/transaction/verify/{reference}")

    def fetch_transaction(self, transaction_id: int) -> PayStackResponse:
        """
        Fetch details of a specific transaction

        :param: transaction_id:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"/transaction/{transaction_id}")

    def transaction_timeline(self, id_or_reference: str) -> PayStackResponse:
        """
        Get the timeline of a transaction

        :param: id_or_reference:

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return self._get_request(f"/transaction/timeline/{id_or_reference}")

    def transaction_totals(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
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

        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

        params = {
            "perPage": per_page,
            "page": page,
            "from": from_date,
            "to": to_date,
        }
        return self._get_request("/transaction/totals", params=params)

    def export_transactions(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            customer: Optional[Union[int, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            amount: Optional[Union[int, None]] = None,
            status: Optional[Union[TransactionStatus, None]] = None,
            settled: Optional[Union[bool, None]] = True,
            settlement: Optional[Union[int, None]] = None,
            payment_page: Optional[Union[int, None]] = None,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
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
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)
        settled = self._convert_to_string(settled)

        params = {
            "perPage": per_page,
            "page": page,
            "customer": customer,
            "currency": currency,
            "amount": amount,
            "status": status,
            "settled": settled,
            "settlement": settlement,
            "payment_page": payment_page,
            "from": from_date,
            "to": to_date,
        }
        return self._get_request("/transaction/export", params=params)
