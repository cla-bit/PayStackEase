""" Wrapper classes for various Synchronous Paystack API endpoints,
providing simplified access to functionality in Paystack
"""

from paystackease.apis import (
    apple_pay,
    bulk_charges,
    charges,
    customers,
)
from paystackease.metadata.__version__ import __version__


class PayStackBase:
    """PayStackBase acts as a wrapper around various client APIs to
    interact with the PayStack API
    """

    VERSION = __version__

    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        self.apple_pay = apple_pay.ApplePayClientAPI()
        self.bulk_charges = bulk_charges.BulkChargesClientAPI()
        self.charges = charges.ChargesClientAPI()
        self.customers = customers.CustomerClientAPI()
