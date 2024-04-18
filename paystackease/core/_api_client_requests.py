"""
Paystackease HTTP requests and aiohttp handlers This aims to simplify the process of making requests
to the Paystack API by providing higher-level methods for different HTTP methods,
"""

from typing import Optional, Any, Union, List, Dict

from paystackease.core._api_base_client import SyncBaseClientAPI, AsyncBaseClientAPI
from paystackease.core._api_client_response import PayStackResponse


class SyncRequestAPI(SyncBaseClientAPI):
    """Requests methods to Paystack API"""

    def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], List[Any], None]] = None,
        params: Optional[Union[Dict[str, Any], None]] = None,
        **kwargs,
    ) -> PayStackResponse:
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
    ) -> PayStackResponse:
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
    ) -> PayStackResponse:
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
    ) -> PayStackResponse:
        """
        Makes the PUT request to Paystack API
        :param endpoint:
        :param data:
        :param kwargs:
        :return:
        """
        return self._request("PUT", endpoint, data=data, **kwargs)

    def _delete_request(self, endpoint: str, **kwargs) -> PayStackResponse:
        """
        Makes the DELETE request to Paystack API
        :param endpoint:
        :param kwargs:
        :return:
        """
        return self._request("DELETE", endpoint, **kwargs)


class AsyncRequestAPI(AsyncBaseClientAPI):
    """Requests methods to Paystack API"""

    async def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], List[Any], None]] = None,
        params: Optional[Union[Dict[str, Any], None]] = None,
        **kwargs,
    ) -> PayStackResponse:
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
    ) -> PayStackResponse:
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
    ) -> PayStackResponse:
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
    ) -> PayStackResponse:
        """
        Makes the PUT request to Paystack API
        :param endpoint:
        :param data:
        :param kwargs:
        :return:
        """
        return await self._request("PUT", endpoint, data=data, **kwargs)

    async def _delete_request(self, endpoint: str, **kwargs) -> PayStackResponse:
        """
        Makes the DELETE request to Paystack API
        :param endpoint:
        :param kwargs:
        :return:
        """
        return await self._request("DELETE", endpoint, **kwargs)
