"""
Demonstrates using Asynchronous and Synchronous Paystack bulk charges API wrappers.
Shows PayStackBase, and AsyncPayStackBase for interacting with Paystack's transactions.

Reference: https://paystack.com/docs/api/bulk-charge/ to learn more
"""

import asyncio
from datetime import date

from paystackease import PayStackBase, AsyncPayStackBase, STATUS


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        list_domains = await paystack_client.bulk_charges.list_bulk_charge_batches(
            from_date=date.today()
        )
        print(f"List all domains: {list_domains}")

        get_bulk_batch = await paystack_client.bulk_charges.fetch_bulk_charge_batch(
            id_or_code="181426836"
        )
        print(f"Fetch a bulk charge of a specific batch: {get_bulk_batch}")

        get_charge_batch = await paystack_client.bulk_charges.fetch_charge_bulk_batch(
            id_or_code="BCH_n27x51vd5hbscoy", status=STATUS.PENDING.value
        )
        print(f"Fetch a charge of a specific batch: {get_charge_batch}")

        pause_bulk = await paystack_client.bulk_charges.pause_bulk_charge_batch(
            batch_code="BCH_n27x51vd5hbscoy"
        )
        print(f"Pause a bulk charge batch: {pause_bulk}")

        resume_bulk = await paystack_client.bulk_charges.resume_bulk_charge_batch(
            batch_code="BCH_n27x51vd5hbscoy"
        )
        print(f"Resume a bulk charge batch: {resume_bulk}")

        # access the API endpoints making a Post request
        init_bulk_charge = await paystack_client.bulk_charges.initiate_bulk_charge(
            [
                {
                    "authorization": "AUTH_xfuz7dy4b9",
                    "amount": 1500,
                    "reference": "dam1266638dhhe",
                }
            ]
        )
        print(f"Initiated a bulk charge: {init_bulk_charge}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """Implementing all the API endpoints"""
    # access the API endpoints making a Get request
    list_bulk = paystack_client.bulk_charges.list_bulk_charge_batches()
    print(f"List all bulk charges: {list_bulk}")

    get_bulk_batch = paystack_client.bulk_charges.fetch_bulk_charge_batch(
        id_or_code="181426836"
    )
    print(f"Fetch a bulk charge of a specific batch: {get_bulk_batch}")

    get_charge_batch = paystack_client.bulk_charges.fetch_charge_bulk_batch(
        id_or_code="BCH_n27x51vd5hbscoy", status=STATUS.PENDING.value
    )
    print(f"Fetch a charge of a specific batch: {get_charge_batch}")

    pause_bulk = paystack_client.bulk_charges.pause_bulk_charge_batch(
        batch_code="BCH_n27x51vd5hbscoy"
    )
    print(f"Pause a bulk charge batch: {pause_bulk}")

    resume_bulk = paystack_client.bulk_charges.resume_bulk_charge_batch(
        batch_code="BCH_n27x51vd5hbscoy"
    )
    print(f"Resume a bulk charge batch: {resume_bulk}")

    # access the API endpoints making a Post request
    init_bulk_charge = paystack_client.bulk_charges.initiate_bulk_charge(
        [
            {
                "authorization": "AUTH_xfuz7dy4b9",
                "amount": 1500,
                "reference": "dam1266638dhhe",
            }
        ]
    )
    print(f"Initiated a bulk charge: {init_bulk_charge}")


if __name__ == "__main__":
    main()
