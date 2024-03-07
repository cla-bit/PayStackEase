"""
Base client API for Paystack API with methods for handling HTTP requests, authentication using a secret key,
constructing HTTP headers, joining URLs with the API base URL, and logging response information.
"""

import json
import logging
from datetime import time, date
from typing import Union

from urllib.parse import urljoin
from decouple import config

import requests

logger = logging.getLogger(__name__)

PAYSTACK_SECRET_KEY = config("PAYSTACK_SECRET_KEY")


class BaseClientAPI:
    """Base Client API for Paystack API"""

    _PAYSTACK_API_URL = "https://api.paystack.co/"
    _VALID_HTTP_METHODS = {"GET", "POST", "PUT", "DELETE"}

    # pylint: disable=too-few-public-methods
    def __init__(self, secret_key: str = None) -> None:
        self._secret_key = secret_key

        # Default to PAYSTACK_SECRET_KEY if not provided in the instance
        if not self._secret_key:
            self._secret_key = PAYSTACK_SECRET_KEY  # or environment variables

        # Raise an error if PAYSTACK_SECRET_KEY is not set in the instance or environment variables
        if not self._secret_key:
            logger.error("Please provide a secret key")
            raise ValueError("Please provide a secret key")

        self._session = requests.Session()

        self._headers = self._make_paystack_http_headers()

    @classmethod
    def _set_secret_key(cls, secret_key: str) -> None:
        """Set the secret key for all instances of this class"""
        cls._secret_key = secret_key

    def _join_url(self, path) -> str:
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
    def _convert_to_string(
        value: Union[bool, date, time, None]
    ) -> Union[str, int, None]:
        """
        Convert the type of value to a string
        :param value: The value to be converted

        :raise TypeError: if the value is not a supported type

        :return: The value as a string
        :rtype: str
        """
        # each supported type is mapped to its corresponding conversion function
        conversion_functions = {
            bool: lambda val: str(val).lower(),
            date: lambda val: val.strftime("%Y-%m-%d %H:%M:%S"),
        }

        if value is None:
            return None
        if type(value) in conversion_functions:
            return conversion_functions[type(value)](value)
        logger.error(f"Unsupported type: %s. Expected type -bool, -date", {type(value)})
        raise TypeError(f"Unsupported type: {type(value)}")

    def _request_url(
        self, method: str, url: str, data: dict = None, params: dict = None, **kwargs
    ) -> dict:
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
                f"Invalid HTTP method. Supported methods are GET, POST, PUT, DELETE. : %s", {method}
            )
            raise ValueError(
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
            with self._session.request(
                method,
                url=url,
                headers=self._headers,
                data=data,
                params=params,
                **kwargs,
                timeout=30,
            ) as response:
                logger.info("Response Status Code: %s", response.status_code)
                logger.info("Response JSON: %s", response.json())
                return response.json()
        except requests.RequestException as error:
            logger.error("Error %s", error)
            raise


class PayStackBaseClientAPI(BaseClientAPI):
    """Requests methods to Paystack API"""

    def _request(
        self,
        method: str,
        endpoint: str,
        data: dict = None,
        params: dict = None,
        **kwargs,
    ) -> dict:
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

    def _get_request(self, endpoint: str, params: dict = None, **kwargs) -> dict:
        """
        Makes the GET request to Paystack API
        :param endpoint:
        :param params:
        :param kwargs:
        :return:
        """
        return self._request("GET", endpoint, params=params, **kwargs)

    def _post_request(self, endpoint: str, data: dict = None, **kwargs) -> dict:
        """
        Makes the POST request to Paystack API
        :param endpoint:
        :param data:
        :param kwargs:
        :return:
        """
        return self._request("POST", endpoint, data=data, **kwargs)

    def _put_request(self, endpoint: str, data: dict = None, **kwargs) -> dict:
        """
        Makes the PUT request to Paystack API
        :param endpoint:
        :param data:
        :param kwargs:
        :return:
        """
        return self._request("PUT", endpoint, data=data, **kwargs)

    def _delete_request(self, endpoint: str, **kwargs) -> dict:
        """
        Makes the DELETE request to Paystack API
        :param endpoint:
        :param kwargs:
        :return:
        """
        return self._request("DELETE", endpoint, **kwargs)

