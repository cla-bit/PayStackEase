"""
Examples
"""

import asyncio

from paystackease import PayStackBase, AsyncPayStackBase


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        list_domains = await paystack_client.apple_pay.list_domains()
        print(f"List all domains: {list_domains}")

        # access the API endpoints making a Post request
        register_domain = await paystack_client.apple_pay.register_domain(domain_name="example")
        print(f"Register domain: {register_domain}")

        # access the API endpoints making a Delete request
        unregister_domain = await paystack_client.apple_pay.unregister_domain(domain_name="example")
        print(f"Unregister domain: {unregister_domain}")

asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()

    """Implementing all the API endpoints"""
    # access the API endpoints making a Get request
    list_domains = paystack_client.apple_pay.list_domains()
    print(f"List all domains: {list_domains}")

    # access the API endpoints making a Post request
    register_domain = paystack_client.apple_pay.register_domain(domain_name="example")
    print(f"Register domain: {register_domain}")

    # access the API endpoints making a Delete request
    unregister_domain = paystack_client.apple_pay.unregister_domain(domain_name="example")
    print(f"Unregister domain: {unregister_domain}")


if __name__ == "__main__":
    main()
