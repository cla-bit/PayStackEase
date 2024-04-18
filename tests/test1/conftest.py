""" Fixtures for testing purposes """

import pytest
import pytest_asyncio
from aioresponses import aioresponses
from paystackease.core._api_base import BaseAPI
from paystackease.core._api_base_client import AsyncBaseClientAPI, SyncBaseClientAPI
from paystackease.core._api_client_requests import AsyncRequestAPI, SyncRequestAPI
from paystackease.apis.sync_apis import (
    apple_pay,
    bulk_charges,
    charges,
    customers,
    dedicated_virtual_accounts,
    disputes,
    integration,
    miscellaneous,
    payment_pages,
    payment_requests,
    plans,
    products,
    refund,
    settlements,
    subaccounts,
    subscriptions,
    terminal,
    transaction_splits,
    transactions,
    transfer_recipients,
    transfers,
    transfers_control,
    verification,
)
from paystackease.apis.async_apis import (
    aapple_pay,
    abulk_charges,
    acharges,
    acustomers,
    adedicated_virtual_accounts,
    adisputes,
    aintegration,
    amiscellaneous,
    apayment_pages,
    apayment_requests,
    aplans,
    aproducts,
    arefund,
    asettlements,
    asubaccounts,
    asubscriptions,
    aterminal,
    atransaction_splits,
    atransactions,
    atransfer_recipients,
    atransfers,
    atransfers_control,
    averification,
)


@pytest.fixture
def base_client():
    """ Base client fixture"""
    return BaseAPI(secret_key="sk_secret_key")
