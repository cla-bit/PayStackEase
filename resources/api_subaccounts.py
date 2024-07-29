"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase


async def main():
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        list_subaccounts = await paystack_client.subaccounts.list_subaccounts()
        print(f"List Subaccounts: {list_subaccounts}")

        get_subaccount = await paystack_client.subaccounts.fetch_subaccount(
            id_or_code="ACCT_subaccount-id-or-code"
        )
        print(f"Get Subaccount: {get_subaccount}")

        # access the API endpoints making a Post request
        create_subaccount = await paystack_client.subaccounts.create_subaccount(
            business_name="Test business name",
            settlement_bank="bank code",
            account_number="0000000000",
            percentage_charge=18.2,
            description="This is just a testing subaccount to create",
        )
        print(f"Created Subaccount: {create_subaccount}")

        # access the API endpoints making a Put request
        update_subaccount = await paystack_client.subaccounts.update_subaccount(
            id_or_code="subaccount-id",
            business_name="Testing Logistics",
            settlement_bank="bank code",
            account_number="0000000000",
            primary_contact_name="Test Environment",
            primary_contact_email="test@gmail.com",
        )
        print(f"Updated Subaccount: {update_subaccount}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()

    # access the API endpoints making a Get request
    list_subaccounts = paystack_client.subaccounts.list_subaccounts()
    print(f"List Subaccounts: {list_subaccounts}")

    get_subaccount = paystack_client.subaccounts.fetch_subaccount(
        id_or_code="ACCT_subaccount-id-or-code"
    )
    print(f"Get Subaccount: {get_subaccount}")

    # access the API endpoints making a Post request
    create_subaccount = paystack_client.subaccounts.create_subaccount(
        business_name="Test business name",
        settlement_bank="bank code",
        account_number="0000000000",
        percentage_charge=18.2,
        description="This is just a testing subaccount to create",
    )
    print(f"Created Subaccount: {create_subaccount}")

    # access the API endpoints making a Put request
    update_subaccount = paystack_client.subaccounts.update_subaccount(
        id_or_code="subaccount-id",
        business_name="Test Testing Logistics",
        settlement_bank="bank code",
        account_number="0000000000",
        primary_contact_name="Test Test",
        primary_contact_email="test1@gmail.com",
    )
    print(f"Updated Subaccount: {update_subaccount}")


if __name__ == "__main__":
    main()
