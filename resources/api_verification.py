"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase, AccountType, DocumentType


async def main():
    # # access the API endpoints making a Get request
    async with AsyncPayStackBase() as paystack_client:
        verify_account = await paystack_client.verification.resolve_account(
            account_number="0000000000", bank_code="057"
        )
        print(f"Verified Account: {verify_account}")

        card_details = await paystack_client.verification.resolve_card_bin(
            bin_code="539983"
        )
        print(f"Card Details: {card_details}")

        # access the API endpoints making a Post request
        validate_account = await paystack_client.verification.validate_account(
            account_name="Test",
            account_number="0000000000",
            account_type=AccountType.PERSONAL.value,
            bank_code="632005",
            country_code="ZA",
            document_type=DocumentType.IDENTITY_NUMBER.value,
            document_number="1234567890123",
        )
        print(f"Validated Account: {validate_account}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    # # access the API endpoints making a Get request
    verify_account = paystack_client.verification.resolve_account(
        account_number="0000000000", bank_code="057"
    )
    print(f"Verified Account: {verify_account}")

    card_details = paystack_client.verification.resolve_card_bin(bin_code="539983")
    print(f"Card Details: {card_details}")

    # access the API endpoints making a Post request
    validate_account = paystack_client.verification.validate_account(
        account_name="Test",
        account_number="0000000000",
        account_type=AccountType.PERSONAL.value,
        bank_code="632005",
        country_code="ZA",
        document_type=DocumentType.IDENTITY_NUMBER.value,
        document_number="1234567890123",
    )
    print(f"Validated Account: {validate_account}")


if __name__ == "__main__":
    main()
