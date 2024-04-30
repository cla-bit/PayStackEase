""" Wrapper classes for various Synchronous Paystack API endpoints,
providing simplified access to functionality in Paystack
"""

from paystackease.apis import (
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
from paystackease.core import SyncRequestAPI
from paystackease.metadata.__version__ import __version__


class PayStackBase(SyncRequestAPI):
    """PayStackBase acts as a wrapper around various client APIs to
    interact with the PayStack API
    """

    VERSION = __version__

    # pylint: disable=too-many-instance-attributes
    def __init__(self, secret_key=None):
        super().__init__(secret_key)
        self.apple_pay = apple_pay.ApplePayClientAPI(secret_key=secret_key)
        self.bulk_charges = bulk_charges.BulkChargesClientAPI(secret_key=secret_key)
        self.charges = charges.ChargesClientAPI(secret_key=secret_key)
        self.customers = customers.CustomerClientAPI(secret_key=secret_key)
        self.dedicated_virtual_accounts = (
            dedicated_virtual_accounts.DedicatedVirtualAccountClientAPI(
                secret_key=secret_key
            )
        )
        self.disputes = disputes.DisputesClientAPI(secret_key=secret_key)
        self.integration = integration.IntegrationClientAPI(secret_key=secret_key)
        self.miscellaneous = miscellaneous.MiscellaneousClientAPI(secret_key=secret_key)
        self.payment_pages = payment_pages.PaymentPagesClientAPI(secret_key=secret_key)
        self.payment_requests = payment_requests.PaymentRequestClientAPI(
            secret_key=secret_key
        )
        self.plans = plans.PlanClientAPI(secret_key=secret_key)
        self.products = products.ProductClientAPI(secret_key=secret_key)
        self.refund = refund.RefundClientAPI(secret_key=secret_key)
        self.settlements = settlements.SettlementClientAPI(secret_key=secret_key)
        self.subaccounts = subaccounts.SubAccountClientAPI(secret_key=secret_key)
        self.subscriptions = subscriptions.SubscriptionClientAPI(secret_key=secret_key)
        self.terminal = terminal.TerminalClientAPI(secret_key=secret_key)
        self.transaction_splits = transaction_splits.TransactionSplitClientAPI(
            secret_key=secret_key
        )
        self.transactions = transactions.TransactionClientAPI(secret_key=secret_key)
        self.transfer_recipients = transfer_recipients.TransferRecipientsClientAPI(
            secret_key=secret_key
        )
        self.transfers = transfers.TransfersClientAPI(secret_key=secret_key)
        self.transfer_control = transfers_control.TransferControlClientAPI(
            secret_key=secret_key
        )
        self.verification = verification.VerificationClientAPI(secret_key=secret_key)
