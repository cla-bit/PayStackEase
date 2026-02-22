""" Fixtures for testing purposes """

import pytest
import pytest_asyncio
from aioresponses import aioresponses
from requests import Session

from paystackease.core import (
    AsyncBaseClientAPI,
    AsyncRequestAPI,
    SyncBaseClientAPI,
    SyncRequestAPI,
    EnvConfig,
)
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
def env_var():
    class MockEnvConfig(EnvConfig):
        def secret_key(self):
            return "test_secret_key"

    return MockEnvConfig()


@pytest.fixture
def client_session():
    return Session()


@pytest.fixture
def sync_base_client(client_session):
    """Base client fixture"""
    return SyncBaseClientAPI(client_session)


@pytest.fixture
def sync_base_client_request(sync_base_client):
    """Base client fixture"""
    return SyncRequestAPI()


@pytest.fixture
def apple_pay_client(sync_base_client_request):
    """Apple pay client fixture"""
    return apple_pay.ApplePayClientAPI()


@pytest.fixture
def bulk_charges_client(sync_base_client_request):
    """Bulk Charges client fixture"""
    return bulk_charges.BulkChargesClientAPI()


@pytest.fixture
def charges_client(sync_base_client_request):
    """Bulk Charges client fixture"""
    return charges.ChargesClientAPI()


@pytest.fixture
def customers_client(sync_base_client_request):
    """Customers client fixture"""
    return customers.CustomerClientAPI()


@pytest.fixture
def dva_client(sync_base_client_request):
    """Customers client fixture"""
    return dedicated_virtual_accounts.DedicatedVirtualAccountClientAPI()


@pytest.fixture
def disputes_client(sync_base_client_request):
    """Disputes client fixture"""
    return disputes.DisputesClientAPI()


@pytest.fixture
def integration_client(sync_base_client_request):
    """Integration client fixture"""
    return integration.IntegrationClientAPI()


@pytest.fixture
def miscellaneous_client(sync_base_client_request):
    """Integration client fixture"""
    return miscellaneous.MiscellaneousClientAPI()


@pytest.fixture
def payment_pages_client(sync_base_client_request):
    """Payment pages client fixture"""
    return payment_pages.PaymentPagesClientAPI()


@pytest.fixture
def payment_requests_client(sync_base_client_request):
    """Payment requests client fixture"""
    return payment_requests.PaymentRequestClientAPI()


@pytest.fixture
def plans_client(sync_base_client_request):
    """Plans client fixture"""
    return plans.PlanClientAPI()


@pytest.fixture
def products_client(sync_base_client_request):
    """Products client fixture"""
    return products.ProductClientAPI()


@pytest.fixture
def refund_client(sync_base_client_request):
    """Refund client fixture"""
    return refund.RefundClientAPI()


@pytest.fixture
def settlements_client(sync_base_client_request):
    """Settlements client fixture"""
    return settlements.SettlementClientAPI()


@pytest.fixture
def subaccounts_client(sync_base_client_request):
    """Subaccounts client fixture"""
    return subaccounts.SubAccountClientAPI()


@pytest.fixture
def subscriptions_client(sync_base_client_request):
    """Subscriptions client fixture"""
    return subscriptions.SubscriptionClientAPI()


@pytest.fixture
def terminal_client(sync_base_client_request):
    """Terminal client fixture"""
    return terminal.TerminalClientAPI()


@pytest.fixture
def transaction_splits_client(sync_base_client_request):
    """Transaction splits client fixture"""
    return transaction_splits.TransactionSplitClientAPI()


@pytest.fixture
def transactions_client(sync_base_client_request):
    """Transactions client fixture"""
    return transactions.TransactionClientAPI()


@pytest.fixture
def transfer_recipients_client(sync_base_client_request):
    """Transfer recipients client fixture"""
    return transfer_recipients.TransferRecipientsClientAPI()


@pytest.fixture
def transfers_client(sync_base_client_request):
    """Transfers client fixture"""
    return transfers.TransfersClientAPI()


@pytest.fixture
def transfers_control_client(sync_base_client_request):
    """Transfers control client fixture"""
    return transfers_control.TransferControlClientAPI()


@pytest.fixture
def verification_client(sync_base_client_request):
    """Verification client fixture"""
    return verification.VerificationClientAPI()


# test fixtures for asynchronous requests


@pytest_asyncio.fixture
async def async_base_client():
    """Async base client fixture"""
    async with AsyncBaseClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_base_client_request(async_base_client):
    """Paystack async request client fixture"""
    async with AsyncRequestAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_apple_pay_client(async_base_client_request):
    """Apple pay client fixture"""
    async with aapple_pay.AsyncApplePayClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_bulk_charges_client(async_base_client_request):
    """Bulk Charges client fixture"""
    async with abulk_charges.AsyncBulkChargesClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_charges_client(async_base_client_request):
    """Charges client fixture"""
    async with acharges.AsyncChargesClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_customers_client(async_base_client_request):
    """Charges client fixture"""
    async with acustomers.AsyncCustomerClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_dva_client(async_base_client_request):
    """Charges client fixture"""
    async with (
        adedicated_virtual_accounts.AsyncDedicatedVirtualAccountClientAPI() as client
    ):
        yield client


@pytest_asyncio.fixture
async def async_disputes_client(async_base_client_request):
    """Disputes client fixture"""
    async with adisputes.AsyncDisputesClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_integration_client(async_base_client_request):
    """Integration client fixture"""
    async with aintegration.AsyncIntegrationClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_miscellaneous_client(async_base_client_request):
    """Miscellaneous client fixture"""
    async with amiscellaneous.AsyncMiscellaneousClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_payment_pages_client(async_base_client_request):
    """Payment pages client fixture"""
    async with apayment_pages.AsyncPaymentPagesClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_payment_requests_client(async_base_client_request):
    """Payment requests client fixture"""
    async with apayment_requests.AsyncPaymentRequestClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_plans_client(async_base_client_request):
    """Plans client fixture"""
    async with aplans.AsyncPlanClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_products_client(async_base_client_request):
    """Products client fixture"""
    async with aproducts.AsyncProductClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_refund_client(async_base_client_request):
    """Refund client fixture"""
    async with arefund.AsyncRefundClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_settlements_client(async_base_client_request):
    """Settlements client fixture"""
    async with asettlements.AsyncSettlementClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_subaccounts_client(async_base_client_request):
    """Subaccounts client fixture"""
    async with asubaccounts.AsyncSubAccountClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_subscriptions_client(async_base_client_request):
    """Subscriptions client fixture"""
    async with asubscriptions.AsyncSubscriptionClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_terminal_client(async_base_client_request):
    """Terminal client fixture"""
    async with aterminal.AsyncTerminalClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_transaction_splits_client(async_base_client_request):
    """Transaction splits client fixture"""
    async with atransaction_splits.AsyncTransactionSplitClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_transactions_client(async_base_client_request):
    """Transactions client fixture"""
    async with atransactions.AsyncTransactionClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_transfer_recipients_client(async_base_client_request):
    """Transfer recipients client fixture"""
    async with atransfer_recipients.AsyncTransferRecipientsClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_transfers_client(async_base_client_request):
    """Transfers client fixture"""
    async with atransfers.AsyncTransfersClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_transfers_control_client(async_base_client_request):
    """Transfers control client fixture"""
    async with atransfers_control.AsyncTransferControlClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def async_verification_client(async_base_client_request):
    """Verification client fixture"""
    async with averification.AsyncVerificationClientAPI() as client:
        yield client


@pytest_asyncio.fixture
async def mocked_responses():
    """Mocked responses fixture"""
    with aioresponses() as mocked:
        yield mocked
