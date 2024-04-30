""" Wrapper classes for various Asynchronous Paystack API endpoints,
providing simplified access to functionality in Paystack
"""

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
from paystackease.core import AsyncRequestAPI
from paystackease.metadata.__version__ import __version__


class AsyncPayStackBase(AsyncRequestAPI):
    """AsyncPayStackBase acts as a wrapper around various client APIs to
    interact with the PayStack API
    """

    VERSION = __version__

    # pylint: disable=too-many-instance-attributes
    def __init__(self, secret_key=None):
        super().__init__(secret_key)
        self.apple_pay = aapple_pay.AsyncApplePayClientAPI(secret_key=secret_key)
        self.bulk_charges = abulk_charges.AsyncBulkChargesClientAPI(
            secret_key=secret_key
        )
        self.charges = acharges.AsyncChargesClientAPI(secret_key=secret_key)
        self.customers = acustomers.AsyncCustomerClientAPI(secret_key=secret_key)
        self.dedicated_virtual_accounts = (
            adedicated_virtual_accounts.AsyncDedicatedVirtualAccountClientAPI(
                secret_key=secret_key
            )
        )
        self.disputes = adisputes.AsyncDisputesClientAPI(secret_key=secret_key)
        self.integration = aintegration.AsyncIntegrationClientAPI(secret_key=secret_key)
        self.miscellaneous = amiscellaneous.AsyncMiscellaneousClientAPI(
            secret_key=secret_key
        )
        self.payment_pages = apayment_pages.AsyncPaymentPagesClientAPI(
            secret_key=secret_key
        )
        self.payment_requests = apayment_requests.AsyncPaymentRequestClientAPI(
            secret_key=secret_key
        )
        self.plans = aplans.AsyncPlanClientAPI(secret_key=secret_key)
        self.products = aproducts.AsyncProductClientAPI(secret_key=secret_key)
        self.refund = arefund.AsyncRefundClientAPI(secret_key=secret_key)
        self.settlements = asettlements.AsyncSettlementClientAPI(secret_key=secret_key)
        self.subaccounts = asubaccounts.AsyncSubAccountClientAPI(secret_key=secret_key)
        self.subscriptions = asubscriptions.AsyncSubscriptionClientAPI(
            secret_key=secret_key
        )
        self.terminal = aterminal.AsyncTerminalClientAPI(secret_key=secret_key)
        self.transaction_splits = atransaction_splits.AsyncTransactionSplitClientAPI(
            secret_key=secret_key
        )
        self.transactions = atransactions.AsyncTransactionClientAPI(
            secret_key=secret_key
        )
        self.transfer_recipients = (
            atransfer_recipients.AsyncTransferRecipientsClientAPI(secret_key=secret_key)
        )
        self.transfers = atransfers.AsyncTransfersClientAPI(secret_key=secret_key)
        self.transfer_control = atransfers_control.AsyncTransferControlClientAPI(
            secret_key=secret_key
        )
        self.verification = averification.AsyncVerificationClientAPI(
            secret_key=secret_key
        )

    async def __aenter__(self):
        await super().__aenter__()
        await self.apple_pay.__aenter__()
        await self.bulk_charges.__aenter__()
        await self.charges.__aenter__()
        await self.customers.__aenter__()
        await self.dedicated_virtual_accounts.__aenter__()
        await self.disputes.__aenter__()
        await self.integration.__aenter__()
        await self.miscellaneous.__aenter__()
        await self.payment_pages.__aenter__()
        await self.payment_requests.__aenter__()
        await self.plans.__aenter__()
        await self.products.__aenter__()
        await self.refund.__aenter__()
        await self.settlements.__aenter__()
        await self.subaccounts.__aenter__()
        await self.subscriptions.__aenter__()
        await self.terminal.__aenter__()
        await self.transaction_splits.__aenter__()
        await self.transactions.__aenter__()
        await self.transfer_recipients.__aenter__()
        await self.transfers.__aenter__()
        await self.transfer_control.__aenter__()
        await self.verification.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self.apple_pay.__aexit__(*args)
        await self.bulk_charges.__aexit__(*args)
        await self.charges.__aexit__(*args)
        await self.customers.__aexit__(*args)
        await self.dedicated_virtual_accounts.__aexit__(*args)
        await self.disputes.__aexit__(*args)
        await self.integration.__aexit__(*args)
        await self.miscellaneous.__aexit__(*args)
        await self.payment_pages.__aexit__(*args)
        await self.payment_requests.__aexit__(*args)
        await self.plans.__aexit__(*args)
        await self.products.__aexit__(*args)
        await self.refund.__aexit__(*args)
        await self.settlements.__aexit__(*args)
        await self.subaccounts.__aexit__(*args)
        await self.subscriptions.__aexit__(*args)
        await self.terminal.__aexit__(*args)
        await self.transaction_splits.__aexit__(*args)
        await self.transactions.__aexit__(*args)
        await self.transfer_recipients.__aexit__(*args)
        await self.transfers.__aexit__(*args)
        await self.transfer_control.__aexit__(*args)
        await self.verification.__aexit__(*args)
        await super().__aexit__(*args)
