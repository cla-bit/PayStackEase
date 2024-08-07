"""
Examples
"""

import asyncio
from paystackease import (
    PayStackBase,
    AsyncPayStackBase,
    Currency,
    Channels,
    convert_to_subunit,
)


async def main():
    async with AsyncPayStackBase() as paystack_client:

        # access the API endpoints making a Get request
        list_transactions = await paystack_client.transactions.list_transactions(
            status="success"
        )
        print(f"List Transactions: {list_transactions}")

        verify_transaction = await paystack_client.transactions.verify_transaction(
            reference="reference"
        )
        print(f"Verify Transaction: {verify_transaction}")

        get_transaction = await paystack_client.transactions.fetch_transaction(
            transaction_id=1
        )
        print(f"Get Transaction: {get_transaction}")

        transaction_timeline = await paystack_client.transactions.transaction_timeline(
            id_or_reference="id_or_reference"
        )
        print(f"Transaction Timeline: {transaction_timeline}")

        transaction_totals = await paystack_client.transactions.transaction_totals()
        print(f"Transaction Totals: {transaction_totals}")

        export_transaction = await paystack_client.transactions.export_transactions()
        print(f"Export Transactions: {export_transaction}")

        # access the API endpoints making a Post request
        # amount should be in subunit in this case 10000 kobo = 100 naira
        money = convert_to_subunit(100, Currency.NGN)
        initiate_transaction = await paystack_client.transactions.initialize(
            email="test@gmail.com",
            amount=money,
            channels=[Channels.BANK.value, Channels.CARD.value],
            metadata={"first_name": "Test", "last_name": "Test"},
        )
        checkout = initiate_transaction.checkout_url
        print(checkout)
        print(f"Initiate Transaction: {initiate_transaction}")

        charge_auth = await paystack_client.transactions.charge_authorization(
            email="email@gmail.com",
            amount=10000,  # use convert_currency() to convert to subunit
            authorization_code="AUTH_authorization-code",
            reference="add_your_unique_reference",
            currency=Currency.NGN.value,
            channels=[Channels.BANK.value, Channels.CARD.value],
            subaccount="ACCT_subaccount-code",
            transaction_charge=10,
            bearer="account" or "subaccount",
            queue=True,
        )
        print(f"Charge Authorization: {charge_auth}")

        partial_debt = await paystack_client.transactions.partial_debit(
            email="email@gmail.com",
            authorization_code="AUTH_authorization-code",
            amount=10000,  # amount should be in subunit in this case 10000 kobo = 100 naira
            currency=Currency.NGN.value,
            reference="add_your_unique_reference",
            at_least=100,
        )
        print(f"Partial Debt: {partial_debt}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()

    # access the API endpoints making a Get request
    list_transactions = paystack_client.transactions.list_transactions(status="success")
    print(f"List Transactions: {list_transactions}")

    verify_transaction = paystack_client.transactions.verify_transaction(
        reference="reference"
    )
    print(f"Verify Transaction: {verify_transaction}")

    get_transaction = paystack_client.transactions.fetch_transaction(transaction_id=1)
    print(f"Get Transaction: {get_transaction}")

    transaction_timeline = paystack_client.transactions.transaction_timeline(
        id_or_reference="id_or_reference"
    )
    print(f"Transaction Timeline: {transaction_timeline}")

    transaction_totals = paystack_client.transactions.transaction_totals()
    print(f"Transaction Totals: {transaction_totals}")

    export_transaction = paystack_client.transactions.export_transactions()
    print(f"Export Transactions: {export_transaction}")

    # access the API endpoints making a Post request
    # amount should be in subunit in this case 10000 kobo = 100 naira
    money = convert_to_subunit(100, Currency.NGN)
    initiate_transaction = paystack_client.transactions.initialize(
        email="test@gmail.com",
        amount=money,
        channels=[Channels.BANK.value, Channels.CARD.value],
        metadata={"first_name": "Test", "last_name": "Test"},
    )
    url = initiate_transaction.checkout_url
    print(f"url: {url}")

    charge_auth = paystack_client.transactions.charge_authorization(
        email="email@gmail.com",
        amount=10000,  # use convert_currency() to convert to subunit
        authorization_code="AUTH_authorization-code",
        reference="add_your_unique_reference",
        currency=Currency.NGN.value,
        channels=[Channels.BANK.value, Channels.CARD.value],
        subaccount="ACCT_subaccount-code",
        transaction_charge=10,
        bearer="account" or "subaccount",
        queue=True,
    )
    print(f"Charge Authorization: {charge_auth}")

    partial_debt = paystack_client.transactions.partial_debit(
        email="email@gmail.com",
        authorization_code="AUTH_authorization-code",
        amount=10000,  # amount should be in subunit in this case 10000 kobo = 100 naira
        currency=Currency.NGN.value,
        reference="add_your_unique_reference",
        at_least=100,
    )
    print(f"Partial Debt: {partial_debt}")


if __name__ == "__main__":
    main()
