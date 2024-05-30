"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase, Resolution


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_disputes = await paystack_client.disputes.list_disputes()
        print(f"All Disputes: {all_disputes}")

        get_dispute = await paystack_client.disputes.fetch_dispute(dispute_id="")
        print(f"Dispute Detail: {get_dispute}")

        get_transaction_dispute = (
            await paystack_client.disputes.list_transaction_disputes(transaction_id="")
        )
        print(f"A Transaction Disputes: {get_transaction_dispute}")

        uploaded_url = await paystack_client.disputes.get_upload_url(
            dispute_id="dispute-id-here", uploaded_filename="filename.pdf"
        )
        print(f"Uploaded Url: {uploaded_url}")

        export_evidence = await paystack_client.disputes.export_disputes()
        print(f"Added Evidence: {export_evidence}")

        # access the API endpoints making a Post request
        add_evidence = await paystack_client.disputes.add_evidence(
            dispute_id="your-dispute-id",
            customer_email="test@gmail.com",
            customer_name="Test",
            customer_phone="+23456789012",
            service_details="claim for buying product",
            delivery_date="3a ladoke street ogbomoso",
        )
        print(f"Added Evidence: {add_evidence}")

        # access the API endpoints making a Put request
        update_dispute = await paystack_client.disputes.update_dispute(
            dispute_id="your-dispute-id",
            refund_amount=1000,
            uploaded_filename="disputed_settled.pdf",
        )
        print(f"Updated Dispute: {update_dispute}")

        resolve_dispute = await paystack_client.disputes.resolve_dispute(
            dispute_id="dispute-id",
            resolution=Resolution.MERCHANT.value,
            message="Your dispute has been resolved and uploaded",
            refund_amount=10000,
            uploaded_filename="qesp8a4df1xejihd9x5q",
            evidence=56,
        )
        print(f"Resolved Dispute: {resolve_dispute}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_disputes = paystack_client.disputes.list_disputes()
    print(f"All Disputes: {all_disputes}")

    get_dispute = paystack_client.disputes.fetch_dispute(dispute_id="")
    print(f"Dispute Detail: {get_dispute}")

    get_transaction_dispute = paystack_client.disputes.list_transaction_disputes(
        transaction_id=""
    )
    print(f"A;; Transaction Disputes: {get_transaction_dispute}")

    uploaded_url = paystack_client.disputes.get_upload_url(
        dispute_id="dispute-id-here", uploaded_filename="filename.pdf"
    )
    print(f"Uploaded Url: {uploaded_url}")

    export_evidence = paystack_client.disputes.export_disputes()
    print(f"Added Evidence: {export_evidence}")

    # access the API endpoints making a Post request
    add_evidence = paystack_client.disputes.add_evidence(
        dispute_id="your-dispute-id",
        customer_email="test@gmail.com",
        customer_name="Test",
        customer_phone="+23456789012",
        service_details="claim for buying product",
        delivery_date="3a ladoke street ogbomoso",
    )
    print(f"Added Evidence: {add_evidence}")

    # access the API endpoints making a Put request
    update_dispute = paystack_client.disputes.update_dispute(
        dispute_id="your-dispute-id",
        refund_amount=1000,
        uploaded_filename="disputed_settled.pdf",
    )
    print(f"Updated Dispute: {update_dispute}")

    resolve_dispute = paystack_client.disputes.resolve_dispute(
        dispute_id="dispute-id",
        resolution=Resolution.MERCHANT.value,
        message="Your dispute has been resolved and uploaded",
        refund_amount=10000,
        uploaded_filename="qesp8a4df1xejihd9x5q",
        evidence=56,
    )
    print(f"Resolved Dispute: {resolve_dispute}")


if __name__ == "__main__":
    main()
