"""
BaseAPI serves as the base for creating client APIs to interact with the Paystack API
with methods for handling HTTP requests, authentication using a secret key,
constructing HTTP headers, joining URLs with the API base URL, and logging response information.
"""

import logging
from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import Union, Optional, Dict, List, Any
from urllib.parse import urljoin

from paystackease.core._api_client_response import PayStackResponse

from paystackease.core._api_errors import TypeValueError
from paystackease.core._api_env import EnvConfig, EnvBase


logger = logging.getLogger(__name__)


class BaseAPI(ABC):
    """Base Client API for Paystack API"""

    _PAYSTACK_API_URL: str = "https://api.paystack.co/"
    _VALID_HTTP_METHODS: set[str] = {"GET", "POST", "PUT", "DELETE"}

    # pylint: disable=too-few-public-methods
    def __init__(self, secret_key: EnvBase = EnvConfig()) -> None:
        self._secret_key = secret_key
        self._headers = self._make_paystack_http_headers()

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
            "Authorization": f"Bearer {self._secret_key.secret_key()}",
            "content-type": "application/json",
        }

    @staticmethod
    def _convert_to_string(
            value: Union[bool, date, datetime, None]
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
            date: lambda val: val.strftime("%Y-%m-%d"),
            datetime: lambda val: val.strftime("%Y-%m-%d %H:%M:%S"),  # Added a datetime
        }

        if value is None:
            return None
        if type(value) in conversion_functions:
            return conversion_functions[type(value)](value)
        error_message = f"Unsupported type: {type(value)}. Expected type -bool, -date, -datetime"
        logger.error(error_message)
        raise TypeValueError(error_message)

    @abstractmethod
    def _request_url(
        self,
        method: str,
        url: str,
        data: Optional[Union[Dict[str, Any], List[Any], None]] = None,
        params: Optional[Union[Dict[str, Any], None]] = None,
        **kwargs,
    ) -> PayStackResponse:
        """
        Handles the request to Paystack API
        :param method:
        :param url:
        :param data:
        :param params:
        :param kwargs:
        :return:
        """
        pass
