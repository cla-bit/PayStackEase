from datetime import date, time
from typing import Union

from paystackease.errors import TypeValueError
from ._tool_kit import Currency


def convert_to_subunit(amount: int, currency: Currency) -> int:
    """
    Convert a subunit amount to a base amount
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


def convert_to_string(value: Union[bool, date, time]) -> Union[str, int]:
    """
    Convert the type of value to a string
    :param value: The value to be converted

    :raise TypeError: if the value is not a supported type

    :return: The value as a string
    :rtype: str
    """
    if isinstance(value, bool):
        return str(value)
    elif isinstance(value, date):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(value, time):
        return value.second
    else:
        raise TypeValueError(f"Unsupported type: {type(value)}")
