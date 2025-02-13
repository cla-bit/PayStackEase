"""
Module: misc.py
==================

This module contains various utility functions that are used across the application to
simplify common tasks, such as url path build-up, data manipulation, string formatting, date handling,
validation, and other helper functions.

Each function in this module is designed to encapsulate a specific task, making the codebase more modular,
reusable, and easier to maintain.
"""

from typing import Union
from datetime import date, datetime
from urllib.parse import urljoin

from paystackease.src._api_errors import TypeValueError
from paystackease.helpers.constants import PAYSTACK_API_URL, Currency


def join_url(path: str) -> str:
    """
    Join URL with Paystack API URL
    :param path:
    :return:
    """
    if path.startswith("/"):
        path = path[1:]
    return urljoin(PAYSTACK_API_URL, path)


def make_paystack_http_headers(secret_key: str) -> dict:
    """
    Make Paystack HTTP Headers
    :return:
    """
    return {
        "Authorization": f"Bearer {secret_key}",
        "content-type": "application/json",
    }


def convert_to_string(value: Union[bool, date, datetime, None]) -> Union[str, int, None]:
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
    raise TypeValueError(error_message)


def convert_to_subunit(amount: int, currency: Union[Currency, None] = Currency.NGN) -> int:
    """
    Convert a subunit amount to a base amount in NGN, GHS, USD, ZAR and KES
    :param amount:
    :param currency:
    :return:
    """
    subunit_multipliers = {
        currency.NGN: 100,
        currency.GHS: 100,
        currency.USD: 100,
        currency.ZAR: 100,
        currency.KES: 100,
    }
    subunit_multiplier = subunit_multipliers.get(currency)
    if not subunit_multiplier:
        raise ValueError(f"Invalid currency: {currency}")
    amount = amount * subunit_multiplier
    return amount
