"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_settlements = await paystack_client.settlements.list_settlements()
        print(f"All Settlements: {all_settlements}")

        settle_detail = await paystack_client.settlements.list_settlement_transactions(
            settlement_id="settlement-id-here"
        )
        print(f"Settlement Transaction Detail: {settle_detail}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_settlements = paystack_client.settlements.list_settlements()
    print(f"All Settlements: {all_settlements}")

    settle_detail = paystack_client.settlements.list_settlement_transactions(
        settlement_id="settlement-id-here"
    )
    print(f"Settlement Transaction Detail: {settle_detail}")


if __name__ == "__main__":
    main()
