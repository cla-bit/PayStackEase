""" Wrapper classes for various Asynchronous Paystack API endpoints,
providing simplified access to functionality in Paystack
"""

from paystackease.apis.async_apis import (
    aapple_pay,
    abulk_charges,
    acharges,
    acustomers,
)
from paystackease.metadata.__version__ import __version__


class AsyncPayStackBase:
    """AsyncPayStackBase acts as a wrapper around various client APIs to
    interact with the PayStack API
    """

    VERSION = __version__

    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        self.apple_pay = aapple_pay.AsyncApplePayClientAPI()
        self.bulk_charges = abulk_charges.AsyncBulkChargesClientAPI()
        self.charges = acharges.AsyncChargesClientAPI()
        self.customers = acustomers.AsyncCustomerClientAPI()

    async def __aenter__(self):
        # await super().__aenter__()
        await self.apple_pay.__aenter__()
        await self.bulk_charges.__aenter__()
        await self.charges.__aenter__()
        await self.customers.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self.apple_pay.__aexit__(*args)
        await self.bulk_charges.__aexit__(*args)
        await self.charges.__aexit__(*args)
        await self.customers.__aexit__(*args)
