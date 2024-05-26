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
        self.dedicated_virtual_accounts = adedicated_virtual_accounts.AsyncDedicatedVirtualAccountClientAPI()
        self.disputes = adisputes.AsyncDisputesClientAPI()
        self.integration = aintegration.AsyncIntegrationClientAPI()
        self.miscellaneous = amiscellaneous.AsyncMiscellaneousClientAPI()
        self.payment_pages = apayment_pages.AsyncPaymentPagesClientAPI()
        self.payment_requests = apayment_requests.AsyncPaymentRequestClientAPI()
        self.plans = aplans.AsyncPlanClientAPI()
        self.products = aproducts.AsyncProductClientAPI()
        self.refund = arefund.AsyncRefundClientAPI()
        self.settlements = asettlements.AsyncSettlementClientAPI()
        self.subaccounts = asubaccounts.AsyncSubAccountClientAPI()
        self.subscriptions = asubscriptions.AsyncSubscriptionClientAPI()
        self.terminal = aterminal.AsyncTerminalClientAPI()
        self.transaction_splits = atransaction_splits.AsyncTransactionSplitClientAPI()
        self.transactions = atransactions.AsyncTransactionClientAPI()
        self.transfer_recipients = atransfer_recipients.AsyncTransferRecipientsClientAPI()
        self.transfers = atransfers.AsyncTransfersClientAPI()
        self.transfer_control = atransfers_control.AsyncTransferControlClientAPI()
        self.verification = averification.AsyncVerificationClientAPI()

    async def __aenter__(self):
        # await super().__aenter__()
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
        # await super().__aexit__(*args)
