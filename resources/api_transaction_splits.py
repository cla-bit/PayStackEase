"""
Examples
"""

import asyncio
from paystackease import (
    PayStackBase,
    AsyncPayStackBase,
    Currency,
    SplitType,
)


async def main():
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        list_transaction_splits = await paystack_client.transaction_splits.list_split()
        print(f"List Transaction Splits: {list_transaction_splits}")

        get_transaction_split = await paystack_client.transaction_splits.fetch_split(
            split_id="SPL_u2EYmrwFlI"
        )
        print(f"Transaction Split Details: {get_transaction_split}")

        # access the API endpoints making a Post request
        create_split = await paystack_client.transaction_splits.create_split(
            transaction_split_name="Testing Percentage Split",
            transaction_split_type=SplitType.FLAT.value,  # if using Flat share value is in units
            currency=Currency.NGN.value,
            subaccounts=[
                {"subaccount": "ACCT_6u06q3cc892r4cy", "share": 10000},
                {"subaccount": "ACCT_6u06q3cc892r4cy", "share": 100000},
            ],
            bearer_type="subaccount",
            bearer_subaccount="ACCT_6u06q3cc892r4cy",
        )
        print(f"Created Splits: {create_split}")

        add_update_split_subaccount = (
            await paystack_client.transaction_splits.add_or_update_subaccount_split(
                split_id="SPL_u2EYmrwFlI",
                subaccount="ACCT_6u06q3cc892r4cy",
                transaction_share=40000,
            )
        )
        print(
            f"Added or Updated a Subaccount to a Split: {add_update_split_subaccount}"
        )

        remove_split_subaccount = (
            await paystack_client.transaction_splits.remove_sub_account_split(
                split_id="SPL_u2EYmrwFlI", subaccount="ACCT_6u06q3cc892r4cy"
            )
        )
        print(f"Removed a Subaccount to a Split: {remove_split_subaccount}")

        # access the API endpoints making a Post request
        updated_split = await paystack_client.transaction_splits.update_split(
            split_id="SPL_fjJJkak25k",
            transaction_split_name="Updated Split",
            active=True,
        )
        print(f"Updated a Split: {updated_split}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    # access the API endpoints making a Get request
    list_transaction_splits = paystack_client.transaction_splits.list_split(
        active=False
    )
    print(f"List Transaction Splits: {list_transaction_splits}")

    get_transaction_split = paystack_client.transaction_splits.fetch_split(
        split_id="SPL_fjJJkak25k"
    )
    print(f"Transaction Split Details: {get_transaction_split}")

    # access the API endpoints making a Post request
    create_split = paystack_client.transaction_splits.create_split(
        transaction_split_name="Testing Percentage Split",
        transaction_split_type=SplitType.FLAT.value,  # if using Flat, share value is in unit
        currency=Currency.NGN.value,
        subaccounts=[
            {"subaccount": "ACCT_6u06q3cc892r4cy", "share": 20000},
            {"subaccount": "ACCT_6u06q3cc892r4cy", "share": 300000},
        ],
        bearer_type="subaccount",
        bearer_subaccount="ACCT_6u06q3cc892r4cy",
    )
    print(f"Created Splits: {create_split}")

    add_update_split_subaccount = (
        paystack_client.transaction_splits.add_or_update_subaccount_split(
            split_id="SPL_fjJJkak25k",
            subaccount="ACCT_6u06q3cc892r4cy",
            transaction_share=40000,
        )
    )
    print(f"Added or Updated a Subaccount to a Split: {add_update_split_subaccount}")

    remove_split_subaccount = (
        paystack_client.transaction_splits.remove_sub_account_split(
            split_id="SPL_fjJJkak25k", subaccount="ACCT_6u06q3cc892r4cy"
        )
    )
    print(f"Removed a Subaccount to a Split: {remove_split_subaccount}")

    # access the API endpoints making a Post request
    updated_split = paystack_client.transaction_splits.update_split(
        split_id="SPL_fjJJkak25k", transaction_split_name="Updated Split", active=True
    )
    print(f"Updated a Split: {updated_split}")


if __name__ == "__main__":
    main()
