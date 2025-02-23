"""
Module: misc.py
==================

This module contains various utility functions that are used across the application to
simplify common tasks, such as url path build-up, data manipulation, string formatting, date handling,
validation, and other helper functions.

Each function in this module is designed to encapsulate a specific task, making the codebase more modular,
reusable, and easier to maintain.
"""

from typing import Union, Dict
from datetime import date, datetime
from urllib.parse import urljoin

from paystackease.src._api_errors import TypeValueError
from paystackease.helpers.constants import PAYSTACK_API_URL, Currency


def join_url(path: str) -> str:
    """
    Joins a given path with the Paystack API base URL.

    Parameters:
        path (str): The path to be joined with the Paystack API URL.

    Returns:
        str: The full URL formed by joining the base URL with the provided path.
    """

    if path.startswith("/"):
        path = path[1:]
    return urljoin(PAYSTACK_API_URL, path)


def make_paystack_http_headers(secret_key: str) -> Dict[str, str]:
    """
    Creates HTTP headers for Paystack API requests.

    Parameters:
        secret_key (str): The secret key used for authorization.

    Returns:
        Dict[str, str]: A dictionary containing the HTTP headers.
    """

    return {
        "Authorization": f"Bearer {secret_key}",
        "content-type": "application/json",
    }


def convert_to_string(value: Union[bool, date, datetime, None]) -> Union[str, int, None]:
    """
    Converts the given value to a string.

    This function supports converting boolean, date, and datetime values to their string representations.
    If the value is None, it returns None. If the value is not a supported type, it raises a TypeError.

    Parameters:
        value (Union[bool, date, datetime, None]): The value to be converted.

    Raises:
        TypeError: If the value is not a supported type.

    Returns:
        Union[str, int, None]: The value as a string, or None if the value is None.
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
    Converts an amount to its subunit value based on the specified currency.

    This function multiplies the given amount by the subunit multiplier for the specified currency.
    Supported currencies are NGN, GHS, USD, ZAR, and KES.

    Parameters:
        amount (int): The amount to be converted.
        currency (Union[Currency, None]): The currency of the amount. Defaults to Currency.NGN.

    Raises:
        ValueError: If the currency is not supported.

    Returns:
        int: The amount converted to its subunit value.
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
