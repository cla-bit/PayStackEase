from paystackease import PayStackBase
from paystackease.helpers import DomainNameModel


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable

    print(DomainNameModel.model_json_schema())

    # domain = DomainNameModel(domainName="example.com")
    # paystack_client = PayStackBase()

    # """Implementing all the API endpoints"""
    # # access the API endpoints making a Get request
    # list_domains = paystack_client.apple_pay.list_domains()
    # print(f"List all domains: {list_domains}")

    # access the API endpoints making a Post request
    # register_domain = paystack_client.apple_pay.register_domain(domain)
    # print(f"Register domain: {register_domain}")

    # # access the API endpoints making a Delete request
    # unregister_domain = paystack_client.apple_pay.unregister_domain(
    #     domain_name="example-of-domain-name")
    # print(f"Unregister domain: {unregister_domain}")


if __name__ == "__main__":
    main()
