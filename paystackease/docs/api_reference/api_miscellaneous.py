"""
Demonstrates using Asynchronous and Synchronous Paystack miscellaneous API wrappers.
Shows PayStackBase and AsyncPayStackBase for interacting with Paystack's verification.

Reference: https://paystack.com/docs/api/miscellaneous/ to learn more
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase, Currency, Channels


async def main():
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_banks = await paystack_client.miscellaneous.list_banks(
            channel_type=Channels.CARD.value,
            country="nigeria",
            currency=Currency.NGN.value,
        )
        for bank in all_banks["data"]:
            print(f"***********\nBank: {bank}\n")
        print(f"Length: {len(all_banks['data'])}")

        all_countries = await paystack_client.miscellaneous.list_countries()
        for country in all_countries["data"]:
            print(f"***********\nBank: {country}\n")
        print(f"Length: {len(all_countries['data'])}")

        all_states = await paystack_client.miscellaneous.list_states(country="CA")
        print(f"All States: {all_states['data']}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    # access the API endpoints making a Get request
    all_banks = paystack_client.miscellaneous.list_banks(
        channel_type=Channels.CARD.value, country="nigeria", currency=Currency.NGN.value
    )
    for bank in all_banks["data"]:
        print(f"***********\nBank: {bank}\n")
    print(f"Length: {len(all_banks['data'])}")

    all_countries = paystack_client.miscellaneous.list_countries()
    for country in all_countries["data"]:
        print(f"***********\nBank: {country}\n")
    print(f"Length: {len(all_countries['data'])}")

    all_states = paystack_client.miscellaneous.list_states(country="CA")
    print(f"All States: {all_states['data']}")


if __name__ == "__main__":
    main()
