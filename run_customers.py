"""
Examples
"""

import asyncio
from paystackease.helpers import CustomerDetails
from paystackease import PayStackBase, AsyncPayStackBase, RiskAction


# async def main():
#     """Implementing all the API endpoints"""
#     async with AsyncPayStackBase() as paystack_client:
#         # access the API endpoints making a Get request
#         all_customers = await paystack_client.customers.list_customers()
#         print(f"All Customers: {all_customers}")
#
#         get_customer = await paystack_client.customers.fetch_customer(
#             email_or_code="test@gmail.com"
#         )
#         print(f"Customer Detail: {get_customer}")
#
#         # access the API endpoints making a Post request
#         create_customer = await paystack_client.customers.create_customer(
#             email="test@gmail.com",
#             first_name="Test",
#             last_name="Test",
#             phone="phone number",
#             metadata={"middle_name": "Test", "nickname": "Tester"},
#         )
#         print(f"Create charge: {create_customer}")
#
#         validate_customer = await paystack_client.customers.validate_customer(
#             email_or_code="test@gmail.com",
#             first_name="Test",
#             last_name="Test",
#             account_type="bank_account",
#             country="country code",
#             bvn="bvn number",
#             bank_code="bank code",
#             account_number="0000000000",
#         )
#         print(f"Validate Customer: {validate_customer}")
#
#         white_blacklist_customer = (
#             await paystack_client.customers.whitelist_blacklist_customer(
#                 email_or_code="test@gmail.com", risk_action=RiskAction.DENY.value
#             )
#         )
#         print(f"Blacklisted Customer: {white_blacklist_customer}")
#
#         deactivate_auth_code = await paystack_client.customers.deactivate_authorization(
#             authorization_code="AUTH_authorization-code"
#         )
#         print(f"Deactivated Auth Code: {deactivate_auth_code}")
#
#         # access the API endpoints making a Put request
#         update_customer = await paystack_client.customers.update_customer(
#             customer_code="CUS_customer-code", metadata={"middle_name": "Test"}
#         )
#         print(f"Updated Customer: {update_customer}")
#
#
# asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()
    customer = CustomerDetails(first_name="John", last_name="Tester", phone="09012345678")

    # """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    # all_customers = paystack_client.customers.list_customers()
    # print(f"All Customers: {all_customers}")
    #
    # get_customer = paystack_client.customers.fetch_customer(
    #     email_or_code="test@gmail.com"
    # )
    # print(f"Customer Detail: {get_customer}")

    # access the API endpoints making a Post request
    create_customer = paystack_client.customers.create_customer(
        email="test@gmail.com",
        customer_details=customer
    )
    print(f"Create charge: {create_customer}")

    # validate_customer = paystack_client.customers.validate_customer(
    #     email_or_code="test@gmail.com",
    #     first_name="Test",
    #     last_name="Test",
    #     account_type="bank_account",
    #     country="country code",
    #     bvn="bvn number",
    #     bank_code="bank code",
    #     account_number="0000000000",
    # )
    # print(f"Validate Customer: {validate_customer}")
    #
    # white_blacklist_customer = paystack_client.customers.whitelist_blacklist_customer(
    #     email_or_code="test@gmail.com", risk_action=RiskAction.DENY.value
    # )
    # print(f"Blacklisted Customer: {white_blacklist_customer}")
    #
    # deactivate_auth_code = paystack_client.customers.deactivate_authorization(
    #     authorization_code="AUTH_authorization-code"
    # )
    # print(f"Deactivated Auth Code: {deactivate_auth_code}")
    #
    # # access the API endpoints making a Put request
    # update_customer = paystack_client.customers.update_customer(
    #     customer_code="CUS_customer-code", metadata={"middle_name": "Test"}
    # )
    # print(f"Updated Customer: {update_customer}")


if __name__ == "__main__":
    main()
