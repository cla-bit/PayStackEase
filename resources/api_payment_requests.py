"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase
from paystackease.helpers.tool_kit import PayMentRequestStatus


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_page_requests = (
            await paystack_client.payment_requests.list_payment_requests()
        )
        print(f"All Payment Requests: {all_page_requests}")

        page_request_detail = (
            await paystack_client.payment_requests.fetch_payment_request(
                id_or_code="PRQ_4ir9mcwxln6sepy"
            )
        )
        print(f"Page Request Detail: {page_request_detail}")

        verify_payment_request = (
            await paystack_client.payment_requests.verify_payment_request(
                code="PRQ_4ir9mcwxln6sepy"
            )
        )
        print(f"Verified Payment Request: {verify_payment_request}")

        payment_request_totals = (
            await paystack_client.payment_requests.payment_request_total()
        )
        print(f"Payment Request Totals: {payment_request_totals}")

        # access the API endpoints making a Post request
        payment_request = await paystack_client.payment_requests.create_payment_request(
            customer="CUS_ehq4eemtrmeuny4",
            amount=10000,
            draft=True,
            has_invoice=True,
            send_notification=True,
        )
        print(f"Created Payment Request: {payment_request}")

        send_notice = await paystack_client.payment_requests.send_notification(
            code="PRQ_4ir9mcwxln6sepy"
        )
        print(f"Notification Sent: {send_notice}")

        final_payment_request = (
            await paystack_client.payment_requests.finalize_payment_request(
                code="PRQ_4ir9mcwxln6sepy", send_notification=True
            )
        )
        print(f"Final Payment Request Notice: {final_payment_request}")

        archive_pay_request = (
            await paystack_client.payment_requests.archive_payment_request(
                code="PRQ_4ir9mcwxln6sepy"
            )
        )
        print(f"Archived Payment Request: {archive_pay_request}")

        # access the API endpoints making a Put request
        update_payment_request = (
            await paystack_client.payment_requests.update_payment_request(
                id_or_code="PRQ_4ir9mcwxln6sepy",
                draft=False,
            )
        )
        print(f"Updated Page: {update_payment_request}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_page_requests = paystack_client.payment_requests.list_payment_requests(
        # include_archive=False, status=PayMentRequestStatus.DRAFT.value
    )
    print(f"All Payment Requests: {all_page_requests}")

    page_request_detail = paystack_client.payment_requests.fetch_payment_request(
        id_or_code="PRQ_4ir9mcwxln6sepy"
    )
    print(f"Page Request Detail: {page_request_detail}")

    verify_payment_request = paystack_client.payment_requests.verify_payment_request(
        code="PRQ_6v2pibmhypo273u"
    )
    print(f"Verified Payment Request: {verify_payment_request}")

    payment_request_totals = paystack_client.payment_requests.payment_request_total()
    print(f"Payment Request Totals: {payment_request_totals}")

    # access the API endpoints making a Post request
    payment_request = paystack_client.payment_requests.create_payment_request(
        customer="CUS_3w65ynsqww97ryp",
        amount=10000,
        line_items=[{"name": "item 1", "amount": 20000}],
        tax=[{"name": "VAT", "amount": 2300}],
        description="Testing payment request",
        has_invoice=False
    )
    print(f"Created Payment Request: {payment_request}")

    send_notice = paystack_client.payment_requests.send_notification(
        code="PRQ_1wexcsdswbexe6f"
    )
    print(f"Notification Sent: {send_notice}")

    final_payment_request = paystack_client.payment_requests.finalize_payment_request(
        code="PRQ_1wexcsdswbexe6f", send_notification=True
    )
    print(f"Final Payment Request Notice: {final_payment_request}")

    archive_pay_request = paystack_client.payment_requests.archive_payment_request(
        code="PRQ_4ir9mcwxln6sepy"
    )
    print(f"Archived Payment Request: {archive_pay_request}")

    # access the API endpoints making a Put request
    update_payment_request = paystack_client.payment_requests.update_payment_request(
        id_or_code="PRQ_6v2pibmhypo273u",
        draft=True,
    )
    print(f"Updated Page: {update_payment_request}")


if __name__ == "__main__":
    main()
