"""
Examples
"""

import asyncio
from datetime import date

from paystackease import PayStackBase, AsyncPayStackBase
from paystackease.helpers import BulkChargeObject, PageModel, DatePageModel, STATUS


# async def main():
#     """Implementing all the API endpoints"""
#     async with AsyncPayStackBase() as paystack_client:
#         # access the API endpoints making a Get request
#         list_domains = await paystack_client.bulk_charges.list_bulk_charge_batches(
#             from_date=date.today()
#         )
#         print(f"List all domains: {list_domains.data}")  # access the data from the PayStackResponse
#
#         get_bulk_batch = await paystack_client.bulk_charges.fetch_bulk_charge_batch(
#             id_or_code="bulk-id-or-code"
#         )
#         print(f"Fetch a bulk charge of a specific batch: {get_bulk_batch}")
#
#         get_charge_batch = await paystack_client.bulk_charges.fetch_charge_bulk_batch(
#             id_or_code="BCH_bulk-code", status=STATUS.PENDING.value
#         )
#         print(f"Fetch a charge of a specific batch: {get_charge_batch}")
#
#         pause_bulk = await paystack_client.bulk_charges.pause_bulk_charge_batch(
#             batch_code="BCH_bulk-code"
#         )
#         print(f"Pause a bulk charge batch: {pause_bulk}")
#
#         resume_bulk = await paystack_client.bulk_charges.resume_bulk_charge_batch(
#             batch_code="BCH_bulk-code"
#         )
#         print(f"Resume a bulk charge batch: {resume_bulk}")
#
#         # access the API endpoints making a Post request
#         init_bulk_charge = await paystack_client.bulk_charges.initiate_bulk_charge(
#             [
#                 {
#                     "authorization": "AUTH_authorization-code",
#                     "amount": 1500,
#                     "reference": "reference",
#                 }
#             ]
#         )
#         print(f"Initiated a bulk charge: {init_bulk_charge}")
#
#
# asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()

    """Implementing all the API endpoints"""
    # access the API endpoints making a Get request

    # list_bulk = paystack_client.bulk_charges.list_bulk_charge_batches()
    # print(f"List all bulk charges: {list_bulk}")

    # get_bulk_batch = paystack_client.bulk_charges.fetch_bulk_charge_batch(
    #     id_or_code="bulk-id-or-code"
    # )
    # print(f"Fetch a bulk charge of a specific batch: {get_bulk_batch}")
    #
    # get_charge_batch = paystack_client.bulk_charges.fetch_charge_bulk_batch(
    #     id_or_code="BCH_n0oecupcht9vy3f", status=STATUS.PENDING.value)
    # print(f"Fetch a charge of a specific batch: {get_charge_batch}")
    #
    # pause_bulk = paystack_client.bulk_charges.pause_bulk_charge_batch(
    #     batch_code="BCH_bulk-code"
    # )
    # print(f"Pause a bulk charge batch: {pause_bulk}")
    #
    # resume_bulk = paystack_client.bulk_charges.resume_bulk_charge_batch(
    #     batch_code="BCH_bulk-code"
    # )
    # print(f"Resume a bulk charge batch: {resume_bulk}")
    #
    # # access the API endpoints making a Post request
    auth_obj = BulkChargeObject(amount=30000)
    init_bulk_charge = paystack_client.bulk_charges.initiate_bulk_charge(objects=auth_obj)
    print(f"Initiated a bulk charge: {init_bulk_charge}")


if __name__ == "__main__":
    main()