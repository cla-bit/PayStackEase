"""Wrapper for both the async and sync api modules"""

from paystackease.apis.async_apis import (
    aapple_pay,
    abulk_charges,
    acharges,
    acustomers,
)

from paystackease.apis.sync_apis import (
    apple_pay,
    bulk_charges,
    charges,
    customers,
)
