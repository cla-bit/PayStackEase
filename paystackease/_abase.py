"""
Async Base client API for Paystack API with methods for handling asynchronous AIOHTTP requests,
authentication using a secret key,
constructing HTTP headers, joining URLs with the API base URL, and logging response information.
"""

import json
import logging

from datetime import date, datetime
from typing import Union, Optional, Dict, List, Any
from urllib.parse import urljoin
from decouple import config

import aiohttp
from paystackease._utils import Response

from paystackease.errors import (
    SecretKeyError,
    TypeValueError,
    InvalidRequestMethodError,
    PayStackError,
)


logger = logging.getLogger(__name__)

PAYSTACK_SECRET_KEY = config("PAYSTACK_SECRET_KEY")


class AsyncBaseClientAPI:
    """Base Client API for Paystack API"""

    _PAYSTACK_API_URL: str = "https://api.paystack.co/"
    _VALID_HTTP_METHODS: set[str] = {"GET", "POST", "PUT", "DELETE"}

    # pylint: disable=too-few-public-methods
    def __init__(self, secret_key: str = None) -> None:
        self._secret_key = secret_key

        # Default to PAYSTACK_SECRET_KEY if not provided in the instance
        if not self._secret_key:
            self._secret_key = PAYSTACK_SECRET_KEY  # or environment variables

        # Raise an error if PAYSTACK_SECRET_KEY is not set in the instance or environment variables
        if not self._secret_key:
            logger.error(
                "Please provide a secret key or set the environment variable PAYSTACK_SECRET_KEY"
            )
            raise SecretKeyError(
                "Please provide a secret key or set the environment variable PAYSTACK_SECRET_KEY"
            )

        self.timeout = aiohttp.ClientTimeout(total=30)

        self._session = aiohttp.ClientSession(
            headers=self._make_paystack_http_headers(),
            timeout=self.timeout
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if not self._session.closed:
            await self._session.close()

    @classmethod
    def _set_secret_key(cls, secret_key: str) -> None:
        """Set the secret key for all instances of this class"""
        cls._secret_key = secret_key

    def _join_url(self, path: str) -> str:
        """
        Join URL with Paystack API URL
        :param path:
        :return:
        """
        if path.startswith("/"):
            path = path[1:]
        return urljoin(self._PAYSTACK_API_URL, path)

    def _make_paystack_http_headers(self) -> dict:
        """
        Make Paystack HTTP Headers
        :return:
        """
        return {
            "Authorization": f"Bearer {self._secret_key}",
            "content-type": "application/json",
        }

    @staticmethod
    def _convert_to_string(value: Union[bool, date, datetime, None]) -> Union[str, int, None]:
        """
        Convert the type of value to a string
        :param value: The value to be converted

        :raise TypeError: if the value is not a supported type

        :return: The value as a string
        :rtype: str
        """
        # each supported type is mapped to its corresponding conversion function
        conversion_functions = {
            bool: lambda val: str(val),
            date: lambda val: val.strftime("%Y-%m-%d"),
            datetime: lambda val: val.strftime("%Y-%m-%d %H:%M:%S"),  # Added a datetime
        }

        if value is None:
            return None
        if type(value) in conversion_functions:
            return conversion_functions[type(value)](value)
        logger.error("Unsupported type: %s Expected type -bool, -date, -datetime", {type(value)})
        raise TypeValueError(
            f"Unsupported type: {type(value)}. Expected type -bool, -date, -datetime"
        )

    async def _request_url(
        self, method: str, url: str, data: Optional[Union[Dict[str, Any], List[Any], None]] = None, params: Optional[Union[Dict[str, Any], None]] = None, **kwargs
    ) -> Response:
        """
        Handles the request to Paystack API
        :param method:
        :param url:
        :param data:
        :param params:
        :param kwargs:
        :return:
        """
        if method.upper() not in self._VALID_HTTP_METHODS:
            logger.error(
                "Invalid HTTP method. Supported methods are GET, POST, PUT, DELETE. : %s",
                {method},
            )
            raise InvalidRequestMethodError(
                f"Invalid HTTP method. Supported methods are GET, POST, PUT, DELETE. : {method}"
            )

        url = self._join_url(url)
        # Filtering params and data, then converting data to JSON
        params = (
            {key: value for key, value in params.items() if value is not None}
            if params
            else None
        )
        data = json.dumps(data) if data else None
        
        try:
            async with self._session.request(
                method, url=url, data=data, params=params, **kwargs,
            ) as response:
                response_json = await response.json()
                logger.info("Response Status Code: %s", response.status)
                logger.info("Response JSON: %s", response_json)
                return response_json
        except aiohttp.ClientError as error:
            # Extract status code if available from the exception
            status_code = getattr(error, 'response', None) and getattr(error.args[0], 'status_code', None)
            logger.error("Error: %s", error)
            raise PayStackError(f"Error making request to Paystack API: {str(error)}", status_code) from error


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

    async def _get_request(self, endpoint: str, params: Optional[Union[Dict[str, Any], None]] = None, **kwargs) -> Response:
        """
        Makes the GET request to Paystack API
        :param endpoint:
        :param params:
        :param kwargs:
        :return:
        """
        return await self._request("GET", endpoint, params=params, **kwargs)

    async def _post_request(self, endpoint: str, data: Optional[Union[Dict[str, Any], List[Any], None]] = None, **kwargs) -> Response:
        """
        Makes the POST request to Paystack API
        :param endpoint:
        :param data:
        :param kwargs:
        :return:
        """
        return await self._request("POST", endpoint, data=data, **kwargs)

    async def _put_request(self, endpoint: str, data: Optional[Union[Dict[str, Any], List[Any], None]] = None, **kwargs) -> Response:
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
