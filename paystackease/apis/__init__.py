""" Wrappers for synchronous API calls to Paystack"""

from paystackease.apis.apple_pay import ApplePayClientAPI
from paystackease.apis.bulk_charges import BulkChargesClientAPI
from paystackease.apis.charges import ChargesClientAPI
from paystackease.apis.customers import CustomerClientAPI
from paystackease.apis.dedicated_virtual_accounts import DedicatedVirtualAccountClientAPI
from paystackease.apis.disputes import DisputesClientAPI
from paystackease.apis.integration import IntegrationClientAPI
from paystackease.apis.miscellaneous import MiscellaneousClientAPI
from paystackease.apis.payment_pages import PaymentPagesClientAPI
from paystackease.apis.payment_requests import PaymentRequestClientAPI
from paystackease.apis.plans import PlanClientAPI
from paystackease.apis.products import ProductClientAPI
from paystackease.apis.refund import RefundClientAPI
from paystackease.apis.settlements import SettlementClientAPI
from paystackease.apis.subaccounts import SubAccountClientAPI
from paystackease.apis.subscriptions import SubscriptionClientAPI
from paystackease.apis.terminal import TerminalClientAPI
from paystackease.apis.transaction_splits import TransactionSplitClientAPI
from paystackease.apis.transactions import TransactionClientAPI
from paystackease.apis.transfer_recipients import TransferRecipientsClientAPI
from paystackease.apis.transfers import TransfersClientAPI
from paystackease.apis.transfers_control import TransferControlClientAPI
from paystackease.apis.verification import VerificationClientAPI
