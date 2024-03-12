"""
Wrapper for Asynchronous Paystack Payment Requests API.

The Payment Requests API allows you manage requests for payment of goods and services.
"""

from datetime import date
from typing import Optional, List, Dict
from paystackease.abase import AsyncPayStackBaseClientAPI


class AsyncPaymentRequestClientAPI(AsyncPayStackBaseClientAPI):
    """
    Paystack Payment Request API
    Reference: https://paystack.com/docs/api/payment-request/
    """

    async def create_payment_request(
            self,
            customer: str,
            amount: int,
            draft: bool,
            has_invoice: bool,
            send_notification: bool,
            due_date: Optional[date] = None,
            description: Optional[str] = None,
            line_items: Optional[List[Dict[str, str]]] = None,
            tax: Optional[List[Dict[str, str]]] = None,
            currency: Optional[str] = None,
            invoice_number: Optional[int] = None,
            split_code: Optional[str] = None,
    ) -> dict:
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

        :return: The response from the API
        :rtype: dict
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
            per_page: Optional[int] = None,
            page: Optional[int] = None,
            customer: Optional[str] = None,
            status: Optional[str] = None,
            currency: Optional[str] = None,
            include_archive: Optional[str] = None,
            from_date: Optional[date] = None,
            to_date: Optional[date] = None,
    ) -> dict:
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

        :return: The response from the API
        :rtype: dict
        """

        # convert date to string
        from_date = self._convert_to_string(from_date)
        to_date = self._convert_to_string(to_date)

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

    async def fetch_payment_request(self, id_or_code: str) -> dict:
        """
        Get details of a payment request on your integration

        :param: id_or_code: ID or Code of the payment request

        :return: The response from the API
        :rtype: dict
        """
        return await self._get_request(f"/paymentrequest/{id_or_code}")

    async def verify_payment_request(self, code: str) -> dict:
        """
        Verify details of a payment request on your integration

        :param: code: Payment request code

        :return: The response from the API
        :rtype: dict
        """
        return await self._get_request(f"/paymentrequest/verify/{code}")

    async def send_notification(self, code: str) -> dict:
        """
        Send notification of a payment request to a customer

        :param: code: Payment request code

        :return: The response from the API
        :rtype: dict
        """
        return await self._post_request(f"/paymentrequest/notify/{code}")

    async def payment_request_total(self) -> dict:
        """
        Get total of a payment request metric

        :return: The response from the API
        :rtype: dict
        """
        return await self._get_request("/paymentrequest/totals")

    async def finalize_payment_request(self, code: str, send_notification: bool) -> dict:
        """
        Finalize a draft payment request

        :param: code: Payment request code
        :param: send_notification: Set true if you want to send a notification to the customer email

        :return: The response from the API
        :rtype: dict
        """
        data = {"send_notification": send_notification}
        return await self._post_request(f"/paymentrequest/finalize/{code}", data=data)

    async def update_payment_request(
            self,
            id_or_code: str,
            customer: Optional[str] = None,
            amount: Optional[int] = None,
            description: Optional[str] = None,
            line_items: Optional[List[Dict[str, str]]] = None,
            tax: Optional[List[Dict[str, str]]] = None,
            currency: Optional[str] = None,
            due_date: Optional[date] = None,
            send_notification: Optional[bool] = None,
            draft: Optional[bool] = None,
            invoice_number: Optional[int] = None,
            split_code: Optional[str] = None,
    ) -> dict:
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

        :return: The response from the API
        :rtype: dict
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

    async def archive_payment_request(self, code: str) -> dict:
        """
        Archive a payment request

        :param: code: Payment request code

        :return: The response from the API
        :rtype: dict
        """
        return await self._post_request(f"/paymentrequest/archive/{code}")
