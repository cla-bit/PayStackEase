""" Wrappers for synchronous API calls to Paystack"""


from paystackease.sync.apis import (
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
from paystackease.sync._api_http_request import PayStackBaseClientAPI
