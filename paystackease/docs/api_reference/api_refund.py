"""
Demonstrates using Asynchronous and Synchronous Paystack Refund API wrappers.
Shows PayStackBase, and AsyncPayStaCKBase for interacting with Paystack's transactions.

Reference: https://paystack.com/docs/api/refund/ to learn more
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_refunds = await paystack_client.refund.list_refunds()
        print(f"Refunds: {all_refunds}")

        get_refund = await paystack_client.refund.fetch_refund(
            reference="reference-here"
        )
        print(f"Refund Detail: {get_refund}")

        # access the API endpoints making a Post request
        create_refund = await paystack_client.refund.create_refund(
            transaction_ref_or_id="transaction-id-here",
        )
        print(f"Created Refund: {create_refund}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_refunds = paystack_client.refund.list_refunds()
    print(f"Refunds: {all_refunds}")

    get_refund = paystack_client.refund.fetch_refund(reference="reference-here")
    print(f"Refund Detail: {get_refund}")

    # access the API endpoints making a Post request
    create_refund = paystack_client.refund.create_refund(
        transaction_ref_or_id="transaction-id-here",
    )
    print(f"Created Refund: {create_refund}")


if __name__ == "__main__":
    main()
