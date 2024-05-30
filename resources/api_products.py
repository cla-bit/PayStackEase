"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase, Currency


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_products = await paystack_client.products.list_products()
        print(f"Timeout Detail: {all_products}")

        get_product = await paystack_client.products.fetch_product(
            product_id="product-id-here"
        )
        print(f"Product Detail: {get_product}")

        # access the API endpoints making a Post request
        create_product = await paystack_client.products.create_product(
            name="Test Product 1",
            description="Testing Product One",
            amount=10000,
            currency=Currency.NGN.value,
            quantity=10
        )
        print(f"Created Product: {create_product}")

        # access the API endpoints making a Put request
        update_product = await paystack_client.products.update_product(
            product_id="product-id-here",
            name="Test Product 1",
            description="Testing Product One",
            amount=10000,
            currency=Currency.NGN.value,
        )
        print(f"Updated Product: {update_product}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_products = paystack_client.products.list_products()
    print(f"All Products: {all_products}")

    get_product = paystack_client.products.fetch_product(product_id="product-id-here")
    print(f"Product Detail: {get_product}")

    # access the API endpoints making a Post request
    create_product = paystack_client.products.create_product(
        name="Test Product 1",
        description="Testing Product One",
        amount=10000,
        currency=Currency.NGN.value,
        quantity=10
    )
    print(f"Created Product: {create_product}")

    # access the API endpoints making a Put request
    update_product = paystack_client.products.update_product(
        product_id="product-id-here",
        name="Test Product 1",
        description="Testing Product One",
        amount=10000,
        currency=Currency.NGN.value,
    )
    print(f"Updated Product: {update_product}")


if __name__ == "__main__":
    main()
