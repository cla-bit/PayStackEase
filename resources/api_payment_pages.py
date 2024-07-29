"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_pages = await paystack_client.payment_pages.list_payment_pages()
        print(f"All Payment Pages: {all_pages}")

        page_detail = await paystack_client.payment_pages.fetch_payment_page(
            page_id_or_slug="g7cojya482"
        )
        print(f"Page Detail: {page_detail}")

        slug_available = await paystack_client.payment_pages.check_slug_available(
            page_slug="g7cojya482"
        )
        print(f"Slug Availability: {slug_available}")

        # access the API endpoints making a Post request
        payment_page = await paystack_client.payment_pages.create_payment_page(
            name="Testing Pay Page Creation",
            description="This is just to test creating a payment page",
            amount=10000,
            split_code="SPL_split-code",
        )
        print(f"Created Payment Page: {payment_page}")

        add_product = await paystack_client.payment_pages.add_products(
            payment_id=56, product=[123, 345]
        )
        print(f"Added Product: {add_product}")

        # access the API endpoints making a Put request
        update_page = await paystack_client.payment_pages.update_payment_page(
            page_id_or_slug="g7cojya482", name="Updated Testing Page"
        )
        print(f"Updated Page: {update_page}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_pages = paystack_client.payment_pages.list_payment_pages()
    print(f"All Payment Pages: {all_pages}")

    page_detail = paystack_client.payment_pages.fetch_payment_page(
        page_id_or_slug="g7cojya482"
    )
    print(f"Page Detail: {page_detail}")

    slug_available = paystack_client.payment_pages.check_slug_available(
        page_slug="g7cojya482"
    )
    print(f"Slug Availability: {slug_available}")

    # access the API endpoints making a Post request
    payment_page = paystack_client.payment_pages.create_payment_page(
        name="Testing Pay Page Creation",
        description="This is just to test creating a payment page",
        amount=1000,
        split_code="SPL_split-code",
    )
    print(f"Created Payment Page: {payment_page}")

    add_product = paystack_client.payment_pages.add_products(
        payment_id=56, product=[123, 345]
    )
    print(f"Added Product: {add_product}")

    # access the API endpoints making a Put request
    update_page = paystack_client.payment_pages.update_payment_page(
        page_id_or_slug="g7cojya482", name="Updated Testing Page"
    )
    print(f"Updated Page: {update_page}")


if __name__ == "__main__":
    main()
