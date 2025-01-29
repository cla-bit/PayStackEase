"""
Module: _api_env.py
========================

This module retrieves the environment variables
"""

from decouple import config
from typing import Protocol

from paystackease.src.logger import CustomLogger
from paystackease.src._api_errors import SecretKeyError


logger = CustomLogger().logger


class EnvBase(Protocol):
    """
    Base class for environment variables
    """
    def secret_key(self) -> str:
        """
        Retrieves the secret key

        Returns:
            str: The secret key
        """


class EnvConfig(EnvBase):
    """
    Config object for the environment
    """
    @classmethod
    def secret_key(cls):
        secret_key = config("PAYSTACK_SECRET_KEY")
        if not secret_key:
            error_message = "Please provide a secret key or set the environment variable PAYSTACK_SECRET_KEY"
            logger.error(error_message)
            raise SecretKeyError(error_message)
        return secret_key
