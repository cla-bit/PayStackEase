""" Paystackease aioHTTP request handler"""

from typing import Optional, Union, Any, List, Dict
from paystackease.a_sync._api_base import AsyncBaseClientAPI
from paystackease._api_http_response import Response


class AsyncPayStackBaseClientAPI(AsyncBaseClientAPI):
    """Requests methods to Paystack API"""

    async def _request(
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
        return await self._request_url(
            method, endpoint, data=data, params=params, **kwargs
        )

    async def _get_request(
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
        return await self._request("GET", endpoint, params=params, **kwargs)

    async def _post_request(
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
        return await self._request("POST", endpoint, data=data, **kwargs)

    async def _put_request(
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
        return await self._request("PUT", endpoint, data=data, **kwargs)

    async def _delete_request(self, endpoint: str, **kwargs) -> Response:
        """
        Makes the DELETE request to Paystack API
        :param endpoint:
        :param kwargs:
        :return:
        """
        return await self._request("DELETE", endpoint, **kwargs)
