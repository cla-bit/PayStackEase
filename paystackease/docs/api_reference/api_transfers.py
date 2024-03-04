"""
Demonstrates using Asynchronous and Synchronous Paystack Transfers API wrappers.
Shows PayStackBase and AsyncPayStaCKbASE for interacting with Paystack's verification.

Reference: https://paystack.com/docs/api/trasfer/ to learn more
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase, convert_to_subunit, Currency


async def main():
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_transfers = await paystack_client.transfers.list_transfers()
        print(f"All Transfers: {all_transfers}")

        get_transfer = await paystack_client.transfers.fetch_transfer(
            id_or_code="TRF_vsyqdmlzble3uii"
        )
        print(f"Transfer Detail: {get_transfer}")

        verify_transfer = await paystack_client.transfers.verify_transfer(
            reference="TRF_vsyqdmlzble3uii"
        )
        print(f"Verified Transfer: {verify_transfer}")

        # # access the API endpoints making a Post request
        sub_amount = convert_to_subunit(amount=100, currency=Currency.NGN)
        create_transfer = await paystack_client.transfers.initiate_transfer(
            transfer_source="balance",
            amount=sub_amount,
            transfer_recipient="RCP_hd2jvfbuif1el1k",
            reason="Testing Transfer",
        )
        print(f"Created Transfer: {create_transfer}")

        final_transfer = await paystack_client.transfers.finalize_transfer(
            transfer_code="TRF_vsyqdmlzble3uii", otp="928783"
        )
        print(f"Final Transfer: {final_transfer}")

        create_bulk_transfer = await paystack_client.transfers.initiate_bulk_transfer(
            transfer_source="balance",
            transfers=[
                {
                    "amount": sub_amount,
                    "recipient": "RCP_hd2jvfbuif1el1k",
                    "reference": "588YtfftReF355894J",
                    "reason": "Testing Bulk Transfer",
                },
                {
                    "amount": sub_amount,
                    "recipient": "RCP_hd2jvfbuif1el1k",
                    "reference": "588YtfftReF355894J",
                    "reason": "Testing Bulk Transfer",
                },
            ],
        )
        print(f"Created Bulk Transfer: {create_bulk_transfer}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    # access the API endpoints making a Get request
    all_transfers = paystack_client.transfers.list_transfers()
    print(f"All Transfers: {all_transfers}")

    get_transfer = paystack_client.transfers.fetch_transfer(
        id_or_code="TRF_vsyqdmlzble3uii"
    )
    print(f"Transfer Detail: {get_transfer}")

    verify_transfer = paystack_client.transfers.verify_transfer(
        reference="TRF_vsyqdmlzble3uii"
    )
    print(f"Verified Transfer: {verify_transfer}")

    # # access the API endpoints making a Post request
    sub_amount = convert_to_subunit(amount=100, currency=Currency.NGN)
    create_transfer = paystack_client.transfers.initiate_transfer(
        transfer_source="balance",
        amount=sub_amount,
        transfer_recipient="RCP_hd2jvfbuif1el1k",
        reason="Testing Transfer",
    )
    print(f"Created Transfer: {create_transfer}")

    final_transfer = paystack_client.transfers.finalize_transfer(
        transfer_code="TRF_vsyqdmlzble3uii", otp="928783"
    )
    print(f"Final Transfer: {final_transfer}")

    create_bulk_transfer = paystack_client.transfers.initiate_bulk_transfer(
        transfer_source="balance",
        transfers=[
            {
                "amount": sub_amount,
                "recipient": "RCP_hd2jvfbuif1el1k",
                "reference": "588YtfftReF355894J",
                "reason": "Testing Bulk Transfer",
            },
            {
                "amount": sub_amount,
                "recipient": "RCP_hd2jvfbuif1el1k",
                "reference": "588YtfftReF355894J",
                "reason": "Testing Bulk Transfer",
            },
        ],
    )
    print(f"Created Bulk Transfer: {create_bulk_transfer}")


if __name__ == "__main__":
    main()
