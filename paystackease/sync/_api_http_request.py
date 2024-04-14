""" Paystackease HTTP request handler"""

from typing import Optional, Any, Union, List, Dict
from paystackease.sync._api_base import BaseClientAPI
from paystackease._api_http_response import Response


class PayStackBaseClientAPI(BaseClientAPI):
    """Requests methods to Paystack API"""

    def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], List[Any], None]] = None,
        params: Optional[Union[Dict[str, Any], None]] = None,
        **kwargs,
    ) -> Response:
        """
        Handles the request to Paystack API
        :param method:
        :param endpoint:
        :param data:
        :param params:
        :param kwargs:
        :return:
        """
        return self._request_url(method, endpoint, data=data, params=params, **kwargs)

    def _get_request(
        self,
        endpoint: str,
        params: Optional[Union[Dict[str, Any], None]] = None,
        **kwargs,
    ) -> Response:
        """
        Makes the GET request to Paystack API
        :param endpoint:
        :param params:
        :param kwargs:
        :return:
        """
        return self._request("GET", endpoint, params=params, **kwargs)

    def _post_request(
        self,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], List[Any], None]] = None,
        **kwargs,
    ) -> Response:
        """
        Makes the POST request to Paystack API
        :param endpoint:
        :param data:
        :param kwargs:
        :return:
        """
        return self._request("POST", endpoint, data=data, **kwargs)

    def _put_request(
        self,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], List[Any], None]] = None,
        **kwargs,
    ) -> Response:
        """
        Makes the PUT request to Paystack API
        :param endpoint:
        :param data:
        :param kwargs:
        :return:
        """
        return self._request("PUT", endpoint, data=data, **kwargs)

    def _delete_request(self, endpoint: str, **kwargs) -> Response:
        """
        Makes the DELETE request to Paystack API
        :param endpoint:
        :param kwargs:
        :return:
        """
        return self._request("DELETE", endpoint, **kwargs)
