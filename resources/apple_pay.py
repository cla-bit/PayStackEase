"""
Apple Pay Examples
"""

import asyncio

from paystackease import PayStackBase, AsyncPayStackBase
from paystackease.helpers import DomainNameModel, ListDomainNamesModel


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request

        # STEP 1:
        list_domains = await paystack_client.apple_pay.list_domains()
        print(f"List all domains: {list_domains}")

        # STEP 2:
        list_domain_values = ListDomainNamesModel(use_cursor=True)  # pass other arguments
        list_domains = await paystack_client.apple_pay.list_domains(list_domains=list_domain_values)
        print(f"List all domains: {list_domains}")

        # access the API endpoints making a Post request
        domain = DomainNameModel(domainName="example.com")
        register_domain = await paystack_client.apple_pay.register_domain(domain_name=domain)
        print(f"Register domain: {register_domain}")

        # access the API endpoints making a Delete request
        unregister_domain = await paystack_client.apple_pay.unregister_domain(domain_name=domain)
        print(f"Unregister domain: {unregister_domain}")

asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()

    # access the API endpoints making a Get request

    # STEP 1:
    list_domains = paystack_client.apple_pay.list_domains()
    print(f"List all domains: {list_domains}")

    # STEP 2:
    list_domain_values = ListDomainNamesModel(use_cursor=True)  # pass other arguments
    list_domains = paystack_client.apple_pay.list_domains(list_domains=list_domain_values)
    print(f"List all domains: {list_domains}")

    # access the API endpoints making a Post request
    domain = DomainNameModel(domainName="example.com")
    register_domain = paystack_client.apple_pay.register_domain(domain_name=domain)
    print(f"Register domain: {register_domain}")

    # access the API endpoints making a Delete request
    unregister_domain = paystack_client.apple_pay.unregister_domain(domain_name=domain)
    print(f"Unregister domain: {unregister_domain}")


if __name__ == "__main__":
    main()