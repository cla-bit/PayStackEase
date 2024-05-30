"""
Examples
"""
import asyncio
from paystackease import PayStackBase, Currency, AsyncPayStackBase


async def main():
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_banks = await paystack_client.miscellaneous.list_banks(
            country="nigeria", currency=Currency.NGN.value,
        )
        bank_names = [bank['name'] for bank in all_banks.data]
        print(f"Bank names: {bank_names}")
        print(f"Total Number of banks: {len(all_banks.data)}")

        all_countries = await paystack_client.miscellaneous.list_countries()
        country_names = [country['name'] for country in all_countries.data]
        print(f"Country names: {country_names}")
        print(f"Total number of countries: {len(all_countries.data)}")

        all_states = await paystack_client.miscellaneous.list_states(country="CA")
        if all_states.data:
            state_names = [state['name'] for state in all_states.data]
            print(f"State names: {state_names}")
            print(f"Total number of states: {len(all_states.data)}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()

    # access the API endpoints making a Get request
    all_banks = paystack_client.miscellaneous.list_banks(
        country="nigeria", currency=Currency.NGN.value
    )
    bank_names = [bank['name'] for bank in all_banks.data]
    print(f"Bank names: {bank_names}")
    print(f"Total Number of banks: {len(all_banks.data)}")

    all_countries = paystack_client.miscellaneous.list_countries()
    country_names = [country['name'] for country in all_countries.data]
    print(f"Country names: {country_names}")
    print(f"Total number of countries: {len(all_countries.data)}")

    all_states = paystack_client.miscellaneous.list_states(country="US")
    if all_states.data:
        state_names = [state['name'] for state in all_states.data]
        print(f"State names: {state_names}")
        print(f"Total number of states: {len(all_states.data)}")


if __name__ == "__main__":
    main()
