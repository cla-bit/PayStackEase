"""
This holds function to convert to subunits in NGN, GHS, USD, ZAR and KES
"""
from typing import Union
from paystackease.helpers.tool_kit import Currency


def convert_to_subunit(amount: int, currency: Union[Currency, None] = Currency.NGN) -> int:
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
