"""
Demonstrates using Asynchronous and Synchronous Paystack Integration API wrappers.
Shows PayStackBase, and AsyncPayStaCKBase for interacting with Paystack's transactions.

Reference: https://paystack.com/docs/api/integration/ to learn more
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        timeout_detail = await paystack_client.integration.fetch_timeout()
        print(f"Timeout Detail: {timeout_detail}")

        # access the API endpoints making a Put request
        update_timeout = await paystack_client.integration.update_timeout(timeout=30)
        print(f"Updated Timeout: {update_timeout}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    timeout_detail = paystack_client.integration.fetch_timeout()
    print(f"Timeout Detail: {timeout_detail}")

    # access the API endpoints making a Put request
    update_timeout = paystack_client.integration.update_timeout(timeout=30)
    print(f"Updated Timeout: {update_timeout}")


if __name__ == "__main__":
    main()
