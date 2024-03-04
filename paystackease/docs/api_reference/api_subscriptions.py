"""
Demonstrates using Asynchronous and Synchronous Paystack Subscriptions API wrappers.
Shows PayStackBase, and AsyncPayStaCKBase for interacting with Paystack's transactions.

Reference: https://paystack.com/docs/api/subscription/ to learn more
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_subscriptions = await paystack_client.subscriptions.list_subscriptions()
        print(f"Subscriptions: {all_subscriptions}")

        get_subscription = await paystack_client.subscriptions.fetch_subscription(
            id_or_code="subscription-id-here"
        )
        print(f"Subscription Detail: {get_subscription}")

        # access the API endpoints making a Post request
        create_subscription = await paystack_client.subscriptions.create_subscription(
            customer="CUS_EQ34235R",
            plan_code="PLN_WRF33454",
            authorization="AUTH_134SDFWERE",
        )
        print(f"Created Subscription: {create_subscription}")

        enable_subscription = await paystack_client.subscriptions.enable_subscription(
            subscription_code="subscription-code-here", token="123456"
        )
        print(f"Enabled Subscription: {enable_subscription}")

        disable_subscription = await paystack_client.subscriptions.disable_subscription(
            subscription_code="subscription-code-here", token="123456"
        )
        print(f"Disabled Subscription: {disable_subscription}")

        generate_subscription_update = (
            await paystack_client.subscriptions.generate_update_subscription(
                subscription_code="subscription-code-here",
            )
        )
        print(f"Generated Subscription Update: {generate_subscription_update}")

        update_sub_link = (
            await paystack_client.subscriptions.send_update_subscription_link(
                subscription_code="subscription-code-here",
            )
        )
        print(f"Updated Subscription Link: {update_sub_link}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_subscriptions = paystack_client.subscriptions.list_subscriptions()
    print(f"Subscriptions: {all_subscriptions}")

    get_subscription = paystack_client.subscriptions.fetch_subscription(
        id_or_code="subscription-id-here"
    )
    print(f"Subscription Detail: {get_subscription}")

    # access the API endpoints making a Post request
    create_subscription = paystack_client.subscriptions.create_subscription(
        customer="CUS_EQ34235R",
        plan_code="PLN_WRF33454",
        authorization="AUTH_134SDFWERE",
    )
    print(f"Created Subscription: {create_subscription}")

    enable_subscription = paystack_client.subscriptions.enable_subscription(
        subscription_code="subscription-code-here", token="123456"
    )
    print(f"Enabled Subscription: {enable_subscription}")

    disable_subscription = paystack_client.subscriptions.disable_subscription(
        subscription_code="subscription-code-here", token="123456"
    )
    print(f"Disabled Subscription: {disable_subscription}")

    generate_subscription_update = (
        paystack_client.subscriptions.generate_update_subscription(
            subscription_code="subscription-code-here",
        )
    )
    print(f"Generated Subscription Update: {generate_subscription_update}")

    update_sub_link = paystack_client.subscriptions.send_update_subscription_link(
        subscription_code="subscription-code-here",
    )
    print(f"Updated Subscription Link: {update_sub_link}")


if __name__ == "__main__":
    main()
