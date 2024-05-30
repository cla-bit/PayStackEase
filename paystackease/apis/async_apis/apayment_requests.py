"""
Wrapper for Asynchronous Paystack Payment Requests API.

The Payment Requests API allows you manage requests for payment of goods and services.
"""

from datetime import date
from typing import Optional, List, Dict, Any, Union

from paystackease.core import AsyncRequestAPI, PayStackResponse
from paystackease.helpers import PayMentRequestStatus, Currency


class AsyncPaymentRequestClientAPI(AsyncRequestAPI):
    """
    Paystack Payment Request API
    Reference: https://paystack.com/docs/api/payment-request/
    """

    async def create_payment_request(
            self,
            customer: str,
            amount: int,
            draft: bool = False,
            has_invoice: bool = True,
            send_notification: bool = True,
            due_date: Optional[Union[date, None]] = None,
            description: Optional[Union[str, Any]] = None,
            line_items: Optional[Union[List[Dict[str, Any]], None]] = None,
            tax: Optional[Union[List[Dict[str, Any]], None]] = None,
            currency: Optional[Union[Currency, Any]] = None,
            invoice_number: Optional[Union[int, Any]] = None,
            split_code: Optional[Union[str, Any]] = None,
    ) -> PayStackResponse:
        """
        Create a payment request for a transaction

        :param: customer: Customer ID of the customer
        :param: amount: Amount of the payment request
        :param: due_date: Due date of the payment request
        :param: description: Description of the payment request
        :param: line_items: Array of line items int the format [{"name":"item 1", "amount":2000, "quantity": 1}]
        :param: tax: Array of tax int the format [{"name":"VAT", "amount":200}]
        :param: currency: Currency of the payment request
        :param: send_notification: Set true if you want to send a notification to the customer email
        :param: draft: Set true if you want to create a draft payment request
        :param: has_invoice: Set true if you want to create a draft payment request
        :param: invoice_number: Invoice number of the payment request
        :param: split_code: split code of the transaction split

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        # convert date and bool to string
        due_date = self._convert_to_string(due_date)

        data = {
            "customer": customer,
            "amount": amount,
            "due_date": due_date,
            "description": description,
            "line_items": line_items,
            "tax": tax,
            "currency": currency,
            "send_notification": send_notification,
            "draft": draft,
            "has_invoice": has_invoice,
            "invoice_number": invoice_number,
            "split_code": split_code,
        }
        return await self._post_request("/paymentrequest", data=data)

    async def list_payment_requests(
            self,
            per_page: Optional[Union[int, None]] = 50,
            page: Optional[Union[int, None]] = 1,
            customer: Optional[Union[str, None]] = None,
            status: Optional[Union[PayMentRequestStatus, None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            include_archive: Optional[Union[bool, None]] = True,
            from_date: Optional[Union[date, None]] = None,
            to_date: Optional[Union[date, None]] = None,
    ) -> PayStackResponse:
        """
        List all the payment requests

        :param: per_page: Number of records to return
        :param: page:  number to return
        :param: customer: Filter by customer ID
        :param: status: Filter by payment request status
        :param: currency:
        :param: include_archive: Show archived payment requests
        :param: from_date: A timestamp from which to get payment requests {2016-09-24T00:00:05.000Z, 2016-09-21}
        :param: to_date: A timestamp from which to get payment requests {2016-09-24T00:00:05.000Z, 2016-09-21}

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)
        include_archive = self._convert_to_string(include_archive)

        params = {
            "perPage": per_page,
            "page": page,
            "customer": customer,
            "status": status,
            "currency": currency,
            "include_archive": include_archive,
            "from": from_date,
            "to": to_date,
        }
        return await self._get_request("/paymentrequest", params=params)

    async def fetch_payment_request(self, id_or_code: str) -> PayStackResponse:
        """
        Get details of a payment request on your integration

        :param: id_or_code: ID or Code of the payment request

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"/paymentrequest/{id_or_code}")

    async def verify_payment_request(self, code: str) -> PayStackResponse:
        """
        Verify details of a payment request on your integration

        :param: code: Payment request code

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request(f"/paymentrequest/verify/{code}")

    async def send_notification(self, code: str) -> PayStackResponse:
        """
        Send notification of a payment request to a customer

        :param: code: Payment request code

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._post_request(f"/paymentrequest/notify/{code}")

    async def payment_request_total(self) -> PayStackResponse:
        """
        Get total of a payment request metric

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._get_request("/paymentrequest/totals")

    async def finalize_payment_request(self, code: str, send_notification: bool) -> PayStackResponse:
        """
        Finalize a draft payment request

        :param: code: Payment request code
        :param: send_notification: Set true if you want to send a notification to the customer email

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        data = {"send_notification": send_notification}
        return await self._post_request(f"/paymentrequest/finalize/{code}", data=data)

    async def update_payment_request(
            self,
            id_or_code: str,
            customer: Optional[Union[str, None]] = None,
            amount: Optional[Union[int, None]] = None,
            description: Optional[Union[str, None]] = None,
            line_items: Optional[Union[List[Dict[str, Any]], None]] = None,
            tax: Optional[Union[List[Dict[str, Any]], None]] = None,
            currency: Optional[Union[Currency, None]] = None,
            due_date: Optional[Union[date, None]] = None,
            send_notification: Optional[Union[bool, None]] = True,
            draft: Optional[Union[bool, None]] = True,
            invoice_number: Optional[Union[int, None]] = None,
            split_code: Optional[Union[str, None]] = None,
    ) -> PayStackResponse:
        """
        Update a payment request

        :param: id_or_code: ID or Code of the payment request
        :param: customer: Customer ID or code of the customer
        :param: amount: Amount of the payment request
        :param: due_date: Due date of the payment request
        :param: description: Description of the payment request
        :param: line_items: Array of line items int the format [{"name":"item 1", "amount":2000, "quantity": 1}]
        :param: tax: Array of tax int the format [{"name":"VAT", "amount":200}]
        :param: currency: Currency of the payment request
        :param: send_notification: Set true if you want to send a notification to the customer email
        :param: draft: Set true if you want to create a draft payment request
        :param: invoice_number: Invoice number of the payment request starts from 1 and autoincrement
        :param: split_code: split code of the transaction split

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """

        # convert date and bool to string
        due_date = self._convert_to_string(due_date)

        data = {
            "customer": customer,
            "amount": amount,
            "due_date": due_date,
            "description": description,
            "line_items": line_items,
            "tax": tax,
            "currency": currency,
            "send_notification": send_notification,
            "draft": draft,
            "invoice_number": invoice_number,
            "split_code": split_code,
        }
        return await self._put_request(f"/paymentrequest/{id_or_code}", data=data)

    async def archive_payment_request(self, code: str) -> PayStackResponse:
        """
        Archive a payment request

        :param: code: Payment request code

        :return: The PayStackResponse from the API
        :rtype: PayStackResponse object
        """
        return await self._post_request(f"/paymentrequest/archive/{code}")
