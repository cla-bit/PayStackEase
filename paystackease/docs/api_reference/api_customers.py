"""
Demonstrates using Asynchronous and Synchronous Paystack Customers API wrappers.
Shows PayStackBase, and AsyncPayStaCKBase for interacting with Paystack's transactions.

Reference: https://paystack.com/docs/api/customer/ to learn more
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase, RiskAction


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_customers = await paystack_client.customers.list_customers()
        print(f"All Customers: {all_customers}")

        get_customer = await paystack_client.customers.fetch_customer(
            email_or_code="test@gmail.com"
        )
        print(f"Customer Detail: {get_customer}")

        # access the API endpoints making a Post request
        create_customer = await paystack_client.customers.create_customer(
            email="faithsusan@gmail.com",
            first_name="Faith",
            last_name="Susan",
            phone="+2348123456789",
            metadata={"middle_name": "Anne", "nickname": "Suzie"},
        )
        print(f"Create charge: {create_customer}")

        validate_customer = await paystack_client.customers.validate_customer(
            email_or_code="faithsusan@gmail.com",
            first_name="Faith",
            last_name="Susan",
            account_type="bank_account",
            country="NG",
            bvn="20012345677",
            bank_code="044",
            account_number="0000000000",
        )
        print(f"Validate Customer: {validate_customer}")

        white_blacklist_customer = (
            await paystack_client.customers.whitelist_blacklist_customer(
                email_or_code="test@gmail.com", risk_action=RiskAction.DENY.value
            )
        )
        print(f"Blacklisted Customer: {white_blacklist_customer}")

        deactivate_auth_code = await paystack_client.customers.deactivate_authorization(
            authorization_code="AUTH_nii6s41xsr"
        )
        print(f"Deactivated Auth Code: {deactivate_auth_code}")

        # access the API endpoints making a Put request
        update_customer = await paystack_client.customers.update_customer(
            customer_code="CUS_7kwefc2jng1usti", metadata={"middle_name": "Ann"}
        )
        print(f"Updated Customer: {update_customer}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_customers = paystack_client.customers.list_customers()
    print(f"All Customers: {all_customers}")

    get_customer = paystack_client.customers.fetch_customer(
        email_or_code="test@gmail.com"
    )
    print(f"Customer Detail: {get_customer}")

    # access the API endpoints making a Post request
    create_customer = paystack_client.customers.create_customer(
        email="faithsusan@gmail.com",
        first_name="Faith",
        last_name="Susan",
        phone="+2348123456789",
        metadata={"middle_name": "Anne", "nickname": "Suzie"},
    )
    print(f"Create charge: {create_customer}")

    validate_customer = paystack_client.customers.validate_customer(
        email_or_code="faithsusan@gmail.com",
        first_name="Faith",
        last_name="Susan",
        account_type="bank_account",
        country="NG",
        bvn="20012345677",
        bank_code="044",
        account_number="0000000000",
    )
    print(f"Validate Customer: {validate_customer}")

    white_blacklist_customer = paystack_client.customers.whitelist_blacklist_customer(
        email_or_code="test@gmail.com", risk_action=RiskAction.DENY.value
    )
    print(f"Blacklisted Customer: {white_blacklist_customer}")

    deactivate_auth_code = paystack_client.customers.deactivate_authorization(
        authorization_code="AUTH_nii6s41xsr"
    )
    print(f"Deactivated Auth Code: {deactivate_auth_code}")

    # access the API endpoints making a Put request
    update_customer = paystack_client.customers.update_customer(
        customer_code="CUS_7kwefc2jng1usti", metadata={"middle_name": "Ann"}
    )
    print(f"Updated Customer: {update_customer}")


if __name__ == "__main__":
    main()
