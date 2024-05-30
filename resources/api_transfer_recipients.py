"""
Examples
"""

import asyncio
from datetime import date

from paystackease import PayStackBase, AsyncPayStackBase, RecipientType


async def main():
    async with AsyncPayStackBase() as paystack_client:

        # access the API endpoints making a Get request
        transfer_recipients = (
            await paystack_client.transfer_recipients.list_transfer_recipients(
                from_date=date.today()
            )
        )
        print(f"All Transfer Recipients: {transfer_recipients}")

        get_transfer_recipient = (
            await paystack_client.transfer_recipients.fetch_transfer_recipient(
                id_or_code="RCP_fh82l0laloo41c4"
            )
        )
        print(f"Transfer Recipient: {get_transfer_recipient}")

        # access the API endpoints making a Post request
        create_recipient = (
            await paystack_client.transfer_recipients.create_transfer_recipients(
                recipient_type=RecipientType.MOBILE_MONEY.value,
                recipient_name="Faith Susan",
                account_number="0000000000",
                bank_code="057",
            )
        )
        print(f"Created Recipient: {create_recipient}")

        create_bulk_recipients = (
            await paystack_client.transfer_recipients.bulk_create_transfer_recipient(
                [
                    {
                        "type": RecipientType.NUBAN.value,
                        "name": "John Doe",
                        "account_number": "0000000000",
                        "bank_code": "057",
                    },
                    {
                        "type": RecipientType.MOBILE_MONEY.value,
                        "name": "Faith Susan",
                        "account_number": "0000000000",
                        "bank_code": "057",
                    },
                ]
            )
        )
        print(f"Created Bulk Recipients: {create_bulk_recipients}")

        # access the API endpoints making a Put request
        update_recipient = (
            await paystack_client.transfer_recipients.update_transfer_recipient(
                id_or_code="RCP_fh82l0laloo41c4",
                recipient_name="Rick Sanchez",
                recipient_email="ricksabchez@gmail.com",
            )
        )
        print(f"Updated Recipient: {update_recipient}")

        # access the API endpoints making a Delete request
        delete_recipient = (
            await paystack_client.transfer_recipients.delete_transfer_recipient(
                id_or_code="72638041",
            )
        )
        print(f"Deleted Recipient: {delete_recipient}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    # access the API endpoints making a Get request
    transfer_recipients = paystack_client.transfer_recipients.list_transfer_recipients(
        from_date=date.today()
    )
    print(f"All Transfer Recipients: {transfer_recipients}")

    get_transfer_recipient = (
        paystack_client.transfer_recipients.fetch_transfer_recipient(
            id_or_code="RCP_fh82l0laloo41c4"
        )
    )
    print(f"Transfer Recipient: {get_transfer_recipient}")

    # access the API endpoints making a Post request
    create_recipient = paystack_client.transfer_recipients.create_transfer_recipients(
        recipient_type=RecipientType.MOBILE_MONEY.value,
        recipient_name="Faith Susan",
        account_number="0000000000",
        bank_code="057",
    )
    print(f"Created Recipient: {create_recipient}")

    create_bulk_recipients = (
        paystack_client.transfer_recipients.bulk_create_transfer_recipient(
            [
                {
                    "type": RecipientType.NUBAN.value,
                    "name": "John Doe",
                    "account_number": "0000000000",
                    "bank_code": "057",
                },
                {
                    "type": RecipientType.MOBILE_MONEY.value,
                    "name": "Faith Susan",
                    "account_number": "0000000000",
                    "bank_code": "057",
                },
            ]
        )
    )
    print(f"Created Bulk Recipients: {create_bulk_recipients}")

    # access the API endpoints making a Put request
    update_recipient = paystack_client.transfer_recipients.update_transfer_recipient(
        id_or_code="RCP_fh82l0laloo41c4",
        recipient_name="Rick Sanchez",
        recipient_email="ricksabchez@gmail.com",
    )
    print(f"Updated Recipient: {update_recipient}")

    # access the API endpoints making a Delete request
    delete_recipient = paystack_client.transfer_recipients.delete_transfer_recipient(
        id_or_code="72638041",
    )
    print(f"Deleted Recipient: {delete_recipient}")


if __name__ == "__main__":
    main()
