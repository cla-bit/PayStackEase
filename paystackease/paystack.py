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
        self.dedicated_virtual_accounts = dedicated_virtual_accounts.DedicatedVirtualAccountClientAPI()
        self.disputes = disputes.DisputesClientAPI()
        self.integration = integration.IntegrationClientAPI()
        self.miscellaneous = miscellaneous.MiscellaneousClientAPI()
        self.payment_pages = payment_pages.PaymentPagesClientAPI()
        self.payment_requests = payment_requests.PaymentRequestClientAPI()
        self.plans = plans.PlanClientAPI()
        self.products = products.ProductClientAPI()
        self.refund = refund.RefundClientAPI()
        self.settlements = settlements.SettlementClientAPI()
        self.subaccounts = subaccounts.SubAccountClientAPI()
        self.subscriptions = subscriptions.SubscriptionClientAPI()
        self.terminal = terminal.TerminalClientAPI()
        self.transaction_splits = transaction_splits.TransactionSplitClientAPI()
        self.transactions = transactions.TransactionClientAPI()
        self.transfer_recipients = transfer_recipients.TransferRecipientsClientAPI()
        self.transfers = transfers.TransfersClientAPI()
        self.transfer_control = transfers_control.TransferControlClientAPI()
        self.verification = verification.VerificationClientAPI()
