"""
Module: _api_base_client.py
==============================

This defines classes SyncBaseClientAPI and AsyncBaseClientAPI which are used for making
synchronous and asynchronous requests to the Paystack API, respectively.
"""

import json

from typing import Union, Dict, List, Any, Optional

from aiohttp import (
    ClientSession, ClientTimeout, ClientError, ClientConnectionError
)
from requests import (
    Session, RequestException, ConnectionError
)

from paystackease.src._api_base import BaseAPI
from paystackease.src._api_client_response import PayStackResponse
from paystackease.src._api_errors import (
    InvalidRequestMethodError, PayStackError, APIConnectionError, PayStackServerError
)
from paystackease.helpers.misc import join_url


class SyncBaseClientAPI(BaseAPI):

    # pylint: disable=too-few-public-methods
    def __init__(self, session: Optional[Session] = None) -> None:
        super().__init__()
        self._session = session or Session()

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
        if method.upper() not in self._VALID_HTTP_METHODS:
            error_message = f"Invalid HTTP method. Supported methods are GET, POST, PUT, DELETE. : {method}"
            self._logger.error(error_message)
            raise InvalidRequestMethodError(error_message)

        url = join_url(url)

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
                response_data = response.json()
                self._logger.info("Response Status Code: %s", response.status_code)
                self._logger.info("Response JSON: %s", response_data)

                # Handle server error
                if 500 <= response.status_code <= 600:
                    error_message = f"Server error occurred: {response.status_code}"
                    self._logger.error(error_message)
                    raise PayStackServerError(message=error_message, status_code=response.status_code)

                return PayStackResponse(
                    status_code=response.status_code,
                    status=response_data.get('status', False),
                    message=response_data.get('message', ''),
                    data=response_data.get('data', None),
                )
        except (RequestException, ConnectionError) as error:
            # Extract status code if available from the exception
            error_message = str(error)
            status_code = getattr(error, "response", None) and getattr(
                error.response, "status_code", None
            )
            self._logger.error("Error %s", error)
            if isinstance(error, ConnectionError):
                raise APIConnectionError(message=error_message)
            raise PayStackError(message=error_message, status_code=status_code) from error


class AsyncBaseClientAPI(BaseAPI):
    """Base Client API for Paystack API"""

    # pylint: disable=too-few-public-methods
    def __init__(self, session: Optional[ClientSession] = None, timeout: Optional[ClientTimeout] = None) -> None:
        super().__init__()

        self.timeout = timeout or ClientTimeout(total=30)
        self._session = session or ClientSession(
            headers=self._headers, timeout=self.timeout
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if not self._session.closed:
            await self._session.close()

    async def _request_url(
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
        if method.upper() not in self._VALID_HTTP_METHODS:
            error_message = f"Invalid HTTP method. '{method}'. Supported methods are GET, POST, PUT, DELETE."
            self._logger.error(error_message)
            raise InvalidRequestMethodError(error_message)

        url = join_url(url)
        # Filtering params and data, then converting data to JSON
        params = (
            {key: value for key, value in params.items() if value is not None}
            if params
            else None
        )
        data = json.dumps(data) if data else None

        try:
            async with self._session.request(
                method,
                url=url,
                data=data,
                params=params,
                **kwargs,
            ) as response:
                response_data = await response.json()
                self._logger.info("Response Status Code: %s", response.status)
                self._logger.info("Response JSON: %s", response_data)

                # Handle server error
                if 500 <= response.status <= 600:
                    error_message = f"Server error occurred: {response.status}"
                    self._logger.error(error_message)
                    raise PayStackServerError(message=error_message, status_code=response.status)

                return PayStackResponse(
                    status_code=response.status,
                    status=response_data.get('status', False),
                    message=response_data.get('message', ''),
                    data=response_data.get('data', None),
                )
        except (ClientError, ClientConnectionError) as error:
            # Extract status code if available from the exception
            error_message = str(error)
            status_code = getattr(error, "response", None) and getattr(
                error.args[0], "status_code", None
            )
            self._logger.error("Error %s", error)
            if isinstance(error, ClientConnectionError):
                raise APIConnectionError(message=error_message)
            raise PayStackError(message=error_message, status_code=status_code) from error
