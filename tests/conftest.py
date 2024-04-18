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


@pytest_asyncio.fixture
async def async_base_client():
    """ Async base client fixture"""
    async with AsyncBaseClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_paystack_base_client():
    """ Paystack async request client fixture"""
    async with AsyncPayStackBaseClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_apple_pay_client():
    """ Apple pay client fixture"""
    async with aapple_pay.AsyncApplePayClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_bulk_charges_client():
    """ Bulk Charges client fixture"""
    async with abulk_charges.AsyncBulkChargesClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_charges_client():
    """ Charges client fixture"""
    async with acharges.AsyncChargesClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_customers_client():
    """ Charges client fixture"""
    async with acustomers.AsyncCustomerClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_dva_client():
    """ Charges client fixture"""
    async with adedicated_virtual_accounts.AsyncDedicatedVirtualAccountClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_disputes_client():
    """ Disputes client fixture"""
    async with adisputes.AsyncDisputesClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_integration_client():
    """ Integration client fixture"""
    async with aintegration.AsyncIntegrationClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_miscellaneous_client():
    """ Miscellaneous client fixture"""
    async with amiscellaneous.AsyncMiscellaneousClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_payment_pages_client():
    """ Payment pages client fixture"""
    async with apayment_pages.AsyncPaymentPagesClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_payment_requests_client():
    """ Payment requests client fixture"""
    async with apayment_requests.AsyncPaymentRequestClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_plans_client():
    """ Plans client fixture"""
    async with aplans.AsyncPlanClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_products_client():
    """ Products client fixture"""
    async with aproducts.AsyncProductClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_refund_client():
    """ Refund client fixture"""
    async with arefund.AsyncRefundClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_settlements_client():
    """ Settlements client fixture"""
    async with asettlements.AsyncSettlementClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_subaccounts_client():
    """ Subaccounts client fixture"""
    async with asubaccounts.AsyncSubAccountClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_subscriptions_client():
    """ Subscriptions client fixture"""
    async with asubscriptions.AsyncSubscriptionClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_terminal_client():
    """ Terminal client fixture"""
    async with aterminal.AsyncTerminalClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_transaction_splits_client():
    """ Transaction splits client fixture"""
    async with atransaction_splits.AsyncTransactionSplitClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_transactions_client():
    """ Transactions client fixture"""
    async with atransactions.AsyncTransactionClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_transfer_recipients_client():
    """ Transfer recipients client fixture"""
    async with atransfer_recipients.AsyncTransferRecipientsClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_transfers_client():
    """ Transfers client fixture"""
    async with atransfers.AsyncTransfersClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_transfers_control_client():
    """ Transfers control client fixture"""
    async with atransfers_control.AsyncTransferControlClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def async_verification_client():
    """ Verification client fixture"""
    async with averification.AsyncVerificationClientAPI(secret_key="sk_secret_key") as client:
        yield client


@pytest_asyncio.fixture
async def mocked_responses():
    """ Mocked responses fixture"""
    with aioresponses() as mocked:
        yield mocked


@pytest.fixture
def base_client():
    """ Base client fixture"""
    return BaseClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def paystack_request_client():
    """ Paystack request client fixture"""
    return PayStackBaseClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def apple_pay_client():
    """ Apple pay client fixture"""
    return apple_pay.ApplePayClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def bulk_charges_client():
    """ Bulk Charges client fixture"""
    return bulk_charges.BulkChargesClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def charges_client():
    """ Bulk Charges client fixture"""
    return charges.ChargesClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def customers_client():
    """ Customers client fixture"""
    return customers.CustomerClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def dva_client():
    """ Customers client fixture"""
    return dedicated_virtual_accounts.DedicatedVirtualAccountClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def disputes_client():
    """ Disputes client fixture"""
    return disputes.DisputesClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def integration_client():
    """ Integration client fixture"""
    return integration.IntegrationClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def miscellaneous_client():
    """ Integration client fixture"""
    return miscellaneous.MiscellaneousClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def payment_pages_client():
    """ Payment pages client fixture"""
    return payment_pages.PaymentPagesClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def payment_requests_client():
    """ Payment requests client fixture"""
    return payment_requests.PaymentRequestClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def plans_client():
    """ Plans client fixture"""
    return plans.PlanClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def products_client():
    """ Products client fixture"""
    return products.ProductClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def refund_client():
    """ Refund client fixture"""
    return refund.RefundClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def settlements_client():
    """ Settlements client fixture"""
    return settlements.SettlementClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def subaccounts_client():
    """ Subaccounts client fixture"""
    return subaccounts.SubAccountClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def subscriptions_client():
    """ Subscriptions client fixture"""
    return subscriptions.SubscriptionClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def terminal_client():
    """ Terminal client fixture"""
    return terminal.TerminalClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def transaction_splits_client():
    """ Transaction splits client fixture"""
    return transaction_splits.TransactionSplitClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def transactions_client():
    """ Transactions client fixture"""
    return transactions.TransactionClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def transfer_recipients_client():
    """ Transfer recipients client fixture"""
    return transfer_recipients.TransferRecipientsClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def transfers_client():
    """ Transfers client fixture"""
    return transfers.TransfersClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def transfers_control_client():
    """ Transfers control client fixture"""
    return transfers_control.TransferControlClientAPI(secret_key="sk_secret_key")


@pytest.fixture
def verification_client():
    """ Verification client fixture"""
    return verification.VerificationClientAPI(secret_key="sk_secret_key")
