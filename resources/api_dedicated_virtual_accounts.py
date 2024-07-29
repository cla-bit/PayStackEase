"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_dv_customers = (
            await paystack_client.dedicated_virtual_accounts.list_dedicated_account()
        )
        print(f"All DV Customers: {all_dv_customers}")

        get_dv_customer = (
            await paystack_client.dedicated_virtual_accounts.fetch_dedicated_account(
                dedicated_account_id=59
            )
        )
        print(f"Customer Detail: {get_dv_customer}")

        requery_dv = (
            await paystack_client.dedicated_virtual_accounts.requery_dedicated_account()
        )
        print(f"Requery DV: {requery_dv}")

        fetch_bank_providers = (
            await paystack_client.dedicated_virtual_accounts.fetch_bank_providers()
        )
        print(f"Bank Providers: {fetch_bank_providers}")

        # access the API endpoints making a Post request
        create_dv_customer = (
            await paystack_client.dedicated_virtual_accounts.create_virtual_account(
                customer_id_or_code="CUS_customer-code", preferred_bank="wema-bank"
            )
        )
        print(f"Create Virtual Customer: {create_dv_customer}")

        assign_dv_customer = await paystack_client.dedicated_virtual_accounts.assign_dedicated_virtual_account(
            email="test@gmail.com",
            first_name="test",
            last_name="test",
            phone="phone number",
            preferred_bank="wema-bank",
            country="country code",
            account_number="0000000000",
        )
        print(f"Assigned DV Customer: {assign_dv_customer}")

        split_dv_transaction = (
            await paystack_client.dedicated_virtual_accounts.split_dedicated_account(
                customer_id_or_code="CUS_customer-code",
                preferred_bank="wema-bank",
                split_code="SPL_split-code",
            )
        )
        print(f"Split DV Transaction: {split_dv_transaction}")

        # access the API endpoints making a Delete request
        delete_dv = await paystack_client.dedicated_virtual_accounts.deactivate_dedicated_account(
            dedicated_account_id=58
        )
        print(f"Deleted DV: {delete_dv}")

        remove_split = await paystack_client.dedicated_virtual_accounts.remove_split_dedicated_account(
            account_number="000000000"
        )
        print(f"Removed Split: {remove_split}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_dv_customers = (
        paystack_client.dedicated_virtual_accounts.list_dedicated_account()
    )
    print(f"All DV Customers: {all_dv_customers}")

    get_dv_customer = (
        paystack_client.dedicated_virtual_accounts.fetch_dedicated_account(
            dedicated_account_id=59
        )
    )
    print(f"Customer Detail: {get_dv_customer}")

    requery_dv = paystack_client.dedicated_virtual_accounts.requery_dedicated_account()
    print(f"Requery DV: {requery_dv}")

    fetch_bank_providers = (
        paystack_client.dedicated_virtual_accounts.fetch_bank_providers()
    )
    print(f"Bank Providers: {fetch_bank_providers}")

    # access the API endpoints making a Post request
    create_dv_customer = (
        paystack_client.dedicated_virtual_accounts.create_virtual_account(
            customer_id_or_code="CUS_customer-code", preferred_bank="wema-bank"
        )
    )
    print(f"Create Virtual Customer: {create_dv_customer}")

    assign_dv_customer = (
        paystack_client.dedicated_virtual_accounts.assign_dedicated_virtual_account(
            email="test@gmail.com",
            first_name="test",
            last_name="test",
            phone="phone number",
            preferred_bank="wema-bank",
            country="country code",
            account_number="0000000000",
        )
    )
    print(f"Assigned DV Customer: {assign_dv_customer}")

    split_dv_transaction = (
        paystack_client.dedicated_virtual_accounts.split_dedicated_account(
            customer_id_or_code="CUS_customer-code",
            preferred_bank="wema-bank",
            split_code="SPL_split-code",
        )
    )
    print(f"Split DV Transaction: {split_dv_transaction}")

    # access the API endpoints making a Delete request
    delete_dv = paystack_client.dedicated_virtual_accounts.deactivate_dedicated_account(
        dedicated_account_id=58
    )
    print(f"Deleted DV: {delete_dv}")

    remove_split = (
        paystack_client.dedicated_virtual_accounts.remove_split_dedicated_account(
            account_number="000000000"
        )
    )
    print(f"Removed Split: {remove_split}")


if __name__ == "__main__":
    main()
