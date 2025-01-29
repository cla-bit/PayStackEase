"""
Module: _api_base.py
======================

BaseAPI serves as the base for creating client APIs to interact with the Paystack API
with methods for handling HTTP requests, authentication using a secret key,
constructing HTTP headers, joining URLs with the API base URL, and logging response information.
"""

from abc import ABC, abstractmethod
from typing import Union, Optional, Dict, List, Any

from paystackease.helpers.misc import make_paystack_http_headers
from paystackease.src.logger import CustomLogger
from paystackease.src._api_client_response import PayStackResponse
from paystackease.src._api_env import EnvConfig, EnvBase


# logger = logging.getLogger(__name__)

# secret_key: EnvBase = EnvConfig()


class BaseAPI(ABC):
    """Base Client API for Paystack API"""

    _VALID_HTTP_METHODS: set[str] = {"GET", "POST", "PUT", "DELETE"}

    # pylint: disable=too-few-public-methods
    def __init__(
            self,
            secret_key: EnvBase = EnvConfig(),
            logger: Optional[CustomLogger] = None
    ) -> None:

        self._logger = logger or CustomLogger().logger
        self._headers = make_paystack_http_headers(secret_key.secret_key())

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
