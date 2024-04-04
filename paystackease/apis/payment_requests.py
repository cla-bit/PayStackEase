"""
Wrapper for Paystack Payment Requests API.

The Payment Requests API allows you manage requests for payment of goods and services.
"""
from requests import Response

from datetime import date
from typing import Optional, List, Dict, Any
from paystackease._base import PayStackBaseClientAPI
from paystackease.helpers.tool_kit import PayMentRequestStatus


class PaymentRequestClientAPI(PayStackBaseClientAPI):
    """
    Paystack Payment Request API
    Reference: https://paystack.com/docs/api/payment-request/
    """

    def create_payment_request(
            self,
            customer: str,
            amount: int,
            draft: bool,
            has_invoice: bool,
            send_notification: bool,
            due_date: Optional[date] = None,
            description: Optional[str] = None,
            line_items: Optional[List[Dict[str, Any]]] = None,
            tax: Optional[List[Dict[str, Any]]] = None,
            currency: Optional[str] = None,
            invoice_number: Optional[int] = None,
            split_code: Optional[str] = None,
    ) -> Response:
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
        :rtype: Response object
        """
        # convert date and bool to string
        due_date = self._convert_to_string(due_date)
        draft = self._convert_to_string(draft)
        has_invoice = self._convert_to_string(has_invoice)
        send_notification = self._convert_to_string(send_notification)

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
        return self._post_request("/paymentrequest", data=data)

    def list_payment_requests(
            self,
            per_page: Optional[int] = 50,
            page: Optional[int] = 1,
            customer: Optional[str] = None,
            status: Optional[PayMentRequestStatus] = None,
            currency: Optional[str] = None,
            include_archive: Optional[bool] = True,
            from_date: Optional[date] = None,
            to_date: Optional[date] = None,
    ) -> Response:
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
        :rtype: Response object
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
        return self._get_request("/paymentrequest", params=params)

    def fetch_payment_request(self, id_or_code: str) -> Response:
        """
        Get details of a payment request on your integration

        :param: id_or_code: ID or Code of the payment request

        :return: The response from the API
        :rtype: Response object
        """
        return self._get_request(f"/paymentrequest/{id_or_code}")

    def verify_payment_request(self, code: str) -> Response:
        """
        Verify details of a payment request on your integration

        :param: code: Payment request code

        :return: The response from the API
        :rtype: Response object
        """
        return self._get_request(f"/paymentrequest/verify/{code}")

    def send_notification(self, code: str) -> Response:
        """
        Send notification of a payment request to a customer

        :param: code: Payment request code

        :return: The response from the API
        :rtype: Response object
        """
        return self._post_request(f"/paymentrequest/notify/{code}")

    def payment_request_total(self) -> Response:
        """
        Get total of a payment request metric

        :return: The response from the API
        :rtype: Response object
        """
        return self._get_request("/paymentrequest/totals")

    def finalize_payment_request(self, code: str, send_notification: bool) -> Response:
        """
        Finalize a draft payment request

        :param: code: Payment request code
        :param: send_notification: Set true if you want to send a notification to the customer email

        :return: The response from the API
        :rtype: Response object
        """
        # convert to strings
        send_notification = self._convert_to_string(send_notification)

        data = {"send_notification": send_notification}
        return self._post_request(f"/paymentrequest/finalize/{code}", data=data)

    def update_payment_request(
            self,
            id_or_code: str,
            customer: Optional[str] = None,
            amount: Optional[int] = None,
            description: Optional[str] = None,
            line_items: Optional[List[Dict[str, Any]]] = None,
            tax: Optional[List[Dict[str, Any]]] = None,
            currency: Optional[str] = None,
            due_date: Optional[date] = None,
            send_notification: Optional[bool] = True,
            draft: Optional[bool] = True,
            invoice_number: Optional[int] = None,
            split_code: Optional[str] = None,
    ) -> Response:
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
        :rtype: Response object
        """

        # convert date and bool to string
        due_date = self._convert_to_string(due_date)
        draft = self._convert_to_string(draft)
        send_notification = self._convert_to_string(send_notification)

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
        return self._put_request(f"/paymentrequest/{id_or_code}", data=data)

    def archive_payment_request(self, code: str) -> Response:
        """
        Archive a payment request

        :param: code: Payment request code

        :return: The response from the API
        :rtype: Response object
        """
        return self._post_request(f"/paymentrequest/archive/{code}")
