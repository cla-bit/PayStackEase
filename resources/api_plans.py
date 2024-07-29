"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase, Interval, Currency


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_plans = await paystack_client.plans.list_plans()  # active, archived, deleted
        print(f"All Plans: {all_plans}")

        plan_detail = await paystack_client.plans.fetch_plan(id_or_code="PLN_plan-id-or-code")
        print(f"Plan Detail: {plan_detail}")

        # access the API endpoints making a Post request
        create_plan = await paystack_client.plans.create_plan(
            name="Testing Plan1",
            amount=100000,
            interval=Interval.MONTHLY.value,
            currency=Currency.NGN.value,
            invoice_limit=100,
            send_invoices=True,
            send_sms=True,
        )
        print(f"Create Plan: {create_plan}")

        # access the API endpoints making a Put request
        update_plan = await paystack_client.plans.update_plan(
            id_or_code="PLN_plan-id-or-code",
            send_sms=True,
            name="Updated Plan",
            send_invoices=True,
            invoice_limit=25,
            currency=Currency.NGN.value,
            amount=300000,
            interval=Interval.QUARTERLY.value,
        )
        print(f"Updated Plan: {update_plan}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_plans = paystack_client.plans.list_plans()
    print(f"All Plans: {all_plans}")

    plan_detail = paystack_client.plans.fetch_plan(id_or_code="PLN_plan-id-or-code")
    print(f"Plan Detail: {plan_detail}")

    # access the API endpoints making a Post request
    create_plan = paystack_client.plans.create_plan(
        name="Testing Plan1",
        amount=100000,
        interval=Interval.MONTHLY.value,
        currency=Currency.NGN.value,
        invoice_limit=100,
        send_invoices=True,
        send_sms=True,
    )
    print(f"Create Plan: {create_plan}")

    # access the API endpoints making a Put request
    update_plan = paystack_client.plans.update_plan(
        id_or_code="PLN_plan-id-or-code",
        send_sms=True,
        name="Updated Plan",
        send_invoices=True,
        invoice_limit=25,
        currency=Currency.NGN.value,
        amount=300000,
        interval=Interval.QUARTERLY.value,
    )
    print(f"Updated Plan: {update_plan}")


if __name__ == "__main__":
    main()
